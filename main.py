from PIL import Image, ImageFont, ImageDraw, ImageFilter
from openpyxl import load_workbook

COLOR = (23, 103, 200)
COR_BG = (255, 255, 255)

# font = ImageFont.truetype(<font-file>, <font-size>)
fontBold = ImageFont.truetype("fonts\\Roboto-Bold.ttf", 16)
fontBNormal = ImageFont.truetype("fonts\\Roboto-Regular.ttf", 14)

fontNormal = ImageFont.truetype("fonts\\Roboto-Regular.ttf", 12)
fontNBold = ImageFont.truetype("fonts\\Roboto-Bold.ttf", 12)


wb = load_workbook(filename="xlsx\\Assinaturas.xlsx")
sheet = wb['Sheet1']

enum = 0
for key, cell in enumerate(sheet):
    img = Image.new('RGB', (500, 135), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((215, 8), cell[0].value, COLOR, font=fontBold)
    draw.text((215, 29), cell[1].value, COLOR, font=fontBNormal)

    stefani = Image.open("img\\Logo-Stefani.jpg")
    stefani = stefani.resize((190, 65), Image.ANTIALIAS)
    img.paste(stefani, (4, 35))

    draw.line([(205, 5), (205, 130)], fill=COLOR)
    draw.line([(215, 50), (490, 50)], fill=COLOR)

    draw.text((215, 55), "Phone:", COLOR, font=fontNBold)
    draw.text((280, 55), "+55 (16) 3209-4788", COLOR, font=fontNormal)

    draw.text((215, 73), "Email:", COLOR, font=fontNBold)
    draw.text((280, 73), cell[2].value, COLOR, font=fontNormal)

    if cell[3].value is None:
        draw.text((215, 91), "Facebook:", COLOR, font=fontNBold)
        draw.text((280, 91), "facebook.com/ceramicastefanisa",
                  COLOR, font=fontNormal)
    else:
        draw.text((215, 91), "Skype:", COLOR, font=fontNBold)
        draw.text((280, 91), cell[3].value, COLOR, font=fontNormal)
        draw.text((215, 109), "Facebook:", COLOR, font=fontNBold)
        draw.text((280, 109), "facebook.com/ceramicastefanisa",
                  COLOR, font=fontNormal)

    img.save("jpg/"+cell[2].value + '.jpg')
    enum = enum + 1

print("Gerei %d arquivos!" % enum)