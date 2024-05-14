import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Color, Spacing



def links() -> rx.Component:
    return rx.vstack(
        title("Music"),
        link_button(
            "Bandcamp",
            "Soporte directo",
            "/icons/bandcamp.svg", 
            const.BANDCAMP_URL,
        ),
        link_button(
            "Soundcloud",
            "Dj set, Previews",
            "/icons/soundcloud.svg", 
            const.SOUNDCLOUD_URL
        ),
        link_button(
            "Spotify",
            "Track completos",
            "/icons/spotify.svg", 
            const.SPOTIFY_URL
        ),
        link_button(
            "Beatport",
            "Track completos en Beatport",
            "/icons/beatport.svg",
            const.BEATPORT_URL
        ),
        title("Visual"),
        link_button(
            "Instagram",
            "Videos vertical, experimentos", 
            "/icons/instagram.svg",
            const.INSTAGRAM_URL
        ),
        link_button(
            "Youtube",
            "Videos experimentales, albumes completos",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),  
        link_button(
            "Vimeo",
            "Algunos videos",
            "/icons/vimeo.svg",
            const.VIMEO_URL
        ),
        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}" 
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )