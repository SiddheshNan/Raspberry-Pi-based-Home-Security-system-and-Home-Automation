import cloudinary
import cloudinary.api
import cloudinary.uploader
import cv2
from datetime import datetime
import time


cloudinary.config(
    cloud_name="",
    api_key="",
    api_secret=""
)


def upload(image):
    print("Trying to upload Image")
    global t, upl
    try:
        upl = cloudinary.uploader.upload("images/"+image)
        t = True
    except Exception as e:
        t = False
        print("Failed to upload Image Due to: " + str(e))

    if t:
        return upl
    else:
        return False


def capture():
    i = 0
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Image Capture")
    print("Trying to Capture Image...")
    while True:
        ret, frame = cam.read()
        cv2.imshow("Image Capture", frame)
        if not ret:
            print("Failed to Capture Image")
            return 0
        k = cv2.waitKey(1000)
        i+=1
        if i >= 6 and k:
            img_name = "img_at_{}.jpg".format(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
            cv2.imwrite("images/"+img_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            print("{} written!".format(img_name))
            time.sleep(1)
            break
    cam.release()
    cv2.destroyAllWindows()
    return img_name
