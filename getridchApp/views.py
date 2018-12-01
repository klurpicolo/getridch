from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser('1e7ab9437dc85f54d08cf117425398ca')


@csrf_exempt
def callback(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    text = event.message.text
                    if text == 'Hello':
                        line_bot_api.reply_message(event.reply_token, TextSendMessage('Hi There!!'))
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
                if isinstance(event.message, ImageMessage):
                    line_bot_api.reply_message(event.reply_token, TextSendMessage('Send Success!!'))

        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest(status=400)
