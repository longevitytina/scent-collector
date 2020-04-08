from django.contrib import admin

# Register your models here.
from .models import Scent, Wafting

admin.site.register(Scent)
admin.site.register(Wafting)
