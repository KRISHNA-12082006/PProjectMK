**[Opening Scene: The presenter (you or your partner) stands in front of a camera, with a computer screen showing the project running.]**

**Presenter:**  
"Hello, and welcome to our face recognition project! In this video, we will walk you through the key features of the system, how it works, and demonstrate its functionality in real time."

---

**[Cut to: Screen recording of the terminal or IDE showing the script running.]**

**Presenter (voiceover):**  
"Let's start by talking about the core functionality of this project. Our goal was to build a system that can detect faces, capture an image, and compare it with a stored admin face to verify a match."

---

**[Cut to: A webcam feed with the system displaying the message: 'Camera Feed - Press "c" to capture.']**

**Presenter (voiceover):**  
"Here, the system is waiting for the user to capture an image. By pressing the 'c' key, the system will take a snapshot and save the image."

**[On screen: The presenter presses the 'c' key, and the webcam feed freezes, indicating the image is being captured.]**

**Presenter (voiceover):**  
"Once the image is captured, the system moves on to detect the face in the captured image."

---

**[Cut to: Terminal showing that the system is detecting faces.]**

**Presenter (voiceover):**  
"The system uses OpenCV's Haar Cascade classifier to detect the faces in both the captured image and the stored admin image. If a face is detected, the next step is face matching."

---

**[Cut to: Terminal showing the output of the face match process.]**

**Presenter (voiceover):**  
"The face matching process compares the detected face from the captured image with the stored admin face. It does this using the Structural Similarity Index (SSI), which calculates how similar the two images are."

**[On screen: Output of the match result, such as 'Face match!' or 'Faces do not match.']**

**Presenter (voiceover):**  
"If the similarity score is above 40%, the system will indicate a successful match. If it's below that threshold, the system will confirm that the faces do not match."

---

**[Cut to: A second demo where the user provides a different face image to test the system.]**

**Presenter (voiceover):**  
"Now, let's test the system with a different face to see how it handles a mismatch. As you can see, the system correctly identifies that the faces do not match, based on the similarity score."

---

**[Cut to: Terminal showing the command to run the script with the explicit update argument.]**

**Presenter (voiceover):**  
"Another feature of the system is the ability to update the admin face. If the system cannot detect a face or if you want to replace the existing admin face, you can run the script with a special command-line argument, `abc@123`."

**[On screen: Command line input of `python project.py abc@123`. The system proceeds with capturing a new admin image.]**

**Presenter (voiceover):**  
"This will allow you to capture a new admin image, which will replace the old one."

---

**[Cut to: Final screen showing the project structure.]**

**Presenter (voiceover):**  
"To summarize, this project integrates face detection, image capture, and face matching into one smooth system. We also included a feature to update the admin face and tested the system using different images."

**Presenter (on camera):**  
"This is the main functionality of the project. We've also included unit tests to ensure each function works as expected, such as image capture, face detection, and face matching."

**[On screen: Text "Project Demo Complete" appears.]**

---

**Presenter:**  
"We hope you enjoyed this demo! Thank you for watching. If you'd like to try the project yourself, you can check out the GitHub repository linked below, and feel free to reach out if you have any questions or feedback."

---

**[Closing Scene: End screen with project title, GitHub link, and contact information.]**
