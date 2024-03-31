from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


#! what is decorators ====>  Decorators are a powerful and elegant feature in Python that allows you to modify or extend the behavior of functions or methods without changing their actual code. They are an excellent way to apply reusable functionality across multiple functions, such as timing, caching, logging, or authentication.

@api_view(["POST"]) #? @api_view decorator must be used if view writing is through a function. The main function of the @api_view decorator is to perform the conversion into an APIView subclass ( the response and request classes are provided) from the function-based view. Allowed methods for the view list are taken by it as an argument.

def api_home(request, *args, **kwargs):
    """
        DRF API VIEW
    
    """
    # model_data = Product.objects.all().order_by("?").first()
    # to add serializers
    
   
    # instance = Product.objects.all().order_by("?").first()
    # data = request
    
    
    # if model_data:
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['Content'] = model_data.Content
    #     # data['price'] = model_data.price
    #     # ! instead of the above lines try the below
    #     data = model_to_dict(model_data)
    
    # if instance:
    #     data = ProductSerializer(instance).data
    
    # data = request.data -----------------|
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        # data = request.data
        return Response(serializer.data)