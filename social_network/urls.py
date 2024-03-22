from rest_framework import routers

from social_network.views import (
    PostViewSet,
    UserFollowingViewSet,
    UserFollowerViewSet
)

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("followings", UserFollowingViewSet)
router.register("followers", UserFollowerViewSet, basename="user-follower")

urlpatterns = router.urls

app_name = "social_network"
