from dataclasses import dataclass
from datetime import datetime
from typing import Tuple

import numpy as np


@dataclass
class CaptureSignalPayload:
    is_capture: bool
    target_pos: Tuple[int, int]
    frame: np.ndarray
    timestamp: datetime


@dataclass
class ImageLabelData:
    image: np.ndarray
    target_pos: Tuple
    face_pos: Tuple
    face_bounds: Tuple
