# MoodTracker
MoodTracker is a multi-modal mood analysis application that provides users with different ways to track and analyze their daily mood. This project combines three components: a camera-based mood analyzer, a text-based mood analyzer, and a voice-based mood analyzer. Each component offers unique features for mood tracking and analysis.

## Features
### Camera-Based Mood Analyzer
- Real-time facial expression analysis using the computer's webcam.
- Pre-trained model for emotion detection.
- Displays detected mood on the screen.

### Text-Based Mood Analyzer(https://mooodd.streamlit.app/)
- Allows users to input daily mood entries in text format.
- Utilizes Natural Language Processing (NLP) techniques to recognize and analyze text emotions.
- Maps recognized emotions to corresponding emojis.
- Provides visual mood feedback through bar graphs.
- Offers a web-based interface for users to input and visualize their mood data.


### Voice-Based Mood Analyzer
- Captures user's spoken input to analyze daily mood.
- Utilizes sentiment analysis for mood tracking.
- Offers a graphical user interface for recording and analyzing mood.

## Requirements
The MoodTracker project requires the following dependencies for each component:

### Camera-Based Mood Analyzer:
- Python
- OpenCV
- Keras
- Haar Cascade Classifier
- Pre-trained Emotion Detection Model

### Text-Based Mood Analyzer:
- Python
- NLTK
- TextBlob
- Flask
- Matplotlib

### Voice-Based Mood Analyzer:
- Python
- SpeechRecognition
- TextBlob
- Tkinter
- Matplotlib

## Usage
To use the MoodTracker application, follow the specific installation and execution instructions for each component. Each component offers a different way to track and analyze your mood.

1. Camera-Based Mood Analyzer: Refer to the code in the `Emotion_Detector` folder.
2. Text-Based Mood Analyzer: Review the code in the `NLP-Text-Emotion` folder.
3. Voice-Based Mood Analyzer: Find the Python file `voice_mood_analyzer.py` in the repository.

## Contributors
## Contributors
- [Riza Mohamed T](https://github.com/codewithriza)
- [Mohammed Habil Kundil](https://github.com/habil619)
- [Rihan Mohamed K](https://github.com/rihanmhmd102)


## Combined Features
- Mood Tracking: Each component tracks daily mood using a specific modality (camera, text, voice).
- Sentiment Analysis: Sentiment analysis is performed on the captured data to determine mood.
- Data Visualization: The text-based and voice-based analyzers provide visual mood feedback using Matplotlib.
- Web and Graphical Interfaces: The text-based component offers a web-based interface, while the voice-based component uses a graphical user interface.
- Real-time Updates: The camera-based component provides real-time feedback based on facial expressions.

The MoodTracker project is designed to help users gain insights into their emotional well-being and better understand their daily mood patterns. It offers a variety of options for tracking and analyzing moods through different sensory modalities.
