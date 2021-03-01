import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Objective is to draw some shapes on the images
    # For the coordinates the left top corner is (0,0) this is not equivalent to cartesian coordinate system

    # Line
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), thickness=10)
    img = cv2.line(img, (width, 0), (0, height), (0, 255, 0), thickness=10)

    # Rectangle
    # if the thickness is specified as -1 then the rectangle will be filled & for other values it controls the line
    # thickness
    img = cv2.rectangle(img, (0, 0), (width, height), (0, 0, 255), thickness=10)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), thickness=-1)

    # Circle
    img = cv2.circle(img, (width // 2, height // 2), 100, (0, 0, 255), thickness=2)

    # Write Text and the org value is being passed the bottom left corner where the text will be displayed
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "This is Jaidip", (10, height - 20), fontFace=font, fontScale=2, color=(0, 0, 0),
                      thickness=5, lineType=cv2.LINE_AA)

    cv2.imshow("Video Frame", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
