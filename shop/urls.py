from django.urls import path
from shop.views import index, detail, checkout, confimation,RegisterPage,CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('', index, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation" ),
]

