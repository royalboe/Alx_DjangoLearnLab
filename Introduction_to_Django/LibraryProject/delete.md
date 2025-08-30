# To delete the instance

## Login to the shell

```bash
python manage.py shell
```

## Retrieve the instance

```python
bk2 = Book.objects.get(title="2024")
```

## Delete the instance

```python
bk2.delete()
```

## Command

```python
>>> bk2 = Book.objects.get(title="1984")
>>> bk2.title = "2024"
>>> bk2.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> Book.objects.filter(title="1984")
<QuerySet []>
>>> Book.objects.filter(title="2024")
<QuerySet [<Book: Book object (1)>]>
>>> bk2.delete()
(1, {'bookshelf.Book': 1})
```

