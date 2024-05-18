import board

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

name = str(getmount('/').label)
is_right = True if name.endswith('R') else False

# GPIO to key mapping - each line is a new row.
_KEY_CFG_LEFT = [
    board.GP0, board.GP1, board.GP2, board.GP5, board.GP4, board.GP3,
    board.GP28, board.GP6, board.GP27, board.GP7, board.GP26, board.GP8,
    board.GP22, board.GP9, board.GP21, board.GP10, board.GP20, board.GP11,
    board.GP19, board.GP12, board.GP18
]

_KEY_CFG_RIGHT = [
    board.GP3, board.GP4, board.GP5, board.GP2, board.GP1, board.GP0,
    board.GP8, board.GP26, board.GP7, board.GP27, board.GP6, board.GP28,
    board.GP11, board.GP20, board.GP10, board.GP21, board.GP9, board.GP22,
    board.GP18, board.GP12, board.GP19
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins = _KEY_CFG_RIGHT if is_right == True else _KEY_CFG_LEFT
        )

    # flake8: noqa
    # fmt: off
    coord_mapping = [
     0,  1,  2,  3,  4,  5,   21, 22, 23, 24, 25, 26,
     6,  7,  8,  9, 10, 11,   27, 28, 29, 30, 31, 32,
    12, 13, 14, 15, 16, 17,   33, 34, 35, 36, 37, 38,
                18, 19, 20,   39, 40, 41
    ]
