import graphene
from graphene_django import DjangoObjectType
from .models import Ine

class IneType(DjangoObjectType):
    class Meta:
        model = Ine

class Query(graphene.ObjectType):
    ines = graphene.List(IneType)

    def resolve_ines(self, info, **kwargs):
        return Ine.objects.all()

class CreateIne(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    calle = graphene.String()
    colonia = graphene.String()
    codigo_postal = graphene.String()
    ciudad = graphene.String()
    estado = graphene.String()
    fecha_nacimiento = graphene.String()
    sexo = graphene.String()
    url = graphene.String()

    class Arguments:
        nombre = graphene.String()
        calle = graphene.String()
        colonia = graphene.String()
        codigo_postal = graphene.String()
        ciudad = graphene.String()
        estado = graphene.String()
        fecha_nacimiento = graphene.String()
        sexo = graphene.String()
        url = graphene.String()

    def mutate(self, info, nombre, calle, colonia, codigo_postal, ciudad, estado, fecha_nacimiento, sexo, url):
        ine = Ine(nombre=nombre, calle=calle, colonia=colonia, codigo_postal=codigo_postal, ciudad=ciudad, estado=estado, fecha_nacimiento=fecha_nacimiento, sexo=sexo, url=url)
        ine.save()

        return CreateIne(
            id=ine.id,
            nombre=ine.nombre,
            calle=ine.calle,
            colonia=ine.colonia,
            codigo_postal=ine.codigo_postal,
            ciudad=ine.ciudad,
            estado=ine.estado,
            fecha_nacimiento=ine.fecha_nacimiento,
            sexo=ine.sexo,
            url=ine.url,
        )

class Mutation(graphene.ObjectType):
    create_ine = CreateIne.Field()
