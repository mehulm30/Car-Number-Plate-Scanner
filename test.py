import cv2
import time
import os
import easyocr
import matplotlib.pyplot as plt

harcascade = "indian_license_plate.xml"
time.sleep(3)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 400
count = 0

# Define the folder path to save the ROI images
save_folder = "ocr"  # Change this to your desired folder path
os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist

def scanner():
  while True:
    success, img = cap.read()
    if success:  # Check if the frame was read successfully
     plate_cascade = cv2.CascadeClassifier(harcascade)
     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

     for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            img_roi = img[y:y + h, x:x + w]
            if img_roi.shape[0] > 0 and img_roi.shape[1] > 0:
                cv2.imshow("ROI", img_roi)  # display the roi

            cv2.imshow("Result", img)
            cv2.waitKey(2000)  # Increase the delay time to 2000 milliseconds
            cv2.destroyAllWindows()

            # Save the cropped image
            file_path = os.path.join(save_folder, f"scanned_img{count}.jpg")
            cv2.imwrite(file_path, img_roi)

            # Use EasyOCR to extract text from the saved image
            reader = easyocr.Reader(['en'])
            saved_image = cv2.imread(file_path)
            results = reader.readtext(saved_image)

            for result in results:
                text = result[1]

                # Check if the extracted text looks like a number plate
                if len(text) >= 5 and any(char.isdigit() for char in text):
                    print(f"Number Plate: {text}")
                    count += 1
                    if text:
                       return text
                    break  # Exit the loop after finding a number plate

     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

def main():
 print(f'{scanner()}')
