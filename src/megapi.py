# -*- coding: utf-8 -*

import sys

if sys.version > '3':
    PY3 = True
    print("\r\nPython Version: " + sys.version);
    print("megapi.py Version: 0.2.0");
    from megapi_python3 import *
else:
    PY3 = False
    print("\r\nPython Version: " + sys.version);
    print("megapi.py Version: 0.2.0");
    from megapi_python2 import *
