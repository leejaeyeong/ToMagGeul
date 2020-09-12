from django.contrib import admin

from .models import TMSeries, TMText, Comment

admin.site.register(TMSeries)
admin.site.register(TMText)
admin.site.register(Comment)