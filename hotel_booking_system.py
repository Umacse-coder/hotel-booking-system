class Room:
    #constructor
    def __init__(self,room_no,type,floor,rate,status=True,amenities=[]):
        self.room_no=room_no
        self.type=type
        self.floor=floor
        self.rate=rate
        self.status=status
        self.amenities=amenities
    # check is the room is available for the particular date
    def is_Available(self,fromDate,toDate):

        if self.status:
            print("The Room is available for the mentioned dates")
        else:
            print("Oops the room is unavailable")
    def updatestatus(self):
        if self.status:
            self.status=False
        else:
            self.status=True
class Booking:
    def __init__(self,booking_id,guest_id,roomNumber,checkIn,checkOut,status=True):
        self.booking_id=booking_id
        self.guest_id=guest_id
        self.roomNumber=roomNumber
        self.checkIn=checkIn
        self.checkOut=checkOut
        self.status=status
class Guest:
    def __init__(self,guest_Id,name,phone,email):
        self.guest_Id=guest_Id
        self.name=name
        self.phone=phone
        self.email=email
        self.bookings=[]
    def make_booking(self,room_no):
        self.bookings.append(room_no)
        
class Invoice:
    def __init__(self,invoice_id,booking_id,roomCost,taxes,extras=0):
        self.invoice_id=invoice_id
        self.booking_id=booking_id
        self.roomCost=roomCost
        self.taxes=taxes
        self.total=0
        self.extras=extras

        
class HotelManager:
    def __init__(self):
           self.manager_details=[]
           self.room={}
           self.guest_details={}
           self.manager_count=1
           self.room_count=1
           self.guest_count=1
    def add_manager(self,manager_id):
        if manager_id not in self.manager_details:
            
            self.manager_details.append(manager_id)
            self.manager_count+=1
            print("Manager ",manager_id,"Is SuccessFully Added")
        else:
            print("Already the manager iD IS PRESENT")
    def  add_room(self,type,floor,rate,status=True,amenities=[]):
        room=Room(self.room_count,type,floor,rate,status,amenities)
        self.room[self.room_count]=room
        print("Room ",self.room_count,"Successfully added")
        self.room_count+=1
    def setRates(self,room_no,rates):
        if room_no in self.room:
            self.room[room_no].rate=rates 
            print("Rate is set  successfully")
        else:
            print("Room no is Not Valid")
    def add_guest(self,name,phone,email):
        guest=Guest(self.guest_count,name,phone,email)
        self.guest_details[self.guest_count]=guest
        print("The Guest ",name ,"is successfully added")
        self.guest_count+=1
    def view_guest(self):
        print("Guest Details")
        print("-------------")
        for i in self.guest_details:
            print("Guest_id: ",self.guest_details[i].guest_Id)
            print("Guest Name: ",self.guest_details[i].name)
            print("Guest Phone: ",self.guest_details[i].phone)
            print("Guest Email: ",self.guest_details[i].email)
    
    def add_booking(self,room_no,guest_id):
        if guest_id in self.guest_details:
            if room_no in self.room:
                self.room[room_no].status=False
                


    
    def viewOccupancy(self):
        for i in self.room:
            print("Free Rooms")
            print("----------")
            print()
            if self.room[i].status==True:
                print("ROOM_NO :",self.room[i].room_no)
                print("Type: ",self.room[i].type)
                print("Floor: ",self.room[i].floor)
                print("Rate : ",self.room[i].rate)
                print()
    def is_manager(self,manager_id):
        if manager_id in self.manager_details:
            return True
        return False


    

    

def main():
    manager=HotelManager()


    
    print("\t\t\t\tWelcome To MindBlowers Hotel ")
    print("\t\t\t\t----------------------------")
    print()
    print("\t\tUser Type:")
    print("1.Management")
    print("2.Customer")
        
    choice=int(input("Please Enter Which Type Of User: "))
    if choice==1:
        while True:
            print("\t\tMENU")
            print("\t\t----")
            print("1.Add Manager")
            print("2.Add Rooms")
            print("3.Set Prices")
            print("4.View Occupancys")
            print("5.Add a Guest")
            print("6.Book a Room")
            print("7.View Guest Details")
            print("8.Exit")
            choice1=int(input("Enter Your Choice (1,2,3,4,5): "))
            #admin code=1234
            if choice1==8:
                print("Exit")
                break
            admincode=input("Please Enter Admin code  To Proceed Further: ")
            print()
            if admincode=="1234" :
                if choice1==1:
                    print()
                   
                    manager_id=int(input("Enter The Manager Id You want to ADD: "))
                    manager.add_manager(manager_id)
                elif choice1==2:
                    manager_id=int(input("Enter Your manager Id: "))
                    if manager.is_manager(manager_id):
                        type=input("Enter the room type: ")
                        floor=input("Enter the floor no: ")
                        rate=int(input("Enter the rate: "))
                        manager.add_room(type,floor,rate)
                    else:
                        print("Manager Id Invalid")
                elif choice1==3:
                    manager_id=int(input("Enter Your manager Id"))
                    if manager.is_manager(manager_id):
                        room_no=int(input("Enter room_no for which you want to change The Rate"))
                        rate=int(input("Enter the rate "))

                        manager.setRates(room_no,rate)
                    else:
                        print("Manager Id Invalid")
                elif choice1==4:
                    manager_id=int(input("Enter Your manager Id"))
                    if manager.is_manager(manager_id):
                        
                        manager.viewOccupancy()
                    else:
                        print("Manager Id Invalid")
                elif choice1==5:
                    manager_id=int(input("Enter Your manager Id"))
                    if manager.is_manager(manager_id):
                        name=input("Enter the name of the Guest: ")
                        phone=input("Enter the phone number: ")
                        email=input("Enter the Email: ")
                        manager.add_guest(name,phone,email)
                    else:
                        print("Manager Id Invalid")
                elif choice1==6:
                    manager_id=int(input("Enter Your manager Id"))
                    if manager.is_manager(manager_id):
                        print("Free Rooms")
                        manager.viewOccupancy()
                        room_no=int(input("Enter a room no from this"))
                    else:
                        print("Manager Id Invalid")


                elif choice1==7:
                    manager_id=int(input("Enter Your manager Id"))
                    if manager.is_manager(manager_id):
                        
                        manager.view_guest()
                    else:
                        print("Manager Id Invalid")

                else:
                    print("Exit")
                    break


                    


            else:
                print("Sorry Wrong Admin code ")
            
            

            

if __name__=="__main__":
    main()

        


    