from flask import Flask, render_template, request
from hate_speech_detection import detect_hate_speech  # Import your hate speech detection function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_text = ""
    processed_text = ""
    
    if request.method == 'POST':
        user_text = request.form.get('user_input', '')
        # Pass the text to the detection function
        processed_text = detect_hate_speech(user_text)  # Process the text for hate speech
    
    return render_template('index.html', user_text=user_text, processed_text=processed_text)

if __name__ == '__main__':
    app.run(debug=True)
