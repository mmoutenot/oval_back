from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# register our api resources
from tastypie.api import Api
# from recommendation_item.api import RestaurantResource
from oval.api import UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = patterns('',
    # api routing
    (r'^api/', include(v1_api.urls)),
    #admin routing
    url(r'^admin/', include(admin.site.urls)),
)
