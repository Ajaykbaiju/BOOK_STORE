from django.db import models

# Create your models here.
class Author2(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return '{}'.format(self.name)
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to='book_media')
    quantity=models.IntegerField()


    author=models.ForeignKey(Author2,on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.title)
    
