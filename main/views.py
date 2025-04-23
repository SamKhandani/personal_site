from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Profile, Skill, Project, BlogPost, Experience, Education
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    blog_posts = BlogPost.objects.all()[:3]
    form = ContactForm()
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'blog_posts': blog_posts,
        'form': form,
    }
    return render(request, 'main/home.html', context)

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'main/about.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'main/projects.html'
    context_object_name = 'projects'
    ordering = ['order']

class BlogListView(ListView):
    model = BlogPost
    template_name = 'main/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'

def resume(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all().order_by('category', '-proficiency')
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'main/resume.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            
            # Send email notification
            subject = f"New Contact Form Submission: {form.cleaned_data['subject']}"
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Message: {form.cleaned_data['message']}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
            except:
                # Log the error but don't show it to the user
                pass
                
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send email notification
            subject = f"New Contact Form Submission: {form.cleaned_data['subject']}"
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Message: {form.cleaned_data['message']}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
                return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
            except:
                return JsonResponse({'status': 'error', 'message': 'Failed to send email. Please try again.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data. Please check your input.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
