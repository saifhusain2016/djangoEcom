from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head_0 = models.CharField(max_length=200, default="")
    chead_0 = models.CharField(max_length=1000, default="")
    head_1 = models.CharField(max_length=500, default="")
    chead_1 = models.CharField(max_length=1000, default="")
    head_2 = models.CharField(max_length=500, default="")
    chead_2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to="blog/images/thumbnails", default="")

    def __str__(self):
        return self.title