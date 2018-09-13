#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_gui:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    if renpy.exists("../game/gui/banner_frame.png"):
        call adutar_frame
    else:
        call GOBFADUGUILock
label adutar_frame:
    if renpy.exists("../game/gui/frame.png"):
        call adutar_overlay
    else:
        call GOBFADUGUILock

label adutar_overlay:
    if renpy.exists("../game/gui/overlay/confirm.png"):
       call gobfadu_gui_verify
    else:
       call GOBFADUGUILock

label gobfadu_gui_verify:
    if renpy.exists("../game/GOBFADUGUILock.rpyc"):
        call gobfadu_policy_resources
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
