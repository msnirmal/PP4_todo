from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

def list(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/task.html', context)
    
