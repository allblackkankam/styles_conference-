from django.shortcuts import render

# Create your views here.
def venue(request):
	return render(request,'venue.html')