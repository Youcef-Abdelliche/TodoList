from django.db import models


class TodoList(models.Model):
    added_date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text
