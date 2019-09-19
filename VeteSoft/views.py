#no borrar
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
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template

from .utils import render_to_pdf #created in step 4


def Inicio(request):
    return render(request,"VeteSoft/Administrador.html")


class MedicoVer(ListView):
    model = Medico 
    template_name = 'VeteSoft/ListarEmpleados.html'

class MedicoDelet(DeleteView):
    model = Medico
    template_name = 'VeteSoft/EliminarMedico.html'
    success_url = reverse_lazy('ListaMedico')

class ClienteDelet(DeleteView):
    model = Cliente
    template_name = 'VeteSoft/EliminarCliente.html'
    success_url = reverse_lazy('EliminarClientes')

class MedicoActua(UpdateView):
    model = Medico
    form_class=ActualizarMedico
    template_name = 'VeteSoft/EditarMedicos.html'
    success_url = reverse_lazy('ListaMedico')

class ClienteActua(UpdateView):
    model = Cliente
    form_class=ActualizarCliente
    template_name = 'VeteSoft/EditarCliente.html'
    success_url = reverse_lazy('ListaCLiente')

class RegistroMedico(CreateView):

    def get(self,request):

        form2=RegistroMedicoForm
        return render(request,'VeteSoft/RegistroMedico.html',{'form':form2})

    def post(self,request):

        form2=RegistroMedicoForm(request.POST)
        form2.save(commit=False)
        nombre=request.POST.get('Nombres')
        email=""
        passs=str(nombre)+"col"
        usermedico=User.objects.create_user(nombre,email,passs)
        permiso= Permission.objects.get(name='Is Doctor')
        usermedico.user_permissions.add(permiso)
        usermedico.save()
        form2.save()
        return redirect(reverse('ListaMedico'))



class RegistroCliente(View):
    def get(self,request):

        form2=RegistroClienteForm
        return render(request,'VeteSoft/RegistroCliente.html',{'form':form2})

    def post(self,request):
        
        form2=RegistroClienteForm(request.POST)
        form2.save(commit=False)
        nombre=request.POST.get('Nombres')
        email=""
        passs=str(nombre)+"col"
        userCliente=User.objects.create_user(nombre,email,passs)
        permiso= Permission.objects.get(name='Is Usuario')
        userCliente.user_permissions.add(permiso)
        userCliente.save()
        form2.save()
        return redirect(reverse('ListaCLiente'))


class ClienteList(ListView):
    model = Cliente 
    template_name = 'VeteSoft/ListaCliente.html'



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
            return redirect(reverse('ListMascotas'))


class ListaMascotas(View):
    def get(self, request):
        datosM = Mascotas.objects.all()
        return render(request, 'VeteSoft/ListarMascotas.html', {'infomas':datosM})

    def post(self, request):
        pass


class ListaMascotasUsers(View):
    def get(self, request):
        datosM = Mascotas.objects.all()
        return render(request, 'VeteSoft/ListMasctUser.html', {'infomas':datosM})

    def post(self, request):
        pass


class ListaCitas(View):
    def get(self, request):
        datosC = Citas.objects.all()
        return render(request, 'VeteSoft/ListarCitas.html', {'infomas':datosC})

    def post(self, request):
        pass


class RegistroMascotasUsers(View):
    
    def get(self, request):
        
        form2 = RegistroMascotasForm
        return render(request, 'VeteSoft/RegistroMascotasUsers.html', {'form': form2})

    def post(self, request):
        usuario= user.username
        cliente = Cliente.objects.get(username=usuario)
        form1 = RegistroMascotasForm(request.POST)
        datosM = Mascotas.objects.all()
        if form1.is_valid():
            llenar = form1.save(commit=False)
            llenar.Cliente = cliente
            llenar.save()
            return redirect(reverse('ListaMascotasUsers'))
        
#Login

class RegistroCitas(View):
    def get(self, request,pk):
        
        form2 = RegistroCitaForm
        return render(request, 'VeteSoft/RegistroCitas.html', {'form': form2})

    def post(self, request, pk):
        mascota = Mascotas.objects.get(id=pk)
        form1 = RegistroCitaForm(request.POST)
        if form1.is_valid():
            llenar = form1.save(commit=False)
            llenar.Mascotas = mascota
            llenar.save()
            return redirect(reverse('ListMascotas'))

class RegistroCitasUser(View):
    def get(self, request,pk):
        
        form2 = RegistroCitaForm
        return render(request, 'VeteSoft/RegistroMascotasUsers.html', {'form': form2})

    def post(self, request, pk):
        mascota = Mascotas.objects.get(id=pk)
        form1 = RegistroCitaForm(request.POST)
        if form1.is_valid():
            llenar = form1.save(commit=False)
            llenar.Mascotas = mascota
            llenar.save()
            return redirect(reverse('ListaMascotasUsers'))

class RegistroDatelle(View):
    def get(self, request,pk):
        
        form2 = RegistroDetalle
        return render(request, 'VeteSoft/DetalleCita.html', {'form': form2})

    def post(self, request, pk):
        cita = Citas.objects.get(id=pk)
        form2 = RegistroDetalle(request.POST)
        if form2.is_valid():
            llenar = form2.save(commit=False)
            llenar.Citas = cita
            llenar.save()
            return redirect(reverse('ListaCitas'))


class ListaDetalle(View):
    model= DetalleCita
    template_name='VeteSoft/DetalleCita.html'




class DetalleCitaEliminar(DeleteView):
    model = Cliente
    template_name = 'VeteSoft/EliminarDetalle.html'
    success_url = reverse_lazy('EliminarClientes')


@login_required
def home (request):
    user = request.user
    if user.has_perm('VeteSoft.is_usuario'):
        return redirect(reverse('IndexUsuarios'))
    elif user.has_perm('VeteSoft.is_admin'):
        return redirect(reverse('IndexAdmin'))
    elif user.has_perm('VeteSoft.is_doctor'):
        return redirect('IndexDoctor')
    

@permission_required('VeteSoft.is_usuario')
def Index_Usuario (request):
    return render (request, template_name='VeteSoft/Usuarios.html')

@permission_required('VeteSoft.is_admin')
def Index_Admin(request):
    return render (request, template_name='VeteSoft/indexAdmin.html')

@permission_required('VeteSoft.is_doctor')
def Index_Doctor (request):
    return render(request, template_name='VeteSoft/indexDoctor.html')
    
