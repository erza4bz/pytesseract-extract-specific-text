import cv2
import re
from glob import glob
import pytesseract
from pytesseract import Output

data_pattern = '^(?!0{4})[0-9]{4}$'

img_mask = './data/*.jpg'
img_names = glob(img_mask)
for i in img_names:
    img = cv2.imread(i, 0)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())
    n_boxes = len(d['text'])
    result = []
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            if re.match(data_pattern, d['text'][i]):
                result.append(d['text'][i])
                #(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])  // HANYA UNTUK TEST MENAMPILKAN GAMBAR
                #img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)           // HANYA UNTUK TEST MENAMPILKAN GAMBAR
            
    print('No. Invoice: ',result[0])
    #cv2.imshow('img', img) // HANYA UNTUK TEST MENAMPILKAN GAMBAR
