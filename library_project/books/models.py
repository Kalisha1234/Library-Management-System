from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    membership_number = models.CharField(max_length=20, default=1, unique=True)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        book = self.book
        book.available_copies -= 1
        book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.name}"

    