from __future__ import annotations

import json
from pathlib import Path

import pytest


def _read_translation(repo_root: Path, language: str) -> dict:
    translation_path = repo_root / "custom_components" / "midea_auto_cloud" / "translations" / language
    return json.loads(translation_path.read_text(encoding="utf-8"))


def test_t0xd9_default_queries_include_db_and_dc(t0xd9_default_mapping: dict) -> None:
    queries = t0xd9_default_mapping["queries"]
    assert queries, "T0xD9 default queries should not be empty"

    query_types = []
    for index, query in enumerate(queries):
        assert isinstance(query, dict), f"T0xD9 query entry {index} should be a dict, got {type(query).__name__}"
        assert "query_type" in query, f"T0xD9 query entry {index} is missing query_type: {query}"
        query_types.append(query["query_type"])

    assert {"db", "dc"} <= set(query_types), (
        "T0xD9 default queries should include both drum channels; "
        f"got query types {sorted(query_types)}"
    )


def test_t0xd9_mapping_exposes_required_dual_drum_entities(t0xd9_default_mapping: dict) -> None:
    entities = t0xd9_default_mapping["entities"]
    required_by_platform = {
        "switch": {"db_wash_dry_link", "dc_appointment", "db_appointment"},
        "select": {"dc_program"},
        "number": {"dc_appointment_time", "db_appointment_time"},
        "sensor": {
            "dc_running_status",
            "dc_appointment_end_time",
            "db_appointment_end_time",
        },
    }

    missing = {
        platform: sorted(required - set(entities.get(platform, {})))
        for platform, required in required_by_platform.items()
        if required - set(entities.get(platform, {}))
    }
    assert not missing, f"T0xD9 is missing required D9 entities: {missing}"


def test_t0xd9_mapping_does_not_expose_dc_location_selection(t0xd9_default_mapping: dict) -> None:
    all_entity_keys = {
        entity_key
        for platform_entities in t0xd9_default_mapping["entities"].values()
        for entity_key in platform_entities
    }
    assert "dc_location_selection" not in all_entity_keys


@pytest.mark.parametrize("language", ["en.json", "zh-Hans.json"])
def test_t0xd9_translations_include_dual_drum_entity_keys(repo_root: Path, language: str) -> None:
    data = _read_translation(repo_root, language)
    required_by_platform = {
        "switch": {"db_wash_dry_link", "dc_appointment", "db_appointment"},
        "number": {"dc_appointment_time", "db_appointment_time"},
        "sensor": {"dc_running_status", "dc_appointment_end_time", "db_appointment_end_time"},
    }

    missing = {
        platform: sorted(required - set(data["entity"].get(platform, {})))
        for platform, required in required_by_platform.items()
        if required - set(data["entity"].get(platform, {}))
    }
    assert not missing, f"{language} is missing D9 translation keys in the expected platforms: {missing}"


@pytest.mark.parametrize("language", ["en.json", "zh-Hans.json"])
def test_t0xd9_translations_include_dc_program_states(repo_root: Path, language: str) -> None:
    data = _read_translation(repo_root, language)
    select_entities = data["entity"]["select"]

    assert "dc_program" in select_entities, f"{language} is missing entity.select.dc_program"

    states = select_entities["dc_program"].get("state", {})
    missing_states = sorted({"mixed_wash", "light_dry_silk"} - set(states))
    assert not missing_states, (
        f"{language} entity.select.dc_program.state is missing labels for {missing_states}"
    )
