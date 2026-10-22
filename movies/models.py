from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField(default=0)
    poster = models.URLField()
    banner = models.URLField(blank=True)

    def __str__(self):
        return self.title


class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mylist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} → {self.movie.title}"