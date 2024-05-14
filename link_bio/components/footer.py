import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logotipo.jpg", 
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
            alt="Logotipo de LLLIT",
            border=f"4px solid {Color.SECONDARY.value}"
        ),
        rx.link(
            rx.box(
                f"© 2022-{datetime.date.today().year} ",
                rx.text(
                "LLLIT by Matias Perez VX.",
                as_="span",
                color=Color.PRIMARY.value
                ),
                " v333",
                padding_top=Size.DEFAULT.value
            ),  
            href=const.INSTAGRAM_URL,
            is_external=True,
            font_size=Size.MEDIUM.value  
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"    
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM CHILE TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value   
                ),
            ),
            href=const.GITHUB_URL,
            is_external=True
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value,           
    )
