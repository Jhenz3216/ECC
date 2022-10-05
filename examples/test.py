import matplotlib.pyplot as plt
import matplotlib.image as mpimg



img = mpimg.imread('examples/stinkbug.png')
print(img)

lum_img = img[:, :, 0]

# This is array slicing.  You can read more in the `Numpy tutorial
# <https://numpy.org/doc/stable/user/quickstart.html>`_.

plt.imshow(lum_img)
plt.show()