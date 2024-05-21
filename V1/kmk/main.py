import board

from kb import KMKKeyboard, is_right

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide

from kmk.modules.holdtap import HoldTap
from kmk.modules.combos import Combos, Chord
from kmk.handlers.sequences import simple_key_sequence as sks

keyboard = KMKKeyboard()

# Split
split_side = SplitSide.RIGHT if is_right else SplitSide.LEFT

split = Split(
    split_side=split_side,
    split_target_left=True,
    uart_interval=20,
    data_pin=board.GP17,  # RX
    data_pin2=board.GP16,  # TX
    uart_flip=False,
    use_pio=False,
)

keyboard.modules.append(split)

# Layers
layers = Layers()
keyboard.modules.append(layers)


# HoldTap
holdtap = HoldTap()
holdtap.tap_time = 175
keyboard.modules.append(holdtap)


# Key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# Mod-taps and layer-taps
# Left hand HRM
A_SFT = KC.HT(KC.A, KC.LSFT)
S_CTR = KC.HT(KC.S, KC.LCTRL)
D_GUI = KC.HT(KC.D, KC.LGUI)
V_VIM = KC.LT(3, KC.V)
F_SYM = KC.LT(1, KC.F)

# Left hand thumbs
SPC_NAV = KC.LT(2, KC.SPC)
TAB_ALT = KC.HT(KC.TAB, KC.LALT)

# Right hand HRM
J_SYM = KC.LT(1, KC.J)
K_GUI = KC.HT(KC.K, KC.RGUI)
L_CTR = KC.HT(KC.L, KC.RCTRL)
M_VIM = KC.LT(3, KC.M)
SCLN_SFT = KC.HT(KC.SCLN, KC.RSFT)

# Right hand thumbs
DEL_ALT = KC.HT(KC.DEL, KC.RALT)
ENT_NAV = KC.LT(2, KC.ENT)
BSP_TMX = KC.LT(4, KC.BSPC)

# Vi-style combos
combos = Combos()

combos.combos = [
    Chord((V_VIM, M_VIM), KC.TG(3)),  # Toggle quasi-Vim layer
    Chord((M_VIM, KC.G), sks((KC.EQL, KC.RABK))),  # => symbol
    Chord((M_VIM, KC.T), sks((KC.MINS, KC.RABK))),  # -> symbol
    Chord((KC.N, KC.G), sks((KC.EXLM, KC.EQL))),  # != symbol
]

keyboard.modules.append(combos)

NXT_W = KC.LCTRL(KC.RIGHT)
PRV_W = KC.LCTRL(KC.LEFT)
O_INP = sks((KC.END, KC.ENT, KC.TO(0)))
I_INP = KC.TO(0)
U_UND = KC.LCTRL(KC.Z)

# TMUX
TM_SCR0 = sks((KC.LCTRL(KC.B), KC.N0))
TM_SCR1 = sks((KC.LCTRL(KC.B), KC.N1))
TM_SCR2 = sks((KC.LCTRL(KC.B), KC.N2))
TM_SCR3 = sks((KC.LCTRL(KC.B), KC.N3))
TM_SCR4 = sks((KC.LCTRL(KC.B), KC.N4))
TM_SCR5 = sks((KC.LCTRL(KC.B), KC.N5))
TM_SCR6 = sks((KC.LCTRL(KC.B), KC.N6))
TM_CRT = sks((KC.LCTRL(KC.B), KC.C))

# fmt: off
keyboard.keymap = [
    [  # QWERTY
       #XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        KC.LBRC,  KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                         KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.RBRC, \
        KC.UNDS,  A_SFT,    S_CTR,    D_GUI,    F_SYM,    KC.G,                         KC.H,     J_SYM,    K_GUI,    L_CTR,    SCLN_SFT, KC.DQT,  \
        KC.COLN,  KC.Z,     KC.X,     KC.C,     V_VIM,    KC.B,                         KC.N,     M_VIM,    KC.COMM,  KC.DOT,   KC.SLSH,  KC.BSLS, \
                                                KC.ESC,   SPC_NAV,  TAB_ALT,  DEL_ALT,  ENT_NAV,  BSP_TMX,
    ],
    [  # SYMBOLS
       #XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        KC.SLSH,  KC.HASH,  KC.N4,    KC.N5,    KC.N6,    KC.MINS,                      KC.CIRC,  KC.RCBR,  KC.LCBR,  KC.DLR,   KC.AT,    KC.TILD, \
        KC.PERC,  KC.N0,    KC.N1,    KC.N2,    KC.N3,    KC.EQL,                       KC.GRV,   KC.RPRN,  KC.LPRN,  KC.RBRC,  KC.LBRC,  KC.QUOT, \
        KC.DOT,   KC.ASTR,  KC.N7,    KC.N8,    KC.N9,    KC.PLUS,                      KC.EXLM,  KC.RABK,  KC.LABK,  KC.AMPR,  KC.QUES,  KC.PIPE, \
                                                _______,  _______,  _______,  _______,  _______,  _______,
    ],
    [  # NAVIGATION
       #XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  KC.LEFT,  KC.UP,    KC.RIGHT, XXXXXXX,                      KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT, XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.DOWN,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
                                                _______,  _______,  _______,  _______,  _______,  _______,
    ],
    [  # QUASI-VIM
       #XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  NXT_W,    XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  U_UND,    I_INP,    O_INP,    XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  KC.LEFT,  KC.PGDN,  KC.RIGHT, XXXXXXX,                      KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT, XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.DOWN,  V_VIM,    PRV_W,                        XXXXXXX,  M_VIM,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
                                                _______,  _______,  _______,  _______,  _______,  _______,
    ],
    [  # TMUX
       #XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  TM_SCR4,  TM_SCR5,  TM_SCR6,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  TM_SCR0,  TM_SCR1,  TM_SCR2,  TM_SCR3,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
        XXXXXXX,  XXXXXXX,  XXXXXXX,  TM_CRT,   XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, \
                                                _______,  _______,  _______,  _______,  _______,  _______,
    ]
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()
