from django.db import models

class Raza(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    Tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.Tipo

class GeneroMascota(models.Model):
    Tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.Tipo


class Cliente(models.Model):
    Documento = models.CharField(max_length=45)
    Nombres = models.CharField(max_length=45)
    PrimerApellido = models.CharField(max_length=45)
    SegundoApellido = models.CharField(max_length=45, null=True)
    FechaNacimiento = models.DateField()
    Genero = models.ForeignKey('Genero',on_delete=models.CASCADE,null=True)
    Celular = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    FechaRegistro = models.DateField(auto_now_add=True, null=True)
    Estado = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.Nombres

class Medico(models.Model):
    Documento = models.CharField(max_length=45)
    Nombres = models.CharField(max_length=45)
    PrimerApellido = models.CharField(max_length=45)
    SegundoApellido = models.CharField(max_length=45)
    FechaNacimiento = models.DateField()
    Genero = models.ForeignKey('Genero',on_delete=models.CASCADE,null=True)
    Celular = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    FechaRegistro = models.DateField(auto_now_add=True, null=True)
    Estado = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.Nombres

class Administrador(models.Model):
    Documento = models.CharField(max_length=45)
    Nombres = models.CharField(max_length=45)
    PrimerApellido = models.CharField(max_length=45)
    SegundoApellido = models.CharField(max_length=45)
    FechaNacimiento = models.DateField()
    Genero = models.ForeignKey('Genero',on_delete=models.CASCADE,null=True)
    Celular = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)
    FechaRegistro = models.DateField(auto_now_add=True, null=True)
    Estado = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.Nombres

class Medicamento(models.Model):
    Nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Examen(models.Model):
    Nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class CentroVeterinario(models.Model):
    Nombre = models.CharField(max_length=45)
    Direccion = models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Mascotas(models.Model):
    Nombre = models.CharField(max_length=45)
    FechaNacimiento = models.DateField()
    GeneroMascota = models.ForeignKey('GeneroMascota',on_delete=models.CASCADE,null=True)
    Cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    Raza = models.ForeignKey('Raza', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.Nombre
        
class HistoriaClinica(models.Model):
    Codigo = models.CharField(max_length=45)
    Mascotas = models.ForeignKey('Mascotas', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Codigo



class Citas(models.Model):
    FechaCita = models.DateField()
    HoraCita = models.TimeField()
    Medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    Mascotas = models.ForeignKey('Mascotas', on_delete=models.CASCADE)
    Estado = models.BooleanField(null=True, default=True)


class ExamenMascota(models.Model):
    Examen = models.ForeignKey('Examen', on_delete=models.CASCADE)

class DetalleCita(models.Model):
    Observacion = models.CharField(max_length=50)
    Citas = models.ForeignKey('Citas', on_delete=models.CASCADE)
    Medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    ExamenMascota = models.ForeignKey('ExamenMascota', on_delete=models.CASCADE)

class ResultadoClinico(models.Model):
    Resultado = models.CharField(max_length=45)
    ExamenMascota = models.ForeignKey('ExamenMascota', on_delete=models.CASCADE)

    def __str__(self):
        return self.Resultado

