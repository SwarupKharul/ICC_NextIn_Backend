from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Avatar
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, AvatarSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


class UserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerProfileOrReadOnly]

    def get_object(self):
        return self.request.user


@api_view(["POST"])
def createAvatar(request):
    data = request.data
    print(data)
    serializer = AvatarSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, safe=False)


@api_view(["GET"])
def getAvatar(request):
    profile = Profile.objects.get(user=request.user)
    avatar = Avatar.objects.get(profile=profile)
    serializer = AvatarSerializer(avatar)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
def reduceBalance(request):
    reduce_amount = request.data["reduce_amount"]
    profile = Profile.objects.get(user=request.user)
    profile.balance -= reduce_amount
    if profile.balance < 0:
        # Send message Balance to low and throw 403 error PermissionDenied
        return JsonResponse({"message": "Balance to low"}, status=403, safe=False)
    profile.save()
    return JsonResponse({"balance": profile.balance}, safe=False)
