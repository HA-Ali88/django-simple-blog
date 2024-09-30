"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from blog.feeds import *
import feedparser

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # class based view
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.share_post, name='share_post'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    # path('feedtest', LatestPostsFeed(), name='post_feed_test'),
    path('feed/', post_feeds, name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
