from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from blog.forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.xhtml'

# Create your views here.
def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tags = None
    if tag_slug:
        tags = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tags])
    # Pagination with 3 posts per page
    pg = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = pg.page(page_number)
    except PageNotAnInteger:
        posts = pg.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = pg.page(pg.num_pages)
    return render(request, 'blog/post/list.xhtml', {'posts':posts, 'tag': tags})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
     # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.xhtml', {'post': post, 'comments': comments, 'form': form, 'similar_posts': similar_posts})

def share_post(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'karimisughra01@gmail.com', [cd['recipient']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.xhtml', {'post': post, 'form': form, 'sent': sent})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    cmnt = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it
        cmnt = form.save(commit=False)
        # Assign the post to the comment
        cmnt.post = post
        cmnt.save()
    return render(request, 'blog/post/comment.xhtml', {'post': post, 'form': form, 'comment': cmnt})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gte=0.1).order_by('-similarity')
    return render(request,
                  'blog/post/search.xhtml',
                  {'form': form,
                   'query': query,
                   'results': results})