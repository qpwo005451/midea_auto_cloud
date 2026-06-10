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

        patch_text = result.stdout.decode("utf-8", errors="surrogateescape")
        patch_text = patch_text.replace("a/upstream/", "a/")
        patch_text = patch_text.replace("b/upstream/", "b/")
        patch_text = patch_text.replace("a/deployed/", "a/")
        patch_text = patch_text.replace("b/deployed/", "b/")
        if not patch_text.strip():
            raise RuntimeError("Generated patch is empty")

        patch_path.write_text(patch_text, encoding="utf-8", newline="\n")
        print(f"Wrote {patch_path}")


if __name__ == "__main__":
    main()
