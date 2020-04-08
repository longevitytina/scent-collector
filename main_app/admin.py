from django.contrib import admin

# Register your models here.
from .models import Scent, Wafting, Power

admin.site.register(Scent)
admin.site.register(Wafting)
admin.site.register(Power)
