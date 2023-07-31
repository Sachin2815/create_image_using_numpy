import numpy as np
import matplotlib.pyplot as plt

# Create a blank canvas for the image
width = 400
height = 300
channels = 3
image = np.zeros((height, width, channels), dtype=np.uint8)

#Background (lemon)
image[:300, 0:400, 0] = 255
image[:300, 0:400, 1] = 255
image[:300, 0:400, 2] = 102

# Table (Brown)
#1st leg

image[200:300, 50:100 , 0] = 55
image[200:300, 50:100, 1] = 0
image[200:300, 50:100, 2] = 9

#2nd leg

image[200:300, 300:350 , 0] = 55
image[200:300, 300:350, 1] = 0
image[200:300,300:350, 2] = 9

# Surface
image[175:200,25:375, 0] = 55
image[175:200,25:375, 1] = 0
image[175:200,25:375, 2] = 9


# TV (Black)
# base (black)

image[160:175,160:240, 0] = 0
image[160:175,160:240, 1] = 0
image[160:175,160:240, 2] = 0

# Screen back
image[50:160, 100:300,0] = 0
image[50:160, 100:300,1] = 0
image[50:160, 100:300,2] = 0

# Screen(view) (sky blue)

image[60:150, 110:290, 0] = 108
image[60:150, 110:290, 1] = 255
image[60:150, 110:290, 2] = 255
# Display the image
plt.imshow(image)
plt.axis('on')
plt.show()
