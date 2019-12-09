import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import home, gene, struct, func, mutations, background, credits, references, tools, discussion
from .components import fa

# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", home.layout),
    ("home", home.layout),
    ("background", background.layout),
    ("tools", tools.layout),
    ("protstruct", struct.layout),
    ("protfunc", func.layout),
    ("mutations", mutations.layout),
    ("discussion", discussion.layout),
    ("references", references.layout),
    ("gene", gene.layout),
    ("credits", credits.layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items = (
    ("home", "Home"),
    ("background", "Background"),
    ("tools", "Methods"),
    ("gene", "Gene"),
    ("protstruct", "Protein Structure"),
    ("protfunc", "Protein Function"),
    ("mutations",  "Mutations"),
    ("discussion", "Discussion"),
    ("references",  "References"),
    ("credits", "Credits"),
)

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
