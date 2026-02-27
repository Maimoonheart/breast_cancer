from django.shortcuts import render
import joblib
import pandas as pd
import numpy as np
import os

from django.shortcuts import render
from .forms import TumorPredictionForm
from django.conf import settings



MODEL_PATH = os.path.join(settings.BASE_DIR, "model.pkl")
model = joblib.load('breast_cancer_model.pkl')


def breast(request):

    prediction = None
    probability = None
    risk_level = None

    if request.method == "POST":
        form = TumorPredictionForm(request.POST)

        if form.is_valid():

            
            features = list(form.cleaned_data.values())
            features = np.array(features).reshape(1, -1)

           
            pred = model.predict(features)[0]
            prob = model.predict_proba(features)[0][1]

            prediction = "Malignant" if pred == 1 else "Benign"
            probability = round(prob * 100, 2)

           
            if prob >= 0.85:
                risk_level = "High Risk"
            elif prob >= 0.60:
                risk_level = "Moderate Risk"
            else:
                risk_level = "Low Risk"

    else:
        form = TumorPredictionForm()

    context = {
        "form": form,
        "prediction": prediction,
        "probability": probability,
        "risk_level": risk_level
    }

    return render(request, "breast.html", context)
