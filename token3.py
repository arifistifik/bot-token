# -*- coding: utf-8 -*-
from bottoken import *
from bottoken.dpktoken import Message
from bottoken.dpktoken import ContentType as Type

line = LINE()
line1 = LINE()
line2 = LINE()

oepoll = OEPoll(line)

def RECEIVE_MESSAGE(op):
    '''
        This is sample for implement BOT TOKEN in LINE group
        Invite your BOT to group, then BOT will auto accept your invitation
        Command availabe :
        > help
        > Bottoken
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
                	line.sendMessage(receiver, 'halo bosku 😃, bot token sudah aktif\nsilahkan ketik > Bottoken untuk melihat tokenmu diline 😆')
                elif text.lower() == 'bottoken':
                    line.sendMessage(receiver,"      ❇TOKEN SATU❇\n───────────────\n"+line.authToken)
                    line.sendMessage(receiver,"      ❇TOKEN DUA❇\n───────────────\n"+line1.authToken)
                    line.sendMessage(receiver,"      ❇TOKEN TIGA❇\n───────────────\n"+line2.authToken)
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
