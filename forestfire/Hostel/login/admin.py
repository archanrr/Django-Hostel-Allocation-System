from django.contrib import admin

from .models import Register,hostel,rooms,Students

admin.site.register(Register)
admin.site.register(hostel)
admin.site.register(rooms)
admin.site.register(Students)
