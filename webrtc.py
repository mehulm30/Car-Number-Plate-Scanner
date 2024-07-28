import streamlit as st
import cv2
import easyocr
import sqlite3
import matplotlib.pyplot as plt
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode

class LicensePlateDetector(VideoProcessorBase):
    def __init__(self):
        super().__init__()
        self.reader = easyocr.Reader(['en'])
        self.camera_started = False

    def recv(self, frame):
     if self.camera_started:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = self.reader.readtext(gray)

        for detection in results:
            if "license plate" in detection[1].lower():
                plate_number = detection[0]
                st.write("License plate found:", plate_number)
                # Check the database for the plate number
                if self.query_vehicle_details(plate_number):
                    st.write("License plate exists in the database")
                else:
                    st.write("License plate does not exist in the database")
                # Visualize the detected license plate
                self.visualize_plate(frame, detection[2])

     return frame

    def visualize_plate(self, frame, box):
        # Convert box coordinates to integer
        box = [int(coord) for coord in box]

        # Draw a rectangle around the detected plate
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

        # Display the frame with the detected plate
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        st.pyplot()

    def query_vehicle_details(self,number_plate):
        conn = sqlite3.connect('car_plates.db')
        c = conn.cursor()
        c.execute("SELECT owner, make, model FROM car_plates WHERE number_plate=?", (number_plate,))
        result = c.fetchone()
        conn.close()
        return result if result else None

def main():
    st.title("License Plate Scanner")

    webrtc_ctx = webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=LicensePlateDetector,
        async_processing=True,
    )

    if webrtc_ctx.video_processor and not webrtc_ctx.state.playing:
        st.write("Click the button below to start the camera")
        start_camera_button = st.button("Start Camera")
        start_scanning_button = st.button("Start Scanning")

        if start_camera_button:
            webrtc_ctx.state.playing = True

        if start_scanning_button:
            webrtc_ctx.video_processor.scanning_started = True

if __name__ == "__main__":
    main()  
