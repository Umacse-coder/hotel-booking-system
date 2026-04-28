# Hotel Booking System (Console-Based)

## Overview

This is a console-based Hotel Booking System implemented in Python using Object-Oriented Programming principles. The system allows hotel management to manage rooms, guests, bookings, and generate invoices during checkout.

---

## Features

### Management Features

* Add Manager
* Add Rooms
* Set Room Rates
* View Room Occupancy
* Add Guests
* Book Rooms
* Checkout and generate invoice
* View Guest Details

---

## Functional Flow

1. Manager logs in using admin code
2. Manager adds rooms and guests
3. Manager books a room for a guest
4. Room status changes to unavailable after booking
5. During checkout:

   * Room becomes available again
   * Invoice is generated
   * Total bill is calculated

---

## Project Structure

### Room

Represents a hotel room.

Attributes:

* room_no
* type
* floor
* rate
* status
* amenities

---

### Booking

Stores booking details.

Attributes:

* booking_id
* guest_id
* roomNumber
* checkIn
* checkOut
* status

---

### Guest

Stores guest information.

Attributes:

* guest_Id
* name
* phone
* email
* bookings

---

### Invoice

Generates billing details during checkout.

Attributes:

* invoice_id
* booking_id
* roomCost
* taxes
* extras
* total

---

### HotelManager

Main controller class managing all operations.

Responsibilities:

* Manage managers
* Manage rooms
* Manage guests
* Handle bookings
* Handle checkout and billing

---

## How to Run

1. Install Python
2. Save the file as:

hotel_booking_system.py

3. Run the program:

python hotel_booking_system.py

---

## Admin Access

Admin Code: 1234

---

## Date Input Format

Enter dates in the following format:

YYYY-MM-DD

Example:
2026-04-28

---

## Billing Logic

* Total days are calculated based on check-in and check-out
* Room cost = rate × number of days
* Tax is applied (10%)
* Final bill = room cost + tax

---

## Sample Workflow

1. Add Manager
2. Add Rooms
3. Add Guest
4. Book Room
5. Enter check-in and check-out dates
6. Checkout using booking ID
7. Invoice is generated

---

## Limitations

* No database (data is not saved permanently)
* No user authentication for customers
* Basic date validation
* No cancellation feature
* No GUI (console-based only)

---

## Future Improvements

* Add database integration (MySQL / SQLite)
* Implement proper date validation
* Add cancellation and refund system
* Build web version using Flask
* Add login system for users
* Enhance invoice generation

---

## Concepts Used

* Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Lists and Dictionaries
* Basic input/output handling

---

## Author

Developed as part of learning Python application development and system design.
