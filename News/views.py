from rest_framework.viewsets import ModelViewSet
from .models import News, Category, Comment, Advertisement,ImageModel
from .serializers import NewsSerializer, CategorySerializer,ImageSerializer
from rest_framework import filters
from News.paginations import DefaultPagination


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','category__name']
    pagination_class=DefaultPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        news_pk = self.kwargs['news_pk']  # <-- lowercase
        return ImageModel.objects.filter(news_id=news_pk)
    def perform_create(self, serializer):
        news_pk = self.kwargs['news_pk']
        serializer.save(news_id=news_pk)

