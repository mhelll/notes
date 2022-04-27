from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Заметка')
    content = models.TextField(null=True, blank=True, verbose_name='Описание заметки')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Заметка создана')

class Meta:
    verbose_name_plural = 'Объявления'
    verbose_name = 'Объявление'
    ordering = ['-published']