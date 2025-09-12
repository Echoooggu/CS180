# CS180 (CS280A): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio

# name of the input file
imname = 'cathedral.jpg'

# read in the image
im = skio.imread(imname)

# convert to double (might want to do this later on to save memory)
im = sk.img_as_float(im)

# compute the height of each part (just 1/3 of total)
height = np.floor(im.shape[0] / 3.0).astype(np.uint64)

# separate color channels
b = im[:height]
g = im[height: 2 * height]
r = im[2 * height: 3 * height]

# align the images
# functions that might be useful for aligning the images include:
# np.roll, np.sum, sk.transform.rescale (for multiscale)
def align(img, ref):
    best_score = float('inf')
    best_shift = (0, 0)
    best_img = im
    max_shift = 15
    # global best_shift, best_img
    for dx in range(-max_shift, max_shift + 1):
        for dy in range(-max_shift, max_shift + 1):
            shifted = np.roll(img, dx, axis=0)  # axis = 0: up and down
            shifted = np.roll(shifted, dy, axis=0)  # axis = 1: left and right

            score = np.sum((shifted - ref) ** 2)

            if score < best_score:
                best_score = score
                best_shift = (dx, dy)
                best_img = shifted

    print("best score:", best_score)
    print("best shift:", best_shift)
    return best_img


ag = align(g, b)
ar = align(r, b)
# create a color image
im_out = np.dstack([ar, ag, b])

# save the image
fname = '/out_path/out_fname.jpg'
skio.imsave(fname, im_out)

# display the image
skio.imshow(im_out)
skio.show()