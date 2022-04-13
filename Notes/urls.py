from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderNotes, name='home'),
    path('register', views.registerUser, name='registerUser'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),
    path('delete/<note_id>', views.deleteNote, name='deleteNote')
]
