from django.shortcuts import render, redirect, get_object_or_404
from .models import Evenimente, User, Task, CompleteTask, Join
from .forms import UserForm, EvenimenteForm, TaskForm, CompleteTaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:login_user')
        else:
            form = UserForm()
            messages.info(request, "Parola este prea scurta! Foloseste minim 8 caractere, simboluri si numere!")
    context = {
        'form':form,
    }
    return render(request, 'my_app/signup.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Numele sau parola sunt incorecte, va rugam sa incercati din nou!")
    return render(request, "my_app/login_user.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("signup"))

@login_required
def dashboard(request):
    user = request.user
    model = user.evenimente_set.all()
    context = {
        'model':model,
    }
    return render(request, 'my_app/dashboard.html', context)

@login_required
def create(request):
    form = EvenimenteForm()
    if request.method == 'POST':
        form = EvenimenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = EvenimenteForm()
    context = {
        'form':form,
    }
    return render(request, 'my_app/create.html', context)

@login_required
def update_event(request, pk):
    model = Evenimente.objects.get(id=pk)
    form = EvenimenteForm(instance=model)
    if request.method == 'POST':
        form = EvenimenteForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            messages.info(request, 'The event has been updated!')
            return redirect('dashboard')
        else:
            form = EvenimenteForm()
    context = {
        'form':form,
    }
    return render(request, 'my_app/update_form.html', context)

@login_required
def delete_event(request, pk):
    model = Evenimente.objects.get(id=pk)
    if request.method == "POST":
        model.delete()
        return redirect("dashboard")
    context = {
        'model':model,
    }
    return render(request, "my_app/delete_event.html", context)

@login_required
def create_task(request, pk):
    event = get_object_or_404(Evenimente, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.event = event
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'my_app/task_create.html', context)

@login_required
def task_details(request):
    form = CompleteTaskForm()
    model = Task.objects.all()
    if request.method == 'POST':
        form = CompleteTaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CompleteTaskForm()
    context = {
        'form': form,
        'model':model
    }
    return render(request, 'my_app/task_details.html', context)

@login_required
def all_event(request):
    event = Evenimente.objects.all()
    context = {
        'event':event,
    }
    return render(request, "my_app/all_event.html", context)

@login_required
def event_details(request, pk):
    event = get_object_or_404(Evenimente, id=pk)
    has_joined = Join.objects.filter(user=request.user, event=event).exists()
    
    if request.method == 'POST':
        if 'join' in request.POST and not has_joined:
            if event.joins.count() < event.number_of_people:
                Join.objects.create(user=request.user, event=event)
                has_joined = True
        elif 'unjoin' in request.POST and has_joined:
            Join.objects.filter(user=request.user, event=event).delete()
            has_joined = False

    joined_count = event.joins.count()
    context = {
        'event': event,
        'has_joined': has_joined,
        'joined_count': joined_count,
        'max_capacity': event.number_of_people,
    }
    return render(request, "my_app/event_details.html", context)

# Create your views here.
