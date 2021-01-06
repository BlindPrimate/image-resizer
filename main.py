from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description="Resize some images")

parser.add_argument('--source')
parser.add_argument('--destination')
parser.add_argument('--size')


args = parser.parse_args()

default_source = os.path.dirname(os.path.abspath(__file__))
default_destination = os.path.join(default_source, 'resized')


class Resizer:
    def __init__(self, source=None, destination=None, size=None):
        if not source:
            source = os.getcwd()
        if source and not destination:
            self.destination = os.path.join(source, 'resized')
        else:
            self.destination = destination
        self.source = source
        if size:
            size = int(size)
        else:
            size = 700
        self.size = (size, size)


    def resize(self):
        count = 1
        for item in os.listdir(self.source):
            f, e = os.path.splitext(item)
            if e not in ['.jpg', '.png']:
                continue
            if not os.path.isdir(self.destination):
                os.mkdir(self.destination)
            file_path = os.path.join(self.source, item)
            if os.path.isfile(file_path):
                im = Image.open(file_path)
                im.thumbnail(self.size, Image.ANTIALIAS)
                im.save(os.path.join(self.destination, f + '-resized.jpg'), 'JPEG', quality=90)
                count += 1

        if count < 1:
            print("No resizeable images found")
        else:
            print("{} images resized and saved to {}".format(count, self.destination))


if __name__ == '__main__':
    resizer = Resizer(source=args.source, destination=args.destination, size=args.size)
    resizer.resize()
