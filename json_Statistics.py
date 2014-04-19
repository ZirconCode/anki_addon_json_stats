#Addon: JSON statistics
#Version: 0.0.2
#Description: Autogenerate a JSON file in your home directory containing statistics about your collections. The file is anki.json.


from os.path import expanduser
import json
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
#from anki.hooks import wrap
#from anki.hooks import addHook

def writeSummary():
    loadCollection()

    data = {}
    stats = mw.col.stats()

    data['cardCount'] = mw.col.cardCount()
    data['todayStats'] = stats.todayStats()
    
    home = expanduser("~")
    filename = home + "/anki.json"
    with open(filename,"w") as f:
        json.dump(data,f)
        f.close()

loadCollection = mw.loadCollection
mw.loadCollection = writeSummary
#addHook("sync", writeSummary) #runHook("sync", "login")

