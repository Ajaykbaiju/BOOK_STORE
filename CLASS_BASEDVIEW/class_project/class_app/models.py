from django.db import models



class Author(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return '{}'.format(self.name)

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200,null=True)
    price=models.IntegerField(null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)
