import os
from PIL import Image
import matplotlib.pyplot as plt

# Directory containing the images
img_dir = ""   # change if needed

# Image filenames in order
image_files = [
    "000_Noisy_image_t_690.png",
    "001_Iter_0_t_690.png",
    "002_Iter_5_t_540.png",
    "003_Iter_10_t_390.png",
    "004_Iter_15_t_240.png",
    "005_Iter_20_t_90.png",
    "006_Final_iterative_denoised_image.png",
    "007_Original_image.png",
    "008_UNet_One_step_denoised_image.png",
    "009_Gaussian_denoised_image.png",
]

# Create captions from filenames
captions = [
    f.replace(".png", "").replace("_", " ")
    for f in image_files
]

# Load images
images = [Image.open(os.path.join(img_dir, f)) for f in image_files]

# Create grid: 2 rows x 5 columns
rows, cols = 2, 5
fig, axes = plt.subplots(rows, cols, figsize=(18, 7))

for i, ax in enumerate(axes.flatten()):
    ax.imshow(images[i])
    ax.set_title(captions[i], fontsize=10)
    ax.axis("off")

plt.tight_layout()
plt.savefig("iterative_denoised_grid.png", dpi=300, bbox_inches="tight")
plt.show()

