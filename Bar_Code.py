from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageOps

code = Code128(
    "MAHINUR2026",
    writer=ImageWriter()
)

file = code.save("cyber_barcode")

img = Image.open(file)

img = ImageOps.invert(img.convert("RGB"))

img.show()


