from django.contrib import admin
from .models import Book, User

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)

# Register your models here.
