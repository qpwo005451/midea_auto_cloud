from homeassistant.const import Platform, UnitOfElectricPotential, UnitOfTemperature, UnitOfTime
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass

DEVICE_MAPPING = {
    "default": {
        "rationale": ["off", "on"],
        "queries": [{"query_type": "db"}, {"query_type": "dc"}],
        "calculate": {
            "get": [
                {
                    "lvalue": "[remaining_time]",
                    "rvalue": "[db_remain_time]"
                }
            ],
            "set": {
            }
        },
        "entities": {
            Platform.BINARY_SENSOR: {
                "db_door_opened": {
                    "device_class": BinarySensorDeviceClass.OPENING,
                    "translation_key": "door_opened"
                },
                "db_bucket_water_overheating": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                    "translation_key": "bucket_water_overheating"
                },
                "db_drying_tunnel_overheating": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                    "translation_key": "drying_tunnel_overheating"
                },
                "db_detergent_needed": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                    "translation_key": "detergent_lack"
                }
            },
            Platform.SWITCH: {
                "db_power": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "db_control_status": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": ["pause", "start"],
                    "translation_key": "db_control_status",
                },
                "db_baby_lock": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "db_baby_lock",
                },
                "db_wash_dry_link": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "db_wash_dry_link",
                },
                "dc_power": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
                "dc_control_status": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": ["pause", "start"],
                    "translation_key": "dc_control_status",
                },
                "dc_baby_lock": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "dc_baby_lock",
                },
                "dc_steam": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_prevent_wrinkle": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_ai": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "dc_ai",
                },
                "dc_smell": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "dc_smell",
                },
                "dc_intelligent_dampproof": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_multidimensional_sterilize": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_cycle_memory": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "dc_cycle_memory",
                },
                "dc_light": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_sterilize": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_remind_sound": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                },
                "dc_appointment": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "dc_appointment",
                },
                "db_appointment": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "db_appointment",
                },
            },
            Platform.SELECT: {
                "db_location_selection": {
                    "options": {
                        "left": {"db_location_selection": "left"},
                        "right": {"db_location_selection": "right"}
                    }
                },
                "db_program": {
                    "options": {
                        "baby_clothes": {"db_program": "baby_clothes"},
                        "baby_clothes_dry": {"db_program": 151},
                        "clean_stains": {"db_program": "clean_stains"},
                        "cold_wash": {"db_program": "cold_wash"},
                        "cook_wash": {"db_program": "cook_wash"},
                        "fast_wash": {"db_program": 137},
                        "hot_wind_dry": {"db_program": 153},
                        "rinsing_dehydration": {"db_program": "rinsing_dehydration"},
                        "self_wash_5": {"db_program": "self_wash_5"},
                        "single_dehytration": {"db_program": "single_dehytration"},
                        "single_drying": {"db_program": "single_drying"},
                        "small_wash_dry": {"db_program": 138},
                        "socks": {"db_program": 148},
                        "standard": {"db_program": "standard"},
                        "underpants": {"db_program": 156},
                        "underwear": {"db_program": "underwear"},
                        "water_ssp": {"db_program": "water_ssp"}
                   }
                },
                "db_temperature": {
                    "options": {
                        "冷水": {"db_temperature": 0},
                        "30℃": {"db_temperature": 3},
                        "40℃": {"db_temperature": 4},
                        "60℃": {"db_temperature": 5},
                        "95℃": {"db_temperature": 6}
                    },
                    "translation_key": "temperature"
                },
                "db_detergent": {
                    "options": {
                        "关闭": {"db_detergent": 0},
                        "L1": {"db_detergent": 1},
                        "L2": {"db_detergent": 2},
                        "L3": {"db_detergent": 3}
                    },
                    "translation_key": "detergent"
                },
                "db_dehydration_speed": {
                    "options": {
                        "免脱水": {"db_dehydration_speed": 0},
                        "800转": {"db_dehydration_speed": 3},
                        "1000转": {"db_dehydration_speed": 4}
                    },
                    "translation_key": "dehydration_speed"
                },
                "db_rinse_count": {
                    "options": {
                        "1次": {"db_rinse_count": 1},
                        "2次": {"db_rinse_count": 2},
                        "3次": {"db_rinse_count": 3},
                        "4次": {"db_rinse_count": 4},
                        "5次": {"db_rinse_count": 5}
                    },
                    "translation_key": "soak_count"
                },
                "db_dry": {
                    "options": {
                        "关闭": {"db_dry": 0},
                        "智能": {"db_dry": 1},
                        "定时240": {"db_dry": 12},
                        "定时180": {"db_dry": 11},
                        "定时120": {"db_dry": 7},
                        "定时60": {"db_dry": 5},
                        "定时30": {"db_dry": 4}
                    }
                },
                "dc_program": {
                    "options": {
                        "cotton": {"dc_program": "cotton"},
                        "fiber": {"dc_program": "fiber"},
                        "mixed_wash": {"dc_program": "mixed_wash"},
                        "jean": {"dc_program": "jean"},
                        "bedsheet": {"dc_program": "bedsheet"},
                        "outdoor": {"dc_program": "outdoor"},
                        "down_jacket": {"dc_program": "down_jacket"},
                        "plush": {"dc_program": "plush"},
                        "wool": {"dc_program": "wool"},
                        "dehumidify": {"dc_program": "dehumidify"},
                        "cold_air_fresh_air": {"dc_program": "cold_air_fresh_air"},
                        "hot_air_dry": {"dc_program": "hot_air_dry"},
                        "sport_clothes": {"dc_program": "sport_clothes"},
                        "underwear": {"dc_program": "underwear"},
                        "baby_clothes": {"dc_program": "baby_clothes"},
                        "shirt": {"dc_program": "shirt"},
                        "standard": {"dc_program": "standard"},
                        "quick_dry": {"dc_program": "quick_dry"},
                        "fresh_air": {"dc_program": "fresh_air"},
                        "low_temp_dry": {"dc_program": "low_temp_dry"},
                        "eco_dry": {"dc_program": "eco_dry"},
                        "intelligent_dry": {"dc_program": "intelligent_dry"},
                        "steam_care": {"dc_program": "steam_care"},
                        "big": {"dc_program": "big"},
                        "fixed_time_dry": {"dc_program": "fixed_time_dry"},
                        "night_dry": {"dc_program": "night_dry"},
                        "bracket_dry": {"dc_program": "bracket_dry"},
                        "western_trouser": {"dc_program": "western_trouser"},
                        "dehumidification": {"dc_program": "dehumidification"},
                        "silk": {"dc_program": "silk"},
                        "bucket_self_clean": {"dc_program": "bucket_self_clean"},
                        "ion_degerm": {"dc_program": "ion_degerm"},
                        "ai_intelligent_dry": {"dc_program": "ai_intelligent_dry"},
                        "small": {"dc_program": "small"},
                        "jacket": {"dc_program": "jacket"},
                        "air_wash": {"dc_program": "air_wash"},
                        "towel": {"dc_program": "towel"},
                        "four_piece_suit": {"dc_program": "four_piece_suit"},
                        "light_dry": {"dc_program": "light_dry"},
                        "degerm": {"dc_program": "degerm"},
                        "wool_care": {"dc_program": "wool_care"},
                        "sun_quilt": {"dc_program": "sun_quilt"},
                        "uniforms": {"dc_program": "uniforms"},
                        "light_dry_wool": {"dc_program": "light_dry_wool"},
                        "light_dry_shirt": {"dc_program": "light_dry_shirt"},
                        "light_dry_down_jacket": {"dc_program": "light_dry_down_jacket"},
                        "light_dry_silk": {"dc_program": "light_dry_silk"},
                        "light_dry_big": {"dc_program": "light_dry_big"},
                        "light_dry_cotton": {"dc_program": "light_dry_cotton"},
                        "light_dry_mink_skin": {"dc_program": "light_dry_mink_skin"},
                        "light_dry_towel": {"dc_program": "light_dry_towel"},
                        "light_dry_suit": {"dc_program": "light_dry_suit"},
                        "light_dry_pajamas": {"dc_program": "light_dry_pajamas"},
                        "light_dry_baby_warm_clothe": {"dc_program": "light_dry_baby_warm_clothe"},
                        "light_dry_seasonal_dispel": {"dc_program": "light_dry_seasonal_dispel"},
                        "light_dry_plush_toy": {"dc_program": "light_dry_plush_toy"},
                        "light_dry_leather_clothe_care": {"dc_program": "light_dry_leather_clothe_care"},
                        "light_dry_wool_coat": {"dc_program": "light_dry_wool_coat"},
                        "light_dry_silk_quilt": {"dc_program": "light_dry_silk_quilt"},
                        "light_dry_pizex": {"dc_program": "light_dry_pizex"},
                        "light_dry_chiffon": {"dc_program": "light_dry_chiffon"},
                        "quick_dry_clothes": {"dc_program": "quick_dry_clothes"},
                        "yoga_clothes": {"dc_program": "yoga_clothes"},
                    },
                    "translation_key": "dc_program"
                },
                "dc_dry_time": {
                    "options": {
                        "关闭": {"dc_dry_time": 0},
                        "30分钟": {"dc_dry_time": 30},
                        "60分钟": {"dc_dry_time": 60},
                        "90分钟": {"dc_dry_time": 90},
                        "120分钟": {"dc_dry_time": 120},
                        "180分钟": {"dc_dry_time": 180},
                        "240分钟": {"dc_dry_time": 240},
                    },
                    "translation_key": "dry_time"
                },
                "dc_temperature_level": {
                    "options": {
                        "低温": {"dc_temperature_level": 0},
                        "中温": {"dc_temperature_level": 1},
                        "高温": {"dc_temperature_level": 2},
                    },
                    "translation_key": "temperature_level"
                },
                "dc_smell_time": {
                    "options": {
                        "关闭": {"dc_smell_time": 0},
                        "30分钟": {"dc_smell_time": 30},
                        "60分钟": {"dc_smell_time": 60},
                        "90分钟": {"dc_smell_time": 90},
                        "120分钟": {"dc_smell_time": 120},
                    },
                    "translation_key": "smell_time"
                }
            },
            Platform.NUMBER: {
                "dc_appointment_time": {
                    "min": 30,
                    "max": 1440,
                    "step": 30,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "translation_key": "dc_appointment_time",
                },
                "db_appointment_time": {
                    "min": 30,
                    "max": 1440,
                    "step": 30,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "translation_key": "db_appointment_time",
                },
            },
            Platform.SENSOR: {
                "db_remain_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "db_progress": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": "%",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "db_running_status": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "running_status"
                },
                "db_error_code": {
                    "device_class": SensorDeviceClass.ENUM
                },
                "dc_remain_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "dc_running_status": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "dc_running_status"
                },
                "dc_dry_status": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "dc_dry_status"
                },
                "dc_error_code": {
                    "device_class": SensorDeviceClass.ENUM
                },
                "dc_intensity": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "dc_material": {
                    "device_class": SensorDeviceClass.ENUM,
                },
                "dc_appointment_end_time": {
                    "device_class": SensorDeviceClass.TIMESTAMP,
                    "translation_key": "dc_appointment_end_time",
                },
                "db_appointment_end_time": {
                    "device_class": SensorDeviceClass.TIMESTAMP,
                    "translation_key": "db_appointment_end_time",
                }
            }
        }
    }
}
