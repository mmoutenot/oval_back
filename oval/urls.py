from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# register our api resources
from tastypie.api import Api
# from recommendation_item.api import RestaurantResource
from oval.api import UserResource
from group.api import GroupResource, PostResource, TagResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(GroupResource())
v1_api.register(PostResource())
v1_api.register(TagResource())

urlpatterns = patterns('',
    # api routing
    (r'^api/', include(v1_api.urls)),
    #admin routing
    url(r'^admin/', include(admin.site.urls)),
)
