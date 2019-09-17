from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView 
from VeteSoft.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .Formulario import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required


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

class RegistroMascotas(View):
    def get(self, request,pk):
        
        form2 = RegistroMascotasForm
        return render(request, 'VeteSoft/RegistrarMascotas.html', {'form': form2})

    def post(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        form1 = RegistroMascotasForm(request.POST)
        datosM = Mascotas.objects.all()
        if form1.is_valid():
            llenar = form1.save(commit=False)
            llenar.Cliente = cliente
            llenar.save()
            return render(request, 'VeteSoft/ListarMascotas.html', {'infomas':datosM})


class ListaMascotas(View):
    def get(self, request):
        datosM = Mascotas.objects.all()
        return render(request, 'VeteSoft/ListarMascotas.html', {'infomas':datosM})

    def post(self, request):
        pass

@login_required
def home (request):
    user = request.user
    if user.has_perm('VeteSoft.is_usuario'):
        return redirect(reverse('IndexUsuarios'))

@permission_required('VeteSoft.is_usuario')
def Index_Usuario (request):
    return render (request, template_name='VeteSoft/indexUsuario.html')
