from rest_framework import routers

from social_network.views import PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = router.urls

app_name = "social_network"
