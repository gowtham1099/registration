from django.shortcuts import render
from myapp.models import Student
from myapp.forms import StudentForm
from django.shortcuts import redirect
# Create your views here.

def form_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'home.html', {'form': form})