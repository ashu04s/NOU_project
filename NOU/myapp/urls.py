from django.urls import path
from . import views
from .views import*
urlpatterns = [
    path('', views.home, name='home'),
    path('superadmindesh',views.superadmindesh,name="superadmindesh"),
    path('base',views.base,name="base"),
     path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('addsession/', views.add_session,name='add_session')
    
]