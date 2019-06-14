from django.db import models
from django.utils import timezone

class Category(models.Model):
    #Category table which will inherit models.Model
    
    name = models.CharField(max_length=100) #compared to varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def _str_(self):
        return self.name #name to be shown when called


class TodoList(models.Model): #class able name that inherits models.Model
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="general")

    class Meta:
        ordering = ["-created"]

    def _str_(self):
        return self.title 
