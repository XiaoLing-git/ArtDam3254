"""Main function entry, mainly used for debugging."""

from pprint import pprint

from src.commands import FunctionCode
from src.utils import assert_function_code

if __name__ == "__main__":
    assert_function_code(FunctionCode.InputRead)
    # print(FunctionCode.get_all_values()[0].value)
