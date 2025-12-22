import cv2
import imutils
import winsound

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

gun_frames = 0
ALERT_THRESHOLD = 10
alert_triggered = False

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(120, 120)
    )

    if len(guns) > 0:
        gun_frames += 1
    else:
        gun_frames = 0

    # Trigger alert only if detected in many frames
    if gun_frames >= ALERT_THRESHOLD:
        if not alert_triggered:
            winsound.Beep(1200, 800)
            alert_triggered = True

        cv2.putText(
            frame,
            "CONFIRMED GUN DETECTED!",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("Security Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
