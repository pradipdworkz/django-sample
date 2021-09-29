from django.contrib import admin
from hello.models import HelloWorld

# Register your models here.
class HelloWorldAdmin(admin.ModelAdmin):
    pass

admin.site.register(HelloWorld, HelloWorldAdmin)