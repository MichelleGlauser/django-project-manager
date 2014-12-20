from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.edit import UpdateView
from PM_app.models import Project, Task
from .forms import ProjectForm, TaskForm

# def index(request):
#     return render(request, 'index.html')

def list_projects(request):
	projects = Project.objects.all()
	return render(request, 'index.html', {'projects': projects})

def create_project(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
			return redirect('list_projects')
	else:
		form = ProjectForm()
	return render(request, 'create_project.html', {'form': form})

def show_project(request, project_pk):
	project = get_object_or_404(Project, pk=project_pk)
	# Needs to show specific tasks for this project:
	tasks = Task.objects.filter(id=project_pk)
	# tasks = get_list_or_404(Task)
	return render(request, 'show_project.html', {'project': project, 'tasks': tasks})

def create_task(request, project_pk):
	project = get_object_or_404(Project, pk=project_pk)
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save()
			# Save the underyling model:
			form.save(commit=False)
			# Needs to link this new task to a specific project:
			task.project_id = project.pk
			task.save()
			# project.task_set.add(task)

			return redirect('show_project', project_pk=project.pk)
	else:
		form = TaskForm()
	return render(request, 'create_task.html', {'form': form})

class TaskUpdate(UpdateView):
	model = Task
	fields = ['name', 'description', 'difficulty_level']
	template_name = 'edit_task.html'
	form_class = TaskForm

def edit_task(request, task_pk, project_pk):
	# Needs to show previous values for this task:
	instance = Task.objects.get(id=project_pk)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=instance)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('show_project', project_pk=project.pk)
	else:
		form = TaskForm()
	return render(request, 'edit_task.html', {'form': form})	
