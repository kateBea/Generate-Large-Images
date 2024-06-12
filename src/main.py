from PIL import Image
import numpy as np

width, height = 2000, 2000

array = np.random.randint(255, size=(height, width, 3), dtype=np.uint8)
image = Image.fromarray(array)

image.save('output.png')