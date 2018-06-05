# -*- coding: utf-8 -*-
from SLACKBOT import *
from datetime import datetime
from time import sleep
# EDITOR: GALANK
# VERSION: PYTHON 3
# MODE: PUBLICBOT
from bs4 import BeautifulSoup
from gtts import gTTS
import time, random, sys, json, codecs,  threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast
#=============================================================#
botStart = time.time()

Galank = LineClient()
Galank.log("Auth Token : " + str(Galank.authToken))
channel = LineChannel(Galank)
Galank.log("Channel Access Token : " + str(channel.channelAccessToken))

GalankProfile = Galank.getProfile()
GalankSettings = Galank.getSettings()
GalankPoll = LinePoll(Galank)
GalankMID = Galank.profile.mid
contact = Galank.getProfile()
backup = Galank.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
cl = Galank

settings = {
    "autoAdd":False,
    "autoJoin":False,
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = GalankProfile.displayName
myProfile["statusMessage"] = GalankProfile.statusMessage
myProfile["pictureStatus"] = GalankProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = Galank.getProfile().mid
    if myid in nm:    
        nm.remove(myid)
    for mm in nm:
        akh = akh + 6
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 7
        akh = akh + 1
        bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
    try:
        Galank.sendMessage(msg.to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)
#===============SB ONLY====================
#===================================#
def help():
    helpMessage = "╭══════╬╬═══════╮\n   PUBLIC BOTS\n╰══════╬╬═══════╯" + "\n" + \
                  "╠➣NAMA BOT" + GalankProfile.displayName + "\n" + \
                  "╠➣Help" + "\n" + \
                  "╠➣Set" + "\n" + \
                  "╠➣Me" + "\n" + \
                  "╠➣Add" + "\n" + \
                  "╠➣Creator" + "\n" + \
                  "╠➣Restart" + "\n" + \
                  "╠➣Speed" + "\n" + \
                  "╠➣Runtime" + "\n" + \
                  "╠➣Mymid" + "\n" + \
                  "╠➣Myname" + "\n" + \
                  "╠➣Mybio" + "\n" + \
                  "╠➣Mypicture" + "\n" + \
                  "╠➣Myvideo" + "\n" + \
                  "╠➣Mycover" + "\n" + \
                  "╠➣Getmid @" + "\n" + \
                  "╠➣Getbio @" + "\n" + \
                  "╠➣Getname @" + "\n" + \
                  "╠➣Getpicture @" + "\n" + \
                  "╠➣Getvideo @" + "\n" + \
                  "╠➣Getcontact @" + "\n" + \
                  "╠➣Getcover @" + "\n" + \
                  "╠➣Getprofile @" + "\n" + \
                  "╠══════════════" + "\n" + \
                  "╠➣Cloneprofile @" + "\n" + \
                  "╠➣Restoreprofile" + "\n" + \
                  "╠➣Cekmid *mid" + "\n" + \
                  "╠➣Friendlist" + "\n" + \
                  "╠➣Blocklist" + "\n" + \
                  "╠➣Mention" + "\n" + \
                  "╠➣Lurk:on" + "\n" + \
                  "╠➣Lurk:off" + "\n" + \
                  "╠➣Lurk:rest" + "\n" + \
                  "╠➣Lurkers" + "\n" + \
                  "╰══════╬╬═══════╯\n╭══════╬╬═══════╮\n    ●TΣΔM SLΔCҜβΩT●\nline.me/ti/p/~fuck.you__"
    return helpMessage
while True:
    try:
        ops=GalankPoll.singleTrace(count=50)
        
        for op in ops:
            if op.type == 5:
                Galank.findAndAddContactsByMid(op.param1)
                xname = Galank.getContact(op.param1).displayName
                Galank.sendMessage(op.param1, "Hay " + xname + "\nBOT PUBLIC: ●SLΔCҜβΩT●\n\nOWNER BOT\nhttp://line.me/ti/p/~fuck.you__")
            if op.type == 13:
                print ("[NOTIFIED_INVITE_INTO_GROUP]")
                if GalankMID in op.param3:
                    G = Galank.getGroup(op.param1)
                    Galank.acceptGroupInvitation(op.param1)
            if op.type == 26: ## JIKA INI DI GANTI KE 25 JADI SELFBOT ONLY
                print ("[ 26 ] READ MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            Galank.sendChatChecked(receiver, msg_id)
                            contact = Galank.getContact(sender)
                            if text.lower() == "help":
                               helpMessage = help()
                               Galank.sendMessage(msg.to, str(helpMessage))
                               Galank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            if text.lower() == 'speed':
                                start = time.time()
                                Galank.sendMessage(receiver, "Sabar sayang..")
                                elapsed_time = time.time() - start
                                Galank.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif text.lower() == 'restart':
                                Galank.sendMessage(msg.to, "Bot Program has been restarted")
                                restartBot()
                            elif text.lower() == 'runtime':
                            	eltime = time.time() - botStart
                            	timerun = "Bot has been active "+waktu(eltime)
                            	Galank.sendMessage(msg.to,timerun)
#==============================================================================#
                            elif text.lower() == 'me':
                                Galank.sendContact(msg.to, GalankMID)
                                Galank.sendMessage(msg.to,"Ini kontak Aku Beb")
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                Galank.sendMessage(msg.to,"Ini kontakmu Beb")
                            elif text.lower() == 'add':		
                                Galank.sendMessage(msg.to,"╭══════╬╬═══════╮")
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': 'u78643d09e42a36836a17cc918963a8b7'}, contentType=13)
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': 'u290d3072b043ff4796a9a91f145931e0'}, contentType=13)
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': 'uf8d981e0bc9184560956ced35c4372be'}, contentType=13)
                                Galank.sendMessage(msg.to,"╰══════╬╬═══════╯")
                            elif text.lower() == 'creator':		
                                Galank.sendMessage(msg.to,"╭══════╬╬═══════╮")
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': 'u78643d09e42a36836a17cc918963a8b7'}, contentType=13)
                                Galank.sendMessage(msg.to,"╰══════╬╬═══════╯")
                            elif text.lower() == 'mymid':
                                Galank.sendMessage(msg.to, sender)
                                Galank.sendMessage(msg.to,"Ini mid kamu beb")
                            elif text.lower() == 'myname':
                                me = Galank.getContact(GalankMID)
                                me1 = Galank.getContact(sender)
                                Galank.sendMessage(msg.to,"nama ku\n" + me.displayName + "\nnama kamu\n" + me1.displayName)
                            elif text.lower() == 'mybio':
                                me = Galank.getContact(sender)
                                Galank.sendMessage(msg.to,"[Status kamu]\n" + me.statusMessage)
                            elif text.lower() == 'mypicture':
                                h = Galank.getContact(GalankMID)
                                path = "http://dl.profile.line.naver.jp/" + h.pictureStatus
                                Galank.sendImageWithURL(msg.to, str(path))
                                Galank.sendMessage(msg.to,"Ini foto profile saya")
                                me1 = Galank.getContact(sender)
                                path = "http://dl.profile.line-cdn.net/" + me1.pictureStatus
                                Galank.sendImageWithURL(msg.to, str(path))
                                Galank.sendMessage(msg.to,"Ini foto profile kamu")
                            elif text.lower() == 'myvideo':
                                me = Galank.getContact(sender)
                                Galank.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = Galank.getContact(GalankMID)
                                cover = channel.getProfileCoverURL(GalankMID)    
                                Galank.sendImageWithURL(msg.to, cover)
                                Galank.sendMessage(msg.to,"Ini foto branda saya")
                                me1 = Galank.getContact(sender)
                                cover1 = channel.getProfileCoverURL(sender)    
                                Galank.sendImageWithURL(msg.to, cover1)
                                Galank.sendMessage(msg.to,"Ini foto branda kamu")
                            elif 'getmid' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}" + ls
                                    Galank.sendMessage(msg.to, str(ret_))
                            elif 'getpicture' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line.naver.jp/" + Galank.getContact(ls).pictureStatus
                                        Galank.sendImageWithURL(msg.to, str(path))
                            elif 'getcover' in text.lower():
                                if channel != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = channel.getProfileCoverURL(ls)
                                            Galank.sendImageWithURL(msg.to, str(path))
                            elif 'getname' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = Galank.getContact(ls)
                                        Galank.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            elif 'getbio' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = Galank.getContact(ls)
                                        Galank.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            elif 'getprofile' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = Galank.getContact(ls)
                                        cu = channel.getProfileCoverURL(ls)
                                        path = str(cu)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        Galank.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                        Galank.sendImageWithURL(msg.to,image)
                                        Galank.sendImageWithURL(msg.to,path)
                            elif 'getcontact' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = Galank.getContact(ls)
                                        mi_d = contact.mid
                                        Galank.sendContact(msg.to, mi_d)
                            elif 'cloneprofile' in text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        Galank.cloneContactProfile(contact)
                                        Galank.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        prank.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    Galank.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    Galank.updateProfile(clientProfile)
                                    Galank.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    Galank.sendMessage(msg.to, "Gagal restore profile")
                            elif 'cekmid' in text.lower():
                                separate = text.split(" ")
                                saya = text.replace(separate[0] + " ","")
                                Galank.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)
                                
                            elif text.lower() == 'friendlist':
                                contactlist = Galank.getAllContactIds()
                                kontak = Galank.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                Galank.sendMessage(msg.to, msgs)
                                
                            elif text.lower() == 'blocklist':
                                blockedlist = Galank.getBlockedContactIds()
                                kontak = Galank.getContacts(blockedlist)
                                num=1
                                msgs="═════════List Blocked═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                                Galank.sendMessage(msg.to, msgs)
                            elif text.lower() == 'mention':
                                group = Galank.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    mention(msg.to, nm5)             
                                Galank.sendMessage(receiver, "Members :"+str(jml))
                            elif text.lower() == 'lurk:on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            prank.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        Galank.sendMessage(msg.to, "Set reading point:\n" + readTime)
                                        
                            elif text.lower() == 'lurk:off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    Galank.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    Galank.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                
                            elif text.lower() == 'lurk:rest':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    Galank.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    Galank.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif text.lower() == 'lurkers':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        prank.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = prank.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        Galank.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    Galank.sendMessage(receiver,"Lurking has not been set.")
                except Exception as e:
                    Galank.log("[SEND_MESSAGE] ERROR : " + str(e))
                    
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass
            GalankPoll.setRevision(op.revision)
            
    except Exception as e:
        Galank.log("[SINGLE_TRACE] ERROR : " + str(e))
