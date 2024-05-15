from enum import Enum


class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#0c1a01"
    BACKGROUND = "#0d0f0f"
    CONTENT = "#151717",
    PURPLE = "#9146ff"
    YELLOW = "#6ced02"

class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    FOOTER = "#A3ABB2"
    
class bg_image(Enum):
    navbar_bg = "center/cover url('/navbar.jpg')"
    back_bg = "url('/bg.png')"