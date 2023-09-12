# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Person
from .serializers import PersonSerializer


################### PERSON API #########################

class PersonApiView(APIView):


    # 1. List all
    def get(self, request):

        # persons = Person.objects.all()
        persons = Person.objects.all().order_by('id')
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # CREATE A PERSON
    def post(self, request):

        try:
            name = request.data.get('name')
            person = Person.objects.get(name=name)
            if person:
                return Response(
                    {"res": "User with name already exist, please pick a different name."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Person.DoesNotExist:
            serializer = PersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)




class PersonIdApiView(APIView):

    # calling function by id
    def get_person_by_id(self, person_id):
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return None

    # calling function by name
    def get_person_by_name(self, person_id):
        try:
            return Person.objects.get(name=person_id)
        except Person.DoesNotExist:
            return None


    # GET PERSON PER NAME ID
    def get(self, request, person_id):

        person = self.get_person_by_name(person_id)
        if not person:
            return Response(
                {"res": "Person with person_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # UPDATE A PARTICULAR PERSON
    def put(self, request, person_id):

        person = self.get_person_by_id(person_id)
        if not person:
            return Response(
                {"res": "Person with person_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PersonSerializer(instance=person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # DELETE A PARTICULAR PERSON
    def delete(self, request, person_id):

        person = self.get_person_by_id(person_id)
        if not person:
            return Response(
                {"res": "Person with person_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        person.delete()
        return Response(
            {"res": "Person deleted!"},
            status=status.HTTP_200_OK
        )
