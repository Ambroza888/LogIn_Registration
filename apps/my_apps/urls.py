from django.conf.urls import url
from . import views
                    
urlpatterns = [
      url(r'^$', views.index),
      url(r'^reg_in_data$', views.reg_in_data),
      url(r'^success$', views.success),
      url(r'log_in_data', views.log_in_data),
      url(r'^go_back$', views.go_back),


      url(r'^wall$', views.dojo_wall),
      url(r'^add_post$', views.add_post),
      url(r'^add_comment$', views.add_comment)
]