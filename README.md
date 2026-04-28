

---

# Hotel Management System (Console-Based)

## Overview

This is a console-based Hotel Management System implemented in Python using Object-Oriented Programming (OOP) principles. The system allows hotel management to handle room management, guest management, booking operations, and occupancy tracking.

---

## Features

### Management Features

* Add Manager
* Add Rooms
* Set Room Rates
* View Room Occupancy
* Add Guests
* Book Rooms
* View Guest Details

### Customer Features

* Guest creation
* Room booking (handled by manager)

---

## Project Structure

### Room Class

Represents a hotel room.

Attributes:

* room_no
* type
* floor
* rate
* status
* amenities

Methods:

* is_Available()
* updatestatus()

---

### Booking Class

Handles booking details.

Attributes:

* booking_id
* guest_id
* roomNumber
* checkIn
* checkOut
* status

---

### Guest Class

Stores guest details.

Attributes:

* guest_Id
* name
* phone
* email
* bookings

Methods:

* make_booking()

---

### Invoice Class

Handles billing.

Attributes:

* invoice_id
* booking_id
* roomCost
* taxes
* extras
* total

---

### HotelManager Class

Main controller class.

Responsibilities:

* Manage managers
* Manage rooms
* Manage guests

Key Methods:

* add_manager()
* add_room()
* setRates()
* add_guest()
* view_guest()
* viewOccupancy()
* is_manager()

---

## How to Run

1. Install Python (if not already installed)
2. Save the file as `hotel_booking_system.py`
3. Run the program using:

python hotel_booking_system.py

---

## Admin Access

Admin Code: 1234

---

## Sample Workflow

1. Select Management
2. Enter admin code
3. Add manager
4. Add rooms
5. Add guest
6. Book room
7. View occupancy

---

## Limitations

* Booking system is incomplete (no date validation)
* No persistent storage (data is lost after program ends)
* Invoice calculation is not implemented
* Room availability does not consider date ranges
* No customer login system

---

## Future Improvements

* Add database support (MySQL or SQLite)
* Implement booking with date validation
* Generate invoices automatically
* Add a graphical interface (Tkinter or Flask)
* Improve authentication and security
* Add cancellation and refund features

---

## Concepts Used

* Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Lists and Dictionaries

---

## Author

Developed as part of learning Python application development and system design.
