from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Question)
admin.site.register(models.Choises)
admin.site.register(models.Participant)
admin.site.register(models.Result)

