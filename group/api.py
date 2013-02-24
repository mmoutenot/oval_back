from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from group.models import Group, Post, Tag

class ApiKeyOrSessionAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True
        return super(ApiKeyOrSessionAuthentication, self).is_authenticated(request, **kwargs)

    def get_identifier(self, request):
        if request.user.is_authenticated():
            return request.user.username
        return super(ApiKeyOrSessionAuthentication, self).get_identifier(request)

    def apply_limits(self, request, object_list=None):
        if request and request.method in ('GET', 'DELETE'):  # 1.
            return object_list.filter(users.contains(request.user))

class GroupResource(ModelResource):
    class Meta:
        authentication = ApiKeyOrSessionAuthentication()
        authorization = DjangoAuthorization()

        queryset = Group.objects.all()
        resource_name = 'group'
        allowed_methods = ['get','put']

class PostResource(ModelResource):
    class Meta:
        authentication = ApiKeyOrSessionAuthentication()
        authorization = DjangoAuthorization()

        queryset = Post.objects.all()
        resource_name = 'post'
        allowed_methods = ['get','put']

class TagResource(ModelResource):
    class Meta:
        authentication = ApiKeyOrSessionAuthentication()
        authorization = DjangoAuthorization()

        queryset = Post.objects.all()
        resource_name = 'tag'
        allowed_methods = ['get','put']

