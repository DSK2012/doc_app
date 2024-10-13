import sqlite3 as sqlite
from root_classes import create_slots



patients_table_create_query = """
            CREATE TABLE IF NOT EXISTS patient(
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(50) NOT NULL,
            phone CHAR(10) NOT NULL,
            DOB CHAR(10) NOT NULL
            )"""



doctors_table_create_query = """
            CREATE TABLE IF NOT EXISTS doctors(
            doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(50) NOT NULL,
            Address CHAR(100) NOT NULL,
            qualifications CHAR(100) NOT NULL
            )
            """

appointments_table_create_query = """
            CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME NOT NULL,
            time DATETIME NOT NULL,
            patient_id INTEGER,
            doc_id INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patients (patient_id),
            FOREIGN KEY (doc_id) REFERENCES doctors (doc_id),
            CHECK ((patient_id IS NULL AND doc_id IS NULL) OR (patient_id IS NOT NULL AND doc_id IS NOT NULL))
            )
            """

insert_slots_query = """
            insert into appointments (date, time, patient_id, doc_id)
            values (?,?, NULL, NULL)
            """

def create_tables():
    con = sqlite.connect("docs_app.db")

    cur = con.cursor()
    cur.execute(patients_table_create_query)
    cur.execute(doctors_table_create_query)
    cur.execute(appointments_table_create_query)


    con.commit()
    con.close()


def insert_slots():
    con = sqlite.connect("docs_app.db")

    cur = con.cursor()
    for slot in create_slots():
        cur.execute(insert_slots_query,slot)
    
    con.commit()
    con.close()

def show_dates_after_today():
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    cur.execute("""
            select distinct date
                from appointments
                where date > DATE('now')
            """)
    dates_after_today = cur.fetchall()
    
    
    con.close()
    return dates_after_today

def show_times_given_day(date_chosen):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    cur.execute("""
            select time
                from appointments
                where date = ? and patient_id IS NULL and doc_id IS NULL
            """,(date_chosen,))
    times_available = cur.fetchall()
    
    con.close()
    return times_available


def check_patient_exists(patient_phone,patient_DOB):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    cur.execute("""
            select *
                from patient
                where phone = ? and DOB = ?
            """,(patient_phone,patient_DOB))

    patient = cur.fetchall()

    con.close()

    if patient:
        return patient
    return False

def add_patient(patient_name,patient_phone,patient_DOB):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    cur.execute("""
            insert into patient(patient_id, name, phone, DOB)
                values (NULL, ?, ?, ?)
            """,(patient_name,patient_phone,patient_DOB))
    
    con.commit()

    if cur.lastrowid:
        print(f"Patient added successfully with ID : {cur.lastrowid}")
    else:
        print("Failed to add patient")
    con.close()
    return cur.lastrowid


def save_appointment(date_chosen, time_chosen,patient_id):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    try:
        cur.execute("""
                update appointments
                    set patient_id = ?, doc_id = ?
                    where date = ? and time = ?
                """,(patient_id, 1, date_chosen, time_chosen))
        con.commit()
        print("Appointment saved successfully")

    except sqlite.Error as e:
        print("something went wrong while saving appointment")


    con.commit()
    con.close()

def get_appointment_using_patient_id(patient_id):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()
    appointments_returned = None
    try:
        cur.execute("""
                select *
                    from appointments
                    where patient_id = ?
                """, (patient_id,))

        appointments_returned = cur.fetchall()
    
    except:
        print("Something went wrong while getting apointment ID")
    
    con.close()
    if appointments_returned:
        return appointments_returned
    return None

def get_doctor_details(doc_id):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    try:
        cur.execute("""
                select *
                    from doctors
                    where doc_id = ?
                """,(doc_id,))
    except:
        print("Doctor not found with given ID")
    
    con.close()

def cancel_appointment_db(appointment_id):
    con = sqlite.connect("docs_app.db")
    cur = con.cursor()

    try:
        cur.execute("""
                update appointments
                    set patient_id = NULL, doc_id = NULL
                    where appointment_id = ?
                """,(appointment_id,))
        print("Appointment cancelled successfully")
    except:
        print("something went wrong while cancelling appointment")
    
    con.commit()
    con.close()