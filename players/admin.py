from django.contrib import admin
from .models import Players

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('playername','playeremail','country','games','score')

# Register your models here.
admin.site.register(Players,PlayersAdmin)