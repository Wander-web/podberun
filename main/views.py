
from django.shortcuts import render, redirect
from django.core.cache import cache
from . import forms, models
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth.models import User

from user import models as UMODEL
from user import forms as UFORM
from partner import models as PMODEL
from partner import forms as PFORM


def not_found_view(request):
    return render(request, '/not_found.html')


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'main/index.html')


def is_partner(user):
    return user.groups.filter(name='PARTNER').exists()


def is_user(user):
    return user.groups.filter(name='USER').exists()


def is_admin(user):
    if not user.groups.filter(name='PARTNER') and not user.groups.filter(name='USER'):
        return True


def afterlogin_view(request):
    if is_user(request.user):
        return redirect('user/user-dashboard')

    elif is_partner(request.user):
        accountapproval = PMODEL.Partner.objects.all().filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('partner/partner-dashboard')
        else:
            return render(request, 'partner/partner_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')


def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_dashboard_view(request):
    tmp = {
        'total_user': UMODEL.Subj.objects.all().count(),
        'total_partner': PMODEL.Partner.objects.all().filter(status=True).count(),
        'pending_partner': PMODEL.Partner.objects.all().filter(status=False).count(),
        'total_course': models.Course.objects.all().count(),
        'total_tags': models.Tag.objects.all().count(),
        'total_university': models.University.objects.all().count(),
        'pending_tag': models.TagToApprove.objects.all().filter(status=False).count(),
    }
    return render(request, 'main/admin_dashboard.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_partner_view(request):
    tmp = {
        'total_partner': PMODEL.Partner.objects.all().filter(status=True).count(),
        'pending_partner': PMODEL.Partner.objects.all().filter(status=False).count(),
    }
    return render(request, 'main/admin_partner.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_partner_view(request):
    partners = PMODEL.Partner.objects.all().filter(status=True)
    return render(request, 'main/admin_view_partner.html', {'partners': partners})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_partner_view(request, pk):
    partner = PMODEL.Partner.objects.get(id=pk)
    user = PMODEL.User.objects.get(id=partner.user_id)
    user_form = PFORM.PartnerUserForm(instance=user)
    partner_form = PFORM.PartnerForm(instance=partner)
    mydict = {'userForm': user_form, 'partnerForm': partner_form}
    if request.method == 'POST':
        user_form = PFORM.PartnerUserForm(request.POST, instance=user)
        partner_form = PFORM.PartnerForm(request.POST, request.FILES, instance=partner)
        if user_form.is_valid() and partner_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            partner_form.save()
            return redirect('admin-view-partner')
    return render(request, 'main/update_partner.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def delete_partner_view(request, pk):
    partner = PMODEL.Partner.objects.get(id=pk)
    user = User.objects.get(id=partner.user_id)
    user.delete()
    partner.delete()
    return HttpResponseRedirect('main/admin-view-partner')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_pending_partner_view(request):
    partners = PMODEL.Partner.objects.all().filter(status=False)
    return render(request, 'main/admin_view_pending_partner.html', {'partners': partners})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def approve_partner_view(request, pk):
    partner = PMODEL.Partner.objects.get(id=pk)
    user = User.objects.get(id=partner.user_id)
    partner.status = True
    partner.save()
    return HttpResponseRedirect('/admin-view-pending-partner')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def reject_partner_view(request, pk):
    partner = PMODEL.Partner.objects.get(id=pk)
    user = User.objects.get(id=partner.user_id)
    user.delete()
    partner.delete()
    return HttpResponseRedirect('/admin-view-pending-partner')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_user_view(request):
    tmp = {
        'total_user': UMODEL.Subj.objects.all().count(),
    }
    return render(request, 'main/admin_user.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_user_view(request):
    users = UMODEL.Subj.objects.all()
    return render(request, 'main/admin_view_user.html', {'users': users})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_user_view(request, pk):
    subj = UMODEL.Subj.objects.get(id=pk)
    user = UMODEL.User.objects.get(id=subj.user_id)
    userForm = UFORM.SubjUserForm(instance=user)
    subjtForm = UFORM.SubjForm(instance=subj)
    mydict = {'userForm': userForm, 'subjtForm': subjtForm}
    if request.method == 'POST':
        userForm = UFORM.SubjUserForm(request.POST, instance=user)
        subjtForm = UFORM.SubjForm(request.POST, instance=subj)
        if userForm.is_valid() and subjtForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            subjtForm.save()
            return redirect('admin-view-user')
    return render(request, 'main/update_user.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def delete_user_view(request, pk):
    subj = UMODEL.Subj.objects.get(id=pk)
    user = User.objects.get(id=subj.user_id)
    user.delete()
    subj.delete()
    return HttpResponseRedirect('/admin-view-user')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_course_view(request):
    return render(request, 'main/admin_course.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_add_course_view(request):
    courseForm = forms.CourseForm()
    if request.method == 'POST':
        courseForm = forms.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request, 'main/admin_add_course.html', {'courseForm': courseForm})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_course_view(request):
    courses = models.Course.objects.all()
    return render(request, 'main/admin_view_course.html', {'courses': courses})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_course_view(request, pk):
    course = models.Course.objects.get(id=pk)
    course_form = forms.CourseForm(instance=course)

    mydict = {'courseForm': course_form}
    if request.method == 'POST':
        course_form = forms.CourseForm(request.POST, instance=course)
        if course_form.is_valid():
            course_form.save()
            return redirect('admin-view-course')
    return render(request, 'main/update_course.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def delete_course_view(request, pk):
    course = models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_tag_view(request):
    tmp = {
        'total_tags': models.Tag.objects.all().count(),
    }
    return render(request, 'main/admin_tag.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_tag_view(request):
    tags = models.Tag.objects.all()
    return render(request, 'main/admin_view_tag.html', {'tags': tags})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_tag_view(request, pk):
    tag = models.Tag.objects.get(id=pk)
    tag_form = forms.TagForm(instance=tag)

    mydict = {'tagForm': tag_form}
    if request.method == 'POST':
        tag_form = forms.TagForm(request.POST, instance=tag)
        if tag_form.is_valid():
            tag_form.save()
            return redirect('admin-view-tag')
    return render(request, 'main/update_tag.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def delete_tag_view(request, pk):
    tag = models.Tag.objects.get(id=pk)
    tag.delete()
    return HttpResponseRedirect('/admin-view-tag')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_pending_tag(request):
    tags = models.TagToApprove.objects.all().filter(status=False)
    return render(request, 'main/admin_view_pending_tag.html', {'tags': tags})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def reject_tag_view(request, pk):
    tag = models.TagToApprove.objects.get(id=pk)
    tag.delete()
    return HttpResponseRedirect('/admin-view-pending-tag')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def add_tag_to_scope(request, tag_id, pk):
    scope = models.Scope.objects.get(id=pk)
    tag = models.TagToApprove.objects.get(id=tag_id)
    scope.tags.create(tag_name=str(tag))
    tag.delete()
    return HttpResponseRedirect('/admin-view-pending-tag')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def approve_partner_tag(request, pk):
    tmp ={
        'scope':models.Scope.objects.all(),
        'tag': models.TagToApprove.objects.get(id=pk)
    }

    return render(request, 'main/admin_choose_scope_to_tag.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_choose_scope_view(request):
    scope = models.Scope.objects.all()
    return render(request, 'main/admin_choose_scope.html', {'scope': scope})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_scope_view(request, pk):
    scope = models.Scope.objects.get(id=pk)
    tag_form = forms.TagForm()
    if request.method == 'POST':
        tag_form = forms.TagForm(request.POST)
        print(tag_form.is_valid())
        if tag_form.is_valid():
            tag_value = request.POST.get("tag_name", '0')
            scope.tags.create(tag_name=str(tag_value))
            return HttpResponseRedirect('/admin-choose-scope')
    return render(request, 'main/admin_add_tag.html', {'tag_form': tag_form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_university_view(request):
    tmp = {
        'total_university': models.University.objects.all().count(),
    }
    return render(request, 'main/admin_university.html', context=tmp)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_view_university_view(request):
    universities = models.University.objects.all()
    return render(request, 'main/admin_view_university.html', {'universities': universities})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def update_university_view(request, pk):
    university = models.University.objects.get(id=pk)
    university_form = forms.UniversityForm(instance=university)

    mydict = {'universityForm': university_form}
    if request.method == 'POST':
        university_form = forms.UniversityForm(request.POST, instance=university)
        if university_form.is_valid():
            university_form.save()
            return redirect('admin-view-university')
    return render(request, 'main/update_university.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def delete_university_view(request, pk):
    university = models.University.objects.get(id=pk)
    university.delete()
    return HttpResponseRedirect('/admin-view-university')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin, login_url='not-found')
def admin_add_university_view(request):
    universityForm = forms.UniversityForm()
    if request.method == 'POST':
        universityForm = forms.UniversityForm(request.POST)
        if universityForm.is_valid():
            universityForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-university')
    return render(request, 'main/admin_add_university.html', {'universityForm': universityForm})


def aboutus_view(request):
    return render(request, 'main/aboutus.html')




