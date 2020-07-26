from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm 

def home(request):
	context ={} 
	context['form'] = InputForm() 
	return render(request,'bmi_calculator/home.html',context)

def calculate_bmi(request):
	print ("Herfe")
	if request.POST:
	    height = float(request.POST.get('height'))
	    weight = float(request.POST.get('weight'))
	    return render(request,'bmi_calculator/result.html',{'calculated_bmi' : (weight/height**2) })

def about(request):
	return render(request,'bmi_calculator/about.html')
