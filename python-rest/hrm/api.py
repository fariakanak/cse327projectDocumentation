from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class UserList(APIView):
    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_user(self, email_id):
        try:
            model = User.objects.get(id=email_id)
            return model
        except User.DoesNotExist:
            return

    def get(self, request, email_id):
       if not self.get_user(email_id):
        return Response(f'User with id= {email_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
       serializer = UserSerializer(self.get_user(email_id))
       return Response(serializer.data)

    def put(self, request, email_id):
        if not self.get_user(email_id):
            return Response(f'User with id= {email_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(email_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, email_id):
        if not self.get_user(email_id):
            return Response(f'User with id= {email_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(email_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeptList(APIView):
    def get(self, request):
        model = Dept.objects.all()
        serializer = DeptSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeptDetail(APIView):
    def get_dept(self, dept_id):
        try:
            model = Dept.objects.get(id=dept_id)
            return model
        except Dept.DoesNotExist:
            return

    def get(self, request, dept_id):
        if not self.get_dept(dept_id):
            return Response(f'Department with id= {dept_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = DeptSerializer(self.get_dept(dept_id))
        return Response(serializer.data)

    def put(self, request, dept_id):
        if not self.get_dept(dept_id):
            return Response(f'Department with id= {dept_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = DeptSerializer(self.get_dept(dept_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, dept_id):
        if not self.get_dept(dept_id):
            return Response(f'Department with id= {dept_id} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_dept(dept_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentList(APIView):
    def get(self, request):
        model = Document.objects.all()
        serializer = DocumentSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentDetail(APIView):
    def get_document(self, record_no):
        try:
            model = Document.objects.get(id=record_no)
            return model
        except Document.DoesNotExist:
            return

    def get(self, request, record_no):
        if not self.get_document(record_no):
            return Response(f'Document with id= {record_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(self.get_document(record_no))
        return Response(serializer.data)

    def put(self, request, record_no):
       if not self.get_document(record_no):
            return Response(f'Document with id= {record_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
       serializer = DocumentSerializer(self.get_document(record_no), data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, record_no):
        if not self.get_document(record_no):
            return Response(f'Document with id= {record_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_document(record_no)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamList(APIView):
    def get(self, request):
        model = Team.objects.all()
        serializer = TeamSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    def get_team(self, team_no):
        try:
            model = Team.objects.get(id=team_no)
            return model
        except Team.DoesNotExist:
            return

    def get(self, request, team_no):
        if not self.get_team(team_no):
            Response(f'Team with id= {team_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(self.get_team(team_no))
        return Response(serializer.data)

    def put(self, request, team_no):
        if not self.get_team(team_no):
            Response(f'Team with id= {team_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(self.get_team(team_no), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, team_no):
        if not self.get_team(team_no):
            Response(f'Team with id= {team_no} does not exist in the database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_team(team_no)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
