import json   
import os   
import re   
import tkinter as tk   
import customtkinter as CTk   
import requests   
from CTkMessagebox import CTkMessagebox   
from PIL import Image   
USERS_PATH =os .path .join (os .path .dirname (os .path .abspath (__file__ )),'users.json')  
class O001ll00O0 (CTk .CTkEntry):  
    def __init__ (OO0OOO0O000O0OOOO ,master =None ,is_protected =True ,buffer_size =10 ,**O000OOOO000OOO0O0 ):  
        super ().__init__ (master ,**O000OOOO000OOO0O0 )  
        OO0OOO0O000O0OOOO .configure (width =250 ,height =50 )  
        OO0OOO0O000O0OOOO .buffer =['']*buffer_size   
        OO0OOO0O000O0OOOO .buffer_size =buffer_size   
        OO0OOO0O000O0OOOO .is_protected =is_protected   
        OO0OOO0O000O0OOOO .bind ('<KeyRelease>', OO0OOO0O000O0OOOO .o00O0lll1llII0o)  
    def o00O0lll1llII0o (OO0OO00O00000O00O, O0O0OO0O0OOO0OOOO)->None :  
        O0OOOO000OO0O000O =OO0OO00O00000O00O .get ()  
        if OO0OO00O00000O00O .is_protected and len (O0OOOO000OO0O000O )>OO0OO00O00000O00O .buffer_size :  
            OO0OO00O00000O00O .delete (OO0OO00O00000O00O .buffer_size ,CTk .END )  
            OO0OO00O00000O00O .o00O0lll1llII0o (O0O0OO0O0OOO0OOOO)  
            return   
        O0OOOO000OO0O000O =list (O0OOOO000OO0O000O )  
        OO0OO00O00000O00O .buffer =['']*OO0OO00O00000O00O .buffer_size   
        for O000000O00OO0O0O0 in range (len (O0OOOO000OO0O000O )):  
            OO0OO00O00000O00O .buffer [O000000O00OO0O0O0 ]=O0OOOO000OO0O000O [O000000O00OO0O0O0 ]  
    def OOOO0000OllIIl0O (O0O0OOOOO0O0000O0)->str :  
        return ''.join (O0O0OOOOO0O0000O0 .buffer )  
def OO000OOO000lII0OI ()->dict :  
    try :  
        with open (USERS_PATH ,'r')as OOOOOOO00OOOOO0O0 :  
            return json .load (OOOOOOO00OOOOO0O0 )  
    except FileNotFoundError :  
        return {}  
def IIIllllIIIOOO0O (OOO00O0O0OO0OO00O :str, O00O00OO0OOO000O0 :str)->dict :  
    OOO00O0000OOOO00O =OO000OOO000lII0OI ()  
    if OOO00O0O0OO0OO00O in OOO00O0000OOOO00O and OOO00O0000OOOO00O [OOO00O0O0OO0OO00O ]['password']==O00O00OO0OOO000O0 :  
        return OOO00O0000OOOO00O [OOO00O0O0OO0OO00O ]  
    else :  
        return None   
def IIIIOOO000OOOlI (OOOOOOO00OOO00OO0 :O001ll00O0, OO00O00OOOOOO0O0O :O001ll00O0, OO00O00000OO00000 :CTk .CTk, O0O0OOO00O00OOOO0 :bool)->None :  
    OO0O00O0OO000O000 =OOOOOOO00OOO00OO0 .OOOO0000OllIIl0O ()  
    O00O00OO0O0OO0000 =OO00O00OOOOOO0O0O .OOOO0000OllIIl0O ()  
    OO0OO0000OO00OO00 =IIIllllIIIOOO0O (OO0O00O0OO000O000, O00O00OO0O0OO0000)  
    if OO0OO0000OO00OO00 :  
        if O0O0OOO00O00OOOO0 :  
            if OO0OO0000OO00OO00 ['role']=='admin':  
                OlllllllIIIII0OOO (OO0O00O0OO000O000, OO00O00000OO00000, O0O0OOO00O00OOOO0)  
            else :  
                IIIIIlll0O0O0O (OO0O00O0OO000O000, OO00O00000OO00000, O0O0OOO00O00OOOO0)  
        else :  
            OlllllllIIIII0OOO (OO0O00O0OO000O000, OO00O00000OO00000, O0O0OOO00O00OOOO0)  
            IIIIIlll0O0O0O (OO0O00O0OO000O000, OO00O00000OO00000, O0O0OOO00O00OOOO0)  
        OO00O00000OO00000 .withdraw ()  
    else :  
        CTkMessagebox (title ="Error",message ="Invalid username or password",icon ="cancel")  
def OOOOO0OOOOO0OOOOOIlI (OO00OOO0O0O0O000O :CTk .CTk, O00O00OOOOO00OO0O :bool):  
    OO00OOO0O0O0O000O .destroy ()  
    IlIlIlIlIl (O00O00OOOOO00OO0O)  
def IIIIIlll0O0O0O (O0OO0OOO00O0O0OOO :str, O000OO0OO00OOOO00 :CTk .CTk, OOOOO00OOOOOO0O0O :bool)->None :  
    OO0O00OOO000O000O =CTk .CTkToplevel (O000OO0OO00OOOO00 )  
    OO0O00OOO000O000O .title ('Account')  
    OO0O00OOO000O000O .geometry ("700x470")  
    O0OO00000OOOO00OO =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 ))  
    O0OO0000O0OOOOOOO =CTk .CTkLabel (master =OO0O00OOO000O000O ,text ="",image =O0OO00000OOOO00OO )  
    O0OO0000O0OOOOOOO .grid (row =0 ,column =1 ,rowspan =2 )  
    O00000O0OO000O0OO =CTk .CTkLabel (master =OO0O00OOO000O000O ,text =f"WELCOME, {O0OO0OOO00O0O0OOO}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 ))  
    O00000O0OO000O0OO .grid (row =0 ,column =0 )  
    OO0O0O0OOOOO0O0O0 =CTk .CTkFrame (master =OO0O00OOO000O000O ,width =400 ,height =400 ,fg_color ="transparent")  
    OO0O0O0OOOOO0O0O0 .grid (row =1 ,column =0 ,padx =25 )  
    O000OO00OOOO0000O =CTk .CTkLabel (master =OO0O0O0OOOOO0O0O0 ,text ="Name",font =("Arial",17 ))  
    O000OO00OOOO0000O .grid (row =0 ,column =0 )  
    O00O0O00OO000O00O =O001ll00O0 (OO0O0O0OOOOO0O0O0, OOOOO00OOOOOO0O0O)  
    O00O0O00OO000O00O .grid (row =0 ,column =1 ,columnspan =2 )  
    OO0O000O0000000OO =CTk .CTkLabel (master =OO0O0O0OOOOO0O0O0 ,text ="Size",font =("Arial",17 ))  
    OO0O000O0000000OO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 )  
    O000O00000OOOOO0O =O001ll00O0 (OO0O0O0OOOOO0O0O0, OOOOO00OOOOOO0O0O)  
    O000O00000OOOOO0O .grid (row =1 ,column =1 ,columnspan =2 )  
    O0OOO0OO000O00O0O =CTk .CTkButton (master =OO0O0O0OOOOO0O0O0, text ="GO", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :IIIllllOlOlO00 (O00O0O00OO000O00O, O000O00000OOOOO0O, OO0O0O0OOOOO0O0O0, OOOOO00OOOOOO0O0O))  
    O0OOO0OO000O00O0O .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 )  
    OO0O00OOO000O000O .protocol ("WM_DELETE_WINDOW", lambda :OOOOO0OOOOO0OOOOOIlI (O000OO0OO00OOOO00, OOOOO00OOOOOO0O0O))  
def IIIllllOlOlO00 (O0O00O000OO00O0O0 :O001ll00O0, OOOOOO00O00000OO0 :O001ll00O0, O0O0OOOOO00O00000 :CTk .CTkToplevel, OOOOOOOOOO000O0O0 :bool)->None :  
    if OOOOOOOOOO000O0O0 :  
        OOO000OOO00O0O0O0 =O0O0OOOOO00O00000 .children ['!ctkbutton']  
        OOO000OOO00O0O0O0 .configure (state =CTk .DISABLED )  
        O0O0OOOOO00O00000 .after (5000 ,lambda :OOO000OOO00O0O0O0 .configure (state =tk .NORMAL ))  
    OO0OO00OO0O00OO0O =O0O00O000OO00O0O0 .OOOO0000OllIIl0O ()  
    OOO0O00OOO0OO00O0 =OOOOOO00O00000OO0 .OOOO0000OllIIl0O ()  
    if OOOOOOOOOO000O0O0 :  
        if not OOOOOOOO0I (OO0OO00OO0O00OO0O , OOO0O00OOO0OO00O0):  
            CTkMessagebox (title ="Error",message ="Invalid data",icon ="cancel")  
            return   
    O0OO00OO00O00OO0O =OOOOOIIIlll0 (OO0OO00OO0O00OO0O, OOO0O00OOO0OO00O0)  
    OIIIlIIIlIII0 (O0OO00OO00O00OO0O, O0O0OOOOO00O00000)  
def OOOOOOOO0I (O000OO00OO00OOO0O :str, O0OO0O0000OOO0O0O :str)->bool :  
    try :  
        O00OOOO00OO0O0000 =len (O000OO00OO00OOO0O )  
        O0O0O000O0O00OO0O =int (O0OO0O0000OOO0O0O )  
        if (15 <=O00OOOO00OO0O0000 or O00OOOO00OO0O0000 <=1 )or (70 <O0O0O000O0O00OO0O or O0O0O000O0O00OO0O <=20 )or not (re .fullmatch ("^[A-z '-]+$",O000OO00OO00OOO0O )):  
            return False   
        else :  
            return True   
    except ValueError :  
        return False   
def OOOOOIIIlll0 (O0000OO0OO0OO0O00 :str, O0O00OOO0OOOO0000 :str)->str :  
    O00O00OO0OO000000 =f'https://api.genderize.io?name={O0000OO0OO0OO0O00}'  
    O00OOO0OOOOO0OO00 =requests .get (O00O00OO0OO000000 )  
    O000OOO0OO00OO0O0 =O00OOO0OOOOO0OO00 .json ()  
    O00O00OO0OO000000 =f'https://catfact.ninja/fact?max_length={O0O00OOO0OOOO0000}'  
    OOOOOO0OOO00O00O0 =requests .get (O00O00OO0OO000000 )  
    OO000O00O0O0OOO0O =OOOOOO0OOO00O00O0 .json ()  
    if O00OOO0OOOOO0OO00 .status_code ==200 and OOOOOO0OOO00O00O0 .status_code ==200 :  
        OOOOO0000OO0OO0OO =O000OOO0OO00OO0O0 ['gender']  
        OOOOOOO00O00O0OOO =OO000O00O0O0OOO0O ['fact']  
        return f'Your name\'s gender is {OOOOO0000OO0OO0OO}.\n Your fact about cats is:\n {OOOOOOO00O00O0OOO}'  
    raise Exception ('Error while getting api')  
def OIIIlIIIlIII0 (O0O0OOO0OOOO00O00 :str, O0O0000OOO000O0O0 :CTk .CTkToplevel)->None :  
    O00OO0OOOOO0OO0OO =O0O0000OOO000O0O0 .winfo_children ()  
    if O00OO0OOOOO0OO0OO :  
        OOOOOOO0OO00O0OOO =O00OO0OOOOO0OO0OO [-1 ]  
        if isinstance (OOOOOOO0OO00O0OOO ,CTk .CTkLabel ):  
            OOOOOOO0OO00O0OOO .destroy ()  
    O000O0O0O0OOO00O0 =CTk .CTkLabel (O0O0000OOO000O0O0 ,text =O0O0OOO0OOOO00O00 )  
    O000O0O0O0OOO00O0 .grid (row =3 ,column =0 ,pady =5 ,columnspan =3 )  
def OlllllllIIIII0OOO (OO0OO00O0O00000OO :str, OO0O00O0OOOO000OO :CTk .CTk, O0OOO000OO00OOO0O :bool)->None :  
    OO0OOO00OO00OO00O =CTk .CTkToplevel (OO0O00O0OOOO000OO )  
    OO0OOO00OO00OO00O .title ('Account')  
    OO0OOO00OO00OO00O .geometry ("700x470")  
    O00O0OOO00OO000O0 =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 ))  
    O0OO0OOO0OOOOO0OO =CTk .CTkLabel (master =OO0OOO00OO00OO00O ,text ="",image =O00O0OOO00OO000O0 )  
    O0OO0OOO0OOOOO0OO .grid (row =0 ,column =0 ,rowspan =2 )  
    O00O000O0OO00O0O0 =CTk .CTkLabel (master =OO0OOO00OO00OO00O ,text =f"WELCOME, {OO0OO00O0O00000OO}.\n You can add user",font =("Arial",20 ))  
    O00O000O0OO00O0O0 .grid (row =0 ,column =1 ,columnspan =3 )  
    OOOO0000OOO000O0O =CTk .CTkFrame (master =OO0OOO00OO00OO00O ,width =400 ,height =400 ,fg_color ="transparent")  
    OOOO0000OOO000O0O .grid (row =1 ,column =1 ,padx =25 ,pady =10 )  
    OOOO0OOOO0O0O00O0 =CTk .CTkLabel (master =OOOO0000OOO000O0O ,text ="Username",font =("Arial",17 ))  
    OOOO0OOOO0O0O00O0 .grid (row =0 ,column =0 )  
    O00O00OOO0OOO000O =O001ll00O0 (OOOO0000OOO000O0O, O0OOO000OO00OOO0O)  
    O00O00OOO0OOO000O .grid (row =0 ,column =1 ,columnspan =2 )  
    OOOO0OO0OOO00O0OO =CTk .CTkLabel (master =OOOO0000OOO000O0O ,text ="Password",font =("Arial",17 ))  
    OOOO0OO0OOO00O0OO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 )  
    OO00000OO0000OO00 =O001ll00O0 (OOOO0000OOO000O0O, O0OOO000OO00OOO0O, show ='*')  
    OO00000OO0000OO00 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 )  
    O00OO0O0OO00OO000 =CTk .CTkButton (master =OOOO0000OOO000O0O, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :OOOIIIIlll000O (O00O00OOO0OOO000O .OOOO0000OllIIl0O (), OO00000OO0000OO00 .OOOO0000OllIIl0O (), O0OOO000OO00OOO0O))  
    O00OO0O0OO00OO000 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 )  
    OO0OOO00OO00OO00O .protocol ("WM_DELETE_WINDOW", lambda :OOOOO0OOOOO0OOOOOIlI (OO0O00O0OOOO000OO, O0OOO000OO00OOO0O))  
def OOOIIIIlll000O (O00O0O0OOO0O0O000 :str, OOOO0OO00O00O00OO :str, OO00OO000OO0O0OO0 :bool)->None :  
    O00000OOOOO0OO0OO =OO000OOO000lII0OI ()  
    if OO00OO000OO0O0OO0 :  
        if O00O0O0OOO0O0O000 not in O00000OOOOO0OO0OO :  
            O00000OOOOO0OO0OO [O00O0O0OOO0O0O000 ]={'password':OOOO0OO00O00O00OO ,'role':'user'}  
            with open (USERS_PATH ,'w')as O00O000O00O00000O :  
                json .dump (O00000OOOOO0OO0OO ,O00O000O00O00000O )  
            CTkMessagebox (title ="Success",message ="You added new user",icon ="check")  
        else :  
            CTkMessagebox (title ="Warning",message ="User already exists",icon ="warning")  
    else :  
        O00000OOOOO0OO0OO [O00O0O0OOO0O0O000 ]={'password':OOOO0OO00O00O00OO ,'role':'user'}  
        with open (USERS_PATH ,'w')as O00O000O00O00000O :  
            json .dump (O00000OOOOO0OO0OO ,O00O000O00O00000O )  
def IlIlIlIlIl (O000000OO0OO00O0O :bool)->None :  
    O0000O000OO00OOO0 =CTk .CTk ()  
    O0000O000OO00OOO0 .geometry ("700x470")  
    O0000O000OO00OOO0 .title ('Authentication')  
    O0000O000OO00OOO0 .resizable (False ,False )  
    CTk .set_appearance_mode ("dark")  
    CTk .set_default_color_theme ("green")  
    OOOOOO000000O0000 =CTk .CTkImage (dark_image =Image .open ("cat1.jpg"),size =(300 ,470 ))  
    OOOOOOO0O0000O00O =CTk .CTkLabel (master =O0000O000OO00OOO0 ,text ="",image =OOOOOO000000O0000 )  
    OOOOOOO0O0000O00O .grid (row =0 ,column =0 ,rowspan =2 )  
    OO000O000OO000OOO =CTk .CTkLabel (master =O0000O000OO00OOO0 ,text ="~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~",font =("Arial",20 ))  
    OO000O000OO000OOO .grid (row =0 ,column =1 ,columnspan =3 )  
    OO0O00OOOOO00O0OO =CTk .CTkFrame (master =O0000O000OO00OOO0 ,width =400 ,height =400 ,fg_color ="transparent")  
    OO0O00OOOOO00O0OO .grid (row =1 ,column =1 ,padx =25 ,pady =10 )  
    O000O00O0OOOO0000 =CTk .CTkLabel (master =OO0O00OOOOO00O0OO ,text ="Username",font =("Arial",17 ))  
    O000O00O0OOOO0000 .grid (row =0 ,column =0 )  
    OOO00OOO0O00OOOO0 =O001ll00O0 (OO0O00OOOOO00O0OO, O000000OO0OO00O0O)  
    OOO00OOO0O00OOOO0 .grid (row =0 ,column =1 ,columnspan =2 )  
    O000O0OO00O00OOOO =CTk .CTkLabel (master =OO0O00OOOOO00O0OO ,text ="Password",font =("Arial",17 ))  
    O000O0OO00O00OOOO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 )  
    OO00O0O000O00OOOO =O001ll00O0 (OO0O00OOOOO00O0OO, O000000OO0OO00O0O, show ='*')  
    OO00O0O000O00OOOO .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 )  
    OO00000O0OOOOO000 =CTk .CTkButton (master =OO0O00OOOOO00O0OO, text ="Login", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :IIIIOOO000OOOlI (OOO00OOO0O00OOOO0, OO00O0O000O00OOOO, O0000O000OO00OOO0, O000000OO0OO00O0O))  
    OO00000O0OOOOO000 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 )  
    O0000O000OO00OOO0 .mainloop ()  

