from django.urls import path
from . import views

urlpatterns = [
    path('', views.resturant_view, name = "resturant-view"),
    path('breakfast/',views.get_breakfast, name = "breakfast"),
    path('main-course/',views.get_main_course, name = "breakfast"),
    path('hot-beverage/',views.get_hot_beverage, name = "breakfast"),
    path('cold-beverage/',views.get_cold_beverage, name = "breakfast"),
    path('dessert/',views.get_dessert, name = "breakfast"),
    path('signup/', views.signup, name = "signup"),
    path('user/', views.user_auth, name= "check_auth"),
    path('signin/', views.signin, name="signin"),
    path('logout_v/', views.logout_v, name="logoutv"),
    path('addToc/', views.add_to_c, name = "add_to_c"),
    path('getcart/', views.get_c, name="get_cart"),
    path('remItemC/', views.remove_item_from_cart, name="remItemC"),
    path('minusItem/', views.neg_q, name="minusItem"),
    path('plusItem/', views.pos_q, name="plusItem"),
    path('order/', views.order , name="order"),
]