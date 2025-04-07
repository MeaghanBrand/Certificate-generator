import jinja2
import pdfkit
from datetime import datetime

my_name = "Meaghan"
item_1 = "Reboot"
item_2 = "Tv"
item_3 = "Bed"
todays_date = datetime.today().strftime("%d %b, %Y")

context = {'my_name': my_name, 'item_1': item_1, 'item_2': item_2, 'item_3': item_3, 'todays_date': todays_date}


template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader = template_loader)

template = template_env.get_template("my-basic-template.html")
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = "\Users\meagh\OneDrive\Documents\GitHub\Certificate-generator")

pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration = config)