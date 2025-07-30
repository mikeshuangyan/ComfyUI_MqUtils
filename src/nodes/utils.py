import codecs

class TextSplitByDelimiter:
    NAME = "MQ Text Splitter"
    CATEGORY = "MQ Utils/Utils"
    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("STRING LIST", "LENGTH",)
    FUNCTION = "run"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True, False)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True,"dynamicPrompts": False}),
                "delimiter":("STRING", {"multiline": False,"default":",","dynamicPrompts": False}),
                "start_index": ("INT", {"default": 0, "min": 0, "max": 1000}),
                "skip_every": ("INT", {"default": 0, "min": 0, "max": 10}),
                "max_count": ("INT", {"default": 10, "min": 1, "max": 1000}),
            }
        }

    def run(self, text, delimiter, start_index, skip_every, max_count):
        delimiter = codecs.decode(delimiter, 'unicode_escape')
        arr = [item.strip() for item in text.split(delimiter) if item.strip()]
        arr = arr[start_index:start_index + max_count * (skip_every + 1):(skip_every + 1)]
        return (arr, len(arr))

class IntSwitch:
    NAME = "MQ Int Switch"
    CATEGORY = "MQ Utils/Utils"
    RETURN_TYPES = ("INT", )
    RETURN_NAMES = ("VALUE", )
    FUNCTION = "run"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, )

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "if_true": ("INT", {"default": 0}),
                "if_false": ("INT", {"default": 0}),
                "condition": ("BOOLEAN", {"default": True}),
            }
        }

    def run(self, if_true, if_false, condition):
        val = if_true
        if not condition:
            val = if_false
        return (val, )

class IntToString:
    NAME = "MQ Int To String"
    CATEGORY = "MQ Utils/Utils"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("STRING", )
    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int": (
                    "INT", {
                        "default": 0,
                        "min": -1e9,
                        "max": 1e9,
                        "step": 1,
                        "forceInput": True,
                    }),
            }
        }

    def run(self, int):
        return (str(int), )

NODE_CLASS_MAPPINGS = {
    "MqTextSplitter": TextSplitByDelimiter,
    "MqIntSwitch": IntSwitch,
    "MqIntToString": IntToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MqTextSplitter": "MQ Text Splitter",
    "MqIntSwitch": "MQ Int Switch",
    "MqIntToString": "MQ Int To String",
}
