from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput, label='')
    class Meta:
        model = Photo
        fields = ('photo', )
