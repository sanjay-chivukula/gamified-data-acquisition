from dataclasses import dataclass
from enum import Enum


class GameState(Enum):
    RUNNING = 0
    QUIT = 1


class FaceState(Enum):
    NOT_VISIBLE = 0
    VISIBLE = 1
    ALIGNED = 2


class CameraState(Enum):
    NOT_AVAILABLE = 0
    AVAILABLE = 1


@dataclass
class SharedEventStateData:
    game_state: GameState
    face_state: FaceState
    camera_state: CameraState
    is_capture: bool
    target_pos: tuple
