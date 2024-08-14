from django.db import models
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Post_Title = models.CharField(max_length=200)
    Post_Desc = models.TextField()
    Post_photo = models.ImageField(upload_to='posts/')
    Auther = models.CharField(max_length=100)
    Post_Date = models.DateField()

    def __str__(self):
        return self.Post_Title
    def __int__(self):
        return self.id