import json

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define your API endpoint
API_ENDPOINT = 'XXXX'  # Replace 'XXXX' with your actual API endpoint


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get data from the form
        data = {
            'day': request.form['day'],
            'month': request.form['month'],
            'year': request.form['year'],
            'hospital_type': request.form['hospital_type']
        }
        with open('res.json', 'r') as file:
            response_data = json.load(file)
            print(response_data)
            return jsonify(response_data)
        # # Send data to API and get response
        # response = requests.post(API_ENDPOINT, json=data)
        #
        # # Check if the request was successful (status code 200)
        # if response.status_code == 200:
        #     # Parse the JSON response
        #     json_response = response.json()
        #
        #     # Check if the number in the response is -1
        #     if json_response['number'] == -1:
        #         return jsonify({'error': 'Error occurred: Number is -1'}), 400
        #
        #     # If not an error, return the response
        #     return jsonify(json_response)
        #
        # else:
        #     # If the request was not successful, return an error message
        #     return jsonify({'error': 'Failed to fetch data from API'}), 500

    except Exception as e:
        # If an exception occurs during the request, return an error message
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
