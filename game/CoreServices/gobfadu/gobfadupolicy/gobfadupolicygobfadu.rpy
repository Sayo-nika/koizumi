#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_gobfadu:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    call adutar_script

label adutar_script:
    if renpy.exists("script.rpyc"):
        call adutar_splash
    else:
        call GOBFADULock

label adutar_splash:
    if renpy.exists("splash.rpyc"):
       call adutar_menu
    else:
       call GOBFADULock

label adutar_menu:
    if renpy.exists("../game/main_menu.rpyc"):
        call adutar_options
    else:
        call GOBFADULock

label adutar_options:
    if renpy.exists("../game/options.rpyc"):
        call adutar_import
    else:
        call GOBFADULock 

label adutar_import:
    if renpy.exists("../game/submods/import_ddlc/import_ddlc.rpyc"):
        call adutar_overide
    else:
        call GOBFADULock

label adutar_overide:
    if renpy.exists("../game/overrides.rpyc"):
        call gobfadu_verify
    else:
        call GOBFADULock

label gobfadu_verify:
    if renpy.exists("../game/GOBFADULock.rpyc"):
        call gobfadu_policy_applet
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
