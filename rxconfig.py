import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="frontend",
    title="Sentiment Analysis App",
    backend_host="0.0.0.0",
    backend_port=3000,
    disable_plugins=[SitemapPlugin],
)
