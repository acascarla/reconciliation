from django.db import models


class Contributor(models.Model):

    name = models.CharField('Title', max_length=255, unique=True)

    def __str__(self):
        return self.name
