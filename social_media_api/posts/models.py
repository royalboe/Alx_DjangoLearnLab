from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'















# Objective: Develop core functionalities of the Social Media API by adding posts and comments features. This task will enable users to create, view, update, and delete posts and comments within the social media platform.

# Task Description:
# Expand your social_media_api project by creating functionality for users to manage posts and engage with them through comments. This includes setting up models, serializers, views, and routes for posts and comments.
# Step 2: Implement Serializers for Posts and Comments

# Step 3: Create Views for CRUD Operations
# View Implementation:
# Using Django REST Framework’s viewsets, set up CRUD operations for both posts and comments in posts/views.py.
# Implement permissions to ensure users can only edit or delete their own posts and comments.
# Step 4: Configure URL Routing
# Routing Configuration:
# Define URL patterns in posts/urls.py that map to the viewsets using Django REST Framework’s routers. This includes routes for listing, creating, editing, and deleting both posts and comments.
# Step 5: Implement Pagination and Filtering
# Enhance API Usability:
# Add pagination to post and comment list endpoints to manage large datasets.
# Implement filtering capabilities in post views to allow users to search posts by title or content.
# Step 6: Test and Validate Functionality
# Testing Guidelines:
# Thoroughly test all endpoints using tools like Postman or automated tests to ensure they behave as expected.
# Validate that permissions are correctly enforced and that data integrity is maintained through the API.
# Step 7: Document API Endpoints
# Documentation:
# Update the API documentation to include detailed information on how to interact with the posts and comments endpoints.
# Provide examples of requests and responses for all operations.
# Deliverables:
# Code Files: Include all models, serializers, views, and URL configurations related to posts and comments.
# API Documentation: Detailed descriptions of each endpoint, including usage examples.
# Testing Results: Evidence of testing and validation, including any scripts or Postman collections used.
