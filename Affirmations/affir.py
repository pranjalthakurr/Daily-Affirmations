from twilio.rest import Client
import schedule
import time
import random

# Twilio credentials (Replace with your details)
ACCOUNT_SID = "**********"
AUTH_TOKEN = "**************"
TWILIO_NUMBER = "**********"
YOUR_PHONE_NUMBER = "*****"

# List of daily affirmations
affirmations = [
    "You are capable of amazing things!",
    "Believe in yourself and your abilities.",
    "Every day is a fresh start to grow and shine.",
    "You are enough, just as you are.",
    "Success comes from small efforts repeated daily."
]

def send_affirmation():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=random.choice(affirmations),  # Pick a random affirmation
        from_=TWILIO_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
    print(f"Affirmation sent: {message.body}")

# Schedule it to run daily D
schedule.every().day.at("15:30").do(send_affirmation)

print("Daily Affirmation Sender is running...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
