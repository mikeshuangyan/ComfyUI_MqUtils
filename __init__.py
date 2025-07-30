__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__author__ = """ComfyUI_MqUtils"""
__email__ = "mikeshuangyan@gmail.com"
__version__ = "0.0.2"

import importlib

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

nodes_list = ["utils", "sys_utils"]
# locale = {}
for module_name in nodes_list:
    imported_module = importlib.import_module(".src.nodes.{}".format(module_name), __name__)
    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}
