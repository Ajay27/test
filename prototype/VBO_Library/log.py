import robot.api.logger
from robot.output import Message
from robot.output.logger import LOGGER
import threading
import sys
import time


def info(msg, html=False, also_console=True,timestamp=None):
    logMsg = Message(msg, 'INFO', html, timestamp=timestamp)
    LOGGER.log_message(logMsg)
    if also_console:
        sys.__stdout__.write('\n %s' %(msg))

def step(msg, html=True, also_console=True, timestamp=None):
    strLen = len(msg)
    fontTag = '<font size = 3 color="blue" style="background: #ADD8E6;"> '
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write("\nSTEP : %s" %(msg))

def fail(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"red\"><b> FAIL:'
    fontEndTag = '</b>,</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\nFAIL: %s' %(msg))



