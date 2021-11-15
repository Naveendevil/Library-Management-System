from django.contrib import admin
from .models import Genre,Language,Book,Student,Borrower,Reviews

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Reviews)
