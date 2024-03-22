from django.db import models
from social_media_service.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    following_user_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user_id", "following_user_id"),)
        index_together = (("user_id", "following_user_id"),)
        ordering = ["-created"]

    def validation_id_folowing_and_id_followers(self):
        if self.user_id == self.following_user_id:
            raise ValueError("Can't be same user_id and following_user_id!")

    def save(self, *args, **kwargs):
        self.validation_id_folowing_and_id_followers()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"
