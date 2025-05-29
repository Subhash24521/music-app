

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


from .forms import PlaylistForm
from .models import Playlist, movies

def upload_media(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = PlaylistForm()
    return render(request, 'playlist.html', {'form': form})

def media_list(request):
    media_items = Playlist.objects.all()
    return render(request, 'media_list.html', {'media_items': media_items})


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
    if request.method == "POST":
        
        form = LoginForm(request, data=request.POST)  
       
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage or dashboard
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()


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
    return render(request, 'home.html', {"obj":display})

def video_list(request,id):
    d=movies.objects.get(id=id)
    return render(request, 'song_list.html', {"obj":d})

def navibar(request):
    return render(request,'nav.html')


def search(request):
    name=request.POST['search']
    obj=movies.objects.filter(name__contains=name)
    return redirect('song',id=obj[0].id)