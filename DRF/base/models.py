from django.db import models



class Base(models.Model):
    title=models.CharField(max_length=200 )
    content=models.CharField(max_length=500)
    time_to_create= models.DateTimeField(auto_now_add=True)
    time_to_update=models.DateTimeField(auto_now= True)
    is_published=models.BooleanField(default=True)
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length= 100, db_index=True)

    def __str__(self):
        return self.name
