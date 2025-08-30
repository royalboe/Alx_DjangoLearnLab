# Create an Instance

## Get into the python shell

```bash
python manage.py shell
```

## Import timezone

There is no need to import the models

```python
from django.utils import timezone
```

## Create an instance of the Book model

```python
bk1 = Book(title="1984", author="George Orwell", publication_year=1949)
```

## Save the instance to the database

```python
bk1.save()
```

## Verify the instance is saved

```python
Book.objects.all()
# or
Book.objects.filter(title="1984")
```

## Output of the commands ran

```python
>>> from django.utils import timezone
>>> bk1 = Book(title="1984", author="George Orwell", publication_year=1949)
>>> bk1.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
```
