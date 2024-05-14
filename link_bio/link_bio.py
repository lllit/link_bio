import reflex as rx
import link_bio.constants as const
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.state.PageState import PageState

class State(rx.State):
    pass

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image="assets/favicon.ico",
    meta=utils.index_meta,
)

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),             
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
)


app.add_page(
    index,
    image="favicon.ico"
)
app.compile()