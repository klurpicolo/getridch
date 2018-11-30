from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('FM6Q6U/BAWJlaQMzPOneNK6QT0Di9qZ93VtKt4w6NnnX1U6/1fqduzsoAjW3/kpnVrLj4GGobh/XsVqZaccp+Ra44QRKxrL6m8fFFDhUOpGvDKFu5P4Qf1c1I0qe6p9FAA7Mno9YPr510Sfh3B8xxwdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('1e7ab9437dc85f54d08cf117425398ca')


@csrf_exempt
def callback(request):
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
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
