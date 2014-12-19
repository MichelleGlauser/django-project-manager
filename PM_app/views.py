from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.edit import UpdateView
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
	tasks = get_list_or_404(Task)
	return render(request, 'show_project.html', {'project': project, 'tasks': tasks})

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
			task = form.save()


			# project.task_set.add(task)

			# # or

			# task.project = project
			# task.save()
			return redirect('PM_app.views.show_project', pk=project.pk)
	else:
		form = TaskForm()
	return render(request, 'create_task.html', {'form': form})

class TaskUpdate(UpdateView):
	model = Task
	fields = ['name', 'description', 'difficulty_level']
	template_name = 'edit_task.html'
	form_class = TaskForm

def edit_task(request):
	instance = Project.objects.get(id=id)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=instance)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('PM_app.views.show_project', pk=project.pk)
	else:
		form = TaskForm()
	return render(request, 'edit_task.html', {'form': form})	
