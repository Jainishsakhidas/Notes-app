from django.shortcuts import render, redirect
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.

#admin password : NotesApp


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("loginUser")

        context = {'form': form}
        return render(request, 'register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("loginUser")


@login_required(login_url="loginUser")
def renderNotes(request):
    user = request.user
    allNotes = Notes.objects.filter(user=user)

    if request.method == 'POST':
        title = request.POST['note_title']
        desc = request.POST['note']
        user = request.user
        noteInfo = Notes(note_title=title, note=desc, user=user)
        noteInfo.save()

        return redirect('/')

    return render(request, 'home.html', {'allNotes': allNotes})


def deleteNote(request, note_id):
    note = Notes.objects.get(pk=note_id)
    if note.user == request.user:
        note.delete()
    return redirect('/')
