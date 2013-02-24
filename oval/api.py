from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class ApiKeyOrSessionAuthentication(ApiKeyAuthentication):
  def is_authenticated(self, request, **kwargs):
    if request.user.is_authenticated():
      return True
    return super(ApiKeyOrSessionAuthentication, self).is_authenticated(request, **kwargs)

  def get_identifier(self, request):
    if request.user.is_authenticated():
      return request.user.username
    return super(ApiKeyOrSessionAuthentication, self).get_identifier(request)

class UserResource(ModelResource):

    def determine_format(self, request):
      return 'application/json'

    class Meta:
        authentication = ApiKeyOrSessionAuthentication()
        authorization = DjangoAuthorization()

        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get','put']
        excludes = ['password', 'is_staff', 'is_superuser']

        filtering = { 'username': ALL, }
