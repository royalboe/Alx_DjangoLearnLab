# Retrieve model instances

## Get into the python shell

```bash
python manage.py shell
```

## Retrieve all books

```python
Book.objects.all()
```

## Retrieve books by title

```python
Book.objects.get(title="1984")
```

## Outputs

```python
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> Book.objects.filter(title="1984")
<QuerySet [<Book: Book object (1)>]>
```