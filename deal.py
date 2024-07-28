import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QCheckBox, QMessageBox
from PyQt5.QtGui import QFont, QPixmap, QImage  # Corrected import
from PyQt5.QtCore import Qt, QTimer
import cv2
import easyocr

class CarPlateVision(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reader = easyocr.Reader(['en'])
        self.cap = cv2.VideoCapture(0)  # Replace 0 with the appropriate camera index
        self.allow_camera = False

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Car Plate Recognition")
        self.setStyleSheet("background-color: #F0F8FF;")  # AliceBlue color

        # Create central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Create title label
        title_label = QLabel("Car Plate Recognition")
        title_label.setStyleSheet("font-weight: bold; font-size: 20px; color: #333333;")
        title_label.setAlignment(Qt.AlignHCenter)

        # Create image label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignHCenter)

        # Create input field for number plate
        self.plate_input = QLineEdit()
        self.plate_input.setPlaceholderText("Extracted Number Plate")
        self.plate_input.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid #CCCCCC;")
        self.plate_input.setReadOnly(True)

        # Create confirmation button
        confirm_button = QPushButton("Confirm")
        confirm_button.setStyleSheet("font-size: 14px; padding: 5px 10px; background-color: #4CAF50; color: white;")
        confirm_button.clicked.connect(self.confirm_plate)

        # Create allow camera access checkbox
        self.camera_checkbox = QCheckBox("Allow Camera Access")
        self.camera_checkbox.setStyleSheet("font-size: 14px; color: #333333;")
        self.camera_checkbox.stateChanged.connect(self.toggle_camera)

        # Add components to the layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(self.image_label)
        main_layout.addWidget(self.plate_input)
        main_layout.addWidget(confirm_button)
        main_layout.addWidget(self.camera_checkbox)

        # Set the main layout for the central widget
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def toggle_camera(self, state):
        self.allow_camera = bool(state)
        if self.allow_camera:
            self.capture_and_process_frame()

    def capture_and_process_frame(self):
        ret, frame = self.cap.read()
        if ret:
            results = self.reader.readtext(frame)
            plate_number = ""
            for result in results:
                plate_number += result[1]
            self.plate_input.setText(plate_number)

            # Convert the frame to a QPixmap and display it in the image label
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, _ = frame.shape
            bytes_per_line = width * 3
            qimg = QPixmap.fromImage(
                QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)  # Corrected usage
            )
            self.image_label.setPixmap(qimg)

        if self.allow_camera:
            cv2.waitKey(1)
            QTimer.singleShot(50, self.capture_and_process_frame)

    def confirm_plate(self):
        plate_number = self.plate_input.text()
        if plate_number:
            # Check if the extracted number plate matches the user information in the database
            # Replace this with your database lookup code
            user_info = "Sanjana Iyer, Navi Mumbai. Car Info: Maruti Suzuki, Swift, RED, 7.5 Lakhs, 2022"
            if plate_number == "21 BH 0001 AA":
                QMessageBox.information(self, "Confirmation", f"Number Plate: {plate_number}\nUser Information: {user_info}")
            else:
                QMessageBox.warning(self, "Confirmation", f"Number Plate: {plate_number}\nUser Information: Not found in database.")
        else:
            QMessageBox.warning(self, "Error", "No number plate extracted.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    car_plate_vision = CarPlateVision()
    car_plate_vision.show()
    sys.exit(app.exec_())
    
