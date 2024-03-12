# MoodTracker
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/findkeys/MoodTracker)](https://github.com/your-username/bot-front-web-app/stargazers)

## MoodTracker Live Demo



**Note:** Scroll all the way down to access the projects

MoodTracker is a multi-modal mood analysis application that provides users with different ways to track and analyze their daily mood. This project combines three components: a real-time face emotion detection application, an emotion classifier app, and a voice-based mood analyzer. Each component offers unique features for mood tracking and analysis.

## Features
### [Real-Time Face Emotion Detection Application](https://webcamm.streamlit.app/#webcam-live-feed)
- Real-time facial expression analysis using the computer's webcam.
- Pre-trained model for emotion detection.
- Displays detected mood on the screen.

### [Emotion Classifier App (Text-Based Mood Analyzer)](https://mooodd.streamlit.app/)
- An NLP-powered web app that can predict emotions from text recognition with 70 percent accuracy.
- Utilizes Python libraries including Numpy, Pandas, Seaborn, Scikit-learn, Scipy, Joblib, eli5, lime, neattext, altair, and Streamlit.
- Employs a Linear regression model from the scikit-learn library to train a dataset containing speeches and their respective emotions.
- Joblib is used for storing and using the trained model in the website.

### [Voice-Based Mood Analyzer](https://www.youtube.com/watch?v=jwudzL8m4CQ)
- Captures user's spoken input to analyze daily mood.
- Utilizes sentiment analysis for mood tracking.
- Offers a graphical user interface for recording and analyzing mood.

## Requirements
The MoodTracker project requires the following dependencies for each component:

### Real-Time Face Emotion Detection Application:
- Python
- OpenCV
- Keras
- Haar Cascade Classifier
- Pre-trained Emotion Detection Model

### Emotion Classifier App (Text-Based Mood Analyzer):
- Numpy
- Pandas
- Seaborn
- Scikit-learn
- Scipy
- Joblib
- eli5
- lime
- neattext
- altair
- Streamlit

### Voice-Based Mood Analyzer:
- Python
- SpeechRecognition
- TextBlob
- Tkinter
- Matplotlib

## Usage
To use the MoodTracker application, follow the specific installation and execution instructions for each component. Each component offers a different way to track and analyze your mood.

1. **Real-Time Face Emotion Detection Application**
- Install the required dependencies for the Real-Time Face Emotion Detection Application.
- Clone or download the project repository.
     ```bash
         git clone https://github.com/CODEWITHRIZA/MoodTracker.git
- Navigate to the `Webcam Opencv Project` folder.
  ```bash
   cd "Webcam Opencv Project"
 - Install the required packages and dependencies by running the following command:
      ```bash
    pip install -r requirements.txt
   
 - Run the application using the following command:
     ```bash
    streamlit run app.py
- The real-time face emotion detection application will open, and you can start using it by facing your webcam.

2. **Emotion Classifier App (Text-Based Mood Analyzer)**
- Install the required dependencies for the Emotion Classifier App.
- - If you've already cloned or downloaded the project repository, there's no need to do it again. The given command below
   ```bash
        git clone https://github.com/CODEWITHRIZA/MoodTracker.git
        cd MoodTracker
- Navigate to the `NLP-Text-Emotion` folder.
     ```bash
         cd NLP-Text-Emotion
- Install the required packages and dependencies by running the following command:
  ```bash
     pip install -r requirements.txt
- Run the application using the following command: 
  ```bash
    streamlit run app.py
 - Access the app in your web browser, as it will provide a web interface for you to enter text and analyze emotions.

3. **Voice-Based Mood Analyzer**

   - Install the required dependencies for the Voice-Based Mood Analyzer.
   - If you've already cloned or downloaded the project repository, there's no need to do it again. The given command below
      ```bash
        git clone https://github.com/CODEWITHRIZA/MoodTracker.git
        cd MoodTracker
   - Navigate to the root folder of the project.
   -    - Install the required packages and dependencies by running the following command:
        ```bash 
         pip install -r requirements.txt
   - Run the voice-based mood analyzer using the following command:
      ```bash
       python voice_mood_analyzer.py

   - The graphical user interface for voice-based mood analysis will open, allowing you to record and analyze your mood through spoken input.

## Note
Each component offers a different way to track and analyze your mood. Make sure you have the required dependencies installed for the component you wish to use.

## Combined Features
- Mood Tracking: Each component tracks daily mood using a specific modality (real-time face, text, voice).
- Sentiment Analysis: Sentiment analysis is performed on the captured data to determine mood.
- Data Visualization: The text-based and voice-based analyzers provide visual mood feedback using Matplotlib.
- Web and Graphical Interfaces: The emotion classifier app offers a web-based interface, while the voice-based component uses a graphical user interface.
- Real-time Updates: The real-time face emotion detection application provides real-time feedback based on facial expressions.

The MoodTracker project is designed to help users gain insights into their emotional well-being and better understand their daily mood patterns. It offers a variety of options for tracking and analyzing moods through different sensory modalities.


---
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/887532157747212370)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/codewithriza)

