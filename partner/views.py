from django.shortcuts import render
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

from main import models as MMODEL
from main import forms as MFORM
from user import models as UMODEL


def partnerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'partner/partnerclick.html')


def partner_signup_view(request):
    user_form = forms.PartnerUserForm()
    partner_form = forms.PartnerForm()
    mydict = {'userForm': user_form, 'partnerForm': partner_form}
    if request.method == 'POST':
        user_form = forms.PartnerUserForm(request.POST)
        partner_form = forms.PartnerForm(request.POST, request.FILES)
        if user_form.is_valid() and partner_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            partner = partner_form.save(commit=False)
            partner.user = user
            partner.save()
            my_partner_group = Group.objects.get_or_create(name='PARTNER')
            my_partner_group[0].user_set.add(user)
        return HttpResponseRedirect('partnerlogin')
    return render(request, 'partner/partnersignup.html', context=mydict)


def is_partner(user):
    return user.groups.filter(name='PARTNER').exists()





@login_required(login_url='partnerlogin')
@user_passes_test(is_partner, '/not-found.html')
def partner_dashboard_view(request):
    partner = models.Partner.objects.get(user_id=request.user.id)
    tmp = {

        'total_course': MMODEL.Course.objects.all().filter(university=partner.university).count(),
    }
    return render(request, 'partner/partner_dashboard.html', context=tmp)


@login_required(login_url='partnerlogin')
@user_passes_test(is_partner)
def partner_course_view(request):
    return render(request, 'partner/partner_course.html')


@login_required(login_url='partnerlogin')
@user_passes_test(is_partner)
def partner_add_course_view(request):
    courseForm = MFORM.CourseForm()
    if request.method == 'POST':
        courseForm = MFORM.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/partner/partner-view-course')
    return render(request, 'partner/partner_add_course.html', {'courseForm': courseForm})


@login_required(login_url='partnerlogin')
@user_passes_test(is_partner)
def partner_view_course_view(request):
    partner = models.Partner.objects.get(user_id=request.user.id)
    courses = MMODEL.Course.objects.all().filter(university=partner.university)
    return render(request, 'partner/partner_view_course.html', {'courses': courses})


@login_required(login_url='partnerlogin')
@user_passes_test(is_partner)
def partner_tag_view(request):
    return render(request, 'partner/partner_tag.html')


@login_required(login_url='partnerlogin')
@user_passes_test(is_partner)
def partner_add_tag_view(request):
    tag_form = forms.PartnerTagForm()
    if request.method == 'POST':
        tag_form = forms.PartnerTagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/partner/partner-tag')
    return render(request, 'partner/partner_add_tag.html', {'tag_form': tag_form})
