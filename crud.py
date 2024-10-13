from datetime import *
from root_classes import Appointment, Patient, date_time_slots, patients, appointments
from create_tables import (show_dates_after_today,
                            show_times_given_day,
                            check_patient_exists,
                            add_patient,
                            save_appointment, 
                            get_appointment_using_patient_id,
                            cancel_appointment_db)


class check_slots:

    @classmethod
    def get_dates(self):
        print("Please enter a date from below to check slots")
        for row in show_dates_after_today():
            print(row[0])
        print("============","\n")
        
    
    @classmethod
    def get_times_given_date(self, date_chosen):
        for row in show_times_given_day(date_chosen):
            print(row[0])
        print("============","\n")


def book_appointment():

    check_slots.get_dates()
    date_chosen = input()
    print("Please enter a time from below to book appointment")
    check_slots.get_times_given_date(date_chosen)
    time_chosen = input()
    patient_phone = input("Please enter patient phone without country code : ")
    patient_DOB = input("Please enter patient DOB in the format mm-dd-yyyy : ")
    patient_id_returned = check_patient_exists(patient_phone,patient_DOB)
    if patient_id_returned:
        save_appointment(date_chosen, time_chosen,patient_id_returned[0][0])
        
    else:
        print("Patient doesn't exist, please create one")
        patient_name = input("Please enter patient name : ")
        added_patient_id = add_patient(patient_name,patient_phone,patient_DOB)
        print(added_patient_id)
        save_appointment(date_chosen, time_chosen, added_patient_id)
    

def update_appointment():
    phone_entered = input("Please enter your phone : ")
    DOB_entered = input("Please enter DOB : ")
    patient_id_returned = check_patient_exists(phone_entered, DOB_entered)[0][0]
    if patient_id_returned:
        appointments_returned = get_appointment_using_patient_id(patient_id_returned)
        if appointments_returned:
            print("below are your appointments in order #appointment_id date time ...")
            for appointment in appointments_returned:
                print(*appointment)
            appointment_id_input = input("Please enter the appointment you would like to update using the appointment ID")
            
            # choice = input("Would you like to change your date or time? (date/time) :")
            
            check_slots.get_dates()
            date_chosen = input()
            check_slots.get_times_given_date(date_chosen)
            time_chosen = input()
            cancel_appointment(appointment_id_input)
            save_appointment(date_chosen, time_chosen, patient_id_returned)
            

        else:
            print("You do not have any appointments")
    else:
        print("Please check the information again")

def cancel_appointment(appointment_id):
    cancel_appointment_db(appointment_id)

def cancel_appointment_prompts():
    phone_entered = input("Please enter your phone : ")
    DOB_entered = input("Please enter DOB : ")
    patient_id_returned = check_patient_exists(phone_entered, DOB_entered)[0][0]
    if patient_id_returned:
        appointments_returned = get_appointment_using_patient_id(patient_id_returned)
        if appointments_returned:
            print("below are your appointments in order #appointment_id date time ...")
            for appointment in appointments_returned:
                print(*appointment)
            appointment_id_input = input("Please enter the appointment you would like to cancel using the appointment ID")
            cancel_appointment(appointment_id_input)
        else:
            print("You do not have any appointments")

    else:
        print("Please check the information again")

def lookup_slots():
    
    check_slots.get_dates()
    date_chosen = input()

    check_slots.get_times_given_date(date_chosen)
