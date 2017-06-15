# -*- coding: utf-8 -*-

def img_join(fnames, nrow, ncol):
    from PIL import Image
    image_list = [Image.open(fname) for fname in fnames]
    image_size = image_list[0].size
    width, height = image_size
    new_size = (ncol * width, nrow * height)
    new_img = Image.new('RGB', new_size, 255)
    x = cntx = y = cnty = 0
    for img in image_list:
        if cnty < nrow:
            if cntx < ncol:
                new_img.paste(img, (x, y))
                x += width
                cntx += 1
                continue
            x = cntx = 0
            y += height
            new_img.paste(img, (x, y))
            x += width
            cntx += 1
    return new_img