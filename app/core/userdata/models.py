from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
# Crear la estructura de la aplicacion en el modelo de datos:

# Modelo de la tabla Roles:
class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"

    # Creo la función para llamar atributos:
    def __str__(self):
        return self.RoleName

# Crear los demás modelos para la aplicacion datos user:
# Modelo de la tabla DatosUser:
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20, verbose_name = "Identificación")
    nombUser = models.CharField(max_length = 200, null=True, verbose_name = "Nombres")
    apelUser = models.CharField(max_length = 200, null=True, verbose_name = "Apellidos")
    profeUser = models.CharField(max_length = 100, null=True, verbose_name = "Profesión")
    fotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="img/perfiles")
    teleUser = models.CharField(max_length = 20,verbose_name = "Número de Teléfono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = "Otro", verbose_name = "Género")
    adddata = models.DateTimeField(auto_now_add = True, null=True)
    modifiat = models.DateTimeField(auto_now = True, null=True)

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"

    # Función de seleccion:
    def __str__(self):
        return self.nombUser

# Modelo de la tabla Habilidades:
class HabilUser(models.Model):
    NombHabil = models.CharField(max_length = 100)
    DescHabil = models.TextField(verbose_name = "Descripción de la Habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"
    # Función de Selección
    def __str__(self):
        return self.NombHabil

# Agregamos los modelos de detalle:
class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtuser = models.DateTimeField(auto_now = True)
    estaRol = models.CharField(max_length = 10)

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"

    # Función de mostrar:
    def __unicode__(self):
        return self.idRole

# Tabla Rates:
class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    pcrHabil = models.DecimalField(max_digits = 3, decimal_places = 1) # 99,9
    udtHabil = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuario"
    # Función para evocar:
    def __unicode__(self):
        return self.idUser