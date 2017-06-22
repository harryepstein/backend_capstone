from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:

        fields = ('phone_number', 'address')
