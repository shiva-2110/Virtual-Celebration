from PIL import Image
import stepic

# Load your image
img = Image.open("G.jpg")

# Hide your message
secret = stepic.encode(img, b"Gaurav is awesome!")

# Save the new image
secret.save("image2.png")
