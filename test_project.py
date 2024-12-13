from project import *
import cv2
import numpy as np


test_face1_image_path = "./admin/test_face1.jpg"
test_face1_image_path_local = "test_face1.jpg"
test_face2_image_path = "./admin/test_face2.jpg"
test_face2_image_path_local = "test_face2.jpg"
test_no_face_image_path = "./admin/test_no_face.jpg"


# Load images
test_face1_image = cv2.imread(test_face1_image_path, cv2.IMREAD_GRAYSCALE)
test_face1_image_local = cv2.imread(test_face1_image_path_local, cv2.IMREAD_GRAYSCALE)
test_face2_image = cv2.imread(test_face2_image_path, cv2.IMREAD_GRAYSCALE)
test_face2_image_local = cv2.imread(test_face2_image_path_local, cv2.IMREAD_GRAYSCALE)
test_no_face_image = cv2.imread(test_no_face_image_path, cv2.IMREAD_GRAYSCALE)

    
def test_capture_image():
    
    # Define the image path for saving
    image_path = "test_image_capture.jpg"
    
    # Call the capture_image function and capture the result
    assert capture_image(image_path, auto_test=True) == "Image captured and saved"
    
    # Assert that the file has been created
    assert os.path.exists(image_path)
    
    # Clean up: remove the test image after the test
    if os.path.exists(image_path):
       os.remove(image_path)
    


def test_detect_faces():

    # Test when face is detected in the image
    face1_result = detect_faces(test_face1_image)
    assert isinstance(face1_result, np.ndarray)

    # Test when another face is detected in a different image
    face2_result = detect_faces(test_face2_image)
    assert isinstance(face2_result, np.ndarray)

    # Test when no face is detected
    assert detect_faces(test_no_face_image) == None


def test_match():

    # Load faces and assert they are detected properly
    test_face1 = detect_faces(test_face1_image)
    assert test_face1 is not None
    
    test_face2 = detect_faces(test_face2_image)
    assert test_face2 is not None
    
    test_face1_local = detect_faces(test_face1_image_local)
    assert test_face1_local is not None
    
    test_face2_local = detect_faces(test_face2_image_local)
    assert test_face2_local is not None
    
    # Test the face matching logic
    assert match(test_face1, test_face1_local) == "Face match!"  # Test the same face from different images
    assert match(test_face1, test_face2_local) == "Faces do not match."  # Test different faces
    assert match(test_face2, test_face2_local) == "Face match!"  # Test the same face from different images
    assert match(test_face1, test_face2) == "Faces do not match."  # Test different faces
