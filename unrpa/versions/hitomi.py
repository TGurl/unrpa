from typing import BinaryIO, Optional, Tuple, Type

from unrpa.versions.version import Version
from unrpa.versions.official_rpa import RPA3
from unrpa.view import ArchiveView


class RPA91(RPA3):
    """Variant of RPA-3.0 used in Hitomi's Sick Pleasure [PantsuDelver]."""

    name = "RPA-9.1"
    header = b"RPA-9.1"
    # Values hardcoded in librenpython.[so/dll]
    # TODO: automated extraction
    main_key = 0x126E6680
    extra_key = 0x46D96FA8FAD5262B
    xorpad = [
        0xF6, 0x02, 0x3F, 0x76, 0x4D, 0x0B, 0x80, 0x1B,
        0x29, 0x10, 0xDF, 0xDD, 0x74, 0x85, 0xDE, 0xA6,
        0xDB, 0x7D, 0xC8, 0x19, 0xBA, 0xE3, 0xD0, 0x63,
        0x2F, 0x50, 0xE7, 0x55, 0xB4, 0x67, 0x0B, 0xFB,
    ]

    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]:
        line = archive.readline()
        parts = line.split()
        offset = int(parts[1], 16) ^ RPA91.extra_key
        return offset, RPA91.main_key

    def postprocess(self, source: ArchiveView, sink: BinaryIO) -> None:
        for segment in iter(source.read1, b""):
            segment = bytes(
                [segment[i] ^ self.xorpad[i % 32] for i in range(len(segment))]
            )
            sink.write(segment)


versions: Tuple[Type[Version], ...] = (RPA91,)
