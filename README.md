# Face Match

#### Video Demo:  <URL HERE>
#### Description:
This project is a face recognition system that captures images via a webcam, detects faces, and compares them to a stored "admin" face. It includes functionalities for updating the admin face and testing the matching of captured faces.

## Features

- **Face Detection:** Uses OpenCV's Haar Cascade classifier to detect faces from grayscale images.
- **Face Matching:** Compares detected faces using the Structural Similarity Index (SSI).
- **Image Capture:** Captures images from a webcam when the 'c' key is pressed.
- **Admin Image Update:** If no admin face is detected, the system allows for an update to capture a new admin face.
- **Command-Line Argument:** An explicit update option is available through a command-line argument (`abc@123`).

## Requirements

- Python 3.x
- OpenCV
- NumPy
- scikit-image

You can install the required dependencies using:

```bash
pip install opencv-python numpy scikit-image
```

## Setup

1. **Admin Image:**
   The project expects an initial "admin" image for comparison. The image should be stored in the `admin/` directory with the name `pht1.jpg`. If the image is not available or needs to be updated, the system will prompt you to capture a new image.
   
2. **Testing Images:**
   The project includes test images such as `test_face1.jpg`, `test_face2.jpg`, and `test_no_face.jpg`. These images can be used for testing the face detection and matching features.

## Usage

### 1. **Capture Image**
   To capture an image using the webcam and save it:

   ```bash
   python project.py
   ```

   The system will display a camera feed and capture the image when the 'c' key is pressed. The captured image will be saved with the name specified in the script.

### 2. **Detect Faces and Match Faces**
   The main function of the script compares faces from the captured image against the "admin" face image (`admin/pht1.jpg`):

   ```bash
   python project.py
   ```

   The system will detect faces from both the admin image and the captured input image, then compare them. If the similarity score is higher than 40%, it returns a "Face match!" message, otherwise, it reports "Faces do not match."

### 3. **Explicit Update of Admin Image**
   If the system cannot detect a face in the admin image (`admin/pht1.jpg`), or if you want to explicitly update it, you can run the script with the `abc@123` argument:

   ```bash
   python project.py abc@123
   ```

   This will allow you to update the admin image by capturing a new one, which will replace the old one in the `admin/` folder.

### 4. **Unit Tests**
   The project includes unit tests that check the functionality of the key methods, including:

   - Capturing an image (`capture_image`)
   - Detecting faces (`detect_faces`)
   - Matching faces (`match`)

   To run the tests, you can execute the following command:

   ```bash
   pytest test_project.py
   ```

   The tests check:
   - Successful image capture and saving.
   - Proper face detection from the test images.
   - Correct behavior of the face matching algorithm.


## Description of the functions:

### `project.py` - Function Descriptions

#### 1. **`main()`**
   - **Description:** This is the entry point of the program. It checks if an admin face exists or if an explicit update is requested via command-line arguments. If no admin face is found or an update is requested, it calls the `update()` function. It then captures an image, detects faces, and matches the captured face with the admin's face. The result is printed to the console.
  
#### 2. **`capture_image(captured_image_path)`**
   - **Description:** This function opens the webcam and captures an image when the 'c' key is pressed. The captured image is saved to the specified path (`captured_image_path`). It returns a success or error message based on whether the image was captured successfully.
  
#### 3. **`update()`**
   - **Description:** This function captures a new image (using the `capture_image()` function) and checks for a detected face. If no face is detected, it exits with an error message. If a face is detected, the old admin image is replaced with the new one. If the script is run with an explicit update argument (`abc@123`), the system will immediately exit after updating the image.

#### 4. **`detect_faces(image)`**
   - **Description:** This function uses OpenCV's pre-trained Haar Cascade classifier to detect faces in the provided image. It returns the cropped face (as a numpy array) if a face is detected. If no face is found, it returns `None`.

#### 5. **`match(admin_face, input_face)`**
   - **Description:** This function compares two faces (the admin face and the input face) by resizing them to the same dimensions and then calculating their similarity using the Structural Similarity Index (SSI) from the `skimage.metrics` library. If the similarity score exceeds 40%, it returns "Face match!", otherwise it returns "Faces do not match."

---

### `test_project.py` - Function Descriptions

#### 1. **`test_capture_image()`**
   - **Description:** This function tests the `capture_image()` function. It checks if the image is correctly captured and saved, verifies that the image file exists, and handles scenarios where the camera is unavailable or a frame cannot be read. It includes assertions to confirm the function behaves as expected in different situations.

#### 2. **`test_detect_faces()`**
   - **Description:** This function tests the `detect_faces()` function with different input images. It verifies that a face is detected correctly in images containing faces (`test_face1.jpg` and `test_face2.jpg`) and checks that the function returns `None` when no face is present (e.g., `test_no_face.jpg`).

#### 3. **`test_match()`**
   - **Description:** This function tests the `match()` function. It first detects faces in various test images and then verifies that the matching function correctly identifies whether two faces are the same or different. It checks several conditions:
     - The same face from different images should match.
     - Different faces should not match.


## Files and Folders

- `admin/`: Directory containing admin images (e.g., `pht1.jpg`).
- `project.py`: The main script for capturing and processing images.
- `test_project.py`: Cntains the unit tests for the functions: `capture_image`, `detect_faces` and `match`.
- `requirements.txt`: List of dependencies and libraries.
- `README.md`: This file.


## Collaboration Overview

The project began with Manjeet creating two scripts. The first script was responsible for capturing an image to verify against a manually stored admin image. The second script was designed to match the captured face with the stored admin image to check for a match. 

During their discussions, Krishna suggested enhancing the structure of the project. Then a new created script that added a `main()` function to serve as the entry point of the project. We integrated the functionalities from the two previous scripts into a single file, `project.py`, and refactored the code into well-defined functions. This approach helped streamline the project and make the individual functionalities modular, improving the overall organization and flow of the project.

OpenCV (cv2) is a powerful library used for various computer vision tasks in this project. It handles capturing images from the webcam, reading and writing image files, detecting faces using Haar Cascades, and cropping and resizing images for comparison. These features make it essential for the image processing and face verification functionalities.

NumPy (numpy) plays a crucial role in managing image data as arrays. It ensures the integrity of this data and facilitates operations such as resizing and cropping, which are vital for preparing images for comparison.

The structural_similarity function from scikit-image (skimage.metrics.structural_similarity) is utilized to calculate the similarity score between two images. This score helps determine if the captured face matches the stored admin face, enabling accurate verification.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The face detection feature uses OpenCV's Haar Cascade classifier.
- Face similarity comparison is done using Structural Similarity Index (SSI) from `skimage`.