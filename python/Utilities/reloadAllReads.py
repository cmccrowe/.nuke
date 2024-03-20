 
import nuke

"""
This module contains functionality of reloading all read nodes in the script.
:return: None
"""


def reload_all_reads():
    """
    reloads all read nodes in the script
    :return: None
    """

    for node in nuke.allNodes('Read'):
    	node.knob("reload").execute()


    #nodes = nuke.allNodes()
 
	#for node in nodes:
	#	if node.Class() == "Read":
	#		node.knob("reload").execute()
