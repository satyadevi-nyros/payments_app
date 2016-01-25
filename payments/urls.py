from django.conf.urls import url
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^instagram/', views.instagram, name='instagram'),
	url(r'^link/', views.link, name='link'),
	url(r'^facebook/', views.facebook, name='facebook'),

	url(r'^$', views.signup, name='signup'),
	url(r'^verification/(?P<text>[A-Za-z0-9\w @%.,_-]+)/', views.verification, name='verification'),
	url(r'^login/', views.login, name='login'),
	url(r'^uploading/(?P<text>[A-Za-z0-9\w @%.,_-]+)/', views.uploading, name='uploading'),
	url(r'^success/', views.success, name='success'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^plan_data', views.plan_data, name='plan_data'),
	url(r'^image_update', views.image_update, name='image_update'),
	url(r'^upgrade/(?P<text>[A-Za-z0-9\w @%.,_-]+)/', views.upgrade, name='upgrade'),
	url(r'^image', views.image_upload, name='image_upload'),
	url(r'^check', views.check, name="check"),
# url(r'^api/(?P<text>[A-Za-z0-9\w @%.,_-]+)/$',
	# url(r'^email/', views.email, name='email'),
	url(r'^home/', views.home, name='home')

	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 9G5AD+hNzd2Cyem/fGFNkAObGugICbXrxwdAZL+H
#url(r'^favorites/(?P<p_id>[\d]+)/$', 'thesweetestdeal.views.favorites', name='favorites'),

