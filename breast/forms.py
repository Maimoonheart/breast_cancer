from django import forms


class TumorPredictionForm(forms.Form):

    #  Mean Features 
    radius_mean = forms.FloatField(label="Radius Mean")
    texture_mean = forms.FloatField(label="Texture Mean")
    perimeter_mean = forms.FloatField(label="Perimeter Mean")
    area_mean = forms.FloatField(label="Area Mean")
    smoothness_mean = forms.FloatField(label="Smoothness Mean")
    compactness_mean = forms.FloatField(label="Compactness Mean")
    concavity_mean = forms.FloatField(label="Concavity Mean")
    concave_points_mean = forms.FloatField(label="Concave Points Mean")
    symmetry_mean = forms.FloatField(label="Symmetry Mean")
    fractal_dimension_mean = forms.FloatField(label="Fractal Dimension Mean")

    # Standard Error Features 
    radius_se = forms.FloatField(label="Radius SE")
    texture_se = forms.FloatField(label="Texture SE")
    perimeter_se = forms.FloatField(label="Perimeter SE")
    area_se = forms.FloatField(label="Area SE")
    smoothness_se = forms.FloatField(label="Smoothness SE")
    compactness_se = forms.FloatField(label="Compactness SE")
    concavity_se = forms.FloatField(label="Concavity SE")
    concave_points_se = forms.FloatField(label="Concave Points SE")
    symmetry_se = forms.FloatField(label="Symmetry SE")
    fractal_dimension_se = forms.FloatField(label="Fractal Dimension SE")

    # Worst Features 
    radius_worst = forms.FloatField(label="Radius Worst")
    texture_worst = forms.FloatField(label="Texture Worst")
    perimeter_worst = forms.FloatField(label="Perimeter Worst")
    area_worst = forms.FloatField(label="Area Worst")
    smoothness_worst = forms.FloatField(label="Smoothness Worst")
    compactness_worst = forms.FloatField(label="Compactness Worst")
    concavity_worst = forms.FloatField(label="Concavity Worst")
    concave_points_worst = forms.FloatField(label="Concave Points Worst")
    symmetry_worst = forms.FloatField(label="Symmetry Worst")
    fractal_dimension_worst = forms.FloatField(label="Fractal Dimension Worst")