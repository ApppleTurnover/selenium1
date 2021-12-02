from jinja2 import Environment, FileSystemLoader


class Scripts:
    _env = Environment(loader=FileSystemLoader("js/"))

    smooth_scroll = _env.get_template("smooth_scroll.js").render()
    get_window_size = _env.get_template("window_size.js").render()
    get_rect = _env.get_template("get_bounding_rect.js").render()
    scroll = _env.get_template("scroll.js").render()
