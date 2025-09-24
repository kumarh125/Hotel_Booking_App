import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__ (self, hotel_id)
        self.hote

    def available(self):
        if
            return True
        else:
            return False

    def book(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_id = input("Enter the ID of the hotel: ")

hotel = Hotel(hotel_id)                #create a instant with specific details in argument
if hotel.available():            #use the method of that instance
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)     #create a instant with specific details in argument
    print(reservation_ticket.generate())                      #create a instant with specific details in argument
else():
    print('Hotel is not free!')



