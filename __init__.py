__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]

__version__ = "0.0.4"

import importlib
import logging

logger = logging.getLogger(__name__)

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODES_LIST = ["utils", "sys_utils"]

for module_name in NODES_LIST:
    try:
        imported_module = importlib.import_module(f".src.nodes.{module_name}", __name__)
        NODE_CLASS_MAPPINGS.update(imported_module.NODE_CLASS_MAPPINGS)
        NODE_DISPLAY_NAME_MAPPINGS.update(imported_module.NODE_DISPLAY_NAME_MAPPINGS)
    except Exception as e:
        logger.warning(f"Failed to import module {module_name}: {e}")
