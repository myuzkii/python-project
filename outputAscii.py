from PIL import Image

asciiCharacters = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

# class Img():
#     def __init__(self, img):
#         self.img = img
#     def get_img(self):
#         return str(self.img)
#     def set_img(self, img):
#         self.img = img

class OutputAscii():
    def __init__(self, img):
        self.img = img
    def get_img(self):
        return str(self.img)
    def set_img(self, img):
        self.img = img

    def ascii(self):
        image = self.img
        width, height = image.size
        aspect_ratio = height/width
        new_width = 140
        new_height = aspect_ratio * new_width * 0.55
        image = image.resize((new_width, int(new_height)))
        ascii_art = convertToAsciiArt(image)
        saveAsText(ascii_art)

def convertToAsciiArt(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convertPixelToCharacter(px)
        ascii_art.append(line)
    return ascii_art

def convertPixelToCharacter(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(asciiCharacters) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return asciiCharacters[index]

def saveAsText(ascii_art):
    with open("cat_nyan.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()
            
    