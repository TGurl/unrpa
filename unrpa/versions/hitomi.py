from typing import BinaryIO, Optional, Tuple, Type

from unrpa.versions.version import Version
from unrpa.versions.official_rpa import RPA3
from unrpa.view import ArchiveView


class RPA91(RPA3):
    """Variant of RPA-3.0 used in Hitomi's Sick Pleasure [PantsuDelver]."""

    name = "RPA-9.1"
    header = b"RPA-9.1"
    extra_key = 0x12ACAC4076A760B9
    xorpad = [
        0x35, 0xF1, 0x32, 0xD7, 0xB6, 0x5C, 0xBA, 0x9E,
        0xB9, 0xDF, 0x47, 0xA2, 0xE1, 0xFB, 0xEF, 0x7C,
        0x99, 0x1A, 0x16, 0x5A, 0xC1, 0xEC, 0x0A, 0x8A,
        0xB4, 0x9A, 0x73, 0xA2, 0xE6, 0x0D, 0xF4, 0x08
    ]

    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]:
        line = archive.readline()
        parts = line.split()
        offset = int(parts[1], 16) ^ RPA91.extra_key
        key = 0xA0C11124
        return offset, key

    def postprocess(self, source: ArchiveView, sink: BinaryIO) -> None:
        for segment in iter(source.read1, b""):
            segment = bytes(
                [segment[i] ^ self.xorpad[i % 32] for i in range(len(segment))]
            )
            sink.write(segment)


versions: Tuple[Type[Version], ...] = (RPA91,)
