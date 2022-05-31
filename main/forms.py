from django import forms
from django.contrib.auth.models import User
from main import models
from main.models import Tag


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['title', 'code', 'link', 'university', 'description', 'tag_1', 'tag_2', 'tag_3']

        widgets = {
            'university': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={"rows": 3, "cols": 10}),
            'tag_1': forms.Select(attrs={'class': 'form-select'}),
            'tag_2': forms.Select(attrs={'class': 'form-select'}),
            'tag_3': forms.Select(attrs={'class': 'form-select'}),
                   }


class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ['tag_name']


class UniversityForm(forms.ModelForm):
    class Meta:
        model = models.University
        fields = ['title', 'link']


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, tag):
        return '%s' % tag.tag_name


class ScopeForm(forms.ModelForm):
    class Meta:
        model = models.Scope
        fields = ['scope_name', 'tags']

        tags = CustomMMCF(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )