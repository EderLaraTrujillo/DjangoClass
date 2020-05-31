from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
# importar modelos de otras apps: 
from userdata.models import DatosUser 

# Create your models here.

class TipoDocu(models.Model):
    nombtido = models.CharField(max_length=50, verbose_name="Nombre de tipo de documento")

    class Meta:
        verbose_name = "Categoria de Documento"
        verbose_name_plural = "Categoría de Documentos"
    
    def __str__(self):
        return self.nombtido

# Modelo de categoria de proyecto
class CateProyecto(models.Model):
    tipoproy = models.CharField(max_length=100, verbose_name="Tipo de proyecto")
    lenguaje = models.CharField(max_length=50, verbose_name="Lenguaje Back-End")
    motordb = models.CharField(max_length=50, verbose_name="Motor BD")
    arquitect = models.CharField(max_length=150, verbose_name="Arquitectura")

    class Meta:
        verbose_name = "Categoria de proyecto"
        verbose_name_plural = "Tipo de Proyecto"

    def __str__(self):
        return self.tipoproy

# Modelo de la entidad proyectos:

class Proyectos(models.Model):
    idcategoria = models.ForeignKey(CateProyecto, on_delete=models.CASCADE, verbose_name="Categoría")
    nombproyect = models.CharField(max_length=256, verbose_name="Nombre de Proyecto")
    descproyect = models.TextField(verbose_name="Descripción del proyecto")
    logoproyect = models.ImageField(upload_to="img/proyectos", verbose_name="Icono")
    fechaini = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Fecha de Inicio")
    fechafin = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Fecha de Finalización")
    urlrepo = models.URLField(verbose_name="Enlace de repositorio")

    class Meta:
        verbose_name = "Proyectos de usuario"
        verbose_name_plural = "Proyectos y Experiencias"

    def __str__(self):
        return self.nombproyect

# Modelo de documentos

class Documentos(models.Model):
    idtipodocu = models.ForeignKey(TipoDocu, on_delete=models.CASCADE, verbose_name="Categoría")
    idusuario = models.ForeignKey(DatosUser, on_delete=models.CASCADE, verbose_name="Usuario")
    idproyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name="Proyectos")
    nombdocu = models.CharField(max_length=256, verbose_name="Nombre de Documento")
    documento = models.FileField(upload_to="documentos/proyectos", verbose_name="Archivo")

    class Meta:
        verbose_name = "Documentos de Proyecto"
        verbose_name_plural = "Documentos de Proyecto"

    def __str__(self):
        return self.nombdocu