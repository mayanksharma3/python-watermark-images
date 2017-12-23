from PIL import Image, ImageDraw, ImageFont
import os
import argparse

parser = argparse.ArgumentParser(description='Watermarks all JPEG and PNG images in a directory')
parser.add_argument('directory', nargs='?', default='.', help='A directory of images to watermark')
parser.add_argument('--font-size', default=24, type=int, help="Sets the font size to FONT-SIZE (default: 24)")
parser.add_argument('-t', '--text', default="Watermark", help="Sets the watermark to TEXT (default: Watermark)")
i = 1
args = parser.parse_args()
image_dir = os.listdir(args.directory)
if not os.path.exists(args.directory + 'watermarked/'):
    os.makedirs(args.directory + 'watermarked/')
for filename in image_dir:
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
        image = Image.open(args.directory + filename)
        width, height = image.size
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', args.font_size)
        text_width, text_height = draw.textsize(args.text, font)
        x = width - text_width - 20
        y = height - text_height - 20
        draw.text((x, y), args.text, font=font)
        image.save(args.directory + 'watermarked/' + filename)
        print str(i) + " image(s) processed"
        i += 1
