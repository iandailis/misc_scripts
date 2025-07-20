import sys

from PIL import Image
from pillow_heif import register_heif_opener

def main():
    if (len(sys.argv) != 2):
        print(f"usage: {sys.argv[0]} <heic hile>")
        return

    input_file = sys.argv[1]
    output_file = ".".join(sys.argv[1].split(".")[:-1]) + ".jpg"

    register_heif_opener()
    image = Image.open(input_file)
    image.save(output_file)

    print(f"wrote to {output_file}")

if (__name__ == "__main__"):
    main()
