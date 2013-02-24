from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication, SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from oval.api import UserResource
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
#
#     def apply_limits(self, request, object_list=None):
#         if request and request.method in ('GET', 'DELETE'):  # 1.
#             return object_list.filter(users__contains=request.user)
#         if isinstance(object_list, Bundle):  # 2.
#             bundle = object_list # for clarity, lets call it a bundle
#             bundle.data['users'].contains(request.user)  # 3.
#             return bundle
#         return []

class GroupResource(ModelResource):
    users = fields.ToManyField(UserResource, attribute=lambda bundle: Group.objects.filter(users__pk=bundle.request.user.pk))
    class Meta:

        queryset = Group.objects.all()
        resource_name = 'group'
        allowed_methods = ['get','put']
        filtering = {
          'users': ALL_WITH_RELATIONS,
        }

        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

   # def obj_create(self, bundle, request=None, **kwargs):
   #     return super(EnvironmentResource, self).obj_create(bundle, request, user=request.user)

    def apply_authorization_limits(self, request, object_list):
        # if request.user.is_superuser:
        return object_list.filter(users__pk=request.user.pk)

    # def obj_get(self, bundle, request, **kwargs):
    #     bundle = self._meta.authorization.apply_limits(request, bundle)
    #     return super(GroupResource, self).obj_create(bundle, request, **kwargs)

    # def obj_create(self, bundle, request, **kwargs):  # 5.
    #     bundle = self._meta.authorization.apply_limits(request, bundle)
    #     return super(GroupResource, self).obj_create(bundle, request, **kwargs)

    # def obj_update(self, bundle, request, **kwargs):  # 6.
    #     bundle = self._meta.authorization.apply_limits(request, bundle)
    #     return super(GroupResource, self).obj_update(bundle, request, **kwargs)

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

