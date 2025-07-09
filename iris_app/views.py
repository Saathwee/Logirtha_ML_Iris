from django.shortcuts import render
import os
import pickle
import numpy as np

# Load the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'iris_model.pkl')
model = pickle.load(open(model_path, 'rb'))

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST['sepal_length'])
        sepal_width = float(request.POST['sepal_width'])
        petal_length = float(request.POST['petal_length'])
        petal_width = float(request.POST['petal_width'])

        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        species = ['Setosa', 'Versicolor', 'Virginica']
        result = species[prediction]

        return render(request, 'result.html', {'result': result})
    return render(request, 'home.html')
