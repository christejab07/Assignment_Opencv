from pyzbar.pyzbar import decode
import cv2

# Read the image
image = cv2.imread("IMG_2022.jpg")

# Decode the barcode
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")
