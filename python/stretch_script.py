import nuke

"""#Setting up default values for ramp directions

def initial_ramp_values_func():
    n = nuke.thisNode()
    k = nuke.thisKnob()
    #Top Ramps
    n['top_from.x'].setValue('root.format.r/2')
    n['top_from.y'].setValue('root.format.t/2')
    n['top_to.x'].setValue('root.format.r/2')
    n['top_to.y'].setValue('root.format.t')
    #Left Ramps
    n['left_from.x'].setValue('root.format.r/2')
    n['left_from.y'].setValue('root.format.t/2')
    n['left_to.x'].setValue('0')
    n['left_to.y'].setValue('root.format.t/2')
    #Right Ramps
    n['right_from.x'].setValue('root.format.r/2')
    n['right_from.y'].setValue('root.format.t/2')
    n['right_to.x'].setValue('root.format.r')
    n['right_to.y'].setValue('root.format.t/2')
    #Bottom Ramps
    n['bottom_from.x'].setValue('root.format.r/2')
    n['bottom_from.y'].setValue('root.format.t/2')
    n['bottom_to.x'].setValue('root.format.r/2')
    n['bottom_to.y'].setValue('0')
"""

#Setting up direction dropdown show/hide functionality

def stretch_func():
    n = nuke.thisNode()
    k = nuke.thisKnob()

    if k.name() == "stretch_direction":
        if k.name() == "stretch_direction" and k.value() == "From Top":
            n['top_group'].setVisible(True)
            n['left_group'].setVisible(False)
            n['right_group'].setVisible(False)
            n['bottom_group'].setVisible(False)
        elif k.name() == "stretch_direction" and k.value() == "From Left":
            n['top_group'].setVisible(False)
            n['left_group'].setVisible(True)
            n['right_group'].setVisible(False)
            n['bottom_group'].setVisible(False)
        elif k.name() == "stretch_direction" and k.value() == "From Right":
            n['top_group'].setVisible(False)
            n['left_group'].setVisible(False)
            n['right_group'].setVisible(True)
            n['bottom_group'].setVisible(False)
        elif k.name() == "stretch_direction" and k.value() == "From Bottom":
            n['top_group'].setVisible(False)
            n['left_group'].setVisible(False)
            n['right_group'].setVisible(False)
            n['bottom_group'].setVisible(True)
    else:
        pass
