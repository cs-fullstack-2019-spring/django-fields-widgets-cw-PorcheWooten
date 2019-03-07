from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeroForm
# Create your views here.

# render's index page
def index(request):
    print('something')
    return render (request, 'heroApp/index.html')

# renders form , validate and save information in the form
def application(request):
    if(request.method=="POST"):
        print('something')
        form=HeroForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        else:
            print(form.errors)
            print('Error')
    return render (request, 'heroApp/application.html', {'form': HeroForm})

# renders submit page after submit button is clicked
def submit(request):
    return render(request, 'heroApp/submit.html')