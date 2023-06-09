
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class OneWireError(Exception): ...
class OneWire:
    def __init__(self, pin: machine.Pin) -> None: ...
    def reset(self, required: Any=bool) -> Any: ...
        #   0: return reset
        # ? 0: return reset
    def readbit(self) -> Any: ...
        #   0: return _ow.readbit(self.pin)
        # ? 0: return _ow.readbit(self.pin)
    def readbyte(self) -> Any: ...
        #   0: return _ow.readbyte(self.pin)
        # ? 0: return _ow.readbyte(self.pin)
    def readinto(self, buf: Any) -> None: ...
    def writebit(self, value: Any) -> Any: ...
        #   0: return _ow.writebit(self.pin,value)
        # ? 0: return _ow.writebit(self.pin, value)
    def writebyte(self, value: Any) -> Any: ...
        #   0: return _ow.writebyte(self.pin,value)
        # ? 0: return _ow.writebyte(self.pin, value)
    def write(self, buf: Any) -> None: ...
    def select_rom(self, rom: Any) -> None: ...
    def scan(self) -> Any: ...
        #   0: return devices
        # ? 0: return devices
    def _search_rom(self, l_rom: Any, diff: Any) -> Union[Tuple[Any, Any], Tuple[None, number]]: ...
    def crc8(self, data: Any) -> Any: ...
        #   0: return _ow.crc8(data)
        # ? 0: return _ow.crc8(data)
