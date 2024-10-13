from datetime import *
# appointments = []
# patients = []

# class Patient :

#     def __init__(self, name, phone, DOB) -> None:
#         self.name = name
#         self.phone = phone
#         self.DOB = DOB


# class Appointment:

#     def __init__(self, date, timeSlot, patient : Patient) -> None:
#         self.date = date
#         self.timeSlot = timeSlot
#         self.patient = patient
    
#     def print_data(self):
#         print(f"appointment at {self.date}, {self.timeSlot} for patient {self.patient.name} {self.patient.phone} {self.patient.DOB} ")
#         print("==============","\n")

date_time_slots = []
## assumptions : only able to book slots starting tomorrow for about 7 days
def create_slots(n_days = 7):
    dates_available = []
    delta_dates = 1
    while len(dates_available) < n_days:
        current_date = date.today() + timedelta(days=delta_dates)
        if date.weekday(current_date) < 5:
            dates_available.append(current_date)
        delta_dates += 1
    
    for slot_date in dates_available:
        for time_slot_each in time_slots_creator(slot_date):
            date_time_slots.append((str(slot_date), str(time_slot_each)))
    return date_time_slots



## Given a start and end time, create time slots with a time difference of 30 minutes
def time_slots_helper(start_time, end_time, interval = 30):
    time_slots = []
    current_time = start_time
    while current_time < end_time:
        time_slots.append(current_time.time())
        current_time += timedelta(minutes=interval)
    return time_slots

## Define start and end times to use time_slots_helper to create all slots of a day
def time_slots_creator(date=date.today()):
    time_slots = []
    appointment_start_time = datetime.combine(date, time(hour=9))
    lunch_start_time = datetime.combine(date, time(hour=12))

    time_slots = time_slots_helper(appointment_start_time, lunch_start_time)


    lunch_end_time = datetime.combine(date, time(hour=13))
    appointment_end_time = datetime.combine(date, time(hour=17))

    time_slots += time_slots_helper(lunch_end_time, appointment_end_time)
    # print(len())
    return time_slots
