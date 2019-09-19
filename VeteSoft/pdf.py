from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import *
from xhtml2pdf import pisa

from VeteSoft.models import *
from django.template.loader import get_template

from .utils import render_to_pdf #created in step 4

class GeneratePDF(View):
    def get(self, request, pk):
        m = Mascotas.objects.get(id=pk)
        d = Cliente.objects.get(id=pk)
        # md = Medico.objects.get(id=pk)
        # c = Citas.objects.get(id=pk)
        # exm = ExamenMascota.objects.get(id=pk)
        # dc = DetalleCita.objects.get(id=pk)
        # rc = ResultadoClinico.objects.get(id=pk)
        rz = Raza.objects.get(id=pk)

        template = get_template('invoice.html')
        medicos  = Medico.objects.all()[0]
        citas    = Citas.objects.all()[0]
        examenes = ExamenMascota.objects.all()[0]
        detallecita = DetalleCita.objects.all()[0]
        resultadoclinico = ResultadoClinico.objects.all()[0]
        mascota  = Mascotas.objects.all()[0]
        raza = Raza.objects.all()[0]
        cliente = Cliente.objects.all()[0]

        #context_dict = get_context_data(medicos)
        #data = {{'Documento': med.Documento, 'Nombres': med.Nombres } for med in medicos}
        #print(data)

        context = {
            'dueño' : cliente.Nombres,
            'nombre' : m.Nombre,
            'raza' : rz.nombre,
            'fechacita' : citas.FechaCita,
            'horacita' : citas.HoraCita,
            'tipoexamen': examenes.TipoExamen,
            'observacion': detallecita.Observacion,
            'resultado': resultadoclinico.Resultado,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')