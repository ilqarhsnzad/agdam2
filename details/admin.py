from django.contrib import admin

from details.models import BackgroundColor, Light, Logo, Reklam

# Register your models here.

admin.site.register(Logo)
admin.site.register(BackgroundColor)
admin.site.register(Light)
admin.site.register(Reklam)