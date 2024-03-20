import nuke
import nukescripts
import os


#clear all of nuke caches

def clearMyCache():
    nuke.clearRAMCache()
    nuke.clearBlinkCache()
    nuke.clearDiskCache()
    nukescripts.cache_clear("")
    os.system('drop_caches 3')