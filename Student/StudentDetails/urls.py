from django.conf.urls import url
from StudentDetails import views

urlpatterns = [
    url(r'^api/student$', views.student_list),
    url(r'^api/student/add-mark/(?P<pk>[0-9]+)$', views.addmarks),
    url(r'^api/percentage$', views.getpercentage),
    url(r'^api/results', views.results),
]