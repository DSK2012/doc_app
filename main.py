from root_classes import create_slots, date_time_slots, appointments
from crud import book_appointment, lookup_slots, update_appointment, cancel_appointment_prompts
from datetime import *
from create_tables import *


def print_menu():
    print("choose a number from below options")
    print("1. book an appointment ")
    print("2. update an appointment")
    print("3. cancel an appointment")
    print("4. check available slots")
    print("5. exit")
    print("============","\n")

def main():

    # create_tables()
    # insert_slots()


    while True:

        print_menu()
        input_number = int(input())

        if input_number == 1:
            book_appointment()
            
        
        if input_number == 2:
            
            update_appointment()
        if input_number == 3:
            cancel_appointment_prompts()


        if input_number == 4:
            lookup_slots()
        
        elif input_number == 5:
            break
            




if __name__ == "__main__":
    main()
