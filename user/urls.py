from django.urls import path
from user import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('userclick', views.user_click_view),
    path('userlogin', LoginView.as_view(template_name='user/userlogin.html'), name='userlogin'),
    path('usersignup', views.user_signup_view, name='usersignup'),
    path('user-dashboard', views.user_dashboard_view, name='user-dashboard'),
    path('user-course', views.user_course_view, name='user-course'),
    path('user-test', views.user_test_view, name='user-test'),
    path('user-result', views.user_result_view, name='user-result'),
    path('user-exam', views.user_exam_view, name='user-exam'),
    path('user-final', views.user_final_view, name='user-final'),




]
