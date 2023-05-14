from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    point = models.IntegerField(default=0)
    class Meta:
        db_table = "user"