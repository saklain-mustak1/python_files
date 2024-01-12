from PIL import Image

me = Image.open('skli.png')
bg = Image.open('bgs.jpg')
bg.paste(me, (1, 10), me)
bg.show()
