# Import necessary libraries/modules
import numpy as np
import cv2
import streamlit as st
from tensorflow import keras
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, WebRtcMode

# Load the emotion labels dictionary
emotion_dict = {0: 'angry', 1: 'happy', 2: 'neutral', 3: 'sad', 4: 'surprise'}

# Load the pre-trained model architecture from a JSON file and its weights
json_file = open('emotion_model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
classifier.load_weights("emotion_model1.h5")

# Load the face cascade classifier
try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")

# Configuration for Real-Time Communication (RTC)
RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# Define a class for face emotion detection inheriting from VideoTransformerBase
class Faceemotion(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to an ndarray in BGR format
        img = frame.to_ndarray(format="bgr24")

        # Convert the frame to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(
            image=img_gray, scaleFactor=1.3, minNeighbors=5)
        
        # Process each detected face
        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
            
            # Extract the region of interest (ROI) for emotion prediction
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            
            # Perform emotion prediction if the ROI is not empty
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                maxindex = int(np.argmax(prediction))
                finalout = emotion_dict[maxindex]
                output = str(finalout)
            
            # Display the predicted emotion label on the face
            label_position = (x, y)
            cv2.putText(img, output, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return img

# Define the main function
def main():
    # Display the title and sidebar for the application
    st.title("Real-Time Face Emotion Detection Application")
    activities = ["Home", "Webcam Face Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    # Display developer information in the sidebar
    st.sidebar.markdown(
        """Developed by Riza Mohamed T   
        Email: codewithriza@gmail.com 
        [LinkedIn](https://www.linkedin.com/in/codewithriza)""")
    
    # Define different functionalities based on the user's choice
    if choice == "Home":
        # Display information about the application
        st.write("""
                 The application has two functionalities.
                 1. Real-time face detection using webcam feed.
                 2. Real-time face emotion recognition.
                 """)
    elif choice == "Webcam Face Detection":
        # Display live webcam feed for face detection and emotion recognition
        st.header("Webcam Live Feed")
        st.write("Click on start to use the webcam and detect your facial emotions")
        webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV, rtc_configuration=RTC_CONFIGURATION,
                        video_processor_factory=Faceemotion)
    elif choice == "About":
        # Display information about the application and developer
        st.subheader("About this app")
        st.markdown("""
                    Real-time face emotion detection application using OpenCV, Custom Trained CNN model, and Streamlit.
                    Developed by Riza Mohamed using Streamlit Framework, OpenCV, Tensorflow, and Keras library for demonstration purposes.
                    """)
        st.markdown("""
                    This Application is developed by Riza Mohamed using Streamlit Framework, OpenCV, Tensorflow, and Keras library for demonstration purpose.
                    If you're on LinkedIn and want to connect, just click on the link in the sidebar and shoot me a request.
                    If you have any suggestions or want to comment, just write an email at codewithriza@gmail.com.
                    Thanks for Visiting!
                    """)
    else:
        pass

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
