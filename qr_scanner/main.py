import cv2
import numpy as np
import sys
import time

def main():
    if (len(sys.argv) != 2):
        print(f"usage: python3 {sys.argv[0]} <image>")
        return

    image = cv2.imread(sys.argv[1])

    qr_detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = qr_detector.detectAndDecode(image)

    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error")

if (__name__ == "__main__"):
    main()
