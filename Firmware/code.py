import keypad
import touchio
from adafruit_midi.control_change import ControlChange
from microcontroller import pin

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys
from kmk.modules.potentiometer import PotentiometerHandler
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner


# KMK doesn't have a scanner for touch pads, so here's a tiny one.
# Don't touch the pads while the board boots - they calibrate on startup!
class TouchScanner(Scanner):
    def __init__(self, pins):
        self.pads = [touchio.TouchIn(p) for p in pins]
        self.pressed = [False] * len(pins)

    @property
    def key_count(self):
        return len(self.pads)

    def scan_for_changes(self):
        for i, pad in enumerate(self.pads):
            touched = pad.value
            if touched != self.pressed[i]:
                self.pressed[i] = touched
                return keypad.Event(i + self.offset, touched)


keyboard = KMKKeyboard()
# These have to be created before we use KC.MIDI_NOTE / KC.VOLU below
midi = MidiKeys()
media_keys = MediaKeys()

keyboard.matrix = [
    # Touch pads 1-8 (keys 0-7)
    TouchScanner([pin.GPIO1, pin.GPIO2, pin.GPIO6, pin.GPIO8, pin.GPIO3, pin.GPIO5, pin.GPIO9, pin.GPIO7]),
    # Switches SW1-SW3 (keys 8-10)
    KeysScanner([pin.GPIO44, pin.GPIO43, pin.GPIO13], value_when_pressed=False, pull=True),
]

# Touch pads play a C major scale, switches play drum sounds
keyboard.keymap = [[
    KC.MIDI_NOTE(60), KC.MIDI_NOTE(62), KC.MIDI_NOTE(64), KC.MIDI_NOTE(65),
    KC.MIDI_NOTE(67), KC.MIDI_NOTE(69), KC.MIDI_NOTE(71), KC.MIDI_NOTE(73),
    KC.MIDI_NOTE(36), KC.MIDI_NOTE(38), KC.MIDI_NOTE(42),  # kick, snare, hi-hat
]]

# Rotary encoder controls your computer's volume
encoder = EncoderHandler()
encoder.pins = ((pin.GPIO11, pin.GPIO10, pin.GPIO12),)  # A = TX, B = RX, no button
encoder.map = [((KC.VOLD, KC.VOLU, KC.NO),)]

keyboard.modules = [midi, encoder]
keyboard.extensions = [
    media_keys,
    RGB(pixel_pin=pin.GPIO3, num_pixels=3, val_default=80, animation_mode=AnimationModes.RAINBOW),
]

if __name__ == '__main__':
    keyboard.go()