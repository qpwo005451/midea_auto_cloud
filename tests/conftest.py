from __future__ import annotations

import importlib.util
import sys
import types
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import pytest


_MISSING = object()
_HOMEASSISTANT_MODULE_NAMES = (
    "homeassistant",
    "homeassistant.const",
    "homeassistant.components",
    "homeassistant.components.sensor",
    "homeassistant.components.binary_sensor",
    "homeassistant.components.switch",
)


def _build_homeassistant_stubs() -> dict[str, types.ModuleType]:
    homeassistant = types.ModuleType("homeassistant")
    components = types.ModuleType("homeassistant.components")
    const = types.ModuleType("homeassistant.const")
    homeassistant.__path__ = []
    components.__path__ = []

    class Platform:
        BINARY_SENSOR = "binary_sensor"
        SWITCH = "switch"
        SELECT = "select"
        SENSOR = "sensor"
        NUMBER = "number"

    class UnitOfElectricPotential:
        pass

    class UnitOfTemperature:
        pass

    class UnitOfTime:
        MINUTES = "min"

    const.Platform = Platform
    const.UnitOfElectricPotential = UnitOfElectricPotential
    const.UnitOfTemperature = UnitOfTemperature
    const.UnitOfTime = UnitOfTime

    sensor = types.ModuleType("homeassistant.components.sensor")
    sensor.SensorStateClass = type("SensorStateClass", (), {"MEASUREMENT": "measurement"})
    sensor.SensorDeviceClass = type(
        "SensorDeviceClass",
        (),
        {
            "DURATION": "duration",
            "BATTERY": "battery",
            "ENUM": "enum",
            "TIMESTAMP": "timestamp",
        },
    )

    binary_sensor = types.ModuleType("homeassistant.components.binary_sensor")
    binary_sensor.BinarySensorDeviceClass = type(
        "BinarySensorDeviceClass",
        (),
        {
            "OPENING": "opening",
            "PROBLEM": "problem",
        },
    )

    switch = types.ModuleType("homeassistant.components.switch")
    switch.SwitchDeviceClass = type("SwitchDeviceClass", (), {"SWITCH": "switch"})

    homeassistant.const = const
    homeassistant.components = components
    components.sensor = sensor
    components.binary_sensor = binary_sensor
    components.switch = switch

    return {
        "homeassistant": homeassistant,
        "homeassistant.const": const,
        "homeassistant.components": components,
        "homeassistant.components.sensor": sensor,
        "homeassistant.components.binary_sensor": binary_sensor,
        "homeassistant.components.switch": switch,
    }


@contextmanager
def _stub_homeassistant_modules() -> Iterator[None]:
    original_modules = {
        module_name: sys.modules.get(module_name, _MISSING)
        for module_name in _HOMEASSISTANT_MODULE_NAMES
    }
    sys.modules.update(_build_homeassistant_stubs())

    try:
        yield
    finally:
        for module_name, original_module in original_modules.items():
            if original_module is _MISSING:
                sys.modules.pop(module_name, None)
            else:
                sys.modules[module_name] = original_module


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def t0xd9_default_mapping(repo_root: Path) -> dict:
    with _stub_homeassistant_modules():
        module_path = repo_root / "custom_components" / "midea_auto_cloud" / "device_mapping" / "T0xD9.py"
        spec = importlib.util.spec_from_file_location("tests_t0xd9_mapping", module_path)
        assert spec is not None and spec.loader is not None

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.DEVICE_MAPPING["default"]
