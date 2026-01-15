from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.pages, name='pages'),
    path("post/<int:pk>/", views.pages_detail, name="blog_detail"),
    path("category/<category>/", views.pages_category, name="blog_category"),
]

urlpatterns += staticfiles_urlpatterns()