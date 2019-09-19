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
        
        template = get_template('invoice.html')
        medicos  = Medico.objects.all()[0]
        citas    = Citas.objects.all()[0]
        examenes = ExamenMascota.objects.all()[0]
        detallecita = DetalleCita.objects.all()[0]
        resultadoclinico = ResultadoClinico.objects.all()[0]
        mascota  = Mascotas.objects.all()[0]

        #context_dict = get_context_data(medicos)
        #data = {{'Documento': med.Documento, 'Nombres': med.Nombres } for med in medicos}
        #print(data)

        context = {
            'nombre' : m.Nombre,
            'fechacita' : citas.FechaCita,
            'horacita' : citas.HoraCita,
            'tipoexamen': examenes.Examen,
            'observacion': detallecita.Observacion,
            'resultado': resultadoclinico.Resultado,
            # 'genero': medicos.Genero,
            # 'celular': medicos.Celular,
            # 'direccion': medicos.Direccion,
            # 'fecharegistro': medicos.FechaRegistro,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')