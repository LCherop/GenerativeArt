import random
import uuid

from PIL import Image,ImageDraw

run_id = uuid.uuid1()

image = Image.new('RGB',(500,500))
width, height = image.size

line_width = 500
line_height = 500

number_of_lines = random.randint(10000,50000)

draw_lines = ImageDraw.Draw(image)

for i in range(number_of_lines):
    line_x = random.randint(0,width)
    line_y = random.randint(0,height)
    
    line_shape = [
        (line_x,line_y),
        (line_x + line_width, line_y + line_height)
    ]

    draw_lines.arc(
        line_shape,1.3,2.5,
        fill=(
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )
    )
image.save(f'./output/{run_id}.png')
