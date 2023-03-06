
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.loginPage, name="Login"),
    path('register/', views.registerPage, name="Register"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'store/logout.html'), name='Logout'),
    path('contact/',views.contact, name="Contact"),
    path('contactSuccess/',views.contactSuccessPage, name="ContactSuccess")
	

]