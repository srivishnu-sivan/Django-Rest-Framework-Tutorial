from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model =  Product
        # it should be fields not field, or it throws an error 
        #!  error=======>  assert not (fields is None and exclude is None), (AssertionError: ("Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the ProductSerializer serializer.",)
        fields= [
            'title',
            'Content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    def get_my_discount(self, obj):
        print(obj.Content)
        return obj.get_discount()