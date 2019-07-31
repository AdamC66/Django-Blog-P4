from django.db import models


class Article(models.Model):
    title = models.CharField(max_length = 255, null=False)
    body = models.TextField(blank = True, null=False)
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length = 63, null = False)
    def __str__(self):
        return (f'{self.title}, By: {self.author}')
