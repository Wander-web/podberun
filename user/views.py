from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from main import models as MMODEL


def user_click_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'user/userclick.html')


def user_signup_view(request):
    user_form = forms.SubjUserForm()
    subj_form = forms.SubjForm()
    mydict = {'userForm': user_form, 'userSubjForm': subj_form}
    if request.method == 'POST':
        user_form = forms.SubjUserForm(request.POST)
        subj_form = forms.SubjForm(request.POST)
        if user_form.is_valid() and subj_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            subj = subj_form.save(commit=False)
            subj.user = user
            subj.save()
            my_subj_group = Group.objects.get_or_create(name='USER')
            my_subj_group[0].user_set.add(user)
        return HttpResponseRedirect('userlogin')
    return render(request, 'user/usersignup.html', context=mydict)


def is_user(user):
    return user.groups.filter(name='USER').exists()


@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_dashboard_view(request):
    tmp = {
        'total_course': MMODEL.Course.objects.all().count(),
    }
    return render(request, 'user/user_dashboard.html', context=tmp)


@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_course_view(request):
    courses = MMODEL.Course.objects.all()

    return render(request, 'user/user_course.html', {'courses': courses})


@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_test_view(request):
    return render(request, 'user/user_test.html')


@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_exam_view(request):
    u = request.user.subj
    subjtForm = forms.SubjForm(instance=u)
    if request.is_ajax():
        u = request.user.subj
        subjtForm = forms.SubjForm(request.POST, instance=u)
        print(subjtForm)
    if request.method == 'POST':
        if subjtForm.is_valid():
            print(subjtForm)
            subjtForm.save()
        return HttpResponseRedirect('/user/user-final')

    return render(request, 'user/user_exam.html')


def user_result_view(request):
    u = request.user.subj
    subjtForm = forms.SubjForm(instance=u)
    if request.method == 'POST':
        subjtForm = forms.SubjForm(request.POST, instance=u)
        if subjtForm.is_valid():
            print(subjtForm)
            subjtForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/user/user-result')

    return render(request, 'user/user_result.html', {'SubjForm': subjtForm})


def user_final_view(request):
    if request.user.subj.main_sphere == request.user.subj.off_sphere:
        return HttpResponseRedirect('/user/user-test')

    main_sphere_id = request.user.subj.main_sphere.id
    off_sphere_id = request.user.subj.off_sphere.id
    main_tags = MMODEL.Scope.objects.get(id=main_sphere_id).tags.values_list('id', flat=True).distinct()
    off_tags = MMODEL.Scope.objects.get(id=off_sphere_id).tags.values_list('id', flat=True).distinct()
    main_tags_list = [entry for entry in main_tags]
    off_tags_list = [entry for entry in off_tags]
    t_list = main_tags_list + off_tags_list

    courses = MMODEL.Course.objects.filter(tag_1_id__in=t_list) | \
              MMODEL.Course.objects.filter(tag_2_id__in=t_list) | \
              MMODEL.Course.objects.filter(tag_3_id__in=t_list)
    print(courses)

    tmp = {
        'user_mainForm': request.user.subj.main_sphere,
        'user_offForm': request.user.subj.off_sphere,
        'user_main_descForm': request.user.subj.main_sphere.description,
        'user_off_descForm': request.user.subj.off_sphere.description,
        'courses': courses

    }
    return render(request, 'user/user_fin.html', context=tmp)
