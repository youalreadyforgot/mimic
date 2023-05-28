#! Python 3
from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as controller
import time

class ClickEvent:
    def __init__(self, button, x, y, timestamp):
        self.button = button
        self.x = x
        self.y = y
        self.timestamp = timestamp

class KeyEvent:
    def __init__(self,key,timestamp):
        self.key = key
        self.timestamp = timestamp

def on_key_press(key):
    try:
        # Print the key that was pressed
        print('Key pressed: {0}'.format(key.char))
    except AttributeError:
        # Handle special keys like 'Ctrl', 'Shift', etc.
        print('Special key pressed: {0}'.format(key))

def on_click(x, y, button, pressed):
    if pressed:
        timestamp = time.time()
        event = ClickEvent(button, x, y, timestamp)
        Clickevents.append(event)
        #print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def repeat_clicks(repeat_infinitely=False):
    mouse = Controller()
    previous_timestamp = Clickevents[0].timestamp  # Set to the timestamp of the first event
    while True:
        for event in Clickevents:
            mouse.position = (event.x, event.y)
            mouse.press(event.button)
            mouse.release(event.button)

            time_diff = event.timestamp - previous_timestamp
            #print('Time between clicks: {0:.2f} seconds'.format(time_diff))

            previous_timestamp = event.timestamp
            if time_diff > 0:
                time.sleep(time_diff)
        
        if not repeat_infinitely:
            break


def repeat_keys(repeat_infinitely=False):
    keyboard = controller()
    previous_timestamp = Keyevents[0].timestamp
    while True:
        for event in KeyEvents:
            keyboard.press(event.Key)
            keyboard.release(event.Key)

            time_diff = event.timestamp - previous_timestamp
            previous_timestamp = event.timestamp
            if time_diff > 0:
                time.sleep(time_diff)

        if not repeat_infinitely:
            break


Clickevents = []
Keyevents = []

# Create keyboard and mouse listener
Klistener = keyboard.Listener(on_press=on_key_press)
Mlistener = mouse.Listener(on_click=on_click)

# Start listening for keyboard and mouse events
Klistener.start()
Mlistener.start()

# Keep the script running
input('Press enter to stop listening...\n')

# Stop listening for keyboard and mouse events
Klistener.stop()
Mlistener.stop()

repeat_option = input('Enter repeat option ("infinitely" for infinite loop, any other key to loop once): ')
repeat_infinitely = repeat_option.lower() == 'infinitely'

repeat_clicks(repeat_infinitely)  # Repeat the recorded clicks
repeat_keys(repeat_infinitely)

