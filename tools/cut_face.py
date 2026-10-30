import sys
from PIL import Image, ImageOps, ImageDraw, ImageFilter
src, out, preview = sys.argv[1:4]
im = ImageOps.exif_transpose(Image.open(src)).convert('RGB').crop((1600,1000,2200,1680))
pts = [(300,86),(220,98),(150,140),(100,200),(72,270),(66,340),(78,410),(92,440),(102,490),(125,530),(150,545),
       (185,595),(230,630),(285,648),(345,640),(400,610),(440,565),(470,530),(492,490),(502,430),(497,380),
       (492,320),(475,240),(440,170),(385,115)]
mask = Image.new('L', im.size, 0)
ImageDraw.Draw(mask).polygon(pts, fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))
face = im.copy(); face.putalpha(mask)
face = face.crop((55,75,515,660))
face = face.resize((face.width*256//face.height, 256), Image.LANCZOS)
face.save(out, optimize=True)
bg = Image.new('RGBA', face.size, (255,0,200,255)); bg.alpha_composite(face); bg.resize((face.width*2,512)).save(preview)
