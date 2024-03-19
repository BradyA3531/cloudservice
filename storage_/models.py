from django.db import models
import datetime
# Create your models here.

class data(models.Model):
    file_name = models.CharField(max_length = 155)
    file_description = models.TextField()
    file = models.FileField(upload_to="files")
    file_size = models.IntegerField(default = 0)
    date = models.DateField(("Date"), default = datetime.date.today)

    def __str__(self):
        return self.file_name
