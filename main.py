from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description="Resize some images")

parser.add_argument('--source')
parser.add_argument('--destination')
parser.add_argument('--size')


args = parser.parse_args()

path = os.path.join('C:\\Users\\ecleek\\temp')
size = 700, 700

def resize():
    output_path = os.path.join(path, "resized")
    for item in os.listdir(path):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
        file_path = os.path.join(path, item)
        if os.path.isfile(file_path):
            im = Image.open(file_path)
            f, e = os.path.splitext(item)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(os.path.join(output_path, f + '-resized.jpg'), 'JPEG', quality=90)
            print("saving")


if __name__ == '__main__':
    resize()
