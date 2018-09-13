#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_frame:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    if renpy.exists("../game/Frameworks/UserNotifications.rpyc"):
        call gobfadu_frame_verify
    else:
        call GOBFADUFrameLock
label gobfadu_frame_verify:
    if renpy.exists("../game/GOBFADUFrameLock.rpyc"):
        call gobfadu_policy_gui
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
