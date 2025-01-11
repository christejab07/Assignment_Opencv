import cv2  # Import OpenCV library

# Read the image 'assignment-001-given.jpg'
image = cv2.imread("assignment-001-given.jpg")

# Draw a green rectangle on the image
cv2.rectangle(image, (260, 200), (990, 920), (0, 255, 0), 8)

# text specifications
text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 6
text_color = (0, 255, 0)

# Calculate the text size and position
(text_width, text_height), baseline = cv2.getTextSize(
    text, font, font_scale, font_thickness
)
x, y = 800, 180

# Calculate the background rectangle coordinates
background_start = (x, y - text_height - 15)
background_end = (x + text_width, y + 15)

# Create a black rectangle with 50% opacity for background
overlay = image.copy()
cv2.rectangle(
    overlay, background_start, background_end, (0, 0, 0), -1
)  # Black rectangle
cv2.addWeighted(overlay, 0.4, image, 0.6, 0, image) # Blend rectangle with original image

# Add the text in the semi-transparent rectangle
cv2.putText(image, text, (x, y), font, font_scale, text_color, font_thickness)

# Display the image in a new window named 'Image'
cv2.imshow("Image", image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite("assignment-001-result.jpg", image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
