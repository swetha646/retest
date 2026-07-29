def book_room(bookings):
    room_number = int(input("enter the room number : "))
    if room_number in bookings:
       print("Room number is already booked")
    else:
       guest_name = input("enter your name : ")
       room_type = input("enter type of room(delux/standard/suite): ")
       number_of_days = int(input("enter the number of days: "))
       total_price = float(input("enter the total price : "))
       if number_of_days > 0 and total_price > 0:
        bookings[room_number] ={
           "Room number":room_number,
           "Room type" : room_type,
           "Guest name":guest_name,
           "number of days":number_of_days,
           "total price":total_price
        }
        print("room booked successfully")
       else:
          print("number of days and total price should be greater than zero")

def view_bookings(bookings):
   if len(bookings) ==0:
      print("No booking records found")
   else:
      print("booking details : ")
      for room_number, details in bookings.items():
         print("Room number : " ,room_number)
         print("Room type :" ,details["Room type"])
         print("Guest name: ",details["Guest name"])
         print("number of days : ",details["number of days"])
         print("total price: ", details["total price"])

def search_bookings(bookings):
   room_number = int(input("enter the room number: "))
   if room_number in bookings:
      details = bookings[room_number]
      print("Room number :" ,room_number)
      print("Room type : ",details["Room type"])
      print("Guest name : ",details["Guest name"])
      print("number of days :",details["number of days"])
      print("total price: ", details["total price"])
   else:
      print("Bookings not found")

def update_days(bookings):
   room_number = int(input("enter the room number : "))
   if room_number in bookings:
      days = int(input("enter new number of days :"))
      if days > 0:
         bookings[room_number]["number of days"] = days
         print("Booking days updated successfully")
      else:
         print("number of days should be greater than zero")
   else:
      print("Bookings not found")

def cancel_booking(bookings):
   room_number = int(input("enter the room number : "))
   if room_number in bookings:
      del bookings[room_number]
      print("Booking cancelled sucessfully")
   else:
      print("Booking not found")

bookings ={}
while True:
   print("HOTEL ROOM BOOKING SYSTEM")
   print("1. Book room")
   print("2. View all bookings")
   print("3. Search bookings")
   print("4. Update booking days")
   print("5. Cancel booking")
   print("6. Exit")

   choice = int(input("enter your choice " ))
   if choice == 1:
      book_room(bookings)
   elif choice == 2:
      view_bookings(bookings)
   elif choice ==3 :
      search_bookings(bookings)
   elif choice ==4:
      update_days(bookings)
   elif choice ==5:
      cancel_booking(bookings)
   else:
      print("Thankyou..program terminated")
      break






         
      
