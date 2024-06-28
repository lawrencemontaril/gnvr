from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('sign_up/', views.SignUpView.as_view(), name="sign_up"),

    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('artists/', views.ArtistListView.as_view(), name="artist-list"),
    path('password_change/', views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', include('django.contrib.auth.urls')),
    
    # Artist urls
    path('artists/create/', views.ArtistCreateView.as_view(), name='artist-create'),
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('artists/<int:pk>/update/', views.ArtistUpdateView.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', views.ArtistDeleteView.as_view(), name='artist-delete'),
    
    # Album urls
    path('albums/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('albums/', views.AlbumListView.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('albums/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
    
    # Track urls
    path('tracks/create/', views.TrackCreateView.as_view(), name='track-create'),
    path('tracks/', views.TrackListView.as_view(), name='track-list'),
    path('tracks/<int:pk>/', views.TrackDetailView.as_view(), name='track-detail'),
    path('tracks/<int:pk>/update/', views.TrackUpdateView.as_view(), name='track-update'),
    path('tracks/<int:pk>/delete/', views.TrackDeleteView.as_view(), name='track-delete'),
]
