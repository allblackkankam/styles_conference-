from django.shortcuts import render
from .models import Speakers

# Create your views here.
def speakers(request):
	return render(request,'speakers.html')