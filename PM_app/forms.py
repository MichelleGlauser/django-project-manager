from django import forms
from PM_app.models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('name', 'description', 'difficulty_level',)