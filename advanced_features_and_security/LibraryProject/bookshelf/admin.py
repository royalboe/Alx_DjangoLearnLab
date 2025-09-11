from django.contrib import admin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
