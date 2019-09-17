"""
import pdfkit
from jinja2 import Enviroment, FileSystemLoader

class ejemplopdf():

env = Enviorement(loader=FileSystemLoader("templates"))
Admin = env.get_Admin("Admin.html")

html = Admin.render(usuario)

options = {
    'page-size' : 'A5'
    'margin-top' : '0.1'
    'margin-right' : '0.1'
    'margin-bottom' : '0.1'
    'margin-left' : '0.1'

}

pdfkit.from_string(html, 'pruebapdf', options=options)
"""