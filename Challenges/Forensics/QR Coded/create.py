import qrcode
import numpy as np
from qrcode.image.pil import PilImage
from PIL import Image
import random

false_flag = "bracco{thi5_1sn7_r34l}"
real_flag = "bronco{th1s_0n3_i5}"

false_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

false_qr.add_data(false_flag)
false_qr.make(fit=True)

false_img = false_qr.make_image(image_factory=PilImage)
false_img = false_img.convert("RGB")

true_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

true_qr.add_data(real_flag)
true_qr.make(fit=True)

true_img = true_qr.make_image(image_factory=PilImage)
true_img = true_img.convert("RGB")

# Pastes used to place a pixel of value F in the L plane (F_IN_L)
WHITE_IN_RED = Image.fromarray(np.full((10,10,3), [254, 255, 255], dtype=np.dtypes.Int8DType), mode="RGB")
WHITE_IN_GREEN = Image.fromarray(np.full((10,10,3), [255, 254, 255], dtype=np.dtypes.Int8DType), mode="RGB")
WHITE_IN_BLUE = Image.fromarray(np.full((10,10,3), [255, 255, 254], dtype=np.dtypes.Int8DType), mode="RGB")
WHITE_IN_ALL = Image.fromarray(np.full((10,10,3), [255, 255, 255], dtype=np.dtypes.Int8DType), mode="RGB")
BLACK_IN_RED = Image.fromarray(np.full((10,10,3), [1,0,0], dtype=np.dtypes.Int8DType), mode="RGB")
BLACK_IN_GREEN = Image.fromarray(np.full((10,10,3), [0,1,0], dtype=np.dtypes.Int8DType), mode="RGB")
BLACK_IN_BLUE = Image.fromarray(np.full((10,10,3), [0,0,1], dtype=np.dtypes.Int8DType), mode="RGB")
BLACK_IN_ALL = Image.fromarray(np.full((10,10,3), [1, 1, 1], dtype=np.dtypes.Int8DType), mode="RGB")

dim = 10
start = 4
width = 29
for i in range(start, width + start):
    for j in range(start, width + start):
        hide_black = true_img.getpixel((i * dim, j * dim))[0] == 0
        show_black = false_img.getpixel((i * dim, j * dim))[0] == 0
        paste_area = (dim*i, dim*j, dim*(i+1), dim*(j+1))
        rand_choice = random.randint(0,2)
        # If this pixel should be black
        if show_black:
            # If you want an LSB to be 0
            if hide_black:
                if rand_choice == 0:
                    false_img.paste(BLACK_IN_RED, paste_area)
                elif rand_choice == 1:
                    false_img.paste(BLACK_IN_GREEN, paste_area)
                else:
                    false_img.paste(BLACK_IN_BLUE, paste_area)
            # If you do not want ANY LSB to be 0
            else:
                false_img.paste(BLACK_IN_ALL, paste_area)
        else:
            if hide_black:
                if rand_choice == 0:
                    false_img.paste(WHITE_IN_RED, paste_area)
                elif rand_choice == 1:
                    false_img.paste(WHITE_IN_GREEN, paste_area)
                else:
                    false_img.paste(WHITE_IN_BLUE, paste_area)
            else:
                false_img.paste(WHITE_IN_ALL, paste_area)

false_img.save("easy_scan.png")
