# two color images:
# 读取彩色图（默认就是 BGR，需要转成 RGB）
import cv2
import numpy as np
from matplotlib import pyplot as plt

im1 = cv2.imread("gaussian_kernel.jpg")[..., ::-1]
im2 = cv2.imread("gs_kernel_matrix.jpg")[..., ::-1]



images = [im1, im2]
titles = [""," "]

# 归一化到 [0,1]（float），保证显示不会过曝
images = [img.astype(np.float32) / 255.0 for img in images]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

for i in range(2):
    axes[i].imshow(images[i])  # 不需要 cmap
    axes[i].axis("off")
    axes[i].set_title(titles[i], fontsize=12, pad=5)

plt.tight_layout()
plt.savefig("gs_kernel.jpg", dpi=300)
plt.show()


# # four color images:
# # 读取彩色图（默认就是 BGR，需要转成 RGB）
# taj_original = cv2.imread("taj.jpg")[..., ::-1]
# taj_blurred_5 = cv2.imread("taj_blurred_5.png")[..., ::-1]
# taj_high_5 = cv2.imread("taj_high_5.png")[..., ::-1]
# taj_sharpened_5 = cv2.imread("taj_sharpened_5.png")[..., ::-1]
#
# images = [taj_original, taj_blurred_5, taj_high_5, taj_sharpened_5]
# titles = ["taj original (5)", "blurred taj (5)", "high frequency of taj (5)", "sharpened taj (5)"]
#
# # 归一化到 [0,1]（float），保证显示不会过曝
# images = [img.astype(np.float32) / 255.0 for img in images]
#
# # 绘制 1×4 grid
# fig, axes = plt.subplots(1, 4, figsize=(16, 5))
#
# for i in range(4):
#     axes[i].imshow(images[i])  # 不需要 cmap
#     axes[i].axis("off")
#     axes[i].set_title(titles[i], fontsize=12, pad=5)
#
# plt.tight_layout()
# plt.savefig("grid_taj_5.png", dpi=300)
# plt.show()


# # four grayscale images:
# dog_original = cv2.imread("dog_original.png", cv2.IMREAD_GRAYSCALE)
# dog_four_loop = cv2.imread("dog_four_loop_convolve.png", cv2.IMREAD_GRAYSCALE)
# dog_two_loop = cv2.imread("dog_two_loop_convolve.png", cv2.IMREAD_GRAYSCALE)
# dog_built_in_convolve2d = cv2.imread("dog_built_in_convolve.png", cv2.IMREAD_GRAYSCALE)
# images = [dog_original, dog_four_loop, dog_two_loop, dog_built_in_convolve2d]
# titles = ["dog original", "four-loop convolution", "two-loop convolution", "built-in convolve2d"]  # 你自定义的文字说明
# images = [img.astype(np.float32) / 255.0 for img in images]
#
# fig, axes = plt.subplots(1, 4, figsize=(16, 4))
#
# for i in range(4):
#     axes[i].imshow(images[i], cmap="gray")
#     axes[i].axis("off")
#     axes[i].set_title(titles[i], fontsize=12, pad=10)
#
# plt.tight_layout()
# plt.savefig("grid_part1_1.png", dpi=300)
# plt.show()


# two grayscale images:
# cameraman_DoG_x = cv2.imread("cameraman_DoG_x.png", cv2.IMREAD_GRAYSCALE)
# cameraman_DoG_y = cv2.imread("cameraman_DoG_y.png", cv2.IMREAD_GRAYSCALE)
# images = [cameraman_DoG_x, cameraman_DoG_y]
# titles = ["cameraman DoG_dx", "cameraman DoG_dy"]
# images = [img.astype(np.float32) / 255.0 for img in images]
#
# fig, axes = plt.subplots(1, 2, figsize=(8, 4))
#
# for i in range(2):
#     axes[i].imshow(images[i], cmap="gray")
#     axes[i].axis("off")
#     axes[i].set_title(titles[i], fontsize=12, pad=10)
#
# plt.tight_layout()
# plt.savefig("grid_cameraman_DoG.png", dpi=300)
# plt.show()

# # for 5 by 3 grayscale:
# cameraman_original = cv2.imread("cameraman_original.png", cv2.IMREAD_GRAYSCALE)
# cameraman_finite_difference_Ix = cv2.imread("cameraman_finite_difference_Ix.png", cv2.IMREAD_GRAYSCALE)
# cameraman_finite_difference_Iy = cv2.imread("cameraman_finite_difference_Iy.png", cv2.IMREAD_GRAYSCALE)
# cameraman_finite_difference_gradient_magnitude = cv2.imread("cameraman_finite_difference_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
# cameraman_finite_difference_binarize_gradient_magnitude = cv2.imread("cameraman_finite_difference_binarize_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
#
# gaussian_blurred_cameraman = cv2.imread("gaussian_blurred_cameraman.png", cv2.IMREAD_GRAYSCALE)
# gaussian_blurred_cameraman_Ix = cv2.imread("gaussian_blurred_cameraman_Ix.png", cv2.IMREAD_GRAYSCALE)
# gaussian_blurred_cameraman_Iy = cv2.imread("gaussian_blurred_cameraman_Iy.png", cv2.IMREAD_GRAYSCALE)
# gaussian_blurred_cameraman_gradient_magnitude = cv2.imread("gaussian_blurred_cameraman_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
# gaussian_blurred_cameraman_binarize_gradient_magnitude = cv2.imread("gaussian_blurred_cameraman_binarize_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
#
# grid_cameraman_DoG = cv2.imread("grid_cameraman_DoG.png", cv2.IMREAD_GRAYSCALE)
# cameraman_gaussian_Ix = cv2.imread("cameraman_gaussian_Ix.png", cv2.IMREAD_GRAYSCALE)
# cameraman_gaussian_Iy = cv2.imread("cameraman_gaussian_Iy.png", cv2.IMREAD_GRAYSCALE)
# cameraman_gaussian_gradient_magnitude = cv2.imread("cameraman_gaussian_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
# cameraman_gaussian_binarize_gradient_magnitude = cv2.imread("cameraman_gaussian_binarize_gradient_magnitude.png", cv2.IMREAD_GRAYSCALE)
#
# images = [cameraman_original, cameraman_finite_difference_Ix, cameraman_finite_difference_Iy,
#           cameraman_finite_difference_gradient_magnitude, cameraman_finite_difference_binarize_gradient_magnitude,
#           gaussian_blurred_cameraman, gaussian_blurred_cameraman_Ix, gaussian_blurred_cameraman_Iy,
#           gaussian_blurred_cameraman_gradient_magnitude, gaussian_blurred_cameraman_binarize_gradient_magnitude,
#           grid_cameraman_DoG, cameraman_gaussian_Ix, cameraman_gaussian_Iy,
#           cameraman_gaussian_gradient_magnitude, cameraman_gaussian_binarize_gradient_magnitude]
# titles = ["cameraman original", "convolved with Dx, \nfinite difference", "convolved with Dy, \nfinite difference",
#           "gradient magnitude, \nfinite difference", "binarized gradient magnitude, \nfinite difference",
#           "blurred with Gaussian kernel", "blurred with Gaussian kernel, \nthen convolved with Dx", "blurred with Gaussian kernel, \nthen convolved with Dy",
#           "gradient magnitude, \nfirst blurred with Gaussian", "binarized gradient magnitude, \nfirst blurred with Gaussian",
#           "DoG", "convolved with DoG_dx", "convolved with DoG_dy",
#           "gradient magnitude, \nconvolved with DoG", "binarized gradient magnitude, \nconvolved with DoG",]
# images = [img.astype(np.float32) / 255.0 for img in images]
#
# fig, axes = plt.subplots(3, 5, figsize=(12, 9))
# axes = axes.ravel()
#
# for i in range(15):
#     axes[i].imshow(images[i], cmap="gray")
#     axes[i].axis("off")
#     axes[i].set_title(titles[i], fontsize=12, pad=10)
#
# plt.tight_layout()
# plt.savefig("grid_cameraman_compare.png", dpi=300)
# plt.show()