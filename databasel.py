import sqlite3

# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('car_plates.db')
c = conn.cursor()

# Create the table
c.execute('''CREATE TABLE IF NOT EXISTS car_plates
             (number_plate TEXT PRIMARY KEY,
              owner TEXT,
              make TEXT,
              model TEXT,
              color TEXT,
              price REAL,
              year INTEGER,
              fuel_type TEXT,
              engine_displacement REAL,
              transmission TEXT,
              body_type TEXT,
              mileage REAL,
              seating_capacity INTEGER,
              length REAL,
              width REAL,
              height REAL,
              ground_clearance REAL,
              kerb_weight REAL,
              gross_weight REAL,
              fuel_tank_capacity REAL,
              tire_size TEXT,
              wheel_size TEXT,
              power REAL,
              torque REAL,
              top_speed REAL,
              acceleration REAL,
              safety_rating INTEGER,
              emissions_rating TEXT,
              service_cost REAL,
              insurance_cost REAL,
              resale_value REAL)''')

# Insert data into the table
car_data = [
    ('DL1ABC1234', 'Sanjana Iyer', 'Maruti Suzuki', 'Swift', 'Red', 7.5, 2022, 'Petrol', 1.2, 'Manual', 'Hatchback', 21.2, 5, 3.84, 1.73, 1.53, 0.17, 930, 1305, 37, '185/60 R15', '15"', 82, 113, 180, 11.2, 4, 'BS6', 25000, 18000, 5.1),
    ('MH12DE3456', 'Mehul More', 'Hyundai', 'Creta', 'White', 11.0, 2021, 'Diesel', 1.5, 'Automatic', 'SUV', 17.8, 5, 4.31, 1.79, 1.62, 0.21, 1300, 1750, 50, '215/60 R17', '17"', 115, 250, 190, 10.5, 5, 'BS6', 30000, 25000, 7.8),
    ('KA51FG7890', 'Aarshin Narsapurkar', 'Tata', 'Nexon', 'Blue', 9.0, 2020, 'Petrol', 1.2, 'Manual', 'SUV', 16.5, 5, 3.99, 1.81, 1.62, 0.21, 1150, 1580, 44, '215/60 R16', '16"', 120, 170, 185, 11.0, 4, 'BS6', 22000, 20000, 6.2),
    ('DL2XYZ5678', 'Rutuja Patankar', 'Honda', 'City', 'Silver', 12.5, 2023, 'Petrol', 1.5, 'Automatic', 'Sedan', 17.8, 5, 4.55, 1.75, 1.49, 0.17, 1150, 1580, 40, '185/55 R16', '16"', 119, 145, 200, 10.8, 5, 'BS6', 35000, 28000, 9.1),
    ('RJ14AB1234', 'Abhishek Easuraj', 'Mahindra', 'Scorpio', 'Black', 15.0, 2019, 'Diesel', 2.2, 'Manual', 'SUV', 14.5, 7, 4.46, 1.86, 1.87, 0.23, 1825, 2550, 60, '235/65 R17', '17"', 140, 320, 180, 12.5, 4, 'BS4', 40000, 35000, 8.5),
    ('21BH0001AA', 'Arnav Mandlik', 'Renault', 'Duster', 'Grey', 10.0, 2021, 'Diesel', 1.5, 'Manual', 'SUV', 19.6, 5, 4.31, 1.82, 1.69, 0.21, 1250, 1700, 50, '215/65 R16', '16"', 110, 245, 175, 11.0, 4, 'BS6', 28000, 22000, 7.0),
    ('GJ01AB1234', 'Rohan Prakasan', 'Toyota', 'Fortuner', 'Pearl White', 37.0, 2022, 'Diesel', 2.8, 'Automatic', 'SUV', 14.2, 7, 4.79, 1.85, 1.83, 0.22, 2190, 3000, 80, '265/60 R18', '18"', 204, 500, 200, 11.0, 5, 'BS6', 50000, 45000, 28.5),
    ('KA05CD5678', 'Iris Soj', 'Kia', 'Seltos', 'Glacier White Pearl', 14.5, 2021, 'Petrol', 1.5, 'Automatic', 'SUV', 16.5, 5, 4.32, 1.8, 1.64, 0.19, 1315, 1700, 50, '215/60 R17', '17"', 115, 144, 190, 11.5, 5, 'BS6', 35000, 30000, 10.2),
    ('MH12EF9012', 'Manish Bhoi', 'Maruti Suzuki', 'Baleno', 'Metallic Blue', 8.5, 2020, 'Petrol', 1.2, 'Manual', 'Hatchback', 21.0, 5, 3.99, 1.75, 1.51, 0.17, 935, 1300, 37, '185/60 R16', '16"', 83, 113, 180, 11.8, 4, 'BS6', 25000, 18000, 5.8),
    ('DL2GH3456', 'Shreyas Khairnar', 'Hyundai', 'Verna', 'Polar White', 10.0, 2023, 'Petrol', 1.5, 'Automatic', 'Sedan', 17.5, 5, 4.48, 1.73, 1.47, 0.17, 1150, 1580, 45, '195/55 R16', '16"', 115, 144, 195, 10.2, 5, 'BS6', 30000, 25000, 8.2)
]

for plate in car_data:
    c.execute("INSERT OR REPLACE INTO car_plates (number_plate, owner, make, model, color, price, year, fuel_type, engine_displacement, transmission, body_type, mileage, seating_capacity, length, width, height, ground_clearance, kerb_weight, gross_weight, fuel_tank_capacity, tire_size, wheel_size, power, torque, top_speed, acceleration, safety_rating, emissions_rating, service_cost, insurance_cost, resale_value) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", plate)
    
# Commit the changes and close the connection
conn.commit()
conn.close()
