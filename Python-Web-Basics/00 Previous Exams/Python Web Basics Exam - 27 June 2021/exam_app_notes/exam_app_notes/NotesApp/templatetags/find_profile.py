from django import template

from exam_app_notes.NotesApp.models import Profile

register = template.Library()


@register.simple_tag
def profile_tag():
    profile = Profile.objects.all()
    return profile
