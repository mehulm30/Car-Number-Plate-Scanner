import streamlit as st
import sqlite3
import scanning as ss
# Function to query the database and return the owner's name, make, and model
def query_vehicle_details(number_plate):
    conn = sqlite3.connect('car_plates.db')
    c = conn.cursor()
    c.execute("SELECT owner, make, model FROM car_plates WHERE number_plate=?", (number_plate,))
    result = c.fetchone()
    conn.close()
    return result if result else None

r1=""
# def getResult(text):
#     r1=text
#     # result=text
    

def main():
    st.title("License Plate Scanner")
    # Input field for vehicle license number
    # Button to submit
    if st.button("Submit"):
        ss.scanner()
        vehicle_details = query_vehicle_details(r1)
        if vehicle_details:
            owner, make, model = vehicle_details[:3]  # Ensure only first 3 values are unpacked
            # st.success(f"Owner Name: {owner} \n Make: {make} \n Model: {model}")
            success_message = f'Owner Name: {owner}\nMake: {make}\nModel: {model}'
            st.markdown(r1)
            st.success(success_message,icon="✅")

        else:
            st.error("No details found for the provided license number.")

if __name__ == "__main__":
    main()
