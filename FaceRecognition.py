import cv2



def return_active_frame():
    # Load face cascade classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize webcams
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)

    while True:
        ret1, cam1_frame = cam1.read()
        ret2, cam2_frame = cam2.read()

        if not ret1 and not ret2:
            break

        # Convert frames to grayscale for face and eye detection
        cam1_gray = cv2.cvtColor(cam1_frame, cv2.COLOR_BGR2GRAY)
        cam2_gray = cv2.cvtColor(cam2_frame, cv2.COLOR_BGR2GRAY)


        # Detect faces in the frame
        cam1_faces = face_cascade.detectMultiScale(cam1_gray, 1.3, 5)
        cam2_faces = face_cascade.detectMultiScale(cam2_gray, 1.3, 5)

        cam1_eyes_detected = faces_have_eyes(cam1_faces, cam1_frame, cam1_gray)
        cam2_eyes_detected = faces_have_eyes(cam2_faces, cam2_frame, cam2_gray)


        # Display the frame
        if cam1_eyes_detected:
            cv2.imshow('Webcam', cam1_frame)
        if cam2_eyes_detected:
            cv2.imshow('Webcam', cam2_frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()

def faces_have_eyes(faces, frame, gray):
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract region of interest (ROI) for eyes
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # Draw rectangle around each eye
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        if len(eyes) > 1:
            return True
    return False

return_active_frame()