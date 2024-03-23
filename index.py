from PIL import Image, ImageDraw, ImageFont
import textwrap


def wrap_text(text, width, font):
    lines = []
    for line in text.splitlines():
        lines.extend(textwrap.wrap(line, width=width))
    return lines


def draw_text(draw, text, position, font, fill_color):
    lines = wrap_text(text, 60, font)  # Adjust width as needed
    y = position[1]
    line_spacing = 1.2
    for line in lines:
        draw.text((position[0], y), line, font=font, fill=fill_color)
        y += font.getsize(line)[1] * line_spacing

# Code to be presented in image form
code = """
num = 7

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
"""

image_width = 1280
image_height = 720
background_color = (255, 255, 255) 
image = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)


font_path = "source-code-pro.regular.ttf" # Load own font here
font_size = 20
font = ImageFont.truetype(font_path, font_size)

text_color = (0, 0, 0)

draw_text(draw, code, (50, 50), font, text_color)


image.save("code_image.png")
code_image = Image.open("code_image.png")
bg_image = Image.open("bg.jpg")

position = ((bg_image.width-code_image.width) // 2, (bg_image.height-code_image.height // 2))
# placing text in middle of the background

bg_image.paste(code_image, position, code_image)

bg_image.save("final.jpg")
