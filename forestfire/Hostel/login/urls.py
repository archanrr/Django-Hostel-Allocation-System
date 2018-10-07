from django.urls import path


from . import views

urlpatterns=[
    path('',views.StudentHostelAllocation,name='StudentHostelAllocation'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogin/register/',views.register_page,name='register_page'),
    path('Studentlogin/',views.Studentlogin,name='Studentlogin'),
    path('Studentlogin/login_user/',views.login_user,name='login user'),
    path('adminlogin/register/signin/',views.signin,name='signin'),
    path('Studentlogin/login_user/hostelAllocation/',views.hostelAllocation,name='hostelAllocation'),
    
]