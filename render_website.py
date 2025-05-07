from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
import json, os

def render_web():
    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        library = json.load(my_file)


    os.makedirs('pages', exist_ok=True)


    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')


    chunked_books = list(chunked(library, 10))
    total_pages = len(chunked_books)

    for page_num, books_chunk in enumerate(chunked_books, 1):
        rendered_page = template.render(
            books=books_chunk,
            current_page=page_num,
            total_pages=total_pages
        )
        page_filename = f'pages/page_{page_num}.html'
        with open(page_filename, 'w', encoding='utf-8') as page_file:
            page_file.write(rendered_page)


if __name__ == '__main__':
    server = Server()
    render_web()
    server.watch('template.html', render_web)
    server.watch('meta_data.json', render_web)
    server.serve(root='.')