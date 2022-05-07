import dash
from dash import html


dash.register_page(
    __name__,
    path="/",
    image="birdhouse.jpeg",
    image_url="url_to_image_whereever_its_hosted",
    url="overall_site_url",
    title="(home) The title, headline or name of the page",
    description="(home) A short description or summary 2-3 sentences",
)


layout = html.Div("The image for the home page is specified as `birdhouse.jpeg'")
