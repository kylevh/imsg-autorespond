import os
import time
import read
import random

chat_id = 1# INSERT CHAT ID FROM 'chat.db', must also be the same chat_id set in read.py
send_to = 1# INSERT PHONE NUMBER TO SEND TO

default_response = "This is an automated response!"

# Custom function that takes in phone number and message you want send, then sends it using AppleScript
def send_message(phone, message):
    os.system('osascript send.scpt {} "{}"'.format(phone, message))

current_id = read.current_message_id(chat_id)

print("Running main.py process")
while(True):
    # If it detects a new message
    # Print what they send to you

    if (current_id != read.current_message_id(chat_id)):
        current_id = read.current_message_id(chat_id)
        message = read.get_recent_messages(chat_id)
        print("They just sent: " + message)

        # Will send any message you want to, and you have their message in the 'message' variable
        # to have your automated response respond to.
        send_message(send_to, default_response)

    time.sleep(2)

