from django.shortcuts import render
from .models import Stureg
from .forms import StuForm


def show(request):
    if request.method == 'POST':
        ty = StuForm(request.POST)
        if ty.is_valid():
            
            nm = ty.cleaned_data['name']
            su = ty.cleaned_data['surname']
            em = ty.cleaned_data['email']
            ps = ty.cleaned_data['password']

            reg = Stureg(name=nm, surname=su, password=ps, email=em)
            reg.save()
            
            ty = StuForm()

    else:
        ty = StuForm()

    return render(request, 'show.html', {'form': ty})