from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    details = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Особенности"
        verbose_name_plural = "Особенности"





# https://www.youtube.com/watch?v=jBzwzrDvZ18&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=17207s на 5.22
