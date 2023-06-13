from PIL import Image, ImageOps

# допустим есть 4 картинки одинакового размера
img_size = (175, 175)


# Открываем картинки
img1 = Image.open('docs/1.png')
img2 = Image.open('docs/2.png')
img3 = Image.open('docs/3.png')
img4 = Image.open('docs/4.png')

# получаем размеры картинок
img1_size = img1.size
img2_size = img2.size
img3_size = img2.size
img2_size = img2.size

# рамка для картинок на постере
border = 4

# если картинки одинакового размера, то 
# ширина фона => img1_size[0] * 2 + border
# высота фона => img1_size[1] * 2 + border
# следовательно размер фонового изображения
new_img_size = (img1_size[0] * 2 + border, 
                img1_size[1] * 2 + border)
# создаем фоновое изображение размером `new_img_size`
img = Image.new('RGB', new_img_size, '#ffffff')

# вставляем картинки в фоновое изображение
# отступ у первой картинки (0, 0) 
img.paste(img1, (0, 0))
# отступ у второй картинки (img_01_size[0] + 2, 0) 
img.paste(img2, (img1_size[0] + border, 0))
# и т. д.
img.paste(img3, (0, img1_size[1] + border))
img.paste(img4, (img1_size[0] + border, img1_size[1] + border))

# в конце создадим белую рамку вокруг постера на 2px толще 
img = ImageOps.expand(img, border=border+2, fill='#ffffff')
# сохраняем новое изображение
img.save('merge_img.jpg', 'JPEG')