# -*- coding: utf-8 -*-
from bottoken import *
from bottoken.dpktoken import Message
from bottoken.dpktoken import ContentType as Type

line = LINE()
oepoll = OEPoll(line)

def RECEIVE_MESSAGE(op):
    '''
        Bot ini dibuat untuk memudahkan anda 
        untuk mengambil token botline 😃
        > help
        > bottoken
    '''
    msg = op.message
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    try:
        if msg.contentType == 0:
            if msg.toType == 2:
                line.sendChatChecked(receiver, msg_id)
                contact = line.getContact(sender)
                
                if text.lower() == 'help':
                	line.sendMessage(receiver, 'halo bosku 😃, bot token sudah aktif\nsilahkan ketik > Bottoken untuk melihat tokenmu digroup line 😆')
                elif text.lower() == 'bottoken':
                    line.sendMessage(receiver,"      ❇TOKEN SATU❇\n───────────────\n"+line.authToken)
    except Exception as e:
        line.log("[RECEIVE_MESSAGE] ERROR : " + str(e))


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        group_id=op.param1
        
        line.acceptGroupInvitation(group_id)
    except Exception as e:
        line.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))


oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    oepoll.trace()
