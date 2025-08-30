""""""

import sys
from pathlib import Path

this_dir = Path(__file__).parent


def get_os() -> str:
    """"""
    return sys.platform


def rename_wheel() -> None:
    """"""
    version = get_os()
    print(version)
    target_str: str = "name ="
    final_content: list[str] = []
    with open(
        this_dir / "pyproject.toml",
        "r",
    ) as f:
        content = f.readlines()
        for line in content:
            if target_str in line:
                line = f'name = "Art-Dam-3254_{version}"\n'
            final_content.append(line)
    with open(
        "pyproject.toml",
        "w",
    ) as f:
        f.writelines(final_content)


if __name__ == "__main__":
    rename_wheel()
