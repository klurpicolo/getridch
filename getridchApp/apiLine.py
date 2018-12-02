from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

# Initial Parameter
channel_access_token = 'FM6Q6U/BAWJlaQMzPOneNK6QT0Di9qZ93VtKt4w6NnnX1U6/1fqduzsoAjW3/kpnVrLj4GGobh/XsVqZaccp+Ra44QRKxrL6m8fFFDhUOpGvDKFu5P4Qf1c1I0qe6p9FAA7Mno9YPr510Sfh3B8xxwdB04t89/1O/w1cDnyilFU='
# Create Line Bot Instance
lineBotApi = LineBotApi(channel_access_token)


def line_muti_post_test():
    well = 'U580968c5793b7a7027781b665ba4b2ac'
    klur = 'U3a5157dd43443a815618e786b339fcfb'
    lineBotApi.multicast([well, klur], TextSendMessage(text='Hello World! Klur , Well'))
    # lineBotApi.multicast(['to1', 'to2'], TextSendMessage(text='Hello World!'))


def line_to_post_test():
    lineBotApi = LineBotApi(channel_access_token)
    to = 'U3a5157dd43443a815618e786b339fcfb'
    lineBotApi.push_message(to, TextSendMessage(text='Hello World! from python(Klur)'))



if __name__ == '__main__':
    line_muti_post_test()
