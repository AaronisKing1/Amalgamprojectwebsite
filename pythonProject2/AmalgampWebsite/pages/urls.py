from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.pages, name='pages'),
    path("post/<int:pk>/", views.pages_detail, name="blog_detail"),
    path("category/<category>/", views.pages_category, name="blog_category"),
    path("home/", views.home, name="home"),
    path("games/", views.games, name="games"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("art/", views.art, name="art"),
]

urlpatterns += staticfiles_urlpatterns()