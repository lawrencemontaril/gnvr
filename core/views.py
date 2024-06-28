from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Artist, Profile, Track, Album

# Create your views here.
class LandingView(TemplateView):
    template_name = 'landing.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login') 
    template_name = 'sign_up.html'
    
    def form_valid(self, form):
        # Save the user instance
        user = form.save()

        # Create a profile instance
        profile = Profile.objects.create(
            user=user,
            display_name=f"{user.first_name} {user.last_name}"
        )

        # Return the result of the parent class's form_valid method
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DashboardView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'dashboard/dashboard.html'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'dashboard/artist-list.html'

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'

@method_decorator(login_required, name='dispatch')
class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


# Artist views
@method_decorator(login_required, name='dispatch')
class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name']
    template_name = 'artists/artist_create.html'
    success_url = reverse_lazy('artist-list')

@method_decorator(login_required, name='dispatch')
class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'

@method_decorator(login_required, name='dispatch')
class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'

@method_decorator(login_required, name='dispatch')
class ArtistUpdateView(UpdateView):
    model = Artist
    fields = ['name']
    template_name = 'artists/artist_update.html'
    success_url = reverse_lazy('artist-list')

@method_decorator(login_required, name='dispatch')
class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artists/artist_confirm_delete.html'
    success_url = reverse_lazy('artist-list')

# Album views
@method_decorator(login_required, name='dispatch')
class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist', 'name']
    template_name = 'albums/album_create.html'
    success_url = reverse_lazy('album-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'

@method_decorator(login_required, name='dispatch')
class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

@method_decorator(login_required, name='dispatch')
class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist', 'name']
    template_name = 'albums/album_update.html'
    success_url = reverse_lazy('album-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')

# Track views
@method_decorator(login_required, name='dispatch')
class TrackCreateView(CreateView):
    model = Track
    fields = ['album', 'name']
    template_name = 'tracks/track_create.html'
    success_url = reverse_lazy('track-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class TrackListView(ListView):
    model = Track
    template_name = 'tracks/track_list.html'

@method_decorator(login_required, name='dispatch')
class TrackDetailView(DetailView):
    model = Track
    template_name = 'tracks/track_detail.html'

@method_decorator(login_required, name='dispatch')
class TrackUpdateView(UpdateView):
    model = Track
    fields = ['album', 'name']
    template_name = 'tracks/track_update.html'
    success_url = reverse_lazy('track-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class TrackDeleteView(DeleteView):
    model = Track
    template_name = 'tracks/track_confirm_delete.html'
    success_url = reverse_lazy('track-list')