from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib import admin
from main import views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('partner/', include('partner.urls')),
    path('user/', include('user.urls')),

    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('aboutus', views.aboutus_view),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('not-found', views.not_found_view, name='not-found'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='main/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-partner', views.admin_partner_view, name='admin-partner'),
    path('admin-view-partner', views.admin_view_partner_view, name='admin-view-partner'),
    path('update-partner/<int:pk>', views.update_partner_view, name='update-partner'),
    path('delete-partner/<int:pk>', views.delete_partner_view, name='delete-partner'),
    path('admin-view-pending-partner', views.admin_view_pending_partner_view, name='admin-view-pending-partner'),
    path('approve-partner/<int:pk>', views.approve_partner_view, name='approve-partner'),
    path('reject-partner/<int:pk>', views.reject_partner_view, name='reject-partner'),

    path('admin-user', views.admin_user_view, name='admin-user'),
    path('admin-view-user', views.admin_view_user_view, name='admin-view-user'),
    path('update-user/<int:pk>', views.update_user_view, name='update-user'),
    path('delete-user/<int:pk>', views.delete_user_view, name='delete-user'),

    path('admin-course', views.admin_course_view, name='admin-course'),
    path('admin-add-course', views.admin_add_course_view, name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view, name='admin-view-course'),
    path('update-course/<int:pk>', views.update_course_view, name='update-course'),
    path('delete-course/<int:pk>', views.delete_course_view, name='delete-course'),

    path('admin-tag', views.admin_tag_view, name='admin-tag'),
    path('admin-view-tag', views.admin_view_tag_view, name='admin-view-tag'),
    path('update-tag/<int:pk>', views.update_tag_view, name='update-tag'),
    path('delete-tag/<int:pk>', views.delete_tag_view, name='delete-tag'),
    path('admin-choose-scope', views.admin_choose_scope_view, name='admin-choose-scope'),
    path('update-scope/<int:pk>', views.update_scope_view, name='update-scope'),
    path('admin-view-pending-tag', views.admin_view_pending_tag, name='admin-view-pending-tag'),
    path('approve-tag/<int:pk>', views.approve_partner_tag, name='approve-tag'),
    path('reject-tag/<int:pk>', views.reject_tag_view, name='reject-tag'),
    path(r'^approve-tags/<int:pk>/<int:tag_id>$', views.add_tag_to_scope, name='approve-tags'),


    path('admin-university', views.admin_university_view, name='admin-university'),
    path('admin-view-university', views.admin_view_university_view, name='admin-view-university'),
    path('update-university/<int:pk>', views.update_university_view, name='update-university'),
    path('delete-university/<int:pk>', views.delete_university_view, name='delete-university'),
    path('admin-add-university', views.admin_add_university_view, name='admin-add-university'),



    ]




