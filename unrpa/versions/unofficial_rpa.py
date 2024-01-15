from typing import Tuple, Type

from unrpa.versions.version import Version
from unrpa.versions.official_rpa import RPA3


class RPA32(RPA3):
    """A slightly custom variant of RPA-3.0."""

    name = "RPA-3.2"
    header = b"RPA-3.2"

class RPA40(RPA3):
    """A slightly custom variant of RPA-3.0."""

    name = "RPA-4.0"
    header = b"RPA-4.0"

class RPAAsenheim(RPA3):
    """A slightly custom variant of RPA-3.0."""
    name = "RPA-Asenheim"
    # "asenheim" in a substitution cipher
    header = b"\x01\x13\x05\x0e\x08\x05\x09\x0d"

versions: Tuple[Type[Version], ...] = (RPA32, RPA40, RPAAsenheim)
