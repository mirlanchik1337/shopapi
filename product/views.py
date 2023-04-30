from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Review, Product

from .serializers import ProductSerializers,CategorySerializers, ReviewSerializers



@api_view(['GET'])
def category_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = CategorySerializers(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_api_view(request):
    movie = Product.objects.all()
    serializer = ProductSerializers(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        movie = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = ProductSerializers(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializers(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,

              data="ERROR! Такой страницы не существует")
    serializer = ReviewSerializers(review)
    return Response(data=serializer.data)

