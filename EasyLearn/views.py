
from django.contrib.auth.models import User
from .serializers import UserSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import *
from .serializers import *



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CourseBlockViewSet(viewsets.ModelViewSet):
    queryset = LessonBlocks.objects.all()
    serializer_class = BlocksSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, IsCourseAuthorOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


    # @action(detail=True, methods=['get', 'post', 'put'], permission_classes=[IsCourseAuthorOrReadOnly])
    # def add_block(self, request, pk=None):
    #     course = self.get_object()
    #
    #     if request.method == 'GET':
    #         blocks = LessonBlocks.objects.filter(course=course)
    #         serializer = BlocksSerializer(blocks, many=True)
    #         return Response(serializer.data)
    #
    #     if request.method == 'POST':
    #         serializer = BlocksSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save(course=course)
    #             return Response(serializer.data, status =201)
    #         else:
    #             return Response(serializer.errors, status=400)
    #
    #
    #     elif request.method == 'PUT':
    #         blocks = LessonBlocks.objects.filter(course=course)
    #         serializer = BlocksSerializer(blocks, data=request.data, many=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=400)


    # @action(detail=True, permission_classes=[IsOwner], methods=['post'])
    # def add_chapter(self, request, pk=None):
    #     course = self.get_object()
    #     serializer = ChapterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(course=course)
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)
    #
    # @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated, IsOwner])
    # def add_content(self, request, pk=None):
    #     chapter = Chapter.objects.get(pk=request.data.get('chapter_id'))
    #     serializer = ContentSerializer(data=request.data)
    #
    #
    #     if serializer.is_valid():
    #         serializer.save(chapter=chapter)
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)






class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyAccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Enrollment.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        enrolled_courses = Enrollment.objects.filter(user=user)
        authored_courses = Course.objects.filter(author=user)
        enrolled_serializer = EnrollmentSerializer(enrolled_courses, many=True)
        authored_serializer = CourseSerializer(authored_courses, many=True)
        return Response({
            'enrolled_courses': enrolled_serializer.data,
            'authored_courses': authored_serializer.data
        })
