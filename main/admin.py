from django.contrib import admin
from .models import Profile, Skill, Project, BlogPost, Experience, Education, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'linkedin_url', 'github_url', 'twitter_url')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_url', 'live_url', 'order')
    list_editable = ('order',)
    filter_horizontal = ('technologies_used',)
    search_fields = ('title', 'description')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'company', 'description')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('institution', 'degree', 'field_of_study')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
