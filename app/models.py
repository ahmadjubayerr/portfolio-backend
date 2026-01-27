from django.db import models


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    resume = models.FileField(upload_to="resumes/")
    website_design_count = models.PositiveIntegerField(default=0)
    mobile_app_design_count = models.PositiveIntegerField(default=0)
    live_project_count = models.PositiveIntegerField(default=0)
    about_me = models.TextField()
    why_hire_me = models.TextField()
    expertise = models.CharField(max_length=255, help_text="Comma separated")
    skills = models.CharField(max_length=255, help_text="Comma separated")
    profile_image = models.FileField(upload_to="profile/", help_text="SVG preferred")
    vision = models.ImageField(upload_to="vision/")
    achievement_images_gallery = models.ManyToManyField(
        "Achievement", blank=True
    )

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=150)
    institute = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("website", "Website"),
        ("mobile", "Mobile"),
        ("live", "Live"),
        ("case_study", "Case Study"),
        ("graphics", "Graphics"),
        ("saas", "SaaS"),
        ("dashboard", "Dashboard"),
        ("landing_page", "Landing Page"),
    ]

    canvas_image = models.ImageField(upload_to="projects/canvas/")
    svg_file = models.FileField(upload_to="projects/svg/", blank=True, null=True)
    tag = models.CharField(max_length=100)
    is_favorite=models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    duration = models.CharField(max_length=50)
    overview_video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email= models.CharField(max_length=100)
    message = models.TextField()
    name=models.CharField(max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Achievement(models.Model):
    image = models.ImageField(upload_to="achievements/")

    def __str__(self):
        return f"Achievement {self.id}"
