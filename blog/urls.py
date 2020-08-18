from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blogs/',views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>/',views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/',views.BloggerListView.as_view(), name='blogger-list'),
    path('blogger/<int:pk>/',views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('<int:pk>/add/',views.add_comment, name = 'add-comment')
]
