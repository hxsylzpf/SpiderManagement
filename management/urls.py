from django.conf.urls import url
from management import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^add_task/$', views.add_task, name='add_task'),
    url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
    url(r'^view_task_list/$', views.view_task_list, name='view_task_list'),
    url(r'^view_book/detail/$', views.book_detail, name='book_detail'),
    url(r'^view_task/detail/$', views.task_detail, name='task_detail'),
]