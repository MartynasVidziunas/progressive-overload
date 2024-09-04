from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import os
import smtplib
from dotenv import load_dotenv
import re
from src.workouts.workout import Workout


load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def load_workouts(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [Workout.from_dict(item) for item in data]

def send_email(subject, body, to_email, attachment_path=None):
    from_email = EMAIL_USER
    password = EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=attachment_path)
        part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def list_workouts():
    workouts = load_workouts('data/workouts.json')

    if not workouts:
        print("No workouts found.")
        return

    print("\nSaved Workouts:")
    for i, workout in enumerate(workouts):
        print(f"{i + 1}. {workout.name}")

    try:
        selection = int(input("\nEnter the number of the workout to send via email: ")) - 1
        if 0 <= selection < len(workouts):
            return workouts[selection]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None
    
def generate_workout_report(workout):
    report = f"Workout: {workout.name}\n\n"
    for exercise in workout.exercises:
        if exercise.history:
            latest_entry = exercise.history[-1]
            report += f"Exercise: {exercise.name}\n"
            report += f"  Sets: {latest_entry['sets']}\n"
            report += f"  Reps: {latest_entry['reps']}\n"
            report += f"  Weight: {latest_entry['weight']}\n\n"
        else:
            report += f"Exercise: {exercise.name}\nNo history recorded.\n\n"
    report +="Good luck and remember to have fun!"
    return report

def send_workout_report_via_email(workout, email):
    report = generate_workout_report(workout)
    send_email(
        subject=f"Workout Report: {workout.name}",
        body=report,
        to_email=email
    )

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def mail_workout():

    while True:
        email = input("\nEnter your email or type 'q' to go quit: ").strip()
        if email == 'q':
            break
        elif is_valid_email(email):
            selected_workout = list_workouts()
            if selected_workout:
                send_workout_report_via_email(selected_workout, email)
                print("Workout report sent successfully.")
                break
            else:
                print("No workouts available.")
                break
        else:
            print("Invalid email address. Please try again.")
