from .models import User, Books
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

content_type = ContentType.objects.get_for_model(Books)
edit_perm = Permission.objects.create(
    codename="can_edit",
    name="Can Edit",
    content_type=content_type
)
create_perm = Permission.objects.create(
    codename="can_create",
    name="Can Create",
    content_type=content_type
)
view_perm = Permission.objects.create(
    codename="can_view",
    name="Can View",
    content_type=content_type
)
delete_perm = Permission.objects.create(
    codename="can_delete",
    name="Can Delete",
    content_type=content_type
)

editors, created = Group.objects.get_or_create(name='Editors')
if created:
    editors.permissions.set([edit_perm, view_perm, create_perm])

viewers, created = Group.objects.get_or_create(name='Viewers')
if created:
    viewers.permissions.set([view_perm])

admin, created = Group.objects.get_or_create(name='Admin')
if created:
    admin.permissions.set([edit_perm, view_perm, delete_perm, create_perm])






