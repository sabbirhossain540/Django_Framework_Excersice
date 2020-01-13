from django import forms
from test_app.models import User

class NewUserFrom(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
