from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

COLOR = (23, 103, 200)

# font = ImageFont.truetype(<font-file>, <font-size>)
fontBold = ImageFont.truetype("Roboto-Bold.ttf", 16)
fontBNormal = ImageFont.truetype("Roboto-Regular.ttf", 14)

fontNormal = ImageFont.truetype("Roboto-Regular.ttf", 12)
fontNBold = ImageFont.truetype("Roboto-Bold.ttf", 12)

img = Image.open("Ass-Email.jpg")
draw = ImageDraw.Draw(img)

# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((215, 8), "Guilherme Haynes Howe", COLOR, font=fontBold)
draw.text((215, 29), "Técnico em Informática", COLOR, font=fontBNormal)

draw.text((215, 55), "Phone:", COLOR, font=fontNBold)
draw.text((280, 55), "+55 (16) 3209-4788", COLOR, font=fontNormal)

draw.text((215, 73), "Email:", COLOR, font=fontNBold)
draw.text((280, 73), "tec@ceramicastefani.com.br", COLOR, font=fontNormal)

draw.text((215, 91), "Skype:", COLOR, font=fontNBold)
draw.text((280, 91), "haynes_g", COLOR, font=fontNormal)

draw.text((215, 109), "Facebook:", COLOR, font=fontNBold)
draw.text((280, 109), "facebook.com/CeramicaStefaniSA", COLOR, font=fontNormal)

img.save('sample-out.jpg')
