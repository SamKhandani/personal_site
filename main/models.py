from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resumes/', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('PROG', 'Programming Languages'),
        ('FRAM', 'Frameworks'),
        ('TOOL', 'Tools & Technologies'),
        ('SOFT', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 rating
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies_used = models.ManyToManyField(Skill)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = RichTextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = RichTextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
