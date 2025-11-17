import cv2
import numpy as np
from matplotlib import pyplot as plt

im1 = cv2.imread("novel1.jpg")[..., ::-1]
im2 = cv2.imread("novel2.jpg")[..., ::-1]
im3 = cv2.imread("novel3.jpg")[..., ::-1]
im4 = cv2.imread("novel4.jpg")[..., ::-1]
# im5 = cv2.imread("iter_6000.png")[..., ::-1]
# im6 = cv2.imread("iter_90002.png")[..., ::-1]



images = [im1, im2, im3, im4]
titles = ["novel view 1", "novel view 2", "novel view 3", "novel view 4"]

# 归一化到 [0,1]（float），保证显示不会过曝
images = [img.astype(np.float32) / 255.0 for img in images]

fig, axes = plt.subplots(1, 4, figsize=(12, 5))

for i in range(4):
    axes[i].imshow(images[i])  # 不需要 cmap
    axes[i].axis("off")
    axes[i].set_title(titles[i], fontsize=12, pad=5)

plt.tight_layout()
plt.savefig("own_novel_views.png", dpi=300)
plt.show()


# # more than one row:
# im1 = cv2.imread("reconstruction_L3_H32.png")[..., ::-1]
# im2 = cv2.imread("reconstruction_L3_H256.png")[..., ::-1]
# im3 = cv2.imread("reconstruction_L10_H32.png")[..., ::-1]
# im4 = cv2.imread("reconstruction_L10_H256.png")[..., ::-1]
#
# images = [im1, im2, im3, im4]
# titles = ["L = 3, W = 32","L = 3, W = 256", "L = 10, W = 32", "L = 10, W = 256"]
#
# images = [img.astype(np.float32) / 255.0 for img in images]
#
# fig, axes = plt.subplots(2, 2, figsize=(12, 8))
#
# for i in range(4):
#     r = i // 2
#     c = i % 2
#     axes[r, c].imshow(images[i])
#     axes[r, c].axis("off")
#     axes[r, c].set_title(titles[i], fontsize=12, pad=5)
#
# plt.tight_layout()
# plt.savefig("part1_grid_oski.png", dpi=300, bbox_inches='tight')
# plt.show()
