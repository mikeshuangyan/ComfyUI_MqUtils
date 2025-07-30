import torch

class CheckFP4Support:
    NAME = "MQ Check Fp4 Support"
    CATEGORY = "MQ Utils/System"
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("FP4 Support", )
    FUNCTION = "run"
    OUTPUT_IS_LIST = (False, )

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {}
        }

    def run(self):
        try:
            if torch.cuda.is_available():
                device = torch.cuda.current_device()
                capabilities = torch.cuda.get_device_capability(device)
                return ((int(capabilities[0]) > 9),)
        except Exception as e:
            pass
        return (False, )

NODE_CLASS_MAPPINGS = {
    "MqCheckFP4Support": CheckFP4Support,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MqCheckFP4Support": "MQ Check FP4 Support",
}
