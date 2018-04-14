from django.shortcuts import render
from .import forms
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = forms.RegisterAttendess(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/register')
	else:
		form = forms.RegisterAttendess()
		return render(request,'register.html',{"form":form })

def test(request):
	return HttpResponse(request.GET['d'])
