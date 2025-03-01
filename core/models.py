from django.db import models

# Model representing a blog post
class Post(models.Model):
    title: str = models.CharField(max_length=255)  # Title of the post
    content: str = models.TextField()  # Content of the post
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created

    def __str__(self) -> str:
        """Returns a string representation of the post (title)."""
        return self.title