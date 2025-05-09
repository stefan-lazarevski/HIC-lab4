from django.contrib import admin
from labapp.models import Suplement
# Register your models here.


class SuplementAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

admin.site.register(Suplement, SuplementAdmin)