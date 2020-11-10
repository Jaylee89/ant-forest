from enum import Enum, unique

class Operator(Enum):
    DETECT_DEVICE_CONNECTION = "DCD"
    CAPTURE_SCREENSHOTS = "CS"

class WorkFlow(Enum):
    CAPTURE_IMAGE = 0
    MATCH = 1
    TAP = 3
    SCROLL = 4


