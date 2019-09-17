from django.urls import path
from VeteSoft.views import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin



urlpatterns =[
    path('Inicio',login_required(Inicio), name="incio"),
    path('',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('LogoutSesion/',login_required(LogoutView.as_view(template_name='accounts/logout.html')),name='logout'),
    path('MedicosList/',login_required(MedicoVer.as_view()),name='ListaMedico'),
    path('RegistroMedico/',login_required(RegistroMedico.as_view()), name='RegistroMedico'),
    path('RegistroCliente/',login_required(RegistroCliente.as_view()), name='RegistroCliente'),
    path('RegistroCitas/', login_required(RegistroCitas.as_view()), name="RegistroCitas"),
    path('RegistroMascotas/<int:pk>', login_required(RegistroMascotas.as_view()), name="RegistroMascotas"),
    path('Medico/eliminar/Medico/<int:pk>',login_required(MedicoDelet.as_view()),name='EliminarMedico'),
    path('Medico/editar/Medico/<int:pk>',login_required(MedicoActua.as_view()),name='ActualizarMedico'),
    path('ListaCLiente/',login_required(ClienteList.as_view()),name='ListaCLiente'),




    path('ListMascota/',login_required(ListaMascotas.as_view()),name='ListMascotas'),

    path('pdf/',login_required(GeneratePDF.as_view()),name="pdf"),
]

