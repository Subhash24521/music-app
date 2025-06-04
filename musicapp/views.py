

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from musicapp.models import movies, Playlist


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def create_playlist(request):
    display = movies.objects.all()
    return render(request, 'home.html',{"obj":display})

# def search(request):
#     query = request.GET.get('q', '')
#     results = Song.objects.filter(title__icontains=query)
#     return render(request, 'search_results.html', {'songs': results})

def movies_list(request):
    display=movies.objects.all()
    return render(request, 'playlist.html', {"obj":display})

def video_list(request,id):
    d=movies.objects.get(id=id)
    return render(request, 'song_list.html', {"obj":d})

def navibar(request):
    return render(request,'nav.html')


def search(request):
    name=request.POST['search']
    obj=movies.objects.filter(name__contains=name)
    return redirect('song',id=obj[0].id)