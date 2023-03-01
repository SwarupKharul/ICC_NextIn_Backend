from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import razorpay
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import paymentRecord
from .serializers import PaymentRecordSerializer
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from users.models import Profile

razorpay_client = razorpay.Client(
    auth=(
        "rzp_test_x2pbcVHTxSvbXk",
        "aFra1Jg0fTiKW0bZkJLoEPz9",
    )
)


def pay(request):
    id = request.GET["user"]
    profile = Profile.objects.get(user=id)

    tickets = request.GET["tickets"]
    tier = request.GET["tier"]
    amount = request.GET["amount"]
    currency = "INR"
    print(profile, "jfhaskdjfhdskfhdsghrehghrjkghioer")
    razorpay_order = razorpay_client.order.create(
        {
            # "id": "order_EKwxwAgItmmXdp",
            "amount": amount,
            "currency": "INR",
            "receipt": "receipt#1",
        }
    )
    # print(razorpay_order)

    # we need to pass these details to frontend.
    context = {}
    context["razorpay_order_id"] = razorpay_order["id"]
    context["razorpay_merchant_key"] = "rzp_test_x2pbcVHTxSvbXk"
    context["razorpay_amount"] = amount
    context["currency"] = currency
    context["user"] = profile
    context["callback_url"] = "paymenthandler/"

    # Create paymentRecord
    payment_instance = paymentRecord(
        user=profile.user,
        razorpay_order_id=razorpay_order["id"],
        razorpay_payment_id="",
        razorpay_signature="",
        no_of_tickets=tickets,
        tier=tier,
        amount=amount,
        status="pending",
    )

    payment_instance.save()

    return render(request, "pay.html", context)


@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        print(request.POST)
        payment_id = request.POST.get("razorpay_payment_id", "")
        razorpay_order_id = request.POST.get("razorpay_order_id", "")
        signature = request.POST.get("razorpay_signature", "")
        params_dict = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature,
        }

        print(params_dict)

        # verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(params_dict)

        # Update paymentRecord
        payment_instance = paymentRecord.objects.filter(
            razorpay_order_id=razorpay_order_id
        ).update(
            razorpay_payment_id=payment_id,
            razorpay_signature=signature,
            status="success",
        )
        # TODO: Combine the below function with update
        payment_instance = paymentRecord.objects.get(
            razorpay_order_id=razorpay_order_id
        )

        # Add amount to user's wallet
        user = payment_instance.user
        profile = Profile.objects.get(user=user)
        profile.balance += payment_instance.amount
        profile.save()

        return HttpResponseRedirect(
            f"http://localhost:3000/MintTicket?{payment_instance.amount}"
        )
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()


@csrf_exempt
def success(request):
    return render(request, "success.html")


@api_view(["GET"])
def myTickets(request):
    tickets = paymentRecord.objects.filter(user=request.user)
    serializer = PaymentRecordSerializer(tickets, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)
