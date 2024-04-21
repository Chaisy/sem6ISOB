import json  
import os  
import re  
import tkinter as tk  
import customtkinter as CTk  
import requests  
from CTkMessagebox import CTkMessagebox  
from PIL import Image  
import random  
USERS_PATH =os .path .join (os .path .dirname (os .path .abspath (__file__ )),'users.json') 
class O00OOO000OOOIII (CTk .CTkEntry):
    def __init__ (O0O0OO0OOOO0O0O0O ,OOO000OOOO0O0000O =None ,O000O000OOO00O0OO =True ,OOO0O00OO0OO0OO0O =10 ,**OO0O00O00OO0OOOO0 ): 
        super ().__init__ (OOO000OOOO0O0000O ,**OO0O00O00OO0OOOO0 ) 
        O0O0OO0OOOO0O0O0O .configure (width =250 ,height =50 ) 
        O0O0OO0OOOO0O0O0O .buffer =['']*OOO0O00OO0OO0OO0O  
        O0O0OO0OOOO0O0O0O .buffer_size =OOO0O00OO0OO0OO0O  
        O0O0OO0OOOO0O0O0O .is_protected =O000O000OOO00O0OO  
        O0O0OO0OOOO0O0O0O .bind ('<KeyRelease>', O0O0OO0OOOO0O0O0O .lllIILIL566LL754)
    def lllIILIL566LL754 (OO0OOO0OOO0000O0O, O00O0O00O0OO00OOO)->None :
        O0O0O000OOO0OO000 =OO0OOO0OOO0000O0O .get () 
        if OO0OOO0OOO0000O0O .is_protected and len (O0O0O000OOO0OO000 )>OO0OOO0OOO0000O0O .buffer_size : 
            OO0OOO0OOO0000O0O .delete (OO0OOO0OOO0000O0O .buffer_size ,CTk .END ) 
            OO0OOO0OOO0000O0O .lllIILIL566LL754 (O00O0O00O0OO00OOO)
            return  
        else : 
            O0O0OOOO0000O0000 =0  
            while O0O0OOOO0000O0000 <100 : 
                O0O0OOOO0000O0000 +=1  
            print ("Thats all") 
        O0O0O000OOO0OO000 =list (O0O0O000OOO0OO000 ) 
        OO0OOO0OOO0000O0O .buffer =['']*OO0OOO0OOO0000O0O .buffer_size  
        for O0O0OOOO0000O0000 in range (len (O0O0O000OOO0OO000 )): 
            OO0OOO0OOO0000O0O .buffer [O0O0OOOO0000O0000 ]=O0O0O000OOO0OO000 [O0O0OOOO0000O0000 ] 
    def y111IIII11IIl0 (OO0OOOO00OO0OOO00)->str :
        return ''.join (OO0OOOO00OO0OOO00 .buffer ) 
def OOOIIIl0 ()->dict :
    try : 
        with open (USERS_PATH ,'r')as OO00OO0OO0000O000 : 
            return json .load (OO00OO0OO0000O000 ) 
    except FileNotFoundError : 
        return {} 
def e111OOO01 (O0O000OO00OOOO00O :str, O0OO0OOOO00O00OO0 :str)->dict :
    O0O00OO00O0O0OOO0 =OOOIIIl0 ()
    if O0O000OO00OOOO00O in O0O00OO00O0O0OOO0 and O0O00OO00O0O0OOO0 [O0O000OO00OOOO00O ]['password']==O0OO0OOOO00O00OO0 : 
        return O0O00OO00O0O0OOO0 [O0O000OO00OOOO00O ] 
    else : 
        return None  
def OOOOOOOO0O9OO0 (O0000O00O0OO00OO0 :str, OOO0OO0OOOOOO0OO0 :str)->dict :
    OO0O00O0000O00OOO =OOOIIIl0 ()
    if O0000O00O0OO00OO0 in OO0O00O0000O00OOO and OO0O00O0000O00OOO [O0000O00O0OO00OO0 ]['password']==OOO0OO0OOOOOO0OO0 : 
        return OO0O00O0000O00OOO [O0000O00O0OO00OO0 ] 
    else : 
        return None  
    OO0O0OOO0O00OO0OO =OOOIIIl0 ()
    if O0000O00O0OO00OO0 in OO0O00O0000O00OOO and OO0O00O0000O00OOO [O0000O00O0OO00OO0 ]['password']==OOO0OO0OOOOOO0OO0 : 
        return OO0O00O0000O00OOO [O0000O00O0OO00OO0 ] 
    else : 
        return None  
    O0O000O0O00OOO0OO =OOOIIIl0 ()
    if O0000O00O0OO00OO0 in OO0O00O0000O00OOO and OO0O00O0000O00OOO [O0000O00O0OO00OO0 ]['password']==OOO0OO0OOOOOO0OO0 : 
        return OO0O00O0000O00OOO [O0000O00O0OO00OO0 ] 
    else : 
        return None  
def lo00O11LL (O00OO0O00OO000OOO :O00OOO000OOOIII, OOO0OO0O0OOOOOO0O :O00OOO000OOOIII, OOO00OO0O0O0OOO00 :CTk .CTk, O0O0O0OOOO00O0O00 :bool)->None :
    O0OOOO00O0O000O0O =O00OO0O00OO000OOO .y111IIII11IIl0 ()
    O0O000OO0O0O0OOO0 =OOO0OO0O0OOOOOO0O .y111IIII11IIl0 ()
    O0O000O00OO00000O =e111OOO01 (O0OOOO00O0O000O0O, O0O000OO0O0O0OOO0)
    if O0O000O00OO00000O : 
        if O0O0O0OOOO00O0O00 : 
            if O0O000O00OO00000O ['role']=='admin': 
                OO00OOO0OO00O00O0 =CTk .CTkToplevel (OOO00OO0O0O0OOO00 ) 
                OO00OOO0OO00O00O0 .title ('Account') 
                OO00OOO0OO00O00O0 .geometry ("700x470") 
                OO00O00O000OOOO0O =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 )) 
                O0O00OO00O000OOOO =CTk .CTkLabel (master =OO00OOO0OO00O00O0 ,text ="",image =OO00O00O000OOOO0O ) 
                O0O00OO00O000OOOO .grid (row =0 ,column =0 ,rowspan =2 ) 
                OOOOOO0O00O0000O0 =CTk .CTkLabel (master =OO00OOO0OO00O00O0 ,text =f"WELCOME, {O0OOOO00O0O000O0O}.\n You can add user",font =("Arial",20 )) 
                OOOOOO0O00O0000O0 .grid (row =0 ,column =1 ,columnspan =3 ) 
                OOOOO00O00O000O0O =CTk .CTkFrame (master =OO00OOO0OO00O00O0 ,width =400 ,height =400 ,fg_color ="transparent") 
                OOOOO00O00O000O0O .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
                OO00OO0OOO0O0O000 =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Username",font =("Arial",17 )) 
                OO00OO0OOO0O0O000 .grid (row =0 ,column =0 ) 
                O00OO00O0O0OO0OO0 =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00)
                O00OO00O0O0OO0OO0 .grid (row =0 ,column =1 ,columnspan =2 ) 
                OOO0OO00000O0OOOO =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Password",font =("Arial",17 )) 
                OOO0OO00000O0OOOO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
                O0OOOO0O0O0OO0O00 =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00, show ='*')
                O0OOOO0O0O0OO0O00 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
                O000O0O000000O000 =CTk .CTkButton (master =OOOOO00O00O000O0O, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :add_10O0o (O00OO00O0O0OO0OO0 .y111IIII11IIl0 (), O0OOOO0O0O0OO0O00 .y111IIII11IIl0 (), O0O0O0OOOO00O0O00))
                O000O0O000000O000 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
                OO00OOO0OO00O00O0 .protocol ("WM_DELETE_WINDOW", lambda :e2200O (OOO00OO0O0O0OOO00, O0O0O0OOOO00O0O00))
            else : 
                O0OO00OOO00OO0OOO =CTk .CTkToplevel (OOO00OO0O0O0OOO00 ) 
                O0OO00OOO00OO0OOO .title ('Account') 
                O0OO00OOO00OO0OOO .geometry ("700x470") 
                OO00O00O000OOOO0O =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 )) 
                O0O00OO00O000OOOO =CTk .CTkLabel (master =O0OO00OOO00OO0OOO ,text ="",image =OO00O00O000OOOO0O ) 
                O0O00OO00O000OOOO .grid (row =0 ,column =1 ,rowspan =2 ) 
                OOOOOO0O00O0000O0 =CTk .CTkLabel (master =O0OO00OOO00OO0OOO ,text =f"WELCOME, {O0OOOO00O0O000O0O}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 )) 
                OOOOOO0O00O0000O0 .grid (row =0 ,column =0 ) 
                OOOOO00O00O000O0O =CTk .CTkFrame (master =O0OO00OOO00OO0OOO ,width =400 ,height =400 ,fg_color ="transparent") 
                OOOOO00O00O000O0O .grid (row =1 ,column =0 ,padx =25 ) 
                O000O000O0OO0OOOO =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Name",font =("Arial",17 )) 
                O000O000O0OO0OOOO .grid (row =0 ,column =0 ) 
                O0O000O00OO0O00OO =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00)
                O0O000O00OO0O00OO .grid (row =0 ,column =1 ,columnspan =2 ) 
                O00O0OO0OOO0O0000 =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Size",font =("Arial",17 )) 
                O00O0OO0OOO0O0000 .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
                OOOOO0O0O0OOO00OO =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00)
                OOOOO0O0O0OOO00OO .grid (row =1 ,column =1 ,columnspan =2 ) 
                O0O0O00O0O00O0OO0 =CTk .CTkButton (master =OOOOO00O00O000O0O, text ="GO", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :ee100_O (O0O000O00OO0O00OO, OOOOO0O0O0OOO00OO, OOOOO00O00O000O0O, O0O0O0OOOO00O0O00))
                O0O0O00O0O00O0OO0 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
                O0OO00OOO00OO0OOO .protocol ("WM_DELETE_WINDOW", lambda :e2200O (OOO00OO0O0O0OOO00, O0O0O0OOOO00O0O00))
        else : 
            UUUUUUUU8UUUU_0000 (O0OOOO00O0O000O0O, OOO00OO0O0O0OOO00, O0O0O0OOOO00O0O00)
            O0OO00OOO00OO0OOO =CTk .CTkToplevel (OOO00OO0O0O0OOO00 ) 
            O0OO00OOO00OO0OOO .title ('Account') 
            O0OO00OOO00OO0OOO .geometry ("700x470") 
            OO00O00O000OOOO0O =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 )) 
            O0O00OO00O000OOOO =CTk .CTkLabel (master =O0OO00OOO00OO0OOO ,text ="",image =OO00O00O000OOOO0O ) 
            O0O00OO00O000OOOO .grid (row =0 ,column =1 ,rowspan =2 ) 
            OOOOOO0O00O0000O0 =CTk .CTkLabel (master =O0OO00OOO00OO0OOO ,text =f"WELCOME, {O0OOOO00O0O000O0O}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 )) 
            OOOOOO0O00O0000O0 .grid (row =0 ,column =0 ) 
            OOOOO00O00O000O0O =CTk .CTkFrame (master =O0OO00OOO00OO0OOO ,width =400 ,height =400 ,fg_color ="transparent") 
            OOOOO00O00O000O0O .grid (row =1 ,column =0 ,padx =25 ) 
            O000O000O0OO0OOOO =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Name",font =("Arial",17 )) 
            O000O000O0OO0OOOO .grid (row =0 ,column =0 ) 
            O0O000O00OO0O00OO =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00)
            O0O000O00OO0O00OO .grid (row =0 ,column =1 ,columnspan =2 ) 
            O00O0OO0OOO0O0000 =CTk .CTkLabel (master =OOOOO00O00O000O0O ,text ="Size",font =("Arial",17 )) 
            O00O0OO0OOO0O0000 .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
            OOOOO0O0O0OOO00OO =O00OOO000OOOIII (OOOOO00O00O000O0O, O0O0O0OOOO00O0O00)
            OOOOO0O0O0OOO00OO .grid (row =1 ,column =1 ,columnspan =2 ) 
            O0O0O00O0O00O0OO0 =CTk .CTkButton (master =OOOOO00O00O000O0O, text ="GO", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :ee100_O (O0O000O00OO0O00OO, OOOOO0O0O0OOO00OO, OOOOO00O00O000O0O, O0O0O0OOOO00O0O00))
            O0O0O00O0O00O0OO0 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
            O0OO00OOO00OO0OOO .protocol ("WM_DELETE_WINDOW", lambda :e2200O (OOO00OO0O0O0OOO00, O0O0O0OOOO00O0O00))
        OOO00OO0O0O0OOO00 .withdraw () 
    else : 
        CTkMessagebox (title ="Error",message ="Invalid username or password",icon ="cancel") 
def e2200O (OO00OOO0O0O00OO00 :CTk .CTk, O0OOO0O0O00O0O00O :bool):
    OO00OOO0O0O00OO00 .destroy () 
    iUIUIUI1_e (O0OOO0O0O00O0O00O)
def on_1eOO0 (OO0OO0O0O0O00O00O :CTk .CTk, OOO000000OOOO000O :bool):
    OO0OO0O0O0O00O00O .destroy () 
    OOO000000OOOO000O =not OOO000000OOOO000O  
    iUIUIUI1_e (OOO000000OOOO000O)
def user1e0OO0 (O0000O00OOOO0OO00 :str, OO0O0O0OO0O0OO0O0 :CTk .CTk, OOO00OOOOO0000000 :bool)->None :
    for O0000O00OOOO0OO00 in range (100 ): 
        O00OOO0000O0000OO =O0000O00OOOO0OO00 .get_string () 
        O0OOOO0OOOOOOO0OO =OOO00OOOOO0000000 .get_string () 
        print (O00OOO0000O0000OO ,O0OOOO0OOOOOOO0OO ) 
    for OO0O0O0OO0O0OO0O0 in range (50 ): 
        print (OO0O0O0OO0O0OO0O0 ) 
    for OOO00OOOOO0000000 in range (27 ): 
        print (not OOO00OOOOO0000000 ) 
    O0OOOOO00OOOO0OO0 =5  
    for O0OOOOO00OOOO0OO0 in range (8 ): 
        print (O0OOOOO00OOOO0OO0 ) 
    O00OOO0000O0000OO =O0000O00OOOO0OO00 .get_string () 
    O0OOOO0OOOOOOO0OO =OOO00OOOOO0000000 .get_string () 
    return O00OOO0000O0000OO ,O0OOOO0OOOOOOO0OO  
def ee100_O (O000O0OOOOOO00000 :O00OOO000OOOIII, OOO0000O0OOOO0000 :O00OOO000OOOIII, OO00OOO0OOO000O00 :CTk .CTkToplevel, OOOOO0OOO000OO000 :bool)->None :
    if OOOOO0OOO000OO000 : 
        O00O0O0OOOOOOO0OO =OO00OOO0OOO000O00 .children ['!ctkbutton'] 
        O00O0O0OOOOOOO0OO .configure (state =CTk .DISABLED ) 
        OO00OOO0OOO000O00 .after (5000 ,lambda :O00O0O0OOOOOOO0OO .configure (state =tk .NORMAL )) 
    O00OOO0000O0OO000 =O000O0OOOOOO00000 .y111IIII11IIl0 ()
    O0OOOOOO000OOO000 =OOO0000O0OOOO0000 .y111IIII11IIl0 ()
    if OOOOO0OOO000OO000 : 
        if not OOOO000OOO9OO00 (O00OOO0000O0OO000 , O0OOOOOO000OOO000):
            CTkMessagebox (title ="Error",message ="Invalid data",icon ="cancel") 
            return  
    O000OO000O0O0OOOO =e18_00o (O00OOO0000O0OO000, O0OOOOOO000OOO000)
    OOOO0OOOOOilili (O000OO000O0O0OOOO, OO00OOO0OOO000O00)
def OOOO000OOO9OO00 (OO000O0O0000OO00O :str, OO000OO0000O00OOO :str)->bool :
    try : 
        O0O0OOO0O00OO000O =len (OO000O0O0000OO00O ) 
        OOO00O0O0O0OO0O0O =int (OO000OO0000O00OOO ) 
        if (15 <=O0O0OOO0O00OO000O or O0O0OOO0O00OO000O <=1 )or (70 <OOO00O0O0O0OO0O0O or OOO00O0O0O0OO0O0O <=20 )or not (re .fullmatch ("^[A-z '-]+$",OO000O0O0000OO00O )): 
            return False  
        else : 
            return True  
    except ValueError : 
        return False  
def e18_00o (O0000OOO000OOO000 :str, O0000O00O00OOOO00 :str)->str :
    O000OO0O00O000000 =f'https://api.genderize.io?name={O0000OOO000OOO000}' 
    O0OO0O000OOOO0000 =requests .get (O000OO0O00O000000 ) 
    O000000O0O000OO00 =O0OO0O000OOOO0000 .json () 
    O000OO0O00O000000 =f'https://catfact.ninja/fact?max_length={O0000O00O00OOOO00}' 
    O000O000000O0OO0O =requests .get (O000OO0O00O000000 ) 
    OOOO000O000O0OOOO =O000O000000O0OO0O .json () 
    if O0OO0O000OOOO0000 .status_code ==200 and O000O000000O0OO0O .status_code ==200 : 
        O000O00OOO00O00OO =O000000O0O000OO00 ['gender'] 
        OOOOO0OOOO0O00OO0 =OOOO000O000O0OOOO ['fact'] 
        return f'Your name\'s gender is {O000O00OOO00O00OO}.\n Your fact about cats is:\n {OOOOO0OOOO0O00OO0}' 
    raise Exception ('Error while getting api') 
def OOOOOOO0OOOiiL (O0O00OO0O0O0OO0OO :str, O00O0O0O00OOOOO0O :str)->str :
    OOOOOOOO0OOOO0OO0 =f'https://api.genderize.io?name={O0O00OO0O0O0OO0OO}' 
    O0O00OOO0OOO00OO0 =requests .get (OOOOOOOO0OOOO0OO0 ) 
    OOO0OO0OO0OOOO0OO =O0O00OOO0OOO00OO0 .json () 
    OOOOOOOO0OOOO0OO0 =f'https://catfact.ninja/fact?max_length={O00O0O0O00OOOOO0O}' 
    OO0OOOO0O00O0O0OO =requests .get (OOOOOOOO0OOOO0OO0 ) 
    O0OO0O0000OO0OO0O =OO0OOOO0O00O0O0OO .json () 
    if O0O00OOO0OOO00OO0 .status_code ==200 and OO0OOOO0O00O0O0OO .status_code ==200 : 
        O00O000000OOOO000 =OOO0OO0OO0OOOO0OO ['gender'] 
        OOOO0OOO0000OOO00 =O0OO0O0000OO0OO0O ['fact'] 
        return f'Your name\'s gender is {O00O000000OOOO000}.\n Your fact about cats is:\n {OOOO0OOO0000OOO00}' 
    raise Exception ('Error while getting api') 
def OOOO0OOOOOilili (OO00OO00O0OOO0OOO :str, O000OO0O0OO000000 :CTk .CTkToplevel)->None :
    O0OO00O000OO00OO0 =O000OO0O0OO000000 .winfo_children () 
    if O0OO00O000OO00OO0 : 
        OOO000000OOO000OO =O0OO00O000OO00OO0 [-1 ] 
        if isinstance (OOO000000OOO000OO ,CTk .CTkLabel ): 
            OOO000000OOO000OO .destroy () 
    OO0O000OOOO0OOO0O =CTk .CTkLabel (O000OO0O0OO000000 ,text =OO00OO00O0OOO0OOO ) 
    OO0O000OOOO0OOO0O .grid (row =3 ,column =0 ,pady =5 ,columnspan =3 ) 
def U000O0OO01 (OO0OO00O00OO000OO :str, OO00OO0OO0OOOOO00 :str)->bool :
    try : 
        O000000O000OO0OO0 =len (OO0OO00O00OO000OO ) 
        O0OO0O000OO0O0O00 =int (OO00OO0OO0OOOOO00 ) 
        if (15 <=O000000O000OO0OO0 or O000000O000OO0OO0 <=1 )or (70 <O0OO0O000OO0O0O00 or O0OO0O000OO0O0O00 <=20 )or not (re .fullmatch ("^[A-z '-]+$",OO0OO00O00OO000OO )): 
            return False  
        else : 
            return True  
    except ValueError : 
        return False  
    OOOO0OO00O0OOOOOO =f'https://api.genderize.io?name={OO0OO00O00OO000OO}' 
    OO000O0000OOO0O0O =requests .get (OOOO0OO00O0OOOOOO ) 
    OOOOOOO00OOO000O0 =OO000O0000OOO0O0O .json () 
    OOOO0OO00O0OOOOOO =f'https://catfact.ninja/fact?max_length={OO00OO0OO0OOOOO00}' 
    O0O0000OO0000O00O =requests .get (OOOO0OO00O0OOOOOO ) 
    O00OOOOO00OO0OOOO =O0O0000OO0000O00O .json () 
    if OO000O0000OOO0O0O .status_code ==200 and O0O0000OO0000O00O .status_code ==200 : 
        OO0O0O00O0OOOO0OO =OOOOOOO00OOO000O0 ['gender'] 
        OOOO0O0O000O0O000 =O00OOOOO00OO0OOOO ['fact'] 
        return f'Your name\'s gender is {OO0O0O00O0OOOO0OO}.\n Your fact about cats is:\n {OOOO0O0O000O0O000}' 
    raise Exception ('Error while getting api') 
def UUUUUUUU8UUUU_0000 (O000O0000O00O0O00 :str, OOO0OOOO000O0O0O0 :CTk .CTk, OO0O0O00O00000OO0 :bool)->None :
    OOOOO0OOO00O00OO0 =CTk .CTkToplevel (OOO0OOOO000O0O0O0 ) 
    OOOOO0OOO00O00OO0 .title ('Account') 
    OOOOO0OOO00O00OO0 .geometry ("700x470") 
    O0O0O0O00OOO0O00O =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 )) 
    O0OOO0O0000OOO0O0 =CTk .CTkLabel (master =OOOOO0OOO00O00OO0 ,text ="",image =O0O0O0O00OOO0O00O ) 
    O0OOO0O0000OOO0O0 .grid (row =0 ,column =0 ,rowspan =2 ) 
    O0O00OOOOOO0O00O0 =CTk .CTkLabel (master =OOOOO0OOO00O00OO0 ,text =f"WELCOME, {O000O0000O00O0O00}.\n You can add user",font =("Arial",20 )) 
    O0O00OOOOOO0O00O0 .grid (row =0 ,column =1 ,columnspan =3 ) 
    OO000O0OOOOOOOOO0 =CTk .CTkFrame (master =OOOOO0OOO00O00OO0 ,width =400 ,height =400 ,fg_color ="transparent") 
    OO000O0OOOOOOOOO0 .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
    OOOO0000OOOOOO0OO =CTk .CTkLabel (master =OO000O0OOOOOOOOO0 ,text ="Username",font =("Arial",17 )) 
    OOOO0000OOOOOO0OO .grid (row =0 ,column =0 ) 
    OOO0000OOO0O0OOO0 =O00OOO000OOOIII (OO000O0OOOOOOOOO0, OO0O0O00O00000OO0)
    OOO0000OOO0O0OOO0 .grid (row =0 ,column =1 ,columnspan =2 ) 
    OOOO0O00O0OOO0O0O =CTk .CTkLabel (master =OO000O0OOOOOOOOO0 ,text ="Password",font =("Arial",17 )) 
    OOOO0O00O0OOO0O0O .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
    OO0000000OO0000OO =O00OOO000OOOIII (OO000O0OOOOOOOOO0, OO0O0O00O00000OO0, show ='*')
    OO0000000OO0000OO .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
    OO00OOO00OOO00O0O =CTk .CTkButton (master =OO000O0OOOOOOOOO0, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :add_10O0o (OOO0000OOO0O0OOO0 .y111IIII11IIl0 (), OO0000000OO0000OO .y111IIII11IIl0 (), OO0O0O00O00000OO0))
    OO00OOO00OOO00O0O .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
    OOOOO0OOO00O00OO0 .protocol ("WM_DELETE_WINDOW", lambda :e2200O (OOO0OOOO000O0O0O0, OO0O0O00O00000OO0))
def add_10O0o (O00O0OO0O000O0000 :str, O00OOOO00000OO0O0 :str, OO0OOO0O0000O00OO :bool)->None :
    OOO0OO000O0OO00O0 =OOOIIIl0 ()
    if OO0OOO0O0000O00OO : 
        if O00O0OO0O000O0000 not in OOO0OO000O0OO00O0 : 
            OOO0OO000O0OO00O0 [O00O0OO0O000O0000 ]={'password':O00OOOO00000OO0O0 ,'role':'user'} 
            with open (USERS_PATH ,'w')as OOOOO00OOO0O0OO00 : 
                json .dump (OOO0OO000O0OO00O0 ,OOOOO00OOO0O0OO00 ) 
            CTkMessagebox (title ="Success",message ="You added new user",icon ="check") 
        else : 
            CTkMessagebox (title ="Warning",message ="User already exists",icon ="warning") 
    else : 
        OOO0OO000O0OO00O0 [O00O0OO0O000O0000 ]={'password':O00OOOO00000OO0O0 ,'role':'user'} 
        with open (USERS_PATH ,'w')as OOOOO00OOO0O0OO00 : 
            json .dump (OOO0OO000O0OO00O0 ,OOOOO00OOO0O0OO00 ) 
def iUIUIUI1_e (O0OOO0O0OO0O00OOO :bool)->None :
    OO0OO000O00O0OO00 =CTk .CTk () 
    OO0OO000O00O0OO00 .geometry ("700x470") 
    OO0OO000O00O0OO00 .title ('Authentication') 
    OO0OO000O00O0OO00 .resizable (False ,False ) 
    CTk .set_appearance_mode ("dark") 
    CTk .set_default_color_theme ("green") 
    O0000OO0OOOOOO000 =CTk .CTkImage (dark_image =Image .open ("cat1.jpg"),size =(300 ,470 )) 
    OO0OO0O0OO0O000OO =CTk .CTkLabel (master =OO0OO000O00O0OO00 ,text ="",image =O0000OO0OOOOOO000 ) 
    OO0OO0O0OO0O000OO .grid (row =0 ,column =0 ,rowspan =2 ) 
    O0O0000OO0OOO0O00 =CTk .CTkLabel (master =OO0OO000O00O0OO00 ,text ="~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~",font =("Arial",20 )) 
    O0O0000OO0OOO0O00 .grid (row =0 ,column =1 ,columnspan =3 ) 
    OO00O0O0O0O0O0O00 =CTk .CTkFrame (master =OO0OO000O00O0OO00 ,width =400 ,height =400 ,fg_color ="transparent") 
    OO00O0O0O0O0O0O00 .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
    O00OO00OO00OO000O =CTk .CTkLabel (master =OO00O0O0O0O0O0O00 ,text ="Username",font =("Arial",17 )) 
    O00OO00OO00OO000O .grid (row =0 ,column =0 ) 
    OOOOOOOOO0O00OO00 =O00OOO000OOOIII (OO00O0O0O0O0O0O00, O0OOO0O0OO0O00OOO)
    OOOOOOOOO0O00OO00 .grid (row =0 ,column =1 ,columnspan =2 ) 
    O0O0OOO0OOOOO00OO =CTk .CTkLabel (master =OO00O0O0O0O0O0O00 ,text ="Password",font =("Arial",17 )) 
    O0O0OOO0OOOOO00OO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
    O00OOO00000000OO0 =O00OOO000OOOIII (OO00O0O0O0O0O0O00, O0OOO0O0OO0O00OOO, show ='*')
    O00OOO00000000OO0 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
    O0OO0O0O000O0OOO0 =CTk .CTkButton (master =OO00O0O0O0O0O0O00, text ="Login", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :lo00O11LL (OOOOOOOOO0O00OO00, O00OOO00000000OO0, OO0OO000O00O0OO00, O0OOO0O0OO0O00OOO))
    O0OO0O0O000O0OOO0 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
    OO0OO000O00O0OO00 .mainloop () 
    O00OOOOO0OO000OO0 =False  
    if O00OOOOO0OO000OO0 : 
        O0O00OO00000O00OO =CTk .CTkToplevel (OO0OO000O00O0OO00 ) 
        O0O00OO00000O00OO .title ('Account') 
        O0O00OO00000O00OO .geometry ("700x470") 
        O0000OO0OOOOOO000 =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 )) 
        OO0OO0O0OO0O000OO =CTk .CTkLabel (master =O0O00OO00000O00OO ,text ="",image =O0000OO0OOOOOO000 ) 
        OO0OO0O0OO0O000OO .grid (row =0 ,column =0 ,rowspan =2 ) 
        O0O0000OO0OOO0O00 =CTk .CTkLabel (master =O0O00OO00000O00OO ,text =f"WELCOME.\n You can add user",font =("Arial",20 )) 
        O0O0000OO0OOO0O00 .grid (row =0 ,column =1 ,columnspan =3 ) 
        OO00O0O0O0O0O0O00 =CTk .CTkFrame (master =O0O00OO00000O00OO ,width =400 ,height =400 ,fg_color ="transparent") 
        OO00O0O0O0O0O0O00 .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
        O00OO00OO00OO000O =CTk .CTkLabel (master =OO00O0O0O0O0O0O00 ,text ="Username",font =("Arial",17 )) 
        O00OO00OO00OO000O .grid (row =0 ,column =0 ) 
        OOOOOOOOO0O00OO00 =O00OOO000OOOIII (OO00O0O0O0O0O0O00, O0OOO0O0OO0O00OOO)
        OOOOOOOOO0O00OO00 .grid (row =0 ,column =1 ,columnspan =2 ) 
        O0O0OOO0OOOOO00OO =CTk .CTkLabel (master =OO00O0O0O0O0O0O00 ,text ="Password",font =("Arial",17 )) 
        O0O0OOO0OOOOO00OO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
        O00OOO00000000OO0 =O00OOO000OOOIII (OO00O0O0O0O0O0O00, O0OOO0O0OO0O00OOO, show ='*')
        O00OOO00000000OO0 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
        O0OO0O0O000O0OOO0 =CTk .CTkButton (master =OO00O0O0O0O0O0O00, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :add_10O0o (OOOOOOOOO0O00OO00 .y111IIII11IIl0 (), O00OOO00000000OO0 .y111IIII11IIl0 (), O0OOO0O0OO0O00OOO))
        O0OO0O0O000O0OOO0 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
