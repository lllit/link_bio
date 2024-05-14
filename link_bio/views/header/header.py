import reflex as rx
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.styles.colors import Color, TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.link(
                    rx.image(
                        src="/icons/soundcloud.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value,
                    ), 
                    href=const.SOUNDCLOUD_URL,
                    is_external=True,
                    class_name="blink",
                    border_radius="50%",
                    padding=Size.MEDIUM.value,
                    bg=Color.PURPLE.value,
                    position="absolute",
                    bottom="0",
                    right=Size.BIG.value          
                ),
                rx.avatar(
                    name="Matias Perez",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/yo_som.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="1px",
                    border=f"4px solid {Color.SECONDARY.value}"
                ), 
            ),
            rx.vstack(
                rx.heading(
                    "Matias Perez",
                    size=Spacing.BIG.value,
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@lllit_3",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        "https://github.com/lllit",
                        "GitHub"
                    ),    
                    link_icon(
                        "/icons/instagram.svg",
                        "https://www.instagram.com/lllit_3/",
                        "Instagram"
                    ),    
                    link_icon(
                        "/icons/bandcamp.svg",
                        "https://lllit3.bandcamp.com/",
                        "Bandcamp"
                    ),    
                    link_icon(
                        "/icons/soundcloud.svg",
                        "https://soundcloud.com/lllit_3",
                        "Soundcloud"
                    ),    
                    link_icon(
                        "/icons/youtube.svg",
                        "https://www.youtube.com/@lllit",
                        "Youtube"
                    ),    
                    link_icon(
                        "/icons/linkedin.svg",
                        "https://www.linkedin.com/in/matias-perez-b04a952b7/",
                        "LinkedIn"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value    
                ),
                spacing=Spacing.ZERO.value,
                aling_items="start"   
            ),
            align="end",
            spacing=Spacing.DEFAULT.value,                   
        ),
        rx.vstack(
                rx.flex(
                info_text(
                    "+Visual", "Desinger"
                ),
                rx.spacer(),
                info_text(
                    "+Music", "Producer"
                ),
                rx.spacer(),
                info_text(
                    "+Learning", "Technologies"
                ),
                width="100%"
            ),  
            rx.text(
                f"""
                Visceral and mental improvisation, creating sonic landscapes that transport you to unknown dimensions.
                """,
                font_size=Size.DEFAULT.value,
                color=TextColor.BODY.value
            ),
            width="100%",
            spacing=Spacing.BIG.value,   
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",      
    ),      

        