import sqlite3
import os


DB_NAME = "data/patients.db"


def get_connection():
    """
    Create database connection.
    """
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_NAME)


def create_table():
    """
    Create patients table if it does not exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dob TEXT,
            email TEXT,
            glucose REAL,
            haemoglobin REAL,
            cholesterol REAL,
            remarks TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def add_patient(
    name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):
    """
    Insert new patient record.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO patients
        (
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
    )

    conn.commit()
    conn.close()


def get_patients():
    """
    Fetch all patient records.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM patients
        ORDER BY id DESC
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data


def update_patient(
    patient_id,
    name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):
    """
    Update existing patient record.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE patients
        SET
            name = ?,
            dob = ?,
            email = ?,
            glucose = ?,
            haemoglobin = ?,
            cholesterol = ?,
            remarks = ?
        WHERE id = ?
        """,
        (
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks,
            patient_id
        )
    )

    conn.commit()
    conn.close()


def delete_patient(patient_id):
    """
    Delete patient record.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM patients
        WHERE id = ?
        """,
        (patient_id,)
    )

    conn.commit()
    conn.close()