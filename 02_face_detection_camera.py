import cv2

camera_index = 1
vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print(":(")
        break
    boxes = detector.detectMultiScale(frame)
    for box in boxes:
        x1, y1, width, height = box
        x2, y2 = x1 + width, y1 + height
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('pooya', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


