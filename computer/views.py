from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer, ComputerSpecification
from django.contrib import messages

# Create your views here.
def index(request):
  if request.method == 'POST':
    computerCode = request.POST.get('computerCode')
    computer_id = request.POST.get('computer')
    quantity = request.POST.get('quantity')
    unitRate = request.POST.get('unitRate')

    try:
      computer = ComputerSpecification.objects.get(id=computer_id)
    except:
      messages.error(request, "Computer specification not found")

    quantity = int(quantity)
    unitRate = float(unitRate)  
      
    computerCreate = Computer.objects.create(
      computer_code = computerCode,
      computer = computer,
      quantity = quantity, 
      unit_rate = unitRate
    )
    computerCreate.save()
    messages.success(request, "Computer added successfully")
    return redirect('index')

  computers = Computer.objects.all()
  computerspecs = ComputerSpecification.objects.all()
  context = {
    'computers': computers,
    'computerspecs': computerspecs,
  }
  return render(request, 'main/index.html', context)

def update(request, id):
  computer = get_object_or_404(Computer, id=id)
  if request.method == 'POST':
    computerCode = request.POST.get('computerCode')
    computer_id = request.POST.get('computer')
    quantity = int(request.POST.get('quantity'))
    unitRate = float(request.POST.get('unitRate'))
    computer_spec = ComputerSpecification.objects.get(id=computer_id)

    computer.computer_code = computerCode
    computer.computer = computer_spec
    computer.quantity = quantity
    computer.unit_rate = unitRate
    computer.save()
    messages.success(request, 'Computer information updated successfully')
    return redirect('index')

  computerspecs = ComputerSpecification.objects.all()
  context = {
    'computer': computer,
    'computerspecs': computerspecs,
  }
  return render(request, 'main/update.html', context)

def delete(request, id):
  computer =  get_object_or_404(Computer, id=id)
  if request.method == 'POST':
    computer.delete()
    messages.success(request, 'Computer information deleted successfully')
    return redirect('index')