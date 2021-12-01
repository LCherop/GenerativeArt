import sys
import PIL.Image


#ASCII characters used to build image
ASCII_CHARS = ["@","#","$","%","?","*","+",";",":",",","."]

#resize image to new fixed width
def resize_image(image,new_width=100):
    width,height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resize_image = image.resize((new_width,new_height))
    return(resize_image)

#convert pixels to grayscale

def greyify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
#convert pixel to ASCII x-ters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixels//25] for pixel in pixels])
    return(characters)

def main(new_width = 100):
    #open image from user input
    path = input("Enter a valid pathname to your image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path,"is not a valid pathname to image")
    
    #convert to ascii
    new_image_data = pixels_to_ascii(greyify(resize_image(image)))

    #format
    pixel_count =len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))

    #print result
    print(ascii_image)

    #save result to output folder
    with open("ascii_iamge.txt","w") as f:
        f.write(ascii_image)
main()
