class Room:
    def __init__(self, room_no, type, floor, rate, status=True, amenities=None):
        self.room_no = room_no
        self.type = type
        self.floor = floor
        self.rate = rate
        self.status = status
        self.amenities = amenities if amenities else []

    def is_Available(self, fromDate, toDate):
        if self.status:
            print("The Room is available for the mentioned dates")
        else:
            print("Oops the room is unavailable")

    def updatestatus(self):
        self.status = not self.status


class Booking:
    def __init__(self, booking_id, guest_id, roomNumber, checkIn, checkOut, status=True):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.roomNumber = roomNumber
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.status = status


class Guest:
    def __init__(self, guest_Id, name, phone, email):
        self.guest_Id = guest_Id
        self.name = name
        self.phone = phone
        self.email = email
        self.bookings = []

    def make_booking(self, booking_id):
        self.bookings.append(booking_id)


class Invoice:
    def __init__(self, invoice_id, booking_id, roomCost, taxes, extras=0):
        self.invoice_id = invoice_id
        self.booking_id = booking_id
        self.roomCost = roomCost
        self.taxes = taxes
        self.extras = extras
        self.total = roomCost + taxes + extras


class HotelManager:
    def __init__(self):
        self.manager_details = []
        self.room = {}
        self.guest_details = {}
        self.bookings = {}
        self.invoices = {}
        self.manager_count = 1
        self.room_count = 1
        self.guest_count = 1
        self.booking_count = 1
        self.invoice_count = 1

    def add_manager(self, manager_id):
        if manager_id not in self.manager_details:
            self.manager_details.append(manager_id)
            self.manager_count += 1
            print("Manager", manager_id, "Is Successfully Added")
        else:
            print("Manager ID already exists")

    def add_room(self, type, floor, rate, status=True, amenities=None):
        room = Room(self.room_count, type, floor, rate, status, amenities)
        self.room[self.room_count] = room
        print("Room", self.room_count, "Successfully added")
        self.room_count += 1

    def setRates(self, room_no, rates):
        if room_no in self.room:
            self.room[room_no].rate = rates
            print("Rate updated successfully")
        else:
            print("Invalid room number")

    def add_guest(self, name, phone, email):
        guest = Guest(self.guest_count, name, phone, email)
        self.guest_details[self.guest_count] = guest
        print("Guest", name, "added with ID", self.guest_count)
        self.guest_count += 1

    def view_guest(self):
        for g in self.guest_details.values():
            print("Guest ID:", g.guest_Id)
            print("Name:", g.name)
            print("Phone:", g.phone)
            print("Email:", g.email)
            print()

    def viewOccupancy(self):
        print("Free Rooms")
        print("----------")
        for r in self.room.values():
            if r.status:
                print("Room No:", r.room_no)
                print("Type:", r.type)
                print("Floor:", r.floor)
                print("Rate:", r.rate)
                print()

    def add_booking(self, room_no, guest_id, checkIn, checkOut):
        if guest_id in self.guest_details and room_no in self.room:
            room = self.room[room_no]
            if room.status:
                booking = Booking(self.booking_count, guest_id, room_no, checkIn, checkOut)
                self.bookings[self.booking_count] = booking
                room.status = False
                self.guest_details[guest_id].make_booking(self.booking_count)
                print("Booking successful. Booking ID:", self.booking_count)
                self.booking_count += 1
            else:
                print("Room is not available")
        else:
            print("Invalid guest ID or room number")

    def checkout(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings[booking_id]
            room = self.room[booking.roomNumber]
            room.status = True

            days = 1
            roomCost = room.rate * days
            taxes = roomCost * 0.1

            invoice = Invoice(self.invoice_count, booking_id, roomCost, taxes)
            self.invoices[self.invoice_count] = invoice

            print("Checkout successful")
            print("Invoice ID:", self.invoice_count)
            print("Room Cost:", roomCost)
            print("Taxes:", taxes)
            print("Total:", invoice.total)

            self.invoice_count += 1
        else:
            print("Invalid booking ID")

    def is_manager(self, manager_id):
        return manager_id in self.manager_details


def main():
    manager = HotelManager()

    print("Welcome To MindBlowers Hotel")

    while True:
        print("\n1.Add Manager")
        print("2.Add Rooms")
        print("3.Set Prices")
        print("4.View Occupancy")
        print("5.Add Guest")
        print("6.Book Room")
        print("7.View Guests")
        print("8.Checkout")
        print("9.Exit")

        choice = int(input("Enter choice: "))

        if choice == 9:
            break

        admincode = input("Enter admin code: ")

        if admincode != "1234":
            print("Wrong admin code")
            continue

        if choice == 1:
            manager_id = int(input("Enter manager ID: "))
            manager.add_manager(manager_id)

        elif choice == 2:
            manager_id = int(input("Enter manager ID: "))
            if manager.is_manager(manager_id):
                type = input("Room type: ")
                floor = input("Floor: ")
                rate = int(input("Rate: "))
                manager.add_room(type, floor, rate)

        elif choice == 3:
            manager_id = int(input("Enter manager ID: "))
            if manager.is_manager(manager_id):
                room_no = int(input("Room number: "))
                rate = int(input("New rate: "))
                manager.setRates(room_no, rate)

        elif choice == 4:
            manager.viewOccupancy()

        elif choice == 5:
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_guest(name, phone, email)

        elif choice == 6:
            manager.viewOccupancy()
            room_no = int(input("Room number: "))
            guest_id = int(input("Guest ID: "))
            checkIn = input("Check-in: ")
            checkOut = input("Check-out: ")
            manager.add_booking(room_no, guest_id, checkIn, checkOut)

        elif choice == 7:
            manager.view_guest()

        elif choice == 8:
            booking_id = int(input("Booking ID: "))
            manager.checkout(booking_id)


if __name__ == "__main__":
    main()