import PIL
from PIL import Image, ImageDraw, ImageFont
import os

list_of_names = []


def cleanup_data():
    with open("name_list.txt") as file:
        for line in file:
            list_of_names.append(line.strip())
            
def generate_certificates(name, output_path="Certificate of Completion.pdf"):
    # Load the certificate template
    template = Image.open("CoC.png")
    
    # Define font and position
    font = ImageFont.truetype("PinyonScript-Regular.ttf", 50)  # Adjust size as needed
    draw = ImageDraw.Draw(template)
    text_position = (500, 300)  # Adjust coordinates

    # Add name to certificate
    draw.text(text_position, name, fill="black", font=font)

    # Save as PDF
    template.save(output_path, "PDF")
    print(f"Certificate generated for {name}!")


# Example usage
generate_certificates(list_of_names)
cleanup_data()





#def generate_certificates():
#    for name in list_of_names:
#        template = pil.Image.open("CoC.png")
#        ImageDraw.text(template, name, (420, 690), font, 5, (0, 0, 255), 5 )
#        Image.save(f'Generated_Certificate/{name}.png', template)