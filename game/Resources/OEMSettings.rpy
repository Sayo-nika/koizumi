##################################################
## AliceOS OEM Configurations
# This file can be used to set OEM settings such
# as colors, fonts, and custom branding. In code,
# replace the default strings with the OEM
# counterparts.
##################################################
    
## Define whether you want the OEM mode on or off.
## Turning the OEM mode on will use OEM fonts and
## settings instead of AliceOS's defaults.

define aliceos.oem_mode = True

## Define OEM properties such as the name, version,
## website, and support emails.

define aliceos.oem_name = "Sayonika"
define aliceos.oem_website = "https://sayonika.moe"
define aliceos.oem_support = "enra@headbow.stream"

## Define the AliceOS OEM Fonts here. This covers
## required font weights to match the standard
## system.

define aliceos.oem_font_regular = "Resources/systemfont/OEM/Regular.otf"
define aliceos.oem_font_bold = "Resources/systemfont/OEM/Bold.otf"
define aliceos.oem_font_italic = "Resources/systemfont/OEM/Italic.otf"
define aliceos.oem_font_black = "Resources/systemfont/OEM/Black.otf"
define alceos.oem_font_thin = "Resources/systemfont/OEM/Thin.otf"
define aliceos.oem_font_medium = "Resources/systemfont/OEM/Medium.otf"

## Define the AliceOS OEM Colors here. This covers
## branding colors scaling from the 100 (lightest)
## to 900 (darkest). If you can make use of AliceOS's
## default color palette (Elementary), you can simply
## ignore this.

init -10 python:
    aliceos_oem_colors = {
        100: "",
        300: "",
        500: "",
        700: "",
        900: ""
    }