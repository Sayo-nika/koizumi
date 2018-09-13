#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_applet:
    stop music fadeout 2.0
##    scene black
#    with dissolve_scene_full
    if renpy.exists("../game/Applets/Renpy/RenPy.rpyc"):
        call gobfadu_app_verify
    else:
        call GOBFADUAppletLock
label gobfadu_app_verify:
    if renpy.exists("../game/GOBFADUAppletLock.rpyc"):
        call gobfadu_policy_gobfadu64
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
