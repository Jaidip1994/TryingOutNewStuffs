import numpy as np
import cv2

# 0 Specifies here whats the whats the video capture device
cap = cv2.VideoCapture(0)

while True:
    # ret   : If the video capture worked properly or not if in case the same videoCapture device if in use
    #         this will return False if the videoCapture was not successful else this will return true
    # frame : Frame / Image in the numpy format
    ret, frame = cap.read()
    if not ret:
        continue

    # To get the Frame height and width
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Idea is to take the image and then do some manipulation
    # Get the main Video Frame and show it four times

    image = np.zeros(shape=frame.shape, dtype=np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    blueColorChannelImage = smaller_frame.copy()
    blueColorChannelImage[:, :, 0] = np.zeros([smaller_frame.shape[0], smaller_frame.shape[1]])

    image[:height // 2, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height // 2:, :width // 2] = blueColorChannelImage
    image[height // 2:, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    cv2.imshow("Video Capture Frame", image)
    # This will basically break out if in case the q button is being pressed
    if cv2.waitKey(1) == ord('q'):
        break
# Release the Video Capture resource
cap.release()
cv2.destroyAllWindows()
