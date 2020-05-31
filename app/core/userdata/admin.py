from django.contrib import admin
# Importamos las clases desde los modelos:
from .models import Roles, DatosUser, HabilUser, DetaRoles, Rates

# Register your models here.
# Registro del modelo de Roles:
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]

    class Meta:
        model = Roles

admin.site.register(Roles)

# Registro del modelo de DatosUser:
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser","apelUser",]
    list_display_links = ["nombUser","apelUser",]

    class Meta:
        model = DatosUser
        
admin.site.register(DatosUser)

# Registro del modelo HabilUser:
class HabilUserModel(admin.ModelAdmin):
    list_display = ["NombHabil"]

    class Meta:
        model = HabilUser

admin.site.register(HabilUser)

# REgistro del modelo DetaRoles
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["estaRol"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

# Registro del modelo Rates
class RatesModel(admin.ModelAdmin):
    list_display = ["pcrHabil"]

    class Meta:
        model = Rates

admin.site.register(Rates)