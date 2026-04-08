import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="frontend",
    title="Sentiment Analysis App",
    backend_port=8001,
    disable_plugins=[SitemapPlugin],
)
