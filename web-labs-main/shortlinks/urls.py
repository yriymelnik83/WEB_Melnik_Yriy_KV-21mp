from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path('logOut', views.log_out, name= "log_out"),
    path('userPage', views.user_page, name = "user_page"),
    path('about',views.about, name= "about"),
    path('createShort',views.create_short_post, name = "create_short_post"),
    path('getAllLinksData',views.get_all_links, name= 'get_all_links'),
    path('updateLink',views.update_link, name = 'update_link'),
    path('deleteLink',views.delete_link, name = 'delete_link'),
    re_path(r'[^ws\/][a-zA-Z]+',views.redirect_to_original, name = "redirect_to_original")
]