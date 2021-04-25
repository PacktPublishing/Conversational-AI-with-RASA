import os
import runpy

from jinja2 import Environment, FileSystemLoader

port = os.getenv("PORT", 5005)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("index.tpl.html")
template.stream(port=port).dump("index.html")

runpy.run_module("http.server", run_name="__main__")