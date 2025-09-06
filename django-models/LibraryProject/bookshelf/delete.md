# To delete the instance

## Login to the shell

```bash
python manage.py shell
```

## Retrieve the instance

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
```

## Delete the instance

```python
book.delete()
```

## Command

```python
>>> book = Book.objects.get(title="1984")
>>> book.title = "2024"
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> Book.objects.filter(title="1984")
<QuerySet []>
>>> Book.objects.filter(title="2024")
<QuerySet [<Book: Book object (1)>]>
>>> book.delete()
(1, {'bookshelf.Book': 1})
```

