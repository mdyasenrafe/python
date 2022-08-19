from django.contrib import admin
from basic.models import Blog, Contact, User

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Blog)

