  
from django.urls import path , include , reverse_lazy
from accounts import views
from django_email_verification import urls as email_urls
from django.contrib.auth import views as auth_views


app_name = 'accounts'


urlpatterns = [
    path('addUser/', views.signup, name="register"),
    path('login/', views.login, name="login"),
    path('logout/',views.logout_view , name ='logout'),
    # path('logout/', Logout.as_view(), name="logout"),
    # path('forget-password/', views.changepasswadd_to_cartord, name="changepassword"),
    path('email/', include(email_urls)),
    path('confirm_template/<uidb64>/<token>',views.activate_user, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ='password_reset.html' , email_template_name='password_reset_emaill.html' ,success_url = reverse_lazy('accounts:password_reset_done')), name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ='password_reset_done.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ='password_reset_confirm.html' , success_url = reverse_lazy('accounts:password_reset_complete')), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name ='password_reset_complete.html'), name = 'password_reset_complete'),
    path('editprofile/' ,views.ProfileEditView , name='profile' ),
    path('favorites/', views.Favorites.as_view() , name='favorites' ),
    path('asd/<id>', views.asd , name='comment' ),
    path('favorites/remove_fav/<id>', views.remove_favorite , name='remove_favorites' ),





]





