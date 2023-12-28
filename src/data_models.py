from dataclasses import dataclass
from typing import Tuple

import numpy.typing as npt


@dataclass
class CaptureSignalPayload:
    is_capture: bool
    target_pos: Tuple[int, int]
    frame: npt.NDArray
