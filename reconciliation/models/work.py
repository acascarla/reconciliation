from django.db import models


class Work(models.Model):

    title = models.CharField('Title', max_length=255)
    contributors = models.ManyToManyField('Contributor')
    iswc = models.CharField('ISWC', max_length=255, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.iswc, self.title)
