# Django Simple Blog
A simple blog application built with Django that allows users to browse blog posts, write comments, and share posts via email. It includes features like pagination, tags, an RSS feed, and more.

## Features
- List Posts:
  - Paginated list of blog posts
  - View posts by tags

- View Post Details:
  - View detailed information of individual posts, including the post content, comments, and tags

- Write Comments:
  - Leave comments on blog posts
  - View other users' comments

- Share Posts:
  - Share blog posts with others via email

- RSS Feed:
  - Subscribe to an RSS feed of the latest blog posts

- Post Highlights:
  - View the most commented posts
  - See the latest posts

Prerequisites
- Python 3

Installation
1. Clone the repository
bash
git clone https://github.com/ HA-Ali88/django-simple-blog.git
cd django-simple-blog

 2. Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

 3. Install dependencies
pip install -r requirements.txt

 4. Set up the database
Run the migrations to create the database tables:
python manage.py migrate

 5. Create a superuser (optional)
If you'd like to access the Django admin interface:
python manage.py createsuperuser

 6. Run the development server
python manage.py runserver
Visit `http://localhost:8000/blog/` in your browser to access the blog.

RSS Feed
- The RSS feed can be accessed at ` /blog/feed/ `, which provides the latest blog posts.
Sitemap
- Visit ‘/sitemap.xml’ to see the sitemap.
Share blog posts
- To Share blog posts with others via email change the Email server configuration in the settings.py file.

## Key Features
 1. Pagination of Posts
The blog post list is paginated to improve user experience and performance.

 2. Tag Filtering
Each post can be associated with tags, and users can filter the post list by clicking on a tag.

 3. Commenting System
Users can submit comments on individual blog posts, and these comments are displayed below each post.

 4. Email Sharing
Each blog post includes a "Share via Email" option, allowing users to send the post to others via email.

 5. RSS Feed
Users can subscribe to the blog’s RSS feed to stay updated with the latest posts.

 6. Post Highlights
The sidebar includes a list of the latest posts and the most commented posts.

Contributing
Contributions are welcome! If you'd like to contribute to this project, feel free to open a pull request.
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

 
