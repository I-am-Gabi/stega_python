from scipy import misc
import numpy as np


def read_image(file_name):
    return misc.imread(file_name)


def image():
    f = misc.face()
    misc.imsave('face.png', f)

    face = misc.imread('face.png')
    print face.shape, face.dtype  # 8-bit images (0-255)

    face.tofile('face.raw')
    face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
    face_from_raw.shape = (768, 1024, 3)

    import matplotlib.pyplot as plt
    plt.imshow(f)  # plt.show()
