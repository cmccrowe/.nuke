import nuke

###Adding paths
nuke.pluginAddPath('./plugins')
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./GrayAutoBackdrop')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./comma')
nuke.pluginAddPath('./python/utilities/')
nuke.pluginAddPath('./icons')
#nuke.pluginAddPath('./pixelfudger')
#nuke.pluginAddPath('./python/utilities/readWrite')
nuke.pluginAddPath('./Damian_Binder')
nuke.pluginAddPath('./Damian_Binder/Looper')
Expression_path = "/Users/cmccr/.nuke/Expression"
nuke.pluginAddPath(Expression_path)
nuke.pluginAddPath('pixelfudger3')
nuke.pluginAddPath('A_ReconcileHelper')

# Hides viewer input pipes
# nuke.knobDefault( 'Viewer.hide_input', 'true' )


#/////////////////////////////////////#
#           Formats                   #
#/////////////////////////////////////#
party_pirate = '2048 1152 party_pirate'
nuke.addFormat( party_pirate )


########################
## Default Resolution ##
########################
nuke.knobDefault('Root.format', 'UHD_4K')
#nuke.knobDefault('Root.format', 'party_pirate')

########################
## Default FrameRange ##
########################
#nuke.knobDefault('Root.first_frame', '1001')
#nuke.knobDefault('Root.last_frame', '1100')


###################
## Node Defaults ##
###################


#sets multiply to rgba by default
nuke.knobDefault( 'Multiply.channels', 'rgba' )

#Sets roto clip to none
nuke.knobDefault( 'Roto.cliptype', 'none' )

#Sets Paint node clone strokes to impulse and turns off rounded pixels
nuke.knobDefault("RotoPaint.toolbox", "clone {{source_filter Impluse} {source_translate_round false}}")

#Sets blur nodes to alpha by default
nuke.knobDefault( 'Blur.channels', 'alpha' )

#Sets project3D to no crop
nuke.knobDefault( 'Project3D.crop', 'false' )

#Sets Remove defaults to keep rgba 
nuke.knobDefault( 'Remove.operation', 'keep' )
nuke.knobDefault( 'Remove.channels', 'rgba' )

###Shuffle label displays Selected Channel
nuke.knobDefault("Shuffle.label", '[value in]')
