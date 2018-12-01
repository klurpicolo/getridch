from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser('1e7ab9437dc85f54d08cf117425398ca')
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id=event.message.package_id,
                                                                     sticker_id=event.message.sticker_id)
                               )


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    if text == 'Hello':
        line_bot_api.reply_message(event.reply_token, TextSendMessage('Hi There!!'))
    elif text == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Display name: ' + profile.user_id)
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
    elif text == 'test':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Display name: ' + profile.user_id)
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Do it?', actions=[MessageAction(label='Yes', text='Yes!'),
                                                                   MessageAction(label='No', text='No!')])
        template_message = TemplateSendMessage(alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'ping':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='pong'))
    elif event.postback.data == 'datetime_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
    elif event.postback.data == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))


@handler.default()
def default(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Currently Not Support None Text Message')
    )


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage('Send Success!!'))


@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(title=event.message.title, address=event.message.address, latitude=event.message.latitude,
                            longitude=event.message.longitude
                            )
    )


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

    app.run(debug=options.debug, port=options.port)
