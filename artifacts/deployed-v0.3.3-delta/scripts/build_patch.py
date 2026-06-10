from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


TAG = "v0.3.3"
UPSTREAM_FILES = (
    "custom_components/midea_auto_cloud/device_mapping/T0xD9.py",
    "custom_components/midea_auto_cloud/translations/en.json",
    "custom_components/midea_auto_cloud/translations/zh-Hans.json",
)
DEPLOYED_FILES = (
    # Preserve the deployed state verbatim, including backup residue, so the
    # artifact bundle reflects what was actually installed on the HA host.
    "custom_components/midea_auto_cloud/device_mapping/T0xD9.py",
    "custom_components/midea_auto_cloud/device_mapping/T0xD9.py.bak",
    "custom_components/midea_auto_cloud/translations/en.json",
    "custom_components/midea_auto_cloud/translations/zh-Hans.json",
)


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    raise RuntimeError(f"Could not find repo root from {start}")


def write_bytes(root: Path, relative_path: str, data: bytes) -> None:
    target = root / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def git_show(repo_root: Path, spec: str) -> bytes:
    result = subprocess.run(
        ["git", "show", spec],
        cwd=repo_root,
        check=True,
        capture_output=True,
    )
    return result.stdout


def normalize_header_path(path_token: str) -> str:
    if path_token == "/dev/null":
        return path_token
    if path_token.startswith("a/upstream/"):
        return "a/" + path_token[len("a/upstream/") :]
    if path_token.startswith("b/upstream/"):
        return "b/" + path_token[len("b/upstream/") :]
    if path_token.startswith("a/deployed/"):
        return "a/" + path_token[len("a/deployed/") :]
    if path_token.startswith("b/deployed/"):
        return "b/" + path_token[len("b/deployed/") :]
    return path_token


def normalize_patch_headers(patch_text: str) -> str:
    normalized_lines: list[str] = []
    for line in patch_text.splitlines(keepends=True):
        line_content = line.rstrip("\r\n")
        line_ending = line[len(line_content) :]

        if line_content.startswith("diff --git "):
            parts = line_content.split(" ", 3)
            if len(parts) == 4:
                normalized_lines.append(
                    " ".join(
                        (
                            parts[0],
                            parts[1],
                            normalize_header_path(parts[2]),
                            normalize_header_path(parts[3]),
                        )
                    )
                    + line_ending
                )
                continue

        if line_content.startswith("--- "):
            normalized_lines.append(
                f"--- {normalize_header_path(line_content[4:])}{line_ending}"
            )
            continue

        if line_content.startswith("+++ "):
            normalized_lines.append(
                f"+++ {normalize_header_path(line_content[4:])}{line_ending}"
            )
            continue

        normalized_lines.append(line)

    return "".join(normalized_lines)


def main() -> None:
    script_path = Path(__file__).resolve()
    artifact_root = script_path.parent.parent
    repo_root = find_repo_root(artifact_root)
    live_root = artifact_root / "live"
    patch_path = artifact_root / "patches" / "upstream-v0.3.3-to-deployed.patch"

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        upstream_root = temp_root / "upstream"
        deployed_root = temp_root / "deployed"

        for relative_path in UPSTREAM_FILES:
            write_bytes(
                upstream_root,
                relative_path,
                git_show(repo_root, f"{TAG}:{relative_path}"),
            )

        for relative_path in DEPLOYED_FILES:
            write_bytes(
                deployed_root,
                relative_path,
                (live_root / relative_path).read_bytes(),
            )

        result = subprocess.run(
            [
                "git",
                "diff",
                "--no-index",
                "--binary",
                "--full-index",
                "--no-ext-diff",
                "upstream/custom_components/midea_auto_cloud",
                "deployed/custom_components/midea_auto_cloud",
            ],
            cwd=temp_root,
            capture_output=True,
            check=False,
        )
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))

        patch_text = normalize_patch_headers(
            result.stdout.decode("utf-8", errors="surrogateescape")
        )
        if not patch_text.strip():
            raise RuntimeError("Generated patch is empty")

        patch_path.write_text(patch_text, encoding="utf-8", newline="\n")
        print(f"Wrote {patch_path}")


if __name__ == "__main__":
    main()
