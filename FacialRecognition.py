# Imported libraries
import cv2

# Make an instance of CascadeClassifier(collection, "file_path") provided by openCV in order to detect faces
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open device's default camera
video_capture = cv2.VideoCapture(0)

# Function for counting faces and drawing a rectanglular containers arount the face
def count_faces_and_draw_rectangles(frame):
    # Introduce face_count so the function can modify it (variable declared later in the code)
    global face_count

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame using the cascade classifier
    faces = face_classifier.detectMultiScale(gray_frame, 1.1, 5, minSize=(40, 40)) 
    
    # Draw rectangles and labels for each face
    for (x, y, w, h) in faces:
        face_count += 1 # Increment the counter for each rectangle drawn
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3) # Draw rectangle with cv2.rectangle(image, start_point, end_point, color, thickness) 
        cv2.putText(frame, f'face number: {face_count}', (x - 1, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) # Draw text with cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

    # Return the image
    return frame

# Count and label rectangles
while True:
    # Read frames from the video
    result, frame = video_capture.read()

    # Terminate the loop if the frame is not read successfully
    if not result:
        break

    # Initialise/reset counter for each frame
    face_count = 0

    # Process the frame (detect faces and label appropriatly)
    frame_with_rectangles = count_faces_and_draw_rectangles(frame)

    # Display the processed frame
    cv2.imshow("My face detection demo", frame_with_rectangles)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
