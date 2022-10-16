
from django import forms
from listings.models import Listing

class OwnerRegistration(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title','address','district','state','zipcode','description','price','photo_main','photo_1']
