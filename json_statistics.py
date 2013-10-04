#Addon: JSON statistics
#Version: 0.0.1
#Description: Autogenerate a JSON file in your home directory containing statistics about your collections. The file is anki.json.


from os.path import expanduser
import json
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import wrap

def writeSummary():
    loadCollection()
    home = expanduser("~")
    filename = home + "/anki.json"
    with open(filename,"w") as f:
       json.dump({"cardCounts": mw.col.cardCount()},f)
       f.close()

loadCollection = mw.loadCollection
mw.loadCollection = writeSummary
