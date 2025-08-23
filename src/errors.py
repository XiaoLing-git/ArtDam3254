import logging

logger = logging.getLogger(__name__)


class ArtException(Exception):
    """
    Art DAM 3524 base exception.
    """

    def __init__(self, msg: str) -> None:
        self._msg = msg
        logger.error(f"{self.__class__.__name__} - {self._msg}")

    def __str__(self) -> str:
        return self._msg

    def __repr__(self) -> str:
        return self._msg


class ModBusCrc16Exception(ArtException):
    """
    ModBus Crc16 Exception.
    """


class HexCodeException(ArtException):
    """
    Hex Code Exception.
    """


class DeviceAddressException(ArtException):
    """
    Device Address Exception.
    """


class RegisterAddressException(ArtException):
    """
    Register Address Exception.
    """


class DeviceConnectionException(ArtException):
    """
    Device Connection Exception.
    """


class DeviceReconnectionException(ArtException):
    """
    Device Reconnection Exception.
    """


class DeviceDisconnectionException(ArtException):
    """
    Device Discconnection Exception.
    """
