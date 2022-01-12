from django.http import JsonResponse
from .models import NFT
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view

@api_view(['GET'])
def getAllNFT(request):
    if request.method == 'GET':
        try:
            nfts = NFT.nodes.all()
            response = []
            for nft in nfts :
                obj = {
                    "uid": nft.uid,
                    "name": nft.name,
                    "price": nft.price,
                }
                response.append(obj)
        except:
            response = {"error": "Error occurred"}
        return JsonResponse(response, safe=False)

@api_view(['GET'])
def nftDetails(request,name):
    if request.method == 'GET':
        # Get NFT by Name
        # body_unicode = request.body.decode('utf-8')
        # json_data=json.loads(request.body)
        # print(json_data)
        try:
            nft = NFT.nodes.get(name=name)
            response = {
                "uid": nft.uid,
                "name": nft.name,
                "price": nft.price,
            }
            
        except :
            response = {"error": "Error occurred"}
        return JsonResponse(response, safe=False)

@api_view(['POST'])
def nftCreate(request):
    if request.method == 'POST':
        # create one NFT
        
        body_unicode = request.body.decode('utf-8')
        json_data=json.loads(body_unicode)
        
        
        name = json_data['name']
        price = int(json_data['price'])
        
        try:
            nft = NFT(name=name, price=price)
            nft.save()
            response = {
                "uid": nft.uid,
            }
            
        except :
            response = {"error": "Error occurred"}
        return JsonResponse(response, safe=False)


@api_view(['DELETE'])
def nftDelete(request,name):
        # create one NFT
    try:
        nft = NFT.nodes.get(name=name)
        nft.delete()
        response={"Status":"Node Deleted Successfully"}
    except :
         response = {"error": "Error occurred"}
    return JsonResponse(response, safe=False)

    
