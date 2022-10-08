from rest_framework import generics
from . import serializers
from news.models import Category,News,Comment
from rest_framework import permissions
from .. import permissions as my_permission
# import django_filters.rest_framework
from rest_framework.filters import SearchFilter

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['title']

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class CategoryNewsDetailAPIView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializer
    permission_classes = [my_permission.IsAdminUserOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        category = generics.get_object_or_404(Category,pk=pk)
        return News.objects.filter(category=category)
    


class NewsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title']
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['title','category','location']


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]



class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAdminUser]

class CommentDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAdminUser]



class CommentWriteAPIView(generics.CreateAPIView):
    serializer_class = serializers.CommentWriteSerializer
    
    def perform_create(self, serializer):
        news = generics.get_object_or_404(News)
        serializer.save(owner = self.request.user, news = news)


class DailyNewsListAPIView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = News.objects.all().order_by('-read_count')
    # print(queryset[0])
    # def get_queryset(self):
    #     return News.objects.all().order_by('-read_count')

# class CategoryDailyNewsListAPIView(generics.ListAPIView):
#     serializer_class = serializers.NewsSerializer
#     queryset = News.objects.all().order_by('-read_count')

class DailyCategoryNewsListAPIView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        category = generics.get_object_or_404(Category, pk=pk)
        return News.objects.filter(category=category).order_by('-read_count')















# class NewsListCreateAPIVew(APIView):

#     def get(self, request):
#         news = models.News.objects.filter(active=True)
#         serializer = serializers.NewsSerializer(news, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = serializers.NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class NewsDetailView(APIView):
    
#     def get_object(self, pk):
#         news = get_object_or_404(models.News, pk=pk)
#         return news

#     def get(self, request, pk):
#         news = self.get_object(pk)
#         serializer = serializers.NewsSerializer(news)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         news = self.get_object(pk)
#         serializer = serializers.NewsSerializer(news, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         news = self.get_object(pk)
#         news.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    

# class CategoryListCreateAPIView(APIView):
#     def get(self, request):
#         category = models.Category.objects.all()
#         serializer = serializers.CategorySerializer(category,
#                                                     many=True,
#                                                     context={'request':request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = serializers.CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CategoryDetaliAPIView(APIView):

#     def get(self, request, pk):
#         category = get_object_or_404(models.Category, pk=pk)
#         serializer = serializers.CategorySerializer(category,
#                                                     context={'request':request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         category = get_object_or_404(models.Category, pk=pk)
#         serializer = serializers.CategorySerializer(category, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         category = get_object_or_404(models.Category, pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    