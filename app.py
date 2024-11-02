from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML template

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request contains JSON data
    if request.is_json:
        data = request.get_json()
        features = [
            data['online_order'],
            data['book_table'],
            data['votes'],
            data['location'],
            data['rest_type'],
            data['cuisines'],
            data['cost'],
            data['menu_item']
        ]
    else:  # Handle form submission
        features = [
            int(request.form['online_order']),
            int(request.form['book_table']),
            int(request.form['votes']),
            int(request.form['location']),
            int(request.form['rest_type']),
            int(request.form['cuisines']),
            int(request.form['cost']),
            int(request.form['menu_item'])
        ]

    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 1)

    # Return JSON response regardless of the request type
    return jsonify({'prediction': output})

if __name__ == "__main__":
    app.run(debug=True)
