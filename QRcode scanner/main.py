import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    scanned_data = set()

    print("Press 'q' to quit.")
    while True:
        success, frame = cap.read()
        if not success:
            break

        for code in decode(frame):
            data = code.data.decode('utf-8')

            if data not in scanned_data:
                print(f"QR Code Data: {data}")
                scanned_data.add(data)
                cap.release()
                cv2.destroyAllWindows()
                return

            # Draw bounding box around QR code
            pts = code.polygon
            pts = [(point.x, point.y) for point in pts]
            pts = pts + [pts[0]]
            for i in range(len(pts)-1):
                cv2.line(frame, pts[i], pts[i+1], (0, 255, 0), 3)

            # Display data on the frame
            cv2.putText(frame, data, (code.rect.left, code.rect.top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the scanner
scan_qr_code()
