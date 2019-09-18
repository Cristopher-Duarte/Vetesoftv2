from django.urls import path
from VeteSoft.views import *
from VeteSoft.pdf import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.urls import url
from VeteSoft import views




urlpatterns =[
    path('Inicio',login_required(Inicio), name="incio"),
    path('',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('LogoutSesion/',login_required(LogoutView.as_view(template_name='accounts/logout.html')),name='logout'),
    path('Admin/MedicosList/',login_required(MedicoVer.as_view()),name='ListaMedico'),
    path('Admin/RegistroMedico/',login_required(RegistroMedico.as_view()), name='RegistroMedico'),
    path('Admin/RegistroCliente/',login_required(RegistroCliente.as_view()), name='RegistroCliente'),
    path('Admin/RegistroCitas/<int:pk>', login_required(RegistroCitas.as_view()), name="RegistroCitas"),
    path('Admin/RegistroMascotas/<int:pk>', login_required(RegistroMascotas.as_view()), name="RegistroMascotas"),
    path('Admin/Medico/eliminar/Medico/<int:pk>',login_required(MedicoDelet.as_view()),name='EliminarMedico'),
    path('Admin/Medico/editar/Medico/<int:pk>',login_required(MedicoActua.as_view()),name='ActualizarMedico'),
    path('Admin/ListaCLiente/',login_required(ClienteList.as_view()),name='ListaCLiente'),
    path('Home/Users',login_required(home),name='Home'),
    path('User/Index/',login_required(Index_Usuario),name='IndexUsuarios'),
    path('Admin/Index/',login_required(Index_Admin),name='IndexAdmin'),
    path('Doc/Index/',login_required(Index_Doctor),name='IndexDoctor'),





    path('ListMascota/',login_required(ListaMascotas.as_view()),name='ListMascotas'),


    #URl pdf
    path('pdf/<int:pk>',login_required(GeneratePDF.as_view()),name="pdf"),
]

