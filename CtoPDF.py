from fpdf import FPDF
from PIL import Image

pdf = FPDF(unit="mm")

imagelist = ['image1.jpg', 'image2.png']

for img in imagelist:
    im = Image.open(img)
    width, height = [v * 0.264583 for v in im.size]
    pdf.add_page(format=(width, height))
    pdf.image(img, 0, 0, width, height)

pdf.output("yourfile.pdf")
