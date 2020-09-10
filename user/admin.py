from django.contrib import admin

from .models import TMUser, TMAuthor
# Register your models here.

admin.site.register(TMUser)
admin.site.register(TMAuthor)