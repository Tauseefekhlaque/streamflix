from rest_framework import generics, permissions
from .models import Movie, MyList
from .serializers import RegisterSerializer, MovieSerializer, MyListSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = Movie.objects.all()
        search = self.request.query_params.get('search')
        genre = self.request.query_params.get('genre')
        if search:
            qs = qs.filter(title__icontains=search)
        if genre:
            qs = qs.filter(genre__iexact=genre)
        return qs

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MyListView(generics.ListCreateAPIView):
    serializer_class = MyListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyListDeleteView(generics.DestroyAPIView):
    serializer_class = MyListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyList.objects.filter(user=self.request.user)