from django.conf.urls import url
from management import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^add_task/$', views.add_task, name='add_task'),
    url(r'^view_task_list/$', views.view_task_list, name='view_task_list'),
    url(r'^view_task/detail/$', views.task_detail, name='task_detail'),
    url(r'^view_task/crawl/$', views.crawl, name='crawl'),
    url(r'^view_task/download/$', views.download, name='download'),
    url(r'^view_task/data/$', views.view_task_data, name='data'),
    url(r'^douban/$', views.view_douban, name='view_douban'),
    url(r'^douban/crawle/$', views.douban, name='crawle_douban'),
    url(r'^douban/download/$', views.download_douban, name='download_douban'),
    url(r'^brand_finance/$', views.view_brand_finance, name='view_brand_finance'),
    url(r'^brand_finance/crawle/$', views.brand_finance, name='crawle_brand_finance'),
    url(r'^brand_finance/download/$', views.download_brand_finance, name='download_brand_finance'),
]
