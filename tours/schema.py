import graphene

from graphene_django.types import DjangoObjectType
from .models import User, Zone, Tour


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ZoneType(DjangoObjectType):
    class Meta:
        model = Zone


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_zones = graphene.List(ZoneType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_all_zones(self, info, **kwargs):
        return Zone.objects.all()


class CreateZone(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        latitude = graphene.Decimal()
        longitude = graphene.Decimal()
    
    zone = graphene.Field(ZoneType)

    def mutate(self,
               info,
               name,
               description=None,
               latitude=None,
               longitude=None):
        zone = Zone(
            name=name,
            description=description,
            latitude=latitude,
            longitude=longitude
        )
        zone.save()
        return CreateZone(zone=zone)


class DeleteZone(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            zone = Zone.objects.get(pk=id)
            zone.delete()
            ok = True
        except Zone.DoesNotExist:
            ok = False
        
        return DeleteZone(ok=ok)


class Mutations(graphene.ObjectType):
    create_zone = CreateZone.Field()
    delete_zone = DeleteZone.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
