from django.shortcuts import render, redirect
from .models import Computer, ComputerSpecification
# Create your views here.
def index(request):
  computers = Computer.objects.all()
  computerspecs = ComputerSpecification.objects.all()
  context = {
    'computers': computers,
    'computerspecs': computerspecs,
  }
  return render(request, 'main/index.html', context)