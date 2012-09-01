from django import forms
from django.contrib.auth.models import User

from models import *

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity 
        fields = ('name','slug','content')
