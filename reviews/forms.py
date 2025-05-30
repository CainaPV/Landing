from django.forms import ModelForm, RadioSelect
from reviews.models import Review

class Review_Form(ModelForm):
    class Meta:
        model = Review
        fields = ['stars']
        widgets = {'stars': RadioSelect }