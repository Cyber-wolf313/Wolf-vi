import subprocess
import time
import json

def handle_sms(sms_body):
    if sms_body.lower() == 'capture':
        subprocess.run(['python3', '/data/data/com.termux/files/home/capture_and_send.py'])

def main():
    print("Listening for SMS commands...")
    while True:
        result = subprocess.run(['termux-sms-list'], capture_output=True, text=True)
        sms_data = result.stdout
        try:
            messages = json.loads(sms_data)
            for message in messages:
                if 'body' in message:
                    handle_sms(message['body'])
        except json.JSONDecodeError:
            print("Failed to parse SMS data.")
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
