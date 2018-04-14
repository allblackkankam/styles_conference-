from django import forms
from . import models

class RegisterAttendess(forms.ModelForm):
	class Meta:
		model = models.Attendess
		fields = ["name" ,"email" ,"passes", "comment"]			
		