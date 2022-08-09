from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Characters)
admin.site.register(Race)
admin.site.register(Gender)
admin.site.register(Genre)
admin.site.register(ShelvingCategory)
admin.site.register(CharRaceConn)
admin.site.register(CharGenderConn)
