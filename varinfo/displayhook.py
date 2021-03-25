"""
Sets the default print-function of your 
python-interpreter to pprint
"""
import sys
from pprint import pprint as print

sys.displayhook = print