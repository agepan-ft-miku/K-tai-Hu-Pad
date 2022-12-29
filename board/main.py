import board
import busio as io

from kmk.keys import KC

from kmk.hid import HIDModes
from kb import KMKKeyboard, BatteryMonitor
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.handlers.sequences import simple_key_sequence as SQ
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode, PointingHandler, KeyHandler, ScrollHandler, ScrollDirection
from kmk.modules.oneshot import OneShot
from kmk.modules.power import Power

def ble_clear_bonds(*args):
    import supervisor
    import _bleio
    _bleio.adapter.erase_bonding()
    print("BLE clear bounds.")
    supervisor.reload()

i2c = io.I2C(scl=board.SCL, sda=board.SDA)
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(TapDance())
keyboard.modules.append(OneShot())
keyboard.modules.append(Power())
pointing = PointingHandler(press=KC.NO)
scroll = ScrollHandler(press=KC.NO, scroll_direction=ScrollDirection.REVERSE)
trackball = Trackball(i2c, mode=TrackballMode.MOUSE_MODE, handlers=[pointing, scroll])

# BLE Key
BLE_DISCONNECT = KC.NO.clone()
BLE_DISCONNECT.after_press_handler(ble_clear_bonds)
BLE_UNPAIR = KC.TD(KC.NO, KC.NO, KC.NO, KC.NO, BLE_DISCONNECT)

# Trackball Key
CHG_SCROLL_MODE = SQ((KC.TB_MODE, KC.TG(1),))
CHG_SCROLL_MODE.after_press_handler(lambda *args: trackball.set_rgbw(0, 96, 0, 0))
CHG_POINTING_MODE = CHG_SCROLL_MODE.clone()
CHG_POINTING_MODE.after_press_handler(lambda *args: trackball.set_rgbw(0, 0, 96, 0))

# forward / backward key
KC_FB = KC.TD(KC.LALT(KC.LEFT), KC.LALT(KC.RIGHT))
# move next tab / previous tab key
KC_MOTAB = KC.TD(KC.LCTL(KC.LSFT(KC.TAB)), KC.LCTL(KC.TAB))
# backspace / delete key
KC_BSDEL = KC.TD(KC.BSPC, KC.DEL)
# space / tab key
KC_SPTAB = KC.TD(KC.SPC, KC.TAB)
# ctrl+z / ctrl+y key
KC_UNREDO = KC.TD(KC.LCTL(KC.Z), KC.LCTL(KC.Y))
# ctrl+v / ctrl+c key
KC_PSTCP = KC.TD(KC.LCTL(KC.V), KC.LCTL(KC.C))

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LY_ONE = 2
LY_TWO = 3
LY_THR = 4
LY_FOU = 5
LY_FIV = 6
LY_SIX = 7
LY_SEV = 8
LY_EIG = 9
LY_NIN = 10
LY_ZER = 11

keyboard.keymap = [
    [  # Pointing Mode
        KC.MB_LMB,	KC_UNREDO,	KC_PSTCP,	KC_FB,
        KC.OS(KC.MO(LY_ONE)),	KC.OS(KC.MO(LY_TWO)),	KC.OS(KC.MO(LY_THR)),
        KC.OS(KC.MO(LY_FOU)),	KC.OS(KC.MO(LY_FIV)),	XXXXXXX,
        XXXXXXX,	XXXXXXX,	XXXXXXX,
        KC.ENT,		KC.LALT(KC.ZKHK),	KC_BSDEL,
    ],
    [  # Scroll Mode
        KC_MOTAB,	_______,	_______,	_______,
        _______,	_______,	_______,
        _______,	_______,	_______,
        _______,	_______,	_______,
        _______,	BLE_UNPAIR,	_______,
    ],
	[	# LY_ONE
        _______,	_______,	_______,	_______,
        KC.A,		KC.B,		KC.C,
        KC.D,		KC.E,		KC.F, 
        KC.G,		KC.H,		KC.I,
        KC.SPC,		KC.COMMA,	KC.DOT,
    ],
	[	# LY_TWO
        _______,	_______,	_______,	_______,
        KC.J,		KC.K,		KC.L,
        KC.M,		KC.N,		KC.O,
        KC.P,		KC.Q,		KC.R,
        KC.UNDS,	KC.EQL,		KC.BSLS,
    ],
	[	# LY_THR
        _______,	_______,	_______,	_______,
        KC.S,		KC.T,		KC.U,
        KC.V,		KC.W,		KC.X,
        KC.Y,		KC.Z,		KC.NO,
        KC.LCBR,	KC.RCBR,	KC.COLN,
    ],
	[	# LY_FOU
        _______,	_______,	_______,	_______,
        KC.LSFT(KC.N1),		KC.LSFT(KC.N2),	KC.LSFT(KC.N3),
        KC.LSFT(KC.N4),		KC.LSFT(KC.N5),	KC.LSFT(KC.N6),
        KC.LSFT(KC.N7),		KC.LSFT(KC.N8),	KC.LSFT(KC.N9),
        KC.MINS,	KC.N0,	KC.SLSH,
    ],
	[	# LY_FIV
        _______,	_______,	_______,	_______,
        KC.N1,		KC.N2,	KC.N3,
        KC.N4,		KC.N5,	KC.N6,
        KC.N7,		KC.N8,	KC.N9,
        XXXXXXX,	KC.N0,	XXXXXXX,
    ],
]

pointing.setup_press(press=CHG_SCROLL_MODE)
scroll.setup_press(press=CHG_POINTING_MODE)
keyboard.modules.append(trackball)
keyboard.modules.append(
    BatteryMonitor(low_handler=lambda *args: trackball.set_rgbw(96, 0, 0, 0))
)
trackball.set_rgbw(0, 0, 96, 0)
keyboard.tap_key(KC.PS_ON)
print("boot done.")

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='K-tai Hu-pad')
    # keyboard.go(hid_type=HIDModes.USB)
	