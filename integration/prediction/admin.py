from django.contrib import admin

from . import models

class PredictionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Predictions, PredictionAdmin)
