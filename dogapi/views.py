from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

# Create your views here.
### BEHOLD THE DOGS ###
class DogDetail(APIView):
    # GET a dog if it's valid
    def get(self, request, dog_id, format=None):
        # Make sure the dog exists in the DB first
        try:
            doggie = Dog.objects.get(pk=dog_id)
        # Yell loudly if it doesn't.
        except Dog.DoesNotExist:
            return Response({"error": "Dog does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Make the data nice to return outwards
        serializer = DogSerializer(doggie)
        # Spit it out.
        return Response(serializer.data)

    # PUT a dog if it's valid
    def put(self, request, dog_id, format=None):
        # Make sure the dog exists... this is getting repetitive. I can't find a way to repeat this code easily.
        try:
            doggie = Dog.objects.get(pk=dog_id)
        except Dog.DoesNotExist:
            return Response({"error": "Dog does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Make it good data.
        doggie_cereal = DogSerializer(doggie, data=request.data)
        # Check it's good data.
        if doggie_cereal.is_valid():
            # Save to DB.
            doggie_cereal.save()
            # Return what was saved.
            return Response(doggie_cereal.data)
        else:
            return Response(DogSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE a dog (PUT a dog down)
    def delete(self, request, dog_id, format=None):
        try:
            doggie = Dog.objects.get(pk=dog_id)
        except Dog.DoesNotExist:
            return Response({"error": "Dog does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Kill the dog. :(
        doggie.delete()
        return Response({"message": "He's dead, Jim."}, status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    # GET a dog if it's valid
    def get(self, request, format=None):
        doggie = Dog.objects.all()

        # Let's enumerate those values for our filters.
        name = request.query_params.get('name', None)
        if name is not None:
            doggie = doggie.filter(name=name)

        age = request.query_params.get('age', None)
        if age is not None:
            doggie = doggie.filter(age=age)

        breed = request.query_params.get('breed', None)
        if breed is not None:
            doggie = doggie.filter(breed=breed)

        gender = request.query_params.get('gender', None)
        if gender is not None:
            doggie = doggie.filter(gender=gender)

        color = request.query_params.get('color', None)
        if color is not None:
            doggie = doggie.filter(color=color)

        favoritefood = request.query_params.get('favoritefood', None)
        if favoritefood is not None:
            doggie = doggie.filter(favoritefood=favoritefood)

        favoritetoy = request.query_params.get('favoritetoy', None)
        if favoritetoy is not None:
            doggie = doggie.filter(favoritetoy=favoritetoy)

        # Finally return the list of dogs...
        serializer = DogSerializer(doggie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        doggie_data = JSONParser().parse(request)
        doggie_cereal = DogSerializer(data=doggie_data, many=True)
        if doggie_cereal.is_valid():
            doggie_cereal.save()
            return Response(doggie_cereal.data)
        else:
            return Response(DogSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


## Do it again, but for the breeds now.
class BreedDetail(APIView):
    # GET a breed if it's valid
    def get(self, request, breed_id, format=None):
        # Make sure the breed exists in the DB first
        try:
            the_breed = Breed.objects.get(pk=breed_id)
        # Yell loudly if it doesn't.
        except Breed.DoesNotExist:
            return Response({"error": "Breed does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Make the data nice to return outwards
        serializer = BreedSerializer(the_breed)
        # Spit it out.
        return Response(serializer.data)

    # PUT a breed if it's valid
    def put(self, request, breed_id, format=None):
        # Make sure the breed exists... this is getting repetitive. I can't find a way to repeat this code easily. (x2)
        try:
            the_breed = Breed.objects.get(pk=breed_id)
        except Breed.DoesNotExist:
            return Response({"error": "Breed does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Make it good data.
        breed_serial = BreedSerializer(the_breed, data=request.data)
        # Check it's good data.
        if breed_serial.is_valid():
            # Save to DB.
            breed_serial.save()
            # Return what was saved.
            return Response(breed_serial.data)
        else:
            return Response(BreedSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE a breed (PUT a dog down)
    def delete(self, request, breed_id, format=None):
        try:
            the_breed = Breed.objects.get(pk=breed_id)
        except Breed.DoesNotExist:
            return Response({"error": "Breed does not exist"}, status=status.HTTP_404_NOT_FOUND)
        # Kill the dog(s). :(
        the_breed.delete()
        return Response({"message": "They're dead, Jim."}, status=status.HTTP_204_NO_CONTENT)


class BreedList(APIView):
    # GET a dog if it's valid
    def get(self, request, format=None):
        the_breeds = Breed.objects.all()

        # Let's enumerate those values for our filters.
        name = request.query_params.get('name', None)
        if name is not None:
            the_breeds = the_breeds.filter(name=name)

        size = request.query_params.get('size', None)
        if size is not None:
            the_breeds = the_breeds.filter(size=size)

        friendliness = request.query_params.get('friendliness', None)
        if friendliness is not None:
            the_breeds = the_breeds.filter(friendliness=friendliness)

        trainability = request.query_params.get('trainability', None)
        if trainability is not None:
            the_breeds = the_breeds.filter(trainability=trainability)

        sheddingamount = request.query_params.get('sheddingamount', None)
        if sheddingamount is not None:
            the_breeds = the_breeds.filter(sheddingamount=sheddingamount)

        exerciseneeds = request.query_params.get('exerciseneeds', None)
        if exerciseneeds is not None:
            the_breeds = the_breeds.filter(exerciseneeds=exerciseneeds)

        # Finally return the list of breeds...
        serializer = BreedSerializer(the_breeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        breed_data = JSONParser().parse(request)
        breed_serial = BreedSerializer(data=breed_data, many=True)
        if breed_serial.is_valid():
            breed_serial.save()
            return Response(breed_serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(BreedSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
