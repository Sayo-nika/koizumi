## UserNotifications.rpy
# Notification Management System
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## Screen Implementation
# Alert
screen alert(title, message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "Resources/systemui/overlay_confirm.png"

    frame:
        has vbox:
            # xalign .5
            # yalign .5
            spacing 30
            xsize 656

        label _(title):
            style "confirm_prompt"
            # xalign 0.5

        label _(message):
            style "confirm_prompt_details"
            # xalign 0.5

        hbox:
            xalign 1.0
            spacing 100

            textbutton _("OK") action ok_action


# Confirm
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

# Detailed Dialog
screen confirm_alert(title, message, no_action_message, no_action, yes_action_message, yes_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            # xalign .5
            # yalign .5
            spacing 30

        label _(title):
            style "confirm_prompt"
            # xalign 0.5

        label _(message):
            style "confirm_prompt_details"
            # xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(no_action_message) action no_action:
                style "confirm_button_negative"
            textbutton _(yes_action_message) action yes_action

# Permissive Dialog (Variant of Detailed Dialog)
screen ask_permission(app_name, action, no_action,  yes_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30
            xsize 640

        label _(app_name + " Would Like To\n" + action):
            style "confirm_prompt"
            xalign 0.5

        if action == allow_un:
            label _(allow_un_details):
                style "confirm_prompt_details"
                xalign 0.5
        elif action == allow_fs:
            label _(allow_fs_details):
                style "confirm_prompt_details"
                xalign 0.5
        elif action == allow_sip:
            label _(allow_sip_details):
                style "confirm_prompt_details"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Don't Allow") action no_action:
                style "confirm_button_negative"
            textbutton _("OK") action yes_action

# Banner
screen banner(applet, title, message, response):
    zorder 100
    frame at banner_appear:
        style "banner_frame"
        xpadding 24
        ypadding 24
        xalign 0.5
        yalign 0.025
        xsize 676

        vbox:
            hbox:
                xsize 628
                hbox:
                    add "Applets/" + applet.app_dir + "/Resources/icons/" + applet.icons[24]
                    python:
                        appname = applet.long_name.upper()
                    text appname:
                        style "banner_frame_app"
                textbutton _("Respond") action response:
                    style "banner_dismiss"
                    xalign 1.0
                    ypadding 0
            null height 12
            text title:
                style "banner_frame_sender"
            text message:
                style "banner_frame_message"

    timer 5.0 action Return(0)

# Ren'Py Banner (Notification)
screen notify(message):
    zorder 100
    frame at banner_appear:
        style "banner_frame"
        xpadding 24
        ypadding 24
        xalign 0.5
        yalign 0.025
        xsize 676

        vbox:
            hbox:
                xsize 628
                hbox:
                    add "mod_assets/logo.png":
                        size (24, 24)
                    python:
                        nameofapp = config.name.upper()
                    text nameofapp:
                        style "banner_frame_app"
            null height 12
            text "Hey, something's happening!":
                style "banner_frame_sender"
            text message:
                style "banner_frame_message"

    timer 3.25 action Hide('notify')


transform -1 banner_appear:
    on show:
        yalign 0.0 xalign 0.5
        linear 0.25 ypos 0.025
    on hide:
        yalign 0.025 xalign 0.5
        linear 0.25 yalign -1.0

# Stylesheet
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_prompt_details is gui_prompt
init -1 style confirm_prompt_details_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_negative is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1 style confirm_button_negative_text is gui_medium_button_text


init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    font "Resources/systemfont/OEM/Bold.otf"
    outlines []
    text_align 0.0
    size 32
    layout "subtitle"

init -1 style confirm_prompt_details_text:
    color "#000"
    font "Resources/systemfont/OEM/Regular.otf"
    outlines []
    # text_align 0.5
    xpadding 32
    ypadding 8
    layout "tex"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    color strawberry[500]
    font "Resources/systemfont/OEM/Bold.otf"
    hover_color strawberry[100]
    outlines []
    size 28

init -1 style confirm_button_negative:
    properties gui.button_properties("confirm_button")
    color strawberry[500]
    font "Resources/systemfont/OEM/Black.otf"
    hover_color strawberry[100]
    outlines []

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color strawberry[500]
    font "Resources/systemfont/OEM/Regular.otf"
    hover_color strawberry[100]
    outlines []

init -1 style confirm_button_negative_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color strawberry[500]
    font "Resources/systemfont/OEM/Bold.otf"
    hover_color strawberry[100]
    outlines []

init -1 style banner_frame:
    background Frame(["gui/banner_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    xalign .5
    yalign .5

init -1 style banner_frame_app:
    color "333333"
    font "Resources/systemfont/OEM/Regular.otf"
    first_indent 8
    size 20
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_frame_sender:
    color "#000"
    font "Resources/systemfont/OEM/Bold.otf"
    size 22
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_frame_message:
    color "#000"
    font "Resources/systemfont/OEM/Regular.otf"
    size 22
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_dismiss is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "333"
    size 18
    font "Resources/systemfont/OEM/Regular.otf"
    hover_color "000"
    outlines []

init -1 style banner_dismiss_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "000"
    size 18
    font "Resources/systemfont/OEM/Bold.otf"
    hover_color "333"
    outlines []

## Screen Definitions
define allow_un = "Send Notifications"
define allow_fs = "Access The File System"
define allow_sip = "Modify System Settings"

define allow_un_details = "Notifications may include alerts, sounds, and banners. These can be configured in Control Center."
define allow_fs_details = "By giving this app access, this app can modify files beyond your Home folder. Only give file system access to apps that you trust."
define allow_sip_details = "By giving this app access, this app can modify system settings and control your computer. Only give this to apps that you trust."