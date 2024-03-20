import nuke
import os
import reloadAllReads
import GrayAutoBackdrop
import comma
import readWrite
#import merge_transforms_v2
import stretch_script
#import autoCrop
import clearAllCache
#import KnobScripter

### Version Notes Popup ###
###topMenu = nuke.menu("Nuke")
###topMenu.addCommand("Utilities/Display sub notes",
###                   "import display_notes; reload(display_notes);display_notes.start()",
###                   "shift+/")


### ------ Reconcile Helper -----####
menubar = nuke.menu("Nuke")
tools = menubar.addMenu("A_tools")
tools.addCommand('A_ReconcileHelper', 'nuke.createNode("A_ReconcileHelper")')


### ------ optical flares  ------ ###
toolbar = nuke.toolbar("Nodes")
toolbar.addMenu("VideoCopilot", icon="VideoCopilot.png")
toolbar.addCommand( "VideoCopilot/OpticalFlares", "nuke.createNode('OpticalFlares')", icon="OpticalFlares.png")



### nuke.menu("Nuke").addMenu("&File").addCommand("&Open Recent Comp/@recent_file"+str(n), "nuke.scriptOpen(nuke.recentFile("+str(n)+"))") for n in range(7,25)



### Autocrop ###
#nuke.menu( 'Nuke' ).addCommand( 'Utilities/Run Auto Crop on Selected', autoCrop.autoCrop )

### AutoBackdrop ###
nuke.menu('Nuke').addCommand('Utilities/Gray Auto Backdrop', lambda: GrayAutoBackdrop.GrayAutoBackdrop(), "shift+a", shortcutContext=2)


### Reload all reads shortcut ###
nuke.menu("Nuke").addCommand("Utilities/Reload All Read Nodes", "reloadAllReads.reload_all_reads()", "F11", icon="Refresh.png")

# Merge Transforms
#nuke.menu("Nuke").addCommand("Utilities/Merge Transforms", "merge_transforms_v2.start()", "Ctrl+Shift+t", icon="ToolbarTransform.png")

# Clear All Cache
nuke.menu("Nuke").addCommand("Utilities/Clear All Cache", "clearAllCache.clearMyCache()", "F9")

### Adding readWrite Menu
nuke.menu("Nuke").addCommand("Utilities/create read from write", "readWrite.create_read_from_write()", "Alt+r", icon="Read.png")



######################
## Toolbar shotcuts ##
######################


### deepMerge Shortcuts
toolbar.addCommand("Deep/Merge","nuke.createNode('DeepMerge')","ctrl+m", icon="DeepMerge.png")


### Premultiplication Shortcuts
toolbar.addCommand("Merge/Unpremult","nuke.createNode('Unpremult')","[", icon="Unpremult.png")
toolbar.addCommand("Merge/Premult","nuke.createNode('Premult')","]", icon="Premult.png")


### Multiply Shortcut
#toolbar.addCommand("Color/Math/Multiply","nuke.createNode('Mulitply')", "*", icon="ColorMult.png")
nuke.menu('Nodes').findItem('Color').findItem('Math').findItem('Multiply').setShortcut('*')

### backdrop shortcut 'shift+a'
#nuke.menu('Nodes').addCommand('Other/BackdropNode', 'nuke.createNode("BackdropNode")', 'shift+a', shortcutContext=2)

### closes all property panels from anywhere
def clear_properties():
    for n in nuke.allNodes() + [nuke.root(), ]:
        n.hideControlPanel()
nuke.menu("Nuke").addCommand("Edit/Node/Close all properties",clear_properties, "ctrl+shift+a")

m=nuke.menu('Nuke')
r=m.addMenu('CardToTrack') ##,icon='Me.png'
r.addCommand('CardToTrack gizmo', 'nuke.createNode(\'CardToTrack\')') ##,icon='Me.png'



######################
## Toolbar defaults ##
######################


#creates framehold that defaults to current frame
nuke.menu('Nodes').addCommand( 'Time/FrameHold', 'nuke.createNode("FrameHold")["first_frame"].setValue( nuke.frame() )', icon='FrameHold.png')

#Shutteroffset set to centered by default
#nuke.knobDefault("shutteroffset", "centered")

