import matplotlib.pyplot as plt
import cv2
import easyocr

# Load the image
image = cv2.imread('pic.jpg')  # Replace 'image.jpg' with the actual filename

# Create an EasyOCR reader instance
reader = easyocr.Reader(['en'])

# Extract text from the image
results = reader.readtext(image)

# Iterate through the extracted text
for result in results:
    text = result[1]
    bbox = result[0]

    # Check if the extracted text looks like a number plate
    if len(text) >= 5 and any(char.isdigit() for char in text):
        # Get the coordinates of the bounding box
        x1, y1 = tuple(map(int, bbox[0]))
        x2, y2 = tuple(map(int, bbox[2]))

        # Draw a rectangle around the number plate
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the extracted number plate text
        print("Number Plate:", text)

# Display the image with the number plate outlined
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()