from django.db import models
from neomodel import StructuredNode,StringProperty,IntegerProperty,UniqueIdProperty
# Create your models here.

class NFT(StructuredNode):
    uid = UniqueIdProperty()
    price = IntegerProperty(default=0)
    name = StringProperty(default="NFT name")



