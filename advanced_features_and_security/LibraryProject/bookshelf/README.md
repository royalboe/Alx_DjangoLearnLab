# 📖 Permissions & Groups Setup

## 1. Custom Permissions

Defined in `Books.Meta` inside `models.py`:

- **can_view** → View Books  
- **can_create** → Create Books  
- **can_edit** → Edit Books  
- **can_delete** → Delete Books  

These permissions are created when you run `makemigrations` and `migrate`.

---

## 2. Groups (Created Programmatically)

Instead of manually creating groups in the admin, groups are set up **programmatically** using Django’s `post_migrate` signal.  

This ensures that after every migration, the groups and their assigned permissions are automatically created (if they don’t already exist).  

### Groups & Permissions Mapping

- **Editors** → `can_view`, `can_create`, `can_edit`  
- **Viewers** → `can_view`  
- **Admins** → `can_view`, `can_create`, `can_edit`, `can_delete`  

Implementation is in `signals.py`:

```python
@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name != "main":  # replace with your app name
        return
    # permissions + groups creation logic

## 4. Testing

Create test users.
Assign them to Editors, Viewers, or Admins using Django Admin interface and verify their access rights by logging in as those users.
- Viewers -> Can only view
- Editors -> Can view, edit, or create
- Admins -> Can do all


## 5. Notes

- Using post_migrate ensures groups and permissions are always consistent across environments.
- You don’t need to create groups manually via the admin panel.
- Permissions are enforced at the view level, but can also be checked in templates or serializers if needed.