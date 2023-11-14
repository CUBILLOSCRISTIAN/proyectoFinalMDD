import graphene

class Anios2021(graphene.ObjectType):
    fecha = graphene.DateTime()
    mediaViento  = graphene.Float()


class Anios2022(graphene.ObjectType):
    fecha = graphene.DateTime()
    mediaViento  = graphene.Float()

class Anios2023(graphene.ObjectType):
    fecha = graphene.DateTime()
    mediaViento  = graphene.Float()


class Departamento(graphene.ObjectType):
    nombre = graphene.String()
    cantidadEstaciones = graphene.Int()
    media = graphene.Float()
    mediana = graphene.Float()

class Home(graphene.ObjectType):
    media = graphene.Float()
    mediana = graphene.Float()
    cantMunicipio = graphene.Int()
    canDepartamento = graphene.Int()
    cantRegion = graphene.Int()
    cantEstacion = graphene.Int()
    cantRegistros = graphene.Int()

class Region(graphene.ObjectType):
    nombre = graphene.String()
    medianaVelocidad = graphene.Float()
    mediaVelocidad = graphene.Float()
    medianaDireccion = graphene.Float()
    mediaDireccion = graphene.Float()
    numeroEstaciones = graphene.Int()