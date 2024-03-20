with nuke.root():
    for aGroupNode in nuke.allNodes("Group", recurseGroups=True):
        with aGroupNode:
            for aNode in nuke.allNodes("Read", recurseGroups=True):
                if aNode.hasError():
                    print"\n"
                    print aNode.fullName()
                    print aNode['file'].value()
