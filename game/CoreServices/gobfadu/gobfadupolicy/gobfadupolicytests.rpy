#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_tests:
    stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
    call gobfadu_test_verify
label gobfadu_test_verify:
    if renpy.exists("../game/GOBFADUTestLock.rpyc"):
        pause 5.0
        $ persistent.bootpass = 1
        pass
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
    return
