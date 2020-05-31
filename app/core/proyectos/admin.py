from django.contrib import admin
from .models import TipoDocu, CateProyecto, Proyectos, Documentos

# Register your models here.

class TipoDocuAdmin(admin.ModelAdmin):
    list_display = ("nombtido")
    list_display_links = ["nombtido",]
    search_fields = ["nombtido",]

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

class CateProyectoAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    list_display_links = ("__str__",)
    search_fields = ["tipoproy",]

    class Meta:
        model = CateProyecto

admin.site.register(CateProyecto)

class ProyectosAdmin(admin.ModelAdmin):
    list_display = ("logoproyect","__str__",)
    list_display_links = ["nombproyect",]
    search_fields = ["nombproyect",]

    class Meta:
        model = Proyectos

admin.site.register(Proyectos)


class DocumentosAdmin(admin.ModelAdmin):
    list_display = "nombdocu"
    list_display_links = ["nombdocu",]
    search_fields = ["nombdocu",]

    class Meta:
        model = Documentos

admin.site.register(Documentos)