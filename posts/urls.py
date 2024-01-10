from django.urls import include, path
from.import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', views.PostsViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path('api/create-post/', views.create_post, name='addpost'),
    path('api/update-post/', views.update_post, name='updatepost'),
    path('api/get-post/', views.get_post, name='getpost'),
    path('api/delete-post/', views.delete_post, name='deletepost'),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls