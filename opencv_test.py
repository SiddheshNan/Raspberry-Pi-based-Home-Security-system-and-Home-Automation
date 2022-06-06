import cv2
import img as ui
import wh
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite("images/"+img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        url = ui.upload(img_name)
        if url:
            wh.send_image(0000000000, "Image captured", url['secure_url'])
            url = None

cam.release()

cv2.destroyAllWindows()