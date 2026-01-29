from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    MyProfile,
    Project,
    Certification,
    Experience,
    Education,
    Contact
)



@api_view(["GET"])
def my_profile(request):
    profile = MyProfile.objects.first()
    if not profile:
        return Response({"detail": "Profile not found"}, status=404)

    data = {
        "name": profile.name,
        "resume": profile.resume.url,
        "about_me": profile.about_me,
        "why_hire_me": profile.why_hire_me,
        "expertise": profile.expertise.split(","),
        "skills": profile.skills.split(","),
        "counts": {
            "website": profile.website_design_count,
            "mobile": profile.mobile_app_design_count,
            "live": profile.live_project_count,
        },
        "profile_image": profile.profile_image.url,
        "vision": profile.vision.url,
        "achievements": [
            img.image.url for img in profile.achievement_images_gallery.all()
        ],
    }
    return Response(data)


@api_view(["GET"])
def project_list(request):
    category = request.GET.get("category")
    projects = Project.objects.all()

    if category:
        projects = projects.filter(category=category)

    data = [
        {
            "id": p.id,
            "title": p.title,
            "tag": p.tag,
            "category": p.category,
            "duration": p.duration,
            "canvas_image": p.canvas_image.url,
            "svg_file": p.svg_file.url if p.svg_file else None,
            "overview_video_link": p.overview_video_link,
            "body": p.body,
        } for p in projects
    ]
    return Response(data)

@api_view(["GET"])
def favorite_project_list(request):
    projects = Project.objects.filter(is_favorite=True)

    data = [
        {
            "id": p.id,
            "title": p.title,
            "tag": p.tag,
            "category": p.category,
            "duration": p.duration,
            "canvas_image": p.canvas_image.url,
            "svg_file": p.svg_file.url if p.svg_file else None,
            "overview_video_link": p.overview_video_link,
            "body": p.body,
        } for p in projects
    ]
    return Response(data)


@api_view(["GET"])
def project_detail(request, pk):
    p = Project.objects.filter(id=pk).first()

    if not p:
        return Response({"err":"not found"}, 400)
    data = {
            "id": p.id,
            "title": p.title,
            "tag": p.tag,
            "category": p.category,
            "duration": p.duration,
            "canvas_image": p.canvas_image.url,
            "svg_file": p.svg_file.url if p.svg_file else None,
            "overview_video_link": p.overview_video_link,
            "body": p.body,
        }

    return Response(data)

@api_view(["GET"])
def my_certifications(request):
    data = Certification.objects.values("title", "institute", "description", "image", "pdf_file")
    return Response(data)


@api_view(["GET"])
def my_experience(request):
    data = Experience.objects.values("position", "title", "description")
    return Response(data)


@api_view(["GET"])
def my_educations(request):
    data = Education.objects.values("title", "university", "description")
    return Response(data)

def send_contact_email(contact):
  from django.core.mail import send_mail

  message = f"Contact Name: {contact.name}\n\nContact Email:\n{contact.email}\n\nMessage: {contact.message}\n\n"
  subject = f"New contact in my portfolio Confirmation. - {contact.name}"

  # Send the email
  send_mail(
    subject,
    message,
    'jubayeruiuxjvai@gmail.com',
    ['jubayeruiuxjvai@gmail.com'],
    fail_silently=False,
  )
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
from rest_framework import serializers
class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = '__all__'

@api_view(['POST'])
def contact(request):
  serializer=ContactSerializer(request.data)
  print(serializer)
  if not serializer.is_valid():
    return Response(serializer.errors)
  contact=serializer.save()
  send_contact_email(contact)
  return Response({"detail": "Contact message sent successfully."}, status=201)
