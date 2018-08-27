from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^list/$',views.SchoolList.as_view(),name="school_list"),
    url(r'(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name="school_detail"),
    url(r'^create/$',views.CreateSchoolView.as_view(),name="create_school"),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name="update"),

]
