from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('about-us/', views.about, name = 'about'),
    path('lib/', views.lib, name = 'lib'),
    path('training/', views.training, name = 'training'),
    path('help/', views.help, name = 'help'),
    path('blog/', views.blog, name = 'blog'),
    path('create/', views.create, name = 'create'),

    path('5grade/', views.grade5, name='5grade'),
path('6grade/', views.grade6, name='6grade'),
]
