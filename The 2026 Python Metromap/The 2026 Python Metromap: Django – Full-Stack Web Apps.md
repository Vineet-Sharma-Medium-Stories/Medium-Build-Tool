# The 2026 Python Metromap: Django – Full-Stack Web Apps

## Series H: Web Development & Automation | Story 2 of 5

![The 2026 Python Metromap/images/Django – Full-Stack Web Apps](images/Django – Full-Stack Web Apps.png)

## 📖 Introduction

**Welcome to the second stop on the Web Development & Automation Line.**

You've mastered Flask—building REST APIs, URL shorteners, and task management systems. Flask is perfect for microservices and APIs, but when you need a full-featured web application with user authentication, an admin panel, database ORM, and built-in security, Django is the answer.

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It comes with everything you need built-in: an ORM, authentication system, admin interface, form handling, and security features. Django follows the "batteries-included" philosophy, making it ideal for building complex, data-driven web applications.

This story—**The 2026 Python Metromap: Django – Full-Stack Web Apps**—is your guide to building complete web applications with Django. We'll build a blog platform with user authentication, post management, comments, and search. We'll create a task management system with user profiles. We'll implement an admin interface for content management. And we'll deploy our application with proper security and performance considerations.

**Let's build full-stack.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories) – COMPLETED
### Series B: Functions & Modules Yard (6 Stories) – COMPLETED
### Series C: Data Structures Express (5 Stories) – COMPLETED
### Series D: Object-Oriented Programming (OOP) Line (6 Stories) – COMPLETED
### Series E: File & Data Handling Line (5 Stories) – COMPLETED
### Series F: Advanced Python Engineering (6 Stories) – COMPLETED
### Series G: Data Science & Visualization (5 Stories) – COMPLETED

### Series H: Web Development & Automation (5 Stories)

- 🌶️ **The 2026 Python Metromap: Flask – Building Web APIs** – URL shortener service; REST endpoints; database storage; redirect logic.

- 🎸 **The 2026 Python Metromap: Django – Full-Stack Web Apps** – Blog platform; user authentication; admin panel; comments system; search functionality. **⬅️ YOU ARE HERE**

- 🤖 **The 2026 Python Metromap: Automation with os and sys** – File organizer script; type-based sorting; file renaming; temp directory cleaning. 🔜 *Up Next*

- 🕸️ **The 2026 Python Metromap: Web Scraping with BeautifulSoup** – Price monitoring bot; multi-site product tracking; price drop alerts.

- ⏰ **The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler** – Daily report emailer; weekly backup system; cron-style job scheduler.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🎸 Section 1: Django Project Structure and Models

Django projects consist of apps, each with models (database schema), views (logic), templates (HTML), and URLs (routing).

**SOLID Principle Applied: Single Responsibility** – Each Django app handles one functional area.

**Design Pattern: MVC Pattern** – Django follows Model-View-Template (similar to MVC).

```python
"""
DJANGO PROJECT STRUCTURE AND MODELS

This section covers the fundamental structure of a Django project.

SOLID Principle: Single Responsibility
- Each Django app handles one functional area

Design Pattern: MVC Pattern
- Django follows Model-View-Template (similar to MVC)
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
import re


# =============================================================================
# MODELS (Database Schema)
# =============================================================================

class User(AbstractUser):
    """
    Custom User model extending Django's built-in User.
    
    Design Pattern: Template Method Pattern - Extends base User
    """
    
    # Additional fields beyond default User
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)
    github_username = models.CharField(max_length=50, blank=True)
    
    # Preferences
    email_notifications = models.BooleanField(default=True)
    comment_notifications = models.BooleanField(default=True)
    
    # Stats
    posts_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    last_active = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('user_profile', args=[self.username])
    
    def update_stats(self):
        """Update user statistics."""
        from blog.models import Post, Comment
        self.posts_count = Post.objects.filter(author=self, status='published').count()
        self.comments_count = Comment.objects.filter(author=self, is_approved=True).count()
        self.save()


class Category(models.Model):
    """
    Blog post category.
    
    Design Pattern: Repository Pattern - Category storage
    """
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from name if not provided."""
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Blog post tag."""
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """
    Blog post model.
    
    SOLID: Single Responsibility - Manages blog post data
    """
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]
    
    # Core fields
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    
    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    # Metadata
    featured_image = models.ImageField(upload_to='posts/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # Dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # Statistics
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['slug', 'status']),
            models.Index(fields=['author', 'status']),
            models.Index(fields=['-published_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        """Auto-generate slug and handle published date."""
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        
        # Auto-generate excerpt if not provided
        if not self.excerpt and self.content:
            self.excerpt = self.content[:200] + '...'
        
        super().save(*args, **kwargs)
    
    def increment_views(self):
        """Increment view count."""
        self.views += 1
        self.save(update_fields=['views'])
    
    def get_reading_time(self):
        """Calculate estimated reading time in minutes."""
        word_count = len(self.content.split())
        return max(1, round(word_count / 200))
    
    @property
    def is_recent(self):
        """Check if post was published in the last 7 days."""
        if self.published_at:
            return (timezone.now() - self.published_at).days <= 7
        return False


class Comment(models.Model):
    """
    Blog post comment.
    
    Design Pattern: Composite Pattern - Comments can have replies
    """
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField(max_length=1000)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['post', 'is_approved']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
    def get_absolute_url(self):
        return f"{self.post.get_absolute_url()}#comment-{self.id}"
    
    def is_reply(self):
        return self.parent is not None


class UserProfile(models.Model):
    """
    Extended user profile.
    
    Design Pattern: Proxy Pattern - Extends User model
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    favorite_categories = models.ManyToManyField(Category, blank=True)
    saved_posts = models.ManyToManyField(Post, blank=True, related_name='saved_by')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_age(self):
        """Calculate age from birth date."""
        if self.birth_date:
            today = timezone.now().date()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None


# =============================================================================
# FORMS
# =============================================================================

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    """Custom user registration form."""
    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Create user profile
            UserProfile.objects.create(user=user)
        
        return user


class PostForm(forms.ModelForm):
    """Form for creating and editing posts."""
    
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'content', 'excerpt', 'featured_image', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 15, 'class': 'rich-text-editor'}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_title(self):
        """Validate title uniqueness."""
        title = self.cleaned_data.get('title')
        if Post.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise ValidationError("A post with this title already exists.")
        return title


class CommentForm(forms.ModelForm):
    """Form for adding comments."""
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'})
        }


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_django_models():
    """
    Demonstrate Django models structure.
    """
    print("=" * 60)
    print("SECTION 1: DJANGO MODELS AND STRUCTURE")
    print("=" * 60)
    
    print("\n1. MODEL RELATIONSHIPS")
    print("-" * 40)
    
    print("""
    User (extends AbstractUser)
    ├── Post (One-to-Many)
    ├── Comment (One-to-Many)
    └── UserProfile (One-to-One)
    
    Category (Parent-child self-reference)
    └── Post (One-to-Many)
    
    Tag
    └── Post (Many-to-Many)
    
    Post
    ├── Category (ForeignKey)
    ├── Author (ForeignKey)
    ├── Tags (ManyToMany)
    └── Comments (One-to-Many)
    
    Comment
    ├── Post (ForeignKey)
    ├── Author (ForeignKey)
    └── Parent (Self-referential for replies)
    """)
    
    print("\n2. MODEL FIELDS AND OPTIONS")
    print("-" * 40)
    
    field_types = [
        ("CharField", "Short text with max_length", "Titles, names"),
        ("TextField", "Long text without length limit", "Content, descriptions"),
        ("IntegerField", "Integer numbers", "Counts, IDs"),
        ("DateTimeField", "Date and time", "Created/updated timestamps"),
        ("ForeignKey", "Many-to-one relationship", "Post → Author"),
        ("ManyToManyField", "Many-to-many relationship", "Post ↔ Tags"),
        ("ImageField", "File upload for images", "Avatars, featured images"),
        ("SlugField", "URL-friendly string", "URL identifiers"),
        ("BooleanField", "True/False", "Status flags"),
    ]
    
    for field_type, description, example in field_types:
        print(f"  {field_type:20} - {description:35} ({example})")
    
    print("\n3. MODEL METHODS")
    print("-" * 40)
    
    print("""
    Common model methods:
    - __str__(): String representation
    - get_absolute_url(): URL for detail view
    - save(): Custom save logic (slug generation, date handling)
    - Custom methods: update_stats(), increment_views(), get_reading_time()
    """)
    
    print("\n4. DATABASE MIGRATIONS")
    print("-" * 40)
    
    print("""
    # Create migration files
    python manage.py makemigrations
    
    # Apply migrations to database
    python manage.py migrate
    
    # View SQL for migration
    python manage.py sqlmigrate blog 0001
    
    # Rollback migration
    python manage.py migrate blog 0001
    """)
    
    print("\n5. ADMIN REGISTRATION")
    print("-" * 40)
    
    print("""
    # admin.py
    from django.contrib import admin
    from .models import Post, Category, Tag, Comment
    
    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'status', 'created_at']
        list_filter = ['status', 'category', 'created_at']
        search_fields = ['title', 'content']
        prepopulated_fields = {'slug': ('title',)}
        date_hierarchy = 'created_at'
    
    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug', 'parent']
        prepopulated_fields = {'slug': ('name',)}
    
    @admin.register(Tag)
    class TagAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug']
        prepopulated_fields = {'slug': ('name',)}
    
    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        list_display = ['post', 'author', 'created_at', 'is_approved']
        list_filter = ['is_approved', 'created_at']
        actions = ['approve_comments']
        
        def approve_comments(self, request, queryset):
            queryset.update(is_approved=True)
        approve_comments.short_description = "Approve selected comments"
    """)


if __name__ == "__main__":
    demonstrate_django_models()
```

---

## 🔐 Section 2: Views, Templates, and Authentication

Django views handle requests, templates render HTML, and authentication manages users.

**SOLID Principles Applied:**
- Single Responsibility: Each view handles one URL pattern
- Dependency Inversion: Views depend on models, not vice versa

**Design Patterns:**
- Template Method Pattern: Class-based views provide structure
- Front Controller Pattern: URL routing to views

```python
"""
VIEWS, TEMPLATES, AND AUTHENTICATION

This section covers Django views, templates, and authentication system.

SOLID Principles Applied:
- Single Responsibility: Each view handles one URL pattern
- Dependency Inversion: Views depend on models

Design Patterns:
- Template Method Pattern: Class-based views provide structure
- Front Controller Pattern: URL routing to views
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods

# Import models and forms (in a real project, these would be imported)
# from .models import Post, Category, Tag, Comment
# from .forms import PostForm, CommentForm, RegistrationForm


# =============================================================================
# CLASS-BASED VIEWS (List, Detail, Create, Update, Delete)
# =============================================================================

class PostListView(ListView):
    """
    Display list of published posts.
    
    Design Pattern: Template Method Pattern - Provides pagination and filtering
    """
    
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        """Filter and order posts."""
        queryset = Post.objects.filter(status='published')
        
        # Filter by category
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        # Filter by tag
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        
        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(excerpt__icontains=query)
            )
        
        return queryset.order_by('-published_at')
    
    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        
        # Add categories with post counts
        context['categories'] = Category.objects.annotate(
            post_count=Count('posts', filter=Q(posts__status='published'))
        ).filter(post_count__gt=0)
        
        # Add popular tags
        context['popular_tags'] = Tag.objects.annotate(
            post_count=Count('posts', filter=Q(posts__status='published'))
        ).filter(post_count__gt=0).order_by('-post_count')[:10]
        
        # Add recent posts
        context['recent_posts'] = Post.objects.filter(
            status='published'
        ).order_by('-published_at')[:5]
        
        # Add archive by month
        context['archives'] = Post.objects.filter(
            status='published'
        ).dates('published_at', 'month', order='DESC')[:12]
        
        return context


class PostDetailView(DetailView):
    """
    Display a single post with comments.
    
    Design Pattern: Detail View Pattern - Shows one object
    """
    
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Increment view count
        post = self.get_object()
        post.increment_views()
        
        # Get approved comments
        context['comments'] = post.comments.filter(
            is_approved=True, parent=None
        ).select_related('author').prefetch_related('replies')
        
        # Add comment form
        context['comment_form'] = CommentForm()
        
        # Related posts (same category or tags)
        related_posts = Post.objects.filter(
            status='published'
        ).exclude(id=post.id)
        
        # Posts in same category
        if post.category:
            related_posts = related_posts.filter(category=post.category)
        else:
            # Posts with shared tags
            related_posts = related_posts.filter(tags__in=post.tags.all()).distinct()
        
        context['related_posts'] = related_posts[:3]
        
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new post.
    
    Design Pattern: Form View Pattern - Handles form submission
    """
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update an existing post.
    
    Design Pattern: Authorization Pattern - Checks user permissions
    """
    
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        """Check if user is author or admin."""
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser
    
    def form_valid(self, form):
        messages.success(self.request, 'Your post has been updated!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a post.
    """
    
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your post has been deleted.')
        return super().delete(request, *args, **kwargs)


# =============================================================================
# FUNCTION-BASED VIEWS
# =============================================================================

@login_required
@require_http_methods(['POST'])
def add_comment(request, post_slug):
    """
    Add a comment to a post.
    
    Design Pattern: Command Pattern - Processes comment submission
    """
    post = get_object_or_404(Post, slug=post_slug, status='published')
    
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        
        # Check for parent comment (reply)
        parent_id = request.POST.get('parent_id')
        if parent_id:
            comment.parent = get_object_or_404(Comment, id=parent_id)
        
        comment.save()
        
        # Auto-approve comments from trusted users
        if request.user.is_superuser or request.user.posts_count > 10:
            comment.is_approved = True
            comment.save()
        
        messages.success(request, 'Your comment has been added!')
    else:
        messages.error(request, 'Please correct the errors below.')
    
    return redirect('post_detail', slug=post_slug)


@login_required
@require_http_methods(['POST'])
def like_post(request, post_slug):
    """Like or unlike a post."""
    post = get_object_or_404(Post, slug=post_slug)
    
    # Check if user already liked
    liked = request.session.get(f'liked_post_{post.id}', False)
    
    if not liked:
        post.likes += 1
        request.session[f'liked_post_{post.id}'] = True
        message = 'You liked this post!'
    else:
        post.likes -= 1
        del request.session[f'liked_post_{post.id}']
        message = 'You unliked this post.'
    
    post.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'likes': post.likes, 'message': message})
    
    return redirect('post_detail', slug=post_slug)


# =============================================================================
# USER AUTHENTICATION VIEWS
# =============================================================================

def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('post_list')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request, username=None):
    """User profile view."""
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    
    # Get user's posts
    posts = Post.objects.filter(author=user, status='published').order_by('-published_at')
    
    # Paginate posts
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'profile_user': user,
        'posts': page_obj,
        'is_owner': request.user == user,
    }
    
    return render(request, 'user/profile.html', context)


@login_required
def edit_profile(request):
    """Edit user profile."""
    if request.method == 'POST':
        # Update user info
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        
        # Update profile
        profile = user.profile
        profile.bio = request.POST.get('bio', profile.bio)
        profile.location = request.POST.get('location', profile.location)
        profile.occupation = request.POST.get('occupation', profile.occupation)
        profile.website = request.POST.get('website', profile.website)
        profile.twitter_handle = request.POST.get('twitter_handle', profile.twitter_handle)
        profile.github_username = request.POST.get('github_username', profile.github_username)
        
        user.save()
        profile.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'user/edit_profile.html', {'user': request.user})


# =============================================================================
# TEMPLATE TAGS AND FILTERS
# =============================================================================

"""
# templatetags/blog_tags.py

from django import template
from django.utils import timezone
from ..models import Category, Tag, Post

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.annotate(post_count=Count('posts'))

@register.simple_tag
def get_popular_tags(limit=10):
    return Tag.objects.annotate(
        post_count=Count('posts')
    ).filter(post_count__gt=0).order_by('-post_count')[:limit]

@register.simple_tag
def get_recent_posts(limit=5):
    return Post.objects.filter(status='published').order_by('-published_at')[:limit]

@register.filter
def time_since(value):
    from django.utils.timesince import timesince
    return timesince(value)

@register.filter
def reading_time(value):
    word_count = len(value.split())
    return max(1, round(word_count / 200))

@register.simple_tag
def get_archive_months():
    return Post.objects.filter(status='published').dates('published_at', 'month', order='DESC')
"""


# =============================================================================
# URL CONFIGURATION
# =============================================================================

"""
# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Blog posts
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
    # Categories
    path('category/<slug:category_slug>/', views.PostListView.as_view(), name='category_detail'),
    
    # Tags
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='tag_detail'),
    
    # Comments
    path('post/<slug:post_slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<slug:post_slug>/like/', views.like_post, name='like_post'),
    
    # User authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
"""


# =============================================================================
# TEMPLATE EXAMPLES
# =============================================================================

def demonstrate_django_templates():
    """
    Demonstrate Django template syntax.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: DJANGO TEMPLATES")
    print("=" * 60)
    
    print("\n1. BASE TEMPLATE (base.html)")
    print("-" * 40)
    
    print("""
    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}My Blog{% endblock %}</title>
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        <header>
            <nav>
                <a href="{% url 'post_list' %}">Home</a>
                {% if user.is_authenticated %}
                    <span>Welcome, {{ user.username }}</span>
                    <a href="{% url 'logout' %}">Logout</a>
                {% else %}
                    <a href="{% url 'login' %}">Login</a>
                    <a href="{% url 'register' %}">Register</a>
                {% endif %}
            </nav>
        </header>
        
        <main>
            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
            
            {% block content %}{% endblock %}
        </main>
        
        <footer>
            <p>&copy; 2024 My Blog</p>
        </footer>
    </body>
    </html>
    """)
    
    print("\n2. POST LIST TEMPLATE (post_list.html)")
    print("-" * 40)
    
    print("""
    {% extends 'base.html' %}
    
    {% block title %}Blog Posts{% endblock %}
    
    {% block content %}
        <h1>Blog Posts</h1>
        
        <!-- Search form -->
        <form method="get" action="">
            <input type="text" name="q" placeholder="Search..." value="{{ request.GET.q }}">
            <button type="submit">Search</button>
        </form>
        
        <!-- Posts loop -->
        {% for post in posts %}
            <article>
                <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
                <p class="meta">
                    By {{ post.author.username }} | 
                    {{ post.published_at|date:"F j, Y" }} |
                    {{ post.content|reading_time }} min read
                </p>
                <p>{{ post.excerpt }}</p>
                <a href="{{ post.get_absolute_url }}">Read more →</a>
            </article>
        {% empty %}
            <p>No posts found.</p>
        {% endfor %}
        
        <!-- Pagination -->
        {% if is_paginated %}
            <div class="pagination">
                {% if page_obj.has_previous %}
                    <a href="?page=1">&laquo; First</a>
                    <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
                {% endif %}
                
                <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
                
                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}">Next</a>
                    <a href="?page={{ page_obj.paginator.num_pages }}">Last &raquo;</a>
                {% endif %}
            </div>
        {% endif %}
        
        <!-- Sidebar -->
        <aside>
            <h3>Categories</h3>
            <ul>
                {% for category in categories %}
                    <li><a href="{{ category.get_absolute_url }}">{{ category.name }}</a></li>
                {% endfor %}
            </ul>
        </aside>
    {% endblock %}
    """)
    
    print("\n3. POST DETAIL TEMPLATE (post_detail.html)")
    print("-" * 40)
    
    print("""
    {% extends 'base.html' %}
    {% load blog_tags %}
    
    {% block title %}{{ post.title }}{% endblock %}
    
    {% block content %}
        <article>
            <h1>{{ post.title }}</h1>
            <p class="meta">
                By {{ post.author.username }} |
                {{ post.published_at|date:"F j, Y" }} |
                {{ post.content|reading_time }} min read |
                {{ post.views }} views
            </p>
            
            {% if post.featured_image %}
                <img src="{{ post.featured_image.url }}" alt="{{ post.title }}">
            {% endif %}
            
            <div class="content">
                {{ post.content|safe }}
            </div>
            
            <div class="tags">
                Tags: 
                {% for tag in post.tags.all %}
                    <a href="{{ tag.get_absolute_url }}">{{ tag.name }}</a>
                {% endfor %}
            </div>
            
            <div class="actions">
                <button id="like-button" data-post-id="{{ post.id }}">
                    ❤️ {{ post.likes }} likes
                </button>
                
                {% if user == post.author %}
                    <a href="{% url 'post_update' post.slug %}">Edit</a>
                    <a href="{% url 'post_delete' post.slug %}">Delete</a>
                {% endif %}
            </div>
            
            <!-- Comments section -->
            <h3>Comments ({{ post.comments.count }})</h3>
            
            {% if user.is_authenticated %}
                <form method="post" action="{% url 'add_comment' post.slug %}">
                    {% csrf_token %}
                    {{ comment_form.as_p }}
                    <button type="submit">Post Comment</button>
                </form>
            {% else %}
                <p><a href="{% url 'login' %}">Login</a> to comment.</p>
            {% endif %}
            
            {% for comment in comments %}
                <div class="comment">
                    <strong>{{ comment.author.username }}</strong>
                    <small>{{ comment.created_at|timesince }} ago</small>
                    <p>{{ comment.content }}</p>
                    
                    {% if user.is_authenticated %}
                        <button class="reply-btn" data-comment-id="{{ comment.id }}">Reply</button>
                    {% endif %}
                    
                    <!-- Replies -->
                    {% for reply in comment.replies.all %}
                        <div class="reply">
                            <strong>{{ reply.author.username }}</strong>
                            <p>{{ reply.content }}</p>
                        </div>
                    {% endfor %}
                </div>
            {% endfor %}
        </article>
    {% endblock %}
    
    {% block extra_js %}
    <script>
        document.getElementById('like-button')?.addEventListener('click', function() {
            fetch(`/post/${postData.slug}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('like-button').innerHTML = `❤️ ${data.likes} likes`;
            });
        });
    </script>
    {% endblock %}
    """)
    
    print("\n4. TEMPLATE FILTERS AND TAGS")
    print("-" * 40)
    
    filters = [
        ("{{ value|date:\"F j, Y\" }}", "Formats date (January 15, 2024)"),
        ("{{ value|truncatewords:30 }}", "Truncates to 30 words"),
        ("{{ value|safe }}", "Marks string as safe (no escaping)"),
        ("{{ value|default:\"Nothing\" }}", "Default value if None"),
        ("{{ value|length }}", "Returns length"),
        ("{{ value|upper }}", "Converts to uppercase"),
        ("{{ value|lower }}", "Converts to lowercase"),
        ("{{ value|linebreaks }}", "Converts newlines to <br>"),
        ("{{ value|slugify }}", "Converts to URL-friendly slug"),
    ]
    
    for filter_example, description in filters:
        print(f"  {filter_example:40} - {description}")


if __name__ == "__main__":
    demonstrate_django_templates()
```

---

## 📊 Section 3: Admin Interface and Search

Django's admin interface provides automatic CRUD operations for models. Advanced search adds powerful querying.

**SOLID Principles Applied:**
- Single Responsibility: Admin configurations separate from models
- Open/Closed: Admin can be customized without changing models

**Design Patterns:**
- Registry Pattern: Admin classes register with site
- Specification Pattern: Search backends implement query specifications

```python
"""
ADMIN INTERFACE AND SEARCH

This section covers Django admin customization and advanced search.

SOLID Principles Applied:
- Single Responsibility: Admin configurations separate from models
- Open/Closed: Admin can be customized without changing models

Design Patterns:
- Registry Pattern: Admin classes register with site
- Specification Pattern: Search backends implement query specifications
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Count, Q
from django.contrib.admin import SimpleListFilter
from django import forms


# =============================================================================
# CUSTOM ADMIN FILTERS
# =============================================================================

class HasCommentsFilter(SimpleListFilter):
    """Filter posts that have comments."""
    
    title = 'Has Comments'
    parameter_name = 'has_comments'
    
    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.annotate(comment_count=Count('comments')).filter(comment_count__gt=0)
        if self.value() == 'no':
            return queryset.annotate(comment_count=Count('comments')).filter(comment_count=0)
        return queryset


class PopularityFilter(SimpleListFilter):
    """Filter posts by popularity based on views."""
    
    title = 'Popularity'
    parameter_name = 'popularity'
    
    def lookups(self, request, model_admin):
        return (
            ('high', 'High (1000+ views)'),
            ('medium', 'Medium (100-999 views)'),
            ('low', 'Low (<100 views)'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'high':
            return queryset.filter(views__gte=1000)
        if self.value() == 'medium':
            return queryset.filter(views__gte=100, views__lt=1000)
        if self.value() == 'low':
            return queryset.filter(views__lt=100)
        return queryset


# =============================================================================
# MODEL ADMIN CONFIGURATIONS
# =============================================================================

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom User admin with additional fields."""
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'post_count', 'comment_count']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined', 'post_count', 'comment_count']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Info', {'fields': ('bio', 'website', 'twitter_handle', 'github_username')}),
        ('Preferences', {'fields': ('email_notifications', 'comment_notifications')}),
        ('Statistics', {'fields': ('posts_count', 'comments_count', 'last_active')}),
    )
    
    def post_count(self, obj):
        """Display number of posts."""
        return obj.posts_count
    post_count.short_description = 'Posts'
    
    def comment_count(self, obj):
        """Display number of comments."""
        return obj.comments_count
    comment_count.short_description = 'Comments'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin configuration."""
    
    list_display = ['name', 'slug', 'parent', 'post_count', 'created_at']
    list_filter = ['parent', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Hierarchy', {
            'fields': ('parent',),
            'classes': ('collapse',)
        }),
    )
    
    def post_count(self, obj):
        """Display number of posts in category."""
        return obj.posts.filter(status='published').count()
    post_count.short_description = 'Published Posts'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin configuration."""
    
    list_display = ['name', 'slug', 'post_count', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
    def post_count(self, obj):
        return obj.posts.filter(status='published').count()
    post_count.short_description = 'Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post admin configuration with rich features.
    
    Design Pattern: Registry Pattern - Registers custom admin actions
    """
    
    # List view configuration
    list_display = [
        'title', 'author_link', 'category', 'status', 'views', 'likes',
        'comment_count', 'published_at', 'featured_image_preview'
    ]
    list_display_links = ['title']
    list_filter = ['status', 'category', 'tags', 'created_at', HasCommentsFilter, PopularityFilter]
    search_fields = ['title', 'content', 'excerpt', 'author__username', 'author__email']
    readonly_fields = ['created_at', 'updated_at', 'views', 'likes', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ['-published_at', '-created_at']
    
    # Form layout
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'category', 'tags', 'content', 'excerpt')
        }),
        ('Media', {
            'fields': ('featured_image',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('status', 'published_at')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('views', 'likes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Actions
    actions = ['make_published', 'make_draft', 'archive_posts']
    
    def make_published(self, request, queryset):
        """Bulk publish posts."""
        updated = queryset.update(status='published')
        self.message_user(request, f'{updated} posts were published.')
    make_published.short_description = "Publish selected posts"
    
    def make_draft(self, request, queryset):
        """Bulk move to draft."""
        updated = queryset.update(status='draft')
        self.message_user(request, f'{updated} posts were moved to draft.')
    make_draft.short_description = "Move to draft"
    
    def archive_posts(self, request, queryset):
        """Bulk archive posts."""
        updated = queryset.update(status='archived')
        self.message_user(request, f'{updated} posts were archived.')
    archive_posts.short_description = "Archive selected posts"
    
    # Custom methods for list display
    def author_link(self, obj):
        """Link to author's admin page."""
        url = reverse('admin:blog_user_change', args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', url, obj.author.username)
    author_link.short_description = 'Author'
    
    def comment_count(self, obj):
        """Display number of comments."""
        return obj.comments.filter(is_approved=True).count()
    comment_count.short_description = 'Comments'
    
    def featured_image_preview(self, obj):
        """Display thumbnail of featured image."""
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>',
                obj.featured_image.url
            )
        return '-'
    featured_image_preview.short_description = 'Image'
    
    # Inlines for related objects
    class CommentInline(admin.TabularInline):
        model = Comment
        extra = 0
        fields = ['author', 'content', 'is_approved', 'created_at']
        readonly_fields = ['created_at']
    
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin configuration."""
    
    list_display = ['content_preview', 'post_link', 'author', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['content', 'author__username', 'post__title']
    list_editable = ['is_approved']
    readonly_fields = ['created_at', 'updated_at']
    
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        """Bulk approve comments."""
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} comments were approved.')
    approve_comments.short_description = "Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        """Bulk disapprove comments."""
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} comments were disapproved.')
    disapprove_comments.short_description = "Disapprove selected comments"
    
    def content_preview(self, obj):
        """Preview comment content."""
        return obj.content[:50] + ('...' if len(obj.content) > 50 else '')
    content_preview.short_description = 'Comment'
    
    def post_link(self, obj):
        """Link to post's admin page."""
        url = reverse('admin:blog_post_change', args=[obj.post.id])
        return format_html('<a href="{}">{}</a>', url, obj.post.title)
    post_link.short_description = 'Post'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """User profile admin."""
    
    list_display = ['user', 'location', 'occupation', 'birth_date', 'get_age']
    search_fields = ['user__username', 'location', 'occupation']
    
    def get_age(self, obj):
        return obj.get_age() if obj.birth_date else '-'
    get_age.short_description = 'Age'


# =============================================================================
# ADVANCED SEARCH
# =============================================================================

from django.contrib.postgres.search import (
    SearchVector, SearchQuery, SearchRank,
    TrigramSimilarity
)


class SearchBackend:
    """
    Search backend with multiple strategies.
    
    Design Pattern: Strategy Pattern - Different search strategies
    """
    
    @staticmethod
    def simple_search(queryset, query):
        """Simple text search using icontains."""
        return queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(author__username__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    
    @staticmethod
    def full_text_search(queryset, query):
        """PostgreSQL full-text search (requires PostgreSQL)."""
        vector = SearchVector('title', 'content', 'excerpt')
        search_query = SearchQuery(query)
        return queryset.annotate(
            rank=SearchRank(vector, search_query)
        ).filter(rank__gt=0).order_by('-rank')
    
    @staticmethod
    def trigram_search(queryset, query):
        """Trigram similarity search (fuzzy matching)."""
        return queryset.annotate(
            similarity=TrigramSimilarity('title', query)
        ).filter(similarity__gt=0.1).order_by('-similarity')
    
    @staticmethod
    def combined_search(queryset, query):
        """Combined search with multiple strategies."""
        # Start with simple search
        results = SearchBackend.simple_search(queryset, query)
        
        # Add relevance ranking
        return results.annotate(
            relevance=(
                Q(title__icontains=query) * 10 +
                Q(tags__name__icontains=query) * 5 +
                Q(content__icontains=query)
            )
        ).distinct().order_by('-relevance')


# =============================================================================
# CUSTOM ADMIN SITE
# =============================================================================

class MetromapAdminSite(admin.AdminSite):
    """Custom admin site with branding."""
    
    site_header = "Metromap Blog Administration"
    site_title = "Metromap Admin"
    index_title = "Welcome to Metromap Blog Admin"
    
    def get_app_list(self, request):
        """Customize app list ordering."""
        app_list = super().get_app_list(request)
        
        # Custom ordering
        for app in app_list:
            if app['app_label'] == 'blog':
                app['models'].sort(key=lambda x: x['object_name'])
        
        return app_list


# admin_site = MetromapAdminSite(name='metromap_admin')


def demonstrate_admin_features():
    """
    Demonstrate Django admin features.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: DJANGO ADMIN AND SEARCH")
    print("=" * 60)
    
    print("\n1. ADMIN CUSTOMIZATION FEATURES")
    print("-" * 40)
    
    features = [
        "list_display - Custom columns in list view",
        "list_filter - Sidebar filters",
        "search_fields - Search functionality",
        "prepopulated_fields - Auto-generate slugs",
        "readonly_fields - Non-editable fields",
        "fieldsets - Organized form layout",
        "inlines - Edit related objects inline",
        "actions - Bulk operations",
        "date_hierarchy - Date-based navigation",
        "ordering - Default sort order"
    ]
    
    for feature in features:
        print(f"  • {feature}")
    
    print("\n2. CUSTOM ADMIN ACTIONS")
    print("-" * 40)
    
    print("""
    @admin.action(description='Mark as published')
    def make_published(self, request, queryset):
        queryset.update(status='published')
    
    actions = [make_published]
    """)
    
    print("\n3. CUSTOM ADMIN FILTERS")
    print("-" * 40)
    
    print("""
    class HasCommentsFilter(SimpleListFilter):
        title = 'Has Comments'
        parameter_name = 'has_comments'
        
        def lookups(self, request, model_admin):
            return (('yes', 'Yes'), ('no', 'No'))
        
        def queryset(self, request, queryset):
            if self.value() == 'yes':
                return queryset.annotate(comment_count=Count('comments')).filter(comment_count__gt=0)
            return queryset
    """)
    
    print("\n4. SEARCH BACKENDS")
    print("-" * 40)
    
    strategies = [
        ("Simple Search", "icontains (case-insensitive)"),
        ("Full-Text Search", "PostgreSQL full-text search"),
        ("Trigram Search", "Fuzzy matching"),
        ("Combined Search", "Multiple strategies with ranking")
    ]
    
    for strategy, description in strategies:
        print(f"  • {strategy}: {description}")
    
    print("\n5. ADMIN URLS")
    print("-" * 40)
    
    print("""
    # Access admin interface
    http://localhost:8000/admin/
    
    # Default admin login
    python manage.py createsuperuser
    
    # Model-specific URLs
    /admin/blog/post/           # Post list
    /admin/blog/post/add/       # Add post
    /admin/blog/post/1/change/  # Edit post
    /admin/blog/post/1/delete/  # Delete post
    """)


if __name__ == "__main__":
    demonstrate_admin_features()
```

---

## 🚀 Section 4: Deployment and Production Considerations

Deploying Django applications requires security, performance, and configuration management.

**SOLID Principles Applied:**
- Dependency Inversion: Settings separate from code
- Open/Closed: Environment-specific configurations

**Design Patterns:**
- Singleton Pattern: Single settings instance
- Factory Pattern: Settings factory for different environments

```python
"""
DEPLOYMENT AND PRODUCTION CONSIDERATIONS

This section covers deploying Django applications to production.

SOLID Principles Applied:
- Dependency Inversion: Settings separate from code
- Open/Closed: Environment-specific configurations

Design Patterns:
- Singleton Pattern: Single settings instance
- Factory Pattern: Settings factory for different environments
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# =============================================================================
# SETTINGS CONFIGURATION (settings.py)
# =============================================================================

def demonstrate_settings_configuration():
    """
    Demonstrate Django settings configuration for different environments.
    """
    print("=" * 60)
    print("SECTION 4: DJANGO DEPLOYMENT")
    print("=" * 60)
    
    print("\n1. ENVIRONMENT-BASED SETTINGS")
    print("-" * 40)
    
    print("""
    # settings.py
    import os
    from pathlib import Path
    from decouple import config
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Environment detection
    ENVIRONMENT = config('ENVIRONMENT', default='development')
    
    # Security settings
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
    
    # Database configuration
    if ENVIRONMENT == 'production':
        DATABASES = {
            'default': dj_database_url.config(default=config('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    
    # Static files
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Media files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
    
    # Security settings for production
    if ENVIRONMENT == 'production':
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_BROWSER_XSS_FILTER = True
        SECURE_HSTS_SECONDS = 31536000  # 1 year
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD = True
        X_FRAME_OPTIONS = 'DENY'
    """)
    
    print("\n2. ENVIRONMENT VARIABLES (.env)")
    print("-" * 40)
    
    print("""
    # .env (never commit to version control)
    SECRET_KEY=your-secret-key-here
    DEBUG=False
    ENVIRONMENT=production
    ALLOWED_HOSTS=example.com,www.example.com
    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    EMAIL_HOST=smtp.sendgrid.net
    EMAIL_PORT=587
    EMAIL_HOST_USER=apikey
    EMAIL_HOST_PASSWORD=your-sendgrid-api-key
    AWS_ACCESS_KEY_ID=your-aws-key
    AWS_SECRET_ACCESS_KEY=your-aws-secret
    AWS_STORAGE_BUCKET_NAME=my-bucket
    """)
    
    print("\n3. PRODUCTION DEPLOYMENT (Gunicorn + Nginx)")
    print("-" * 40)
    
    print("""
    # gunicorn.conf.py
    import multiprocessing
    
    bind = "0.0.0.0:8000"
    workers = multiprocessing.cpu_count() * 2 + 1
    worker_class = "sync"
    timeout = 120
    keepalive = 5
    accesslog = "/var/log/gunicorn/access.log"
    errorlog = "/var/log/gunicorn/error.log"
    loglevel = "info"
    
    # Run with:
    # gunicorn myproject.wsgi:application
    """)
    
    print("\n4. NGINX CONFIGURATION")
    print("-" * 40)
    
    print("""
    # /etc/nginx/sites-available/myproject
    server {
        listen 80;
        server_name example.com;
        return 301 https://$server_name$request_uri;
    }
    
    server {
        listen 443 ssl http2;
        server_name example.com;
        
        ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
        
        location /static/ {
            alias /path/to/staticfiles/;
        }
        
        location /media/ {
            alias /path/to/media/;
        }
        
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    """)
    
    print("\n5. DOCKER DEPLOYMENT")
    print("-" * 40)
    
    print("""
    # Dockerfile
    FROM python:3.11-slim
    
    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    RUN apt-get update && apt-get install -y --no-install-recommends \\
        gcc \\
        libpq-dev \\
        && rm -rf /var/lib/apt/lists/*
    
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    RUN python manage.py collectstatic --noinput
    
    CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
    
    # docker-compose.yml
    version: '3.8'
    
    services:
      db:
        image: postgres:15
        volumes:
          - postgres_data:/var/lib/postgresql/data
        environment:
          POSTGRES_DB: myproject
          POSTGRES_USER: myuser
          POSTGRES_PASSWORD: mypassword
      
      web:
        build: .
        command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
        volumes:
          - .:/app
          - static_volume:/app/staticfiles
          - media_volume:/app/media
        expose:
          - "8000"
        depends_on:
          - db
        environment:
          - DATABASE_URL=postgresql://myuser:mypassword@db:5432/myproject
      
      nginx:
        image: nginx:alpine
        volumes:
          - ./nginx.conf:/etc/nginx/conf.d/default.conf
          - static_volume:/static
          - media_volume:/media
        ports:
          - "80:80"
          - "443:443"
        depends_on:
          - web
    
    volumes:
      postgres_data:
      static_volume:
      media_volume:
    """)
    
    print("\n6. PERFORMANCE OPTIMIZATION")
    print("-" * 40)
    
    optimizations = [
        "• Use Redis for caching (django-redis)",
        "• Implement database query optimization (select_related, prefetch_related)",
        "• Use CDN for static and media files",
        "• Enable Gzip compression",
        "• Use database connection pooling",
        "• Implement pagination for large querysets",
        "• Use async views for I/O-bound operations (Django 3.1+)",
        "• Implement response caching"
    ]
    
    for opt in optimizations:
        print(f"  {opt}")
    
    print("\n7. MONITORING AND LOGGING")
    print("-" * 40)
    
    print("""
    # logging configuration
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/django/errors.log',
                'maxBytes': 1024 * 1024 * 10,  # 10 MB
                'backupCount': 10,
                'formatter': 'verbose',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
            },
            'myapp': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
    """)
    
    print("\n8. DEPLOYMENT CHECKLIST")
    print("-" * 40)
    
    checklist = [
        "✓ Set DEBUG=False",
        "✓ Configure ALLOWED_HOSTS",
        "✓ Generate new SECRET_KEY",
        "✓ Use HTTPS with SSL certificate",
        "✓ Set secure cookie flags",
        "✓ Configure database for production",
        "✓ Setup static file serving (WhiteNoise or CDN)",
        "✓ Configure media file storage (S3 or similar)",
        "✓ Setup email backend",
        "✓ Implement error logging",
        "✓ Set up database backups",
        "✓ Configure caching",
        "✓ Run security checks (python manage.py check --deploy)",
        "✓ Set up monitoring (Sentry, New Relic)"
    ]
    
    for item in checklist:
        print(f"  {item}")


def demonstrate_django_commands():
    """
    Demonstrate useful Django management commands.
    """
    print("\n" + "=" * 60)
    print("DJANGO MANAGEMENT COMMANDS")
    print("=" * 60)
    
    commands = [
        ("python manage.py runserver", "Run development server"),
        ("python manage.py startapp", "Create new app"),
        ("python manage.py makemigrations", "Create migration files"),
        ("python manage.py migrate", "Apply migrations"),
        ("python manage.py createsuperuser", "Create admin user"),
        ("python manage.py collectstatic", "Collect static files"),
        ("python manage.py shell", "Interactive Python shell"),
        ("python manage.py test", "Run tests"),
        ("python manage.py check --deploy", "Check deployment readiness"),
        ("python manage.py dumpdata", "Export data to JSON"),
        ("python manage.py loaddata", "Import data from JSON"),
        ("python manage.py showmigrations", "List migrations"),
        ("python manage.py sqlmigrate", "Show SQL for migration"),
        ("python manage.py reset_db", "Reset database"),
        ("python manage.py createcachetable", "Create cache table"),
    ]
    
    print("\n" + "-" * 40)
    for command, description in commands:
        print(f"  {command:45} - {description}")


if __name__ == "__main__":
    demonstrate_settings_configuration()
    demonstrate_django_commands()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **Django Models** – Define database schema with Python classes. Relationships: ForeignKey, ManyToManyField, OneToOneField. Custom methods, automatic slug generation.

- **Django ORM** – Query database with `objects.filter()`, `exclude()`, `annotate()`. Lazy evaluation. `select_related` and `prefetch_related` for optimization.

- **Views** – Class-based views (ListView, DetailView, CreateView, UpdateView, DeleteView) and function-based views. LoginRequiredMixin, UserPassesTestMixin for authorization.

- **Templates** – HTML with Django template language. Template inheritance with `{% extends %}` and `{% block %}`. Filters (`|date`, `|truncatewords`) and tags (`{% for %}`, `{% if %}`, `{% url %}`).

- **Forms** – ModelForm for automatic form generation from models. Form validation with `clean_<field>()` methods.

- **Authentication** – Built-in User model. Register, login, logout views. Password reset flows. Custom User model with additional fields.

- **Admin Interface** – Automatic CRUD interface. Custom list_display, list_filter, search_fields. Custom actions and filters. Inline editing of related objects.

- **Search** – Simple search with `icontains`. PostgreSQL full-text search with SearchVector and SearchRank. Trigram similarity for fuzzy matching.

- **Deployment** – Environment-based settings with python-decouple. Gunicorn as WSGI server. Nginx as reverse proxy. Docker containerization. Security settings (HTTPS, secure cookies).

- **SOLID Principles Applied** – Single Responsibility (each app, model, view has one purpose), Open/Closed (admin can be extended), Dependency Inversion (settings separate from code), Interface Segregation (clean admin interfaces).

- **Design Patterns Used** – MVC Pattern (Model-View-Template), Template Method Pattern (class-based views), Registry Pattern (admin registration), Strategy Pattern (search backends), Singleton Pattern (settings), Factory Pattern (settings factory), Front Controller Pattern (URL routing), Repository Pattern (model managers).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Flask – Building Web APIs

- **📚 Series H Catalog:** Web Development & Automation – View all 5 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: Automation with os and sys (Series H, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 5 | 0 | 100% |
| Series F | 6 | 6 | 0 | 100% |
| Series G | 5 | 5 | 0 | 100% |
| Series H | 5 | 2 | 3 | 40% |
| Series I | 4 | 0 | 4 | 0% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **47** | **5** | **90%** |

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap