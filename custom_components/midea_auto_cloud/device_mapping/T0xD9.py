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
                    "translation_key": "wash_dry_link",
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
                    "translation_key": "ai_dry",
                },
                "dc_smell": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": [0, 1],
                    "translation_key": "smell",
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
                    "translation_key": "cycle_memory",
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
                        "棉织物": {"dc_program": "cotton"},
                        "化纤": {"dc_program": "fiber"},
                        "混合洗": {"dc_program": "mixed_wash"},
                        "牛仔": {"dc_program": "jean"},
                        "床单": {"dc_program": "bedsheet"},
                        "户外服": {"dc_program": "outdoor"},
                        "羽绒服": {"dc_program": "down_jacket"},
                        "毛绒": {"dc_program": "plush"},
                        "羊毛": {"dc_program": "wool"},
                        "除湿": {"dc_program": "dehumidify"},
                        "冷风清新": {"dc_program": "cold_air_fresh_air"},
                        "热风烘干": {"dc_program": "hot_air_dry"},
                        "运动服": {"dc_program": "sport_clothes"},
                        "内衣": {"dc_program": "underwear"},
                        "婴童装": {"dc_program": "baby_clothes"},
                        "衬衫": {"dc_program": "shirt"},
                        "标准": {"dc_program": "standard"},
                        "快烘": {"dc_program": "quick_dry"},
                        "清新": {"dc_program": "fresh_air"},
                        "低温烘": {"dc_program": "low_temp_dry"},
                        "节能烘": {"dc_program": "eco_dry"},
                        "智能烘": {"dc_program": "intelligent_dry"},
                        "蒸汽护理": {"dc_program": "steam_care"},
                        "大物": {"dc_program": "big"},
                        "定时烘": {"dc_program": "fixed_time_dry"},
                        "夜间烘": {"dc_program": "night_dry"},
                        "支架烘": {"dc_program": "bracket_dry"},
                        "西裤": {"dc_program": "western_trouser"},
                        "除潮": {"dc_program": "dehumidification"},
                        "丝绸": {"dc_program": "silk"},
                        "筒自洁": {"dc_program": "bucket_self_clean"},
                        "离子除菌": {"dc_program": "ion_degerm"},
                        "AI智能烘": {"dc_program": "ai_intelligent_dry"},
                        "小件": {"dc_program": "small"},
                        "夹克": {"dc_program": "jacket"},
                        "空气洗": {"dc_program": "air_wash"},
                        "毛巾": {"dc_program": "towel"},
                        "四件套": {"dc_program": "four_piece_suit"},
                        "轻柔烘": {"dc_program": "light_dry"},
                        "除菌": {"dc_program": "degerm"},
                        "羊毛护理": {"dc_program": "wool_care"},
                        "晒被": {"dc_program": "sun_quilt"},
                        "工装": {"dc_program": "uniforms"},
                        "轻柔烘羊毛": {"dc_program": "light_dry_wool"},
                        "轻柔烘衬衫": {"dc_program": "light_dry_shirt"},
                        "轻柔烘羽绒": {"dc_program": "light_dry_down_jacket"},
                        "轻柔烘丝绸": {"dc_program": "light_dry_silk"},
                        "轻柔烘大物": {"dc_program": "light_dry_big"},
                        "轻柔烘棉织物": {"dc_program": "light_dry_cotton"},
                        "轻柔烘皮草": {"dc_program": "light_dry_mink_skin"},
                        "轻柔烘毛巾": {"dc_program": "light_dry_towel"},
                        "轻柔烘西装": {"dc_program": "light_dry_suit"},
                        "轻柔烘睡衣": {"dc_program": "light_dry_pajamas"},
                        "轻柔烘婴童暖衣": {"dc_program": "light_dry_baby_warm_clothe"},
                        "轻柔烘季节驱散": {"dc_program": "light_dry_seasonal_dispel"},
                        "轻柔烘毛绒玩具": {"dc_program": "light_dry_plush_toy"},
                        "轻柔烘皮革护理": {"dc_program": "light_dry_leather_clothe_care"},
                        "轻柔烘毛呢大衣": {"dc_program": "light_dry_wool_coat"},
                        "轻柔烘蚕丝被": {"dc_program": "light_dry_silk_quilt"},
                        "轻柔烘派克服": {"dc_program": "light_dry_pizex"},
                        "轻柔烘雪纺": {"dc_program": "light_dry_chiffon"},
                        "速烘衣物": {"dc_program": "quick_dry_clothes"},
                        "瑜伽服": {"dc_program": "yoga_clothes"},
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
                },
                "dc_location_selection": {
                    "options": {
                        "left": {"dc_location_selection": "left"},
                        "right": {"dc_location_selection": "right"}
                    }
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
