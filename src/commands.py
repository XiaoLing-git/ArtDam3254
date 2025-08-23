from enum import Enum


class FunctionCode(Enum):
    """base function code statement."""

    InputRead = "04"
    StateRead = "03"
    SingleWrite = "06"
    MultiWrite = "10"
