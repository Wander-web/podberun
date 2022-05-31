from django.urls import path
from partner import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('partnerclick', views.partnerclick_view),
    path('partnerlogin', LoginView.as_view(template_name='partner/partnerlogin.html'), name='partnerlrogin'),
    path('partnersignup', views.partner_signup_view, name='partnersignup'),
    path('partner-dashboard', views.partner_dashboard_view, name='partner-dashboard'),
    path('partner-course', views.partner_course_view, name='partner-course'),
    path('partner-add-course', views.partner_add_course_view, name='partner-add-course'),
    path('partner-view-course', views.partner_view_course_view, name='partner-view-course'),
    path('partner-tag', views.partner_tag_view, name='partner-tag'),
    path('partner-add-tag', views.partner_add_tag_view, name='partner-add-tag'),

]
