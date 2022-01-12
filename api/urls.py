
from .views import *
from django.urls import path
urlpatterns =[
    path("nft-details/<str:name>",nftDetails),
    path("nft-delete/<str:name>",nftDelete),
    path("all-nft/",getAllNFT),
    path("create-nft",nftCreate),
]