from pathlib import Path


def get_file_path_depth(target: Path, level: int) -> list[str]:
    """
    慎用！用于获取逐级目录的名字，
    :param target: 文件路径，不能是文件夹
    :param level: 文件在当前项目的深度， factory_tools 文件为第一级
    :return: 列表[文件夹名字]
    """
    results: list[str] = []
    current_path = target
    for _ in range(level - 1):
        current_path = current_path.parent
        results.insert(0, current_path.name)
    return results
