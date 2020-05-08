from django.shortcuts import render
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        # retrieve incoming message
        incoming_msg = request.POST['Body'].lower()

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        # msg.body('My response')
        # msg.medial('https://example.com/path/image.jpg')

        if incoming_msg == 'hello':
            response = "*Hi! Mir actually made a working bot, wooohooo*"
            msg.body(response)

        return HttpResponse(str(resp))
