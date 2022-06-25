import requests #line:3
import json #line:4
def checkpremium (OOOO0O00OO000O0O0 ,OO0000O000O000OO0 ):#line:6
    print (OOOO0O00OO000O0O0 ,OO0000O000O000OO0 )#line:7
def do_request (O00OO00OOOO0O00OO ,OOO0000O00O0O0OOO ,OOOOO0O0OO000OOOO ,O0O0OO0O00OOOOO00 ):#line:10
        if OOOOO0O0OO000OOOO =="POST"or OOOOO0O0OO000OOOO =="post":#line:11
            if O0O0OO0O00OOOOO00 =="infinite":#line:12
                while True :#line:13
                    O0O0OO0O0OOO0000O =requests .post (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:14
                    print (O0O0OO0O0OOO0000O )#line:15
            elif isinstance (O0O0OO0O00OOOOO00 ,int ):#line:16
                for OO0OO0O00O0O000O0 in range (0 ,O0O0OO0O00OOOOO00 ):#line:17
                    O0O0OO0O0OOO0000O =requests .post (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:18
                    print (O0O0OO0O0OOO0000O )#line:19
            else :#line:20
                print ('Repetition value in config.json is not valid. Check again in line 11.')#line:21
        elif OOOOO0O0OO000OOOO =="GET"or OOOOO0O0OO000OOOO =="get":#line:22
            if O0O0OO0O00OOOOO00 =="infinite":#line:23
                while True :#line:24
                    O0O0OO0O0OOO0000O =requests .get (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:25
                    print (O0O0OO0O0OOO0000O )#line:26
            elif isinstance (O0O0OO0O00OOOOO00 ,int ):#line:27
                for OO0OO0O00O0O000O0 in range (0 ,O0O0OO0O00OOOOO00 ):#line:28
                    O0O0OO0O0OOO0000O =requests .get (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:29
                    print (O0O0OO0O0OOO0000O )#line:30
            else :#line:31
                print ('Repetition value in config.json is not valid. Check again in line 11.')#line:32
        elif OOOOO0O0OO000OOOO =="PUT"or OOOOO0O0OO000OOOO =="put":#line:33
            if O0O0OO0O00OOOOO00 =="infinite":#line:34
                while True :#line:35
                    O0O0OO0O0OOO0000O =requests .put (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:36
                    print (O0O0OO0O0OOO0000O )#line:37
            elif isinstance (O0O0OO0O00OOOOO00 ,int ):#line:38
                for OO0OO0O00O0O000O0 in range (0 ,O0O0OO0O00OOOOO00 ):#line:39
                    O0O0OO0O0OOO0000O =requests .put (O00OO00OOOO0O00OO ,data =OOO0000O00O0O0OOO ).text #line:40
                    print (O0O0OO0O0OOO0000O )#line:41
            else :#line:42
                print ('Repetition value in config.json is not valid. Check again in line 11.')#line:43
def start ():#line:45
    with open ('config.json')as OO0OOO00O0O0OO00O :#line:46
        O0O00OO0O0000O000 =json .load (OO0OOO00O0O0OO00O )#line:47
        if O0O00OO0O0000O000 ["premium"]["pack"]=="free":#line:49
            OO00OO00O00OO0OOO =O0O00OO0O0000O000 ["websiteURL"]#line:51
            O00OO0O0O00000OOO =O0O00OO0O0000O000 ["data"]#line:52
            OOO0000OO0000O00O =O0O00OO0O0000O000 ["method"]#line:53
            OOO0O0O00000OOOOO =O0O00OO0O0000O000 ["repetition"]#line:54
            do_request (OO00OO00O00OO0OOO ,O00OO0O0O00000OOO ,OOO0000OO0000O00O ,OOO0O0O00000OOOOO )#line:55
        else :#line:56
            checkpremium (O0O00OO0O0000O000 ["premium"]["premiumKEY"],O0O00OO0O0000O000 ["premium"]["method"])#line:57
start ()#line:59
