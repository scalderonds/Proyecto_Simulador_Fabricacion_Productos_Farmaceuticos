from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    list_display_links = ['nombre']    
    ordering = ['id']

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'laboratorio']
    list_display_links = ['nombre','laboratorio']
    ordering = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'laboratorio', 'get_year_fabricacion', 'p_costo', 'p_venta']
    list_display_links = ['nombre','laboratorio']
    ordering = ['nombre', 'laboratorio']
    list_filter = ['nombre','laboratorio']

    def get_year_fabricacion(self, obj):
        return obj.f_fabricacion.year  # Obtener solo el año de fabricación

    get_year_fabricacion.short_description = 'F Fabricacion'








# Registrar los modelos con sus clases personalizadas en el panel de administración
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
