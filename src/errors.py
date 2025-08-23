import logging

logger = logging.getLogger(__name__)


class ArtException(Exception):
    """
    Art DAM 3524 base exception.
    """

    def __init__(self, msg: str) -> None:
        self._msg = msg

    def __str__(self) -> str:
        logger.error(f"{self.__class__.__name__} - {self._msg}")
        return self._msg

    def __repr__(self) -> str:
        return self._msg
