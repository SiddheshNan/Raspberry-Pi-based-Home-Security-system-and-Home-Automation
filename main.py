import img
import wh
import RPi.GPIO as GPIO
import time
from datetime import datetime

phone_no = 0000000000

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pir = 21
lpg = 20
fire = 16

GPIO.setup(pir, GPIO.IN)
GPIO.setup(lpg, GPIO.IN)
GPIO.setup(fire, GPIO.IN)

def capture_and_send_media(cause):
    image = img.capture()
    if image:
        print("Image Captured!")
        url = img.upload(image)
        if url:
            print("Image upload success!")
            whh = wh.send_image(phone_no, cause+" at: "+datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), url['secure_url'])
            if whh:
                print("whatsapp media msg sent! ID :", whh)
                return 1
            else:
                print("whatsapp media msg sending failed! ID :", whh)
                return 0
        else:
            print("Failed to upload Image")
            return 0
    else:
        print("Failed to Capture Image")
        return 0


def doStart():
    print("Starting..")
    while True:
        if GPIO.input(pir) == 1:
            print("------------")
            print("Motion Detected")
            out = capture_and_send_media("Motion Detected")
            if out:
                print("Sending Success!")
            else:
                print("Sending Failed!")
            print("------------")
            time.sleep(1)

        elif GPIO.input(lpg) == 0:
            print("------------")
            print("LPG Detected")
            out = capture_and_send_media("LPG Detected")
            if out:
                print("Sending Success!")
            else:
                print("Sending Failed!")
            print("------------")
            time.sleep(1)

        elif GPIO.input(fire) == 0:
            print("------------")
            print("Fire Detected")
            out = capture_and_send_media("Fire Detected")
            if out:
                print("Sending Success!")
            else:
                print("Sending Failed!")
            print("------------")        
            time.sleep(1)


if __name__ == '__main__':
    doStart()
