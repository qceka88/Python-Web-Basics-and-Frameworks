from django import forms

from lost_and_found.objects_posts.form_mixins import FieldWithFormControlClassMixin
from lost_and_found.objects_posts.models import Post, Object


class PostCreateForm(FieldWithFormControlClassMixin, forms.ModelForm):
    form_control_fields = "__all__"

    class Meta:
        model = Post
        exclude = ('object', 'found')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('object',)


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
