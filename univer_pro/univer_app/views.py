from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAdminUser
import random
import string
from .models import (
    AboutUniversity, AboutCollege, Lyceum, Numberstudents, VerificationCode, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, DSC, Сontacts, OtherLinks, Followus, VerificationCode, Numberstudents
)

from .serializers import (
    AboutUniversitySerializer, AboutCollegeSerializer,
    EventSerializer, EventImageSerializer, LibrarySerializer, JobTitleSerializer,
    LanguageKnowledgeSerializer, LaborActivitySerializer, ManagementSerializer, StructureSerializer,
    RecruitmentSerializer, DocumentSerializer, DirectionSerializer, DSCSerializer, OtherLinksSerializer,
    FollowusSerializer, СontactsSerializer, LibrarySerializer, VerificationCodeSerializer, LyceumSerializer
)


class AboutUniversityViewSet(viewsets.ModelViewSet):
    queryset = AboutUniversity.objects.all()
    serializer_class = AboutUniversitySerializer
    permission_classes = [IsAdminUser]


class AboutCollegeViewSet(viewsets.ModelViewSet):
    queryset = AboutCollege.objects.all()
    serializer_class = AboutCollegeSerializer
    permission_classes = [IsAdminUser]


class LyceumViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LyceumSerializer
    permission_classes = [IsAdminUser]


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class VerificationViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def verify_number(self, request):
        number = request.data.get('number')
        email = request.data.get('email')
        try:
            student = Numberstudents.objects.get(number=number)
            verification_code = ''.join(random.choices(string.digits, k=5))
            VerificationCode.objects.create(number=number, email=email, verification_code=verification_code)

            send_mail(
                'Verification Code',
                f'Your verification code is {verification_code}',
                'admin@library.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'Verification code sent to email'}, status=status.HTTP_200_OK)
        except Numberstudents.DoesNotExist:
            return Response({'detail': 'Number not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def verify_code(self, request):
        number = request.data.get('number')
        code = request.data.get('code')
        try:
            verification = VerificationCode.objects.get(number=number, verification_code=code)
            if verification:
                return Response({'detail': 'Verification successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        except VerificationCode.DoesNotExist:
            return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def resend_code(self, request):
        number = request.data.get('number')
        email = request.data.get('email')
        try:
            verification = VerificationCode.objects.get(number=number, email=email)
            verification_code = ''.join(random.choices(string.digits, k=5))
            verification.verification_code = verification_code
            verification.save()

            send_mail(
                'Verification Code',
                f'Your new verification code is {verification_code}',
                'admin@library.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'New verification code sent to email'}, status=status.HTTP_200_OK)
        except VerificationCode.DoesNotExist:
            return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventImageViewSet(viewsets.ModelViewSet):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class VerificationViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def verify_number(self, request):
        number = request.data.get('number')
        email = request.data.get('email')
        try:
            student = Numberstudents.objects.get(number=number)
            verification_code = ''.join(random.choices(string.digits, k=5))
            VerificationCode.objects.create(number=number, email=email, verification_code=verification_code)

            send_mail(
                'Verification Code',
                f'Your verification code is {verification_code}',
                'admin@library.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'Verification code sent to email'}, status=status.HTTP_200_OK)
        except Numberstudents.DoesNotExist:
            return Response({'detail': 'Number not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def verify_code(self, request):
        number = request.data.get('number')
        code = request.data.get('code')
        try:
            verification = VerificationCode.objects.get(number=number, verification_code=code)
            if verification:
                return Response({'detail': 'Verification successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid code'}, status=status.HTTP_400_BAD_REQUEST)
        except VerificationCode.DoesNotExist:
            return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def resend_code(self, request):
        number = request.data.get('number')
        email = request.data.get('email')
        try:
            verification = VerificationCode.objects.get(number=number, email=email)
            verification_code = ''.join(random.choices(string.digits, k=5))
            verification.verification_code = verification_code
            verification.save()

            send_mail(
                'Verification Code',
                f'Your new verification code is {verification_code}',
                'admin@library.com',
                [email],
                fail_silently=False,
            )

            return Response({'detail': 'New verification code sent to email'}, status=status.HTTP_200_OK)
        except VerificationCode.DoesNotExist:
            return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class LanguageKnowledgeViewSet(viewsets.ModelViewSet):
    queryset = LanguageKnowledge.objects.all()
    serializer_class = LanguageKnowledgeSerializer


class LaborActivityViewSet(viewsets.ModelViewSet):
    queryset = LaborActivity.objects.all()
    serializer_class = LaborActivitySerializer


class ManagementViewSet(viewsets.ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class StructureViewSet(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


'''Об университете бүттү '''
from .models import Numbers, Aboutthecollege, Requirem, Documentation, DSC
from .serializers import NumbersSerializer, AboutthecollegeSerializer, RequiremSerializer, DocumentationSerializer, \
    DSCSerializer


class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer


class AboutthecollegeViewSet(viewsets.ModelViewSet):
    queryset = Aboutthecollege.objects.all()
    serializer_class = AboutthecollegeSerializer


class RequiremViewSet(viewsets.ModelViewSet):
    queryset = Requirem.objects.all()
    serializer_class = RequiremSerializer


class DocumentationViewSet(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer


class DSCViewSet(viewsets.ModelViewSet):
    queryset = DSC.objects.all()
    serializer_class = DSCSerializer


class СontactsViewSetr(viewsets.ModelViewSet):
    queryset = Сontacts.objects.all()
    serializer_class = СontactsSerializer


class OtherLinksViewSet(viewsets.ModelViewSet):
    queryset = OtherLinks.objects.all()
    serializer_class = OtherLinksSerializer


class FollowusViewSet(viewsets.ModelViewSet):
    queryset = Followus.objects.all()
    serializer_class = FollowusSerializer


from .models import Link, News
from .serializers import LinkSerializer, NewsSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
