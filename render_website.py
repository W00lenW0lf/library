from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
import json


def render_web():
    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        meta_data = json.load(my_file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(meta_data=meta_data)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    server = Server()
    render_web()
    server.watch('template.html', render_web)
    server.watch('meta_data.json', render_web)
    server.serve(root='.')