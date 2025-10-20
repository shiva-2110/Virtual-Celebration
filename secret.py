from PIL import Image
import stepic

# Load the stego image
img = Image.open("image2.png")

# Reveal the hidden message
f = stepic.decode(img)
print(f)
