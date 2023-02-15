from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime # date

from django.core import serializers
from information.models import Info

# Create your views here.
def Submit(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        section = request.POST.get('section')
        print(name,' ', email)
        if(name == '' and email == '' and department == '' and section == ''):
            return 
        else:
            data = Info(name=name, email=email, department= department, section = section , date=datetime.today())
            data.save()
            return redirect('index')
  
  
    return render(request, 'submit.html')



def index(request):
  data = serializers.serialize('python',Info.objects.all())

  information = {
    'data': data
  }
  return render(request, 'index.html',information)


