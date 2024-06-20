# app.py
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open(r'/content/drive/MyDrive/Colab Notebooks/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from form
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template('index.html', prediction_text='Predicted House Price: ${}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
