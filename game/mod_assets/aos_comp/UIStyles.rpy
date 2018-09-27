# Stylesheet
init 2:
    style confirm_frame is gui_frame
    style confirm_setup_frame is gui_frame
    style confirm_prompt is gui_prompt
    style confirm_prompt_text is gui_prompt_text
    style confirm_prompt_details is gui_prompt
    style confirm_prompt_details_text is gui_prompt_text
    style confirm_prompt_details_mute is gui_prompt
    style confirm_prompt_details_mute_text is gui_prompt_text
    style confirm_button is gui_medium_button
    style confirm_button_negative is gui_medium_button
    style confirm_button_text is gui_medium_button_text
    style confirm_button_negative_text is gui_medium_button_text
    
    style aliceos_input is gui_prompt_input
    style aliceos_input_text is gui_prompt_input_text

    style setup_title is gui_prompt
    style setup_details is gui_prompt_text
    style setup_mute is gui_prompt
    style setup_title_text is gui_prompt_text
    style setup_details_text is gui_prompt_text
    style setup_mute_text is gui_prompt_text

    # Fonts
    style aliceos_regular is default:
        outlines []

    style aliceos_bold is default:
        outlines []

    style aliceos_medium is default:
        outlines []

    style aliceos_black is default:
        outlines []

    style aliceos_italic is default:
        outlines []

    style aliceos_thin is default:
        outlines []


    style confirm_frame:
        background Frame([ "mod_assets/aos_comp/confirm_frame.png", "mod_assets/aos_comp/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5

    style extra_info_mode:
        background "#fff"

    style confirm_prompt_text is aliceos_bold:
        color "#000"
        outlines []
        text_align 0.0
        size 32
        layout "subtitle"

    style confirm_prompt_details_text is aliceos_regular:
        color "#000"
        outlines []
        # text_align 0.5
        xpadding 32
        ypadding 8
        layout "tex"

    style hyperlink_text is aliceos_regular:
        color blueberry[500]
    
    style confirm_prompt_details_mute_text is aliceos_regular:
        color slate[700]
        size 16
        outlines []
        # text_align 0.5
        xpadding 32
        ypadding 8
        layout "tex"


    style confirm_button is aliceos_bold:
        properties gui.button_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []
        size 28

    style confirm_button_negative is aliceos_bold:
        properties gui.button_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style confirm_button_text is aliceos_regular:
        properties gui.button_text_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style confirm_button_negative_text is aliceos_bold:
        properties gui.button_text_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style banner_frame:
        background Frame(["mod_assets/aos_comp/banner_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign .5
        yalign .5

    style banner_frame_app is aliceos_regular:
        color "333333"
        first_indent 8
        size 20
        outlines []
        text_align 0
        layout "tex"

    style banner_frame_sender is aliceos_bold:
        color "#000"
        size 22
        outlines []
        text_align 0
        layout "tex"

    style banner_frame_message is aliceos_regular:
        color "#000"
        size 22
        outlines []
        text_align 0
        layout "tex"

    style banner_dismiss is navigation_button_text:
        properties gui.button_text_properties("confirm_button")
        color "333"
        size 18
        hover_color "000"
        outlines []

    style banner_dismiss_text is navigation_button_text:
        properties gui.button_text_properties("confirm_button")
        color "000"
        size 18
        hover_color "333"
        outlines []

    style aliceos_input_text is aliceos_italic:
        color blueberry[500]


    ## ASErrorHandler Styles
    style rsod_emoticon is aliceos_regular:
        size 128
        color strawberry[100]
    
    style rsod_title_text is aliceos_regular:
        size 48
        text_align 0.0
        color "#ffffff"
    
    style rsod_prompt_text is aliceos_thin:
        color strawberry[100]
        text_align 0.0
        size 24
    
    style rsod_error_text is aliceos_medium:
        size 24
        color "#ffffff"


init -10000 python:
    strawberry = {
        100: "#ff8c82",
        300: "#ed5353",
        500: "#c6262e",
        700: "#a10705",
        900: "#7a0000"
    }

    orange = {
        100: "#ffc27d",
        300: "#ffa154",
        500: "#f37329",
        700: "#cc3b02",
        900: "#a62100"
    }

    banana = {
        100: "#fff394",
        300: "#ffe16b",
        500: "#f9c440",
        700: "#d48e15",
        900: "#ad5f00"
    }

    lime = {
        100: "#d1ff82",
        300: "#9bdb4d",
        500: "#68b723",
        700: "#3a9104",
        900: "#206b00"
    }

    blueberry = {
        100: "#8cd5ff",
        300: "#64baff",
        500: "#3689e6",
        700: "#0d52bf",
        900: "#002e99"
    }

    grape = {
        100: "#e4c6fa",
        300: "#cd9ef7",
        500: "#a56de2",
        700: "#7239b3",
        900: "#452981"
    }

    cocoa = {
        100: "#a3907c",
        300: "#8a715e",
        500: "#715344",
        700: "#57392d",
        900: "#3d211b"
    }

    silver = {
        100: "#fafafa",
        300: "#d4d4d4",
        500: "#abacae",
        700: "#7e8087",
        900: "#555761"
    }

    slate = {
        100: "#95a3ab",
        300: "#667885",
        500: "#485a6c",
        700: "#273445",
        900: "#0e141f"
    }

    black = {
        100: "#666666",
        300: "#4d4d4d",
        500: "#333333",
        700: "#1a1a1a",
        900: "#000000"
    }