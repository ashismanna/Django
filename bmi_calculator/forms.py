from django import forms 

# creating a form 
class InputForm(forms.Form): 
	height = forms.FloatField()
	weight = forms.FloatField()