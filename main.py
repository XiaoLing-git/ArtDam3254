"""Main function entry, mainly used for debugging."""

from pprint import pprint

from src.commands import FunctionCode

if __name__ == "__main__":
    print(FunctionCode.get_all_values()[0].value)
