from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
model = pickle.load(open('kidney.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    try:
        # Get form data and convert to float
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])
        data5 = float(request.form['e'])
        data6 = float(request.form['f'])
        data7 = float(request.form['g'])
        data8 = float(request.form['h'])
        data9 = float(request.form['i'])
        data10 = float(request.form['j'])

        # Create a NumPy array
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7,
                         data8, data9, data10]], dtype=np.float32)

        # Make prediction
        pred = model.predict(arr)

        # Render the result page
        return render_template('after.html', data=pred)
    except Exception as e:
        # Handle errors gracefully
        return f"Error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
