from django.shortcuts import render
from django.views.generic import UpdateView, CreateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView 
from VeteSoft.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .Formulario import *


def Inicio(request):
    return render(request,"VeteSoft/index.html")

class MedicoVer(ListView):
    model = Medico 
    template_name = 'VeteSoft/ListarEmpleados.html'

class MedicoDelet(DeleteView):
    model = Medico
    template_name = 'VeteSoft/EliminarMedico.html'
    success_url = reverse_lazy('ListaMedico')

class MedicoActua(UpdateView):
    model = Medico
    form_class=ActualizarMedico
    template_name = 'VeteSoft/EditarMedicos.html'
    success_url = reverse_lazy('ListaMedico')


class RegistroMedico(CreateView):
    model=Medico
    form_class=RegistroMedicoForm
    template_name ='VeteSoft/RegistroMedico.html'
    success_url = reverse_lazy('ListaMedico')
    
class ClienteActua(UpdateView):
    model = Cliente
    form_class=ActualizarCliente
    template_name = 'VeteSoft/EditarMedicos.html'
    success_url = reverse_lazy('ListaMedico')


class RegistroCliente(CreateView):
    model=Cliente
    form_class=RegistroClienteForm
    template_name ='VeteSoft/RegistroCliente.html'
    success_url = reverse_lazy('ListaCLiente')


class ClienteList(ListView):
    model = Cliente 
    template_name = 'VeteSoft/ListaCliente.html'

class RegistroCitas(CreateView):
    model=Citas
    form_class=RegistroCitaForm
    template_name ='VeteSoft/RegistroCitas.html'