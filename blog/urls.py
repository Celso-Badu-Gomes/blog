from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

'''comando para subir pro servidor local pro github: usar o shell local do pc
git add --all
git commit -m "#"
git push

comando para puxar do github para um servidor de internet: usar o shell do pythonanywhere
git pull'''