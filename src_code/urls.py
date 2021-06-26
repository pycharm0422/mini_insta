from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register-page'),
    path('add-post/', views.addPost, name='add_post-page'),
    path('likes-count', views.likes, name='likes-count'),
    path('user-account/<int:user_id>/', views.userPage, name='user-page'),
    path('follow_unfollow/<int:id_user>/<str:value>/', views.follow_unfollow, name='follow_unfollow-page'),
    path('login/', auth_views.LoginView.as_view(template_name='src_code/login.html') , name='login-page'),
    path('logout/',auth_views.LogoutView.as_view(template_name='src_code/logout.html'),name='logout-page'),
    path('saved_posts/', views.savedPost, name='saved-post-page'),
    # path('saved_posts/<int:post_id>/', views.savedPost, name='saved-post-page'),
    path('message/<str:receiver>/', views.message, name='message-page'),
    path('send', views.send, name='send'),
    path('getMessages/<str:receiver>/', views.getMessages, name='getMessages'),
    path('individual-post/<int:post_id>/', views.individualPost, name='individual-post-page'),
    path('comment/', views.comment, name='comment-page'),
    path('followers/<int:pk_of_users>/<int:detail_of_user>/', views.followers, name='followers-page'),
    path('following/<int:pk_of_users>/<int:detail_of_user>/', views.following, name='following-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)