import cv2
import numpy as np
import os
import sys
from time import sleep
from skimage.metrics import structural_similarity as ssim

# Default image paths
admin_image_path = "admin/pht1.jpg"
input_image_path = "pht2.jpg"
# If the admin photo is to be update_admind
explicit_update_admin = len(sys.argv) > 1 and sys.argv[1] == "abc@123"


def main():
    # Check if the admin photo exists or needs to be update_admind
    if not isinstance(cv2.imread(admin_image_path), np.ndarray) or explicit_update_admin:
        print("Initiating admin image update...")
        sleep(1)
        # Run udate function to update admin image
        update_admin()
        print("Admin image updated successfully")
        sleep(1)
        # If the admin image was explicitly updated, the program will end here
        if explicit_update_admin:
            exit(0)
    # Program continues to capture an image to verify the user
    print("Initiating image capture...")
    sleep(1)
    print("Press 'c' to capture")
    sleep(1)
    print(capture_image(input_image_path))
    sleep(1)
    print("Initiating verification...")
    sleep(1)

    # Load admin and user images
    admin_image = cv2.imread(admin_image_path, cv2.IMREAD_GRAYSCALE)
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Detect faces in admin and user images and check if appropriate NumPy array was returned
    print("Detecting faces...")
    sleep(1)
    admin_face = detect_faces(admin_image)
    if not isinstance(admin_face, np.ndarray):
        sys.exit("No face found in database")
    input_face = detect_faces(input_image)
    if not isinstance(input_face, np.ndarray):
        sys.exit("No face found in captured image")
    print("Face detected")
    sleep(1)

    # Compare the faces using Structural Similarity Index (SSIM) and print the result
    print(match(admin_face, input_face))
    sleep(0.5)


def capture_image(captured_image_path):

    # Message container
    msg = None

    try: 
        # Trying to access the camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            msg = "Error: Could not open camera."
        # Read the frame
        while True:    
            ret, frame = cap.read()
            if not ret:
                msg = "Error: Could not read frame."
                break
            # Capture Image
            cv2.imshow('Camera Feed - Press "c" to capture', frame)
            if cv2.waitKey(1) & 0xFF == ord('c'):            
                cv2.imwrite(captured_image_path, frame)
                msg = "Image captured and saved"
                break

        # Release the camera and destroy windows
        cap.release()
        cv2.destroyAllWindows()
        return msg
    except Exception as e:
        sys.exit(e)


def update_admin():
    # Default path to save the captured image to a temporary file for face detection
    buffer_image_location = "./admin/pht0.jpg"

    capture_image(buffer_image_location)
    image = cv2.imread(buffer_image_location, cv2.IMREAD_GRAYSCALE)
  
    # Load pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    
    # Check if fac were detected
    if len(faces) <= 0:
        os.remove(buffer_image_location)
        sys.exit("No face detected in captured image") # Exits and deletes the teporary image if no face was detected
    else:
        try:
            os.remove(admin_image_path) # Removes the previous admin image if it exists
        except:
            pass
        print("Saving image...")
        sleep(0.5)
        os.rename(buffer_image_location, admin_image_path)
        print("Image saved successfully.") # Replaces the admin image
        sleep(1)



def detect_faces(image):   

    # Load pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, 1.3, 5)

    if len(faces) != 0:
        # Return coordinates of faces
        x1, y1, w1, h1 = faces[0]   

        # Crop the faces from the images
        face = image[y1:y1+h1, x1:x1+w1]
        return face
    
    return None
             

def match(admin_face, input_face):  

    print("Running verification tests...")
    sleep(1)

    # Resize the faces to the same size for comparison
    admin_face_resized = cv2.resize(admin_face, (input_face.shape[1], input_face.shape[0]))

    # Compare the faces using structural similarity index (SSI)
    score, _ = ssim(admin_face_resized, input_face, full=True)    

    print(f"Similarity score: {score * 100:.2f}%")  
    sleep(0.5)

    # If similarity score is more than 0.4, print "Face match"
    sleep(0.5)
    if score > 0.4:
        return "Face match!"
    else:
        return "Faces do not match."


if __name__ == "__main__":
    main()