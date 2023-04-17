from django import forms

from store.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields =['subject', 'review', 'rating']