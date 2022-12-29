import board
import digitalio
import analogio
from kmk.kmktime import PeriodicTimer
from kmk.modules import Module
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.D10, board.D9, board.D8, board.D7)
    col_pins = (
        board.D0,
        board.D1,
        board.D2,
        board.D3,
    )
    diode_orientation = DiodeOrientation.COLUMNS

    coord_mapping = [
        3, 7, 11, 15,
        0, 1, 2,
        4, 5, 6,
        8, 9, 10,
        12, 13, 14,
    ]

class BatteryMonitor(Module):
    def __init__(self, low_handler):
        self.battery_low = low_handler
        self.bat = analogio.AnalogIn(board.VBATT)
        self.bat_en = digitalio.DigitalInOut(board.READ_BATT_ENABLE)

        # battery voltage = analogIn read value * reference voltage(3.3) / analogIn max value(65535) * Ratio of resistors for voltage divider
        self.convert_value = self.bat.reference_voltage/65536/510*1510
        self.polling_interval = 5000

    def process_key(self, keyboard, key, is_pressed, int_coord):
        return key

    def during_bootup(self, keyboard):
        self._timer = PeriodicTimer(self.polling_interval)
        return

    def before_matrix_scan(self, keyboard):
        if not self._timer.tick():
            return

        # Battery Monitoring Enabled
        self.bat_en.direction = digitalio.Direction.OUTPUT
        self.bat_en.value = False
		# Ignore the first result
        self.bat_voltage = self.bat.value

        self.bat_voltage = self.bat.value*self.convert_value
        if self.bat_voltage < 3.4:
            self.battery_low()
            # print("Battery voltage is low:", self.bat_voltage)
        # else:
            # print("Battery voltage is normal:", self.bat_voltage)

		# Battery Monitoring Disabled
        self.bat_en.direction = digitalio.Direction.INPUT
        return

    def after_matrix_scan(self, keyboard):
        return
        
    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return
