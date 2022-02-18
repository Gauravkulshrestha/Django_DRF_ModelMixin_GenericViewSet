from posixpath import basename
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctorapi/', views.ListCreateDoctor.as_view({'get': 'list', 'post': 'create'})),
    path('doctorapi/<int:pk>/', views.RetrieveUpdateDestroyDoctor.as_view({'put': 'update',
    'get': 'retrieve','delete': 'destroy','patch': 'partial_update',})),
]
