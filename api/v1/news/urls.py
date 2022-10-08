from django.urls import path
from . import views

urlpatterns = [
    path('news/',views.NewsListCreateAPIView.as_view(),name='news-list'),
    path('news/<int:pk>/',views.NewsDetailAPIView.as_view(),name="news-detail"),

    path('news/<int:pk>/comment-write',views.CommentWriteAPIView.as_view(), name="news-detail"),

    path('categories/',views.CategoryListCreateAPIView.as_view(),name='category-list'),
    path('categories/<int:pk>/',views.CategoryDetailAPIView.as_view(),name="category-detail"),

    path('categories/<int:pk>/news/',views.CategoryNewsDetailAPIView.as_view(), name="category-news-detail"),

    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailAPIView.as_view(),name="comment-detail"),

    path('daily-news/', views.DailyNewsListAPIView.as_view(), name='daily-news'),
    # path('category-daily-news/', views.CategoryDailyNewsListAPIView.as_view(), name='category-daily-news'),

    path('categories/<int:pk>/daily-news/', views.DailyCategoryNewsListAPIView.as_view(), name='daily-categories')

]
