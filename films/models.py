from django.db import models

class Film(models.Model):
    title = models.CharField("Название", max_length=100)
    director = models.CharField("Режиссёр", max_length=100)
    duration = models.IntegerField("Длительность (минуты)")
    description = models.TextField("Описание")
    image = models.ImageField("Постер", upload_to='films/')
    trailer_url = models.URLField("Ссылка на трейлер")
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Reviews(models.Model):
    films_choice = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name='как вас зовут?')
    text = models.TextField(verbose_name='как вам фильм?')

    def __str__(self):
        return f'{self.films_choice}-{self.user_name}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'