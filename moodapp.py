from flask import Flask, request, render_template
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import matplotlib.pyplot as plt

app = Flask(__name__)

def preprocess(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def get_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarityx
    return sentiment

def analyze_mood(entries):
    sentiments = [get_sentiment(preprocess(entry)) for entry in entries]
    mood_score = sum(sentiments) / len(sentiments)
    return mood_score

def plot_mood_trends(entries):
    sentiments = [get_sentiment(preprocess(entry)) for entry in entries]
    plt.plot(sentiments)
    plt.xlabel("Days")
    plt.ylabel("Mood Score")
    plt.title("Mood Trends")
    plt.show()

@app.route('/')
def index():
    return render_template('index.html')  # You need to create 'index.html' as your HTML template

@app.route('/analyze', methods=['POST'])
def analyze():
    entries = request.form.get('entries').split('\n')
    mood_score = analyze_mood(entries)
    plot_mood_trends(entries)
    return f'Mood Score: {mood_score}'

if __name__ == '__main__':
    app.run(debug=True)
