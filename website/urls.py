from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'website'

urlpatterns = [
    # TODO add blog categories
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('portfolio/', views.PortfolioPageView.as_view(), name='portfolio'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('success/', views.EmailSuccess.as_view(), name='success'),
    path('blog/', views.PostsListView.as_view(), name='blog'),
    path('blog/article/post-new/', views.AddPostView.as_view(), name='post-new'),
    path('blog/article/<slug:slug>/', views.PostArticleView.as_view(), name='article-detail'),
    path('blog/article/<slug:slug>/edit/', views.UpdatePostView.as_view(), name='update_post'),
    path('blog/article/<int:pk>/<slug:slug>/comment/', views.AddCommentView.as_view(), name='comment_post'),
    path('blog/article/<slug:slug>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('blog/article/<slug:post_slug>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]

