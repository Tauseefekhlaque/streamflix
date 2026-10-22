from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Seeds the database with sample movies'

    def handle(self, *args, **kwargs):
        movies = [
            {"title":"Inception","description":"Dream heist thriller.","genre":"Sci-Fi","year":2010,"rating":8.8,"poster":"https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"},
            {"title":"Interstellar","description":"Space exploration epic.","genre":"Sci-Fi","year":2014,"rating":8.6,"poster":"https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg"},
            {"title":"The Dark Knight","description":"Batman vs Joker.","genre":"Action","year":2008,"rating":9.0,"poster":"https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
            {"title":"Joker","description":"Origin of the Joker.","genre":"Drama","year":2019,"rating":8.4,"poster":"https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
            {"title":"Avengers: Endgame","description":"Final battle.","genre":"Action","year":2019,"rating":8.4,"poster":"https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"},
            {"title":"Parasite","description":"Korean social thriller.","genre":"Thriller","year":2019,"rating":8.5,"poster":"https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"},
            {"title":"The Matrix","description":"Simulated reality.","genre":"Sci-Fi","year":1999,"rating":8.7,"poster":"https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
            {"title":"Oppenheimer","description":"Atomic bomb story.","genre":"Drama","year":2023,"rating":8.3,"poster":"https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg"},
        ]
        
        for m in movies:
            Movie.objects.get_or_create(title=m["title"], defaults=m)
            
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(movies)} movies!"))