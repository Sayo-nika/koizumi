#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_gobfadu64:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    if renpy.exists("../game/CoreServices/Bootloader.rpyc"):
        call adutar_install
    else:
        call GOBFADUOSLock

label adutar_install:
    if renpy.exists("../game/CoreServices/Setup.rpyc"):
        call gobfadu64_verify
    else:
        call GOBFADUOSLock

label gobfadu64_verify:
    if renpy.exists("../game/GOBFADUOSLock.rpyc"):
        call gobfadu_policy_frame
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
