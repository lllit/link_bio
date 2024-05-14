import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color, TextColor


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text(
                "const",
                as_="span",
                color=TextColor.BODY.value
                ),
                rx.text(
                "LLLIT",
                as_="span",
                color=TextColor.HEADER.value
                ),
                style=styles.navbar_title_style   
            ),
            href=const.INSTAGRAM_URL,
            is_external=True,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",  
        top="0"  
    )