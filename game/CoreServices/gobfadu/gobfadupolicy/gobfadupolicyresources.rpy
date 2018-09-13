#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadu_policy_resources:
stop music fadeout 2.0
#    scene black
#    with dissolve_scene_full
if renpy.exists("../game/Resources/Branding.rpyc"):
    call adutar_foblack
else:
    call GOBFADUResourceLock

label adutar_foblack:
if renpy.exists("../game/Resources/systemfont/Black.ttf"):
    call adutar_foblaital
else:
    call GOBFADUResourceLock

label adutar_foblaital:
if renpy.exists("../game/Resources/systemfont/BlackItalic.ttf"):
    call adutar_fobold
else:
    call GOBFADUResourceLock

label adutar_fobold:
if renpy.exists("../game/Resources/systemfont/Bold.ttf"):
    call adutar_foboital
else:
    call GOBFADUResourceLock

label adutar_foboital:
if renpy.exists("../game/Resources/systemfont/BoldItalic.ttf"):
    call adutar_foital
else:
    call GOBFADUResourceLock

label adutar_foital:
if renpy.exists("../game/Resources/systemfont/Italic.ttf"):
    call adutar_foli
else:
    call GOBFADUResourceLock

label adutar_foli:
if renpy.exists("../game/Resources/systemfont/Light.ttf"):
    call adutar_folital
else:
    call GOBFADUResourceLock

label adutar_folital:
if renpy.exists("../game/Resources/systemfont/LightItalic.ttf"):
    call adutar_fomed
else:
    call GOBFADUResourceLock

label adutar_fomed:
if renpy.exists("../game/Resources/systemfont/MediumItalic.ttf"):
    call adutar_fomedital
else:
    call GOBFADUResourceLock

label adutar_fomedital:
if renpy.exists("../game/Resources/systemfont/MediumItalic.ttf"):
    call adutar_foreg
else:
    call GOBFADUResourceLock

label adutar_foreg:
if renpy.exists("../game/Resources/systemfont/Regular.ttf"):
    call adutar_fothin
else:
    call GOBFADUResourceLock

label adutar_fothin:
if renpy.exists("../game/Resources/systemfont/Thin.ttf"):
    call adutar_fothinital
else:
    call GOBFADUResourceLock

label adutar_fothinital:
if renpy.exists("../game/Resources/systemfont/ThinItalic.ttf"):
    call adutar_rif
else:
    call GOBFADUResourceLock

label adutar_rif:
if renpy.exists("../game/Resources/systemfont/branding/RifficFree-Bold.ttf"):
    call adutar_sysui
else:
    call GOBFADUResourceLock

label adutar_sysui:
if renpy.exists("../game/Resources/systemui/frame_notify.png"):
    call adutar_sysuiframe
else:
    call GOBFADUResourceLock

label adutar_sysuiframe:
if renpy.exists("../game/Resources/systemui/frame.png"):
    call adutar_ovlay
else:
    call GOBFADUResourceLock

label adutar_ovlay:
if renpy.exists("../game/Resources/systemui/overlay_confirm.png"):
    call gobfadu_res_verify
else:
    call GOBFADUResourceLock

label gobfadu_res_verify:
if renpy.exists("../game/GOBFADUResourceLock.rpyc"):
    call gobfadu_policy_tests
else:
    call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
