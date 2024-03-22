from rest_framework import routers

from social_network.views import PostViewSet, UserFollowingViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("followings", UserFollowingViewSet)

urlpatterns = router.urls

app_name = "social_network"
