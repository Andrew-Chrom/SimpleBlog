from rest_framework import generics
from blog_app.models import Articles
from .serializers import ArticlesSerializer

class ArticlesListCreate(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    
    
class ArticlesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    lookup_field = "pk"