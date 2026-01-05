from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('pages/', views.pages, name='pages'),
]

urlpatterns += staticfiles_urlpatterns()