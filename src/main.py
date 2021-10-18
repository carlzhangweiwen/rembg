from rembg.bg import remove
import numpy as np
import io
from PIL import Image

if __name__ == '__main__':
    input_path = '/Users/weiwenzhang/Documents/github/rembg/test/example_2_1.png'
    output_path = '/Users/weiwenzhang/Documents/github/rembg/test/example_2_1.out.png'

    f = np.fromfile(input_path)
    result = remove(f, "u2net")
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)
