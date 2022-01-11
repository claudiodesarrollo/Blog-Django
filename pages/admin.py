from django.contrib import admin
from .models import Page
# Register your models here.
admin.site.register(Page)

#Configuracion del Panel
title="Blog Django"
subtitle="Panel de Gestion"
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle
