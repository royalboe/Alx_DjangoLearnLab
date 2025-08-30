# Update an instance


## Get into the shell

```bash
python manage.py shell
```

## Retrieve an instance

```python
bk2 = Book.objects.get(title="1948")
bk2.title = "2024"
bk2.save()
```

## Verify the instance is updated

```python
Book.objects.all()
# or
Book.objects.filter(title="2024")
```

## Output of the commands ran

```python
>>> bk2 = Book.objects.filter(title="1984")
>>> bk2.title = "2025"
>>> bk2.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'save'
>>> bk2 = Book.objects.get(title="1984")
>>> bk2.title = "2024"
>>> bk2.save()
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> Book.objects.filter(title="1984")
<QuerySet []>
>>> Book.objects.filter(title="2024")
<QuerySet [<Book: Book object (1)>]>
>>>
```
