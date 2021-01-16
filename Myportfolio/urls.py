from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('education-experience', views.edu_Exp, name='education-experience'),
    path('contact', views.contact, name='contact'),
    path('todo', views.MyProjects, name='todo'),
    path('web-design', views.MyProjects, name='web-design'),
    path('BscCS', views.bscCS, name='Bcs'),
    path('data-developer', views.dataDev, name='data-developer'),
    path('IT-Diploma', views.diploma, name='IT-Diploma'),
    path('it-intern', views.intern, name='it-intern'),
    path('system-developer', views.sysDev, name='system-developer'),

]