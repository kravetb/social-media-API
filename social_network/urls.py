from rest_framework import routers

from social_network.views import (
    OwnPostViewSet,
    UserFollowingViewSet,
    UserFollowerViewSet,
    FollowingPostViewSet
)

router = routers.DefaultRouter()
router.register("own_posts", OwnPostViewSet, basename="own-post")
router.register(
    "following_posts",
    FollowingPostViewSet,
    basename="following-post"
)
router.register("followings", UserFollowingViewSet)
router.register("followers", UserFollowerViewSet, basename="user-follower")

urlpatterns = router.urls

app_name = "social_network"
