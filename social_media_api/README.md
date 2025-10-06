# Social Media API

## TASKS

### Task Two

Objective: Develop core functionalities of the Social Media API by adding posts and comments features. This task will enable users to create, view, update, and delete posts and comments within the social media platform.

Task Description:
Expand your social_media_api project by creating functionality for users to manage posts and engage with them through comments. This includes setting up models, serializers, views, and routes for posts and comments.

#### Step 2: Implement Serializers for Posts and Comments

#### Step 3: Create Views for CRUD Operations

View Implementation:
Using Django REST Framework’s viewsets, set up CRUD operations for both posts and comments in posts/views.py.
Implement permissions to ensure users can only edit or delete their own posts and comments.

#### Step 4: Configure URL Routing

Routing Configuration:
Define URL patterns in posts/urls.py that map to the viewsets using Django REST Framework’s routers. This includes routes for listing, creating, editing, and deleting both posts and comments.

#### Step 5: Implement Pagination and Filtering

Enhance API Usability:
Add pagination to post and comment list endpoints to manage large datasets.
Implement filtering capabilities in post views to allow users to search posts by title or content.

#### Step 6: Test and Validate Functionality

Testing Guidelines:
Thoroughly test all endpoints using tools like Postman or automated tests to ensure they behave as expected.
Validate that permissions are correctly enforced and that data integrity is maintained through the API.

#### Step 7: Document API Endpoints

Documentation:
Update the API documentation to include detailed information on how to interact with the posts and comments endpoints.
Provide examples of requests and responses for all operations.
Deliverables:
Code Files: Include all models, serializers, views, and URL configurations related to posts and comments.
API Documentation: Detailed descriptions of each endpoint, including usage examples.
Testing Results: Evidence of testing and validation, including any scripts or Postman collections used.

### Task Three

Objective: Expand the Social Media API by adding features for users to follow other users and view an aggregated feed of posts from users they follow. This task enhances the social aspect of the platform, mimicking key functionalities seen in popular social media networks.

Task Description:
In this task, you will build on your existing social_media_api by incorporating user relationships and a dynamic content feed. This involves managing user follow relationships and creating a feed that displays posts from followed users.

#### Step 1: Update the User Model to Handle Follows

Model Adjustments:
Modify your custom user model to include a following field, which is a many-to-many relationship to itself, representing the users that a given user follows.
Make necessary migrations to update the user model: bash python manage.py makemigrations accounts python manage.py migrate

#### Step 2: Create API Endpoints for Managing Follows

Follow Management Views:
Develop views in the accounts app that allow users to follow and unfollow others. This might include actions like follow_user and unfollow_user, which update the following relationship.
Ensure proper permissions are enforced so users can only modify their own following list.

#### Step 3: Implement the Feed Functionality

Feed Generation:
Create a view in the posts app that generates a feed based on the posts from users that the current user follows.
This view should return posts ordered by creation date, showing the most recent posts at the top.

#### Step 4: Define URL Patterns for New Features

Routing for Follows and Feed:
Set up URL patterns in accounts/urls.py for follow management (e.g., /follow/<int:user_id>/ and /unfollow/<int:user_id>/).
Add a route in posts/urls.py for the feed endpoint, such as /feed/.

#### Step 5: Test Follow and Feed Features

Testing and Validation:
Conduct thorough tests to ensure that the follow system works as intended and that the feed correctly displays posts from followed users.
Use Postman or similar tools to simulate the user experience and verify the correctness of the output.

#### Step 6: Documentation

API Documentation:
Update your project documentation to include details on how to manage follows and access the feed. Provide clear instructions and examples for each new endpoint.
Document any changes made to models, especially modifications to the user model.
Deliverables:
Updated Models and Migrations: Include changes to the user model and any new migrations.
Code Files for Views and Serializers: Implementations for follow management and feed generation.
URL Configurations: New routes added for managing follows and retrieving the feed.
Documentation: Comprehensive API documentation covering the new functionalities.