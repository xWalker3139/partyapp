from django import forms
from .models import Evenimente, Task, CompleteTask
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username...', 'autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email...', 'autocomplete':'off'}),
        }

class EvenimenteForm(forms.ModelForm):
    class Meta:
        model = Evenimente
        fields = '__all__'
        widgets = {
            'user_id':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'name':'user', 'type':'hidden'}),
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title...', 'autocomplete':'off'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description...', 'autocomplete':'off'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location...', 'autocomplete':'off'}),
            'date_posted':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy', 'autocomplete':'off'}),
            'budget':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Bugdet...', 'autocomplete':'off'}),
            'number_of_people':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of people...'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'event':forms.TextInput(attrs={'class':'form-control', 'id':'event1', 'value':'', 'name':'event', 'type':'hidden'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the task...', 'autocomplete':'off'}),
            'budget':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Budget...', 'autocomplete':'off'}),
            'assigned_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Assigned to...', 'autocomplete':'off'}),
        }

class CompleteTaskForm(forms.ModelForm):
    class Meta:
        model = CompleteTask
        fields = '__all__'
        widgets = {
            'complete':forms.Select(attrs={'class':'form-control', 'placeholder':'Name of the task...', 'autocomplete':'off'}),
        }