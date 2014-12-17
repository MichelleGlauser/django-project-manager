from django.shortcuts import render, get_object_or_404, redirect
from PM_app.models import Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def list_projects(request):
	projects = Project.objects.all()
	return render(request, 'index.html', {'projects': projects})

def show_project(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'show_project.html', {'project': project})

def create_project(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
			return redirect('PM_app.views.show_project', pk=project.pk)
	else:
		form = ProjectForm()
	return render(request, 'create_project.html', {'form': form})

def create_task(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('PM_app.views.show_project', pk=project.pk)
	else:
		form = TaskForm()
	return render(request, 'create_task.html', {'form': form})
