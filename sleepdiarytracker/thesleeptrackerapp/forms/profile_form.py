from django import forms
from thesleeptrackerapp.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone_number', 'address')
