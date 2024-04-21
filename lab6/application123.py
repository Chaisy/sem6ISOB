import json  
import os  
import re  
import tkinter as tk  
import customtkinter as CTk  
import requests  
from CTkMessagebox import CTkMessagebox  
from PIL import Image  
USERS_PATH =os .path .join (os .path .dirname (os .path .abspath (__file__ )),'users.json') 
class b3bb3bb3b3b3b3b (CTk .CTkEntry):
    def __init__ (O0O0OOO0O000O0000 ,OO00O00O00O0OOO0O =None ,O00OOO0000O0O00O0 =True ,O0O00OOO0O0O0O000 =10 ,**OOOO0OO0O0O0OOOOO ): 
        super ().__init__ (OO00O00O00O0OOO0O ,**OOOO0OO0O0O0OOOOO ) 
        O0O0OOO0O000O0000 .configure (width =250 ,height =50 ) 
        O0O0OOO0O000O0000 .buffer =['']*O0O00OOO0O0O0O000  
        O0O0OOO0O000O0000 .buffer_size =O0O00OOO0O0O0O000  
        O0O0OOO0O000O0000 .is_protected =O00OOO0000O0O00O0  
        O0O0OOO0O000O0000 .bind ('<KeyRelease>', O0O0OOO0O000O0000 .o3o3o3o3o3o3oo3o3)
    def o3o3o3o3o3o3oo3o3 (O0O0O000O0OOOOO00, OOOOO0OO000O000O0)->None :
        OOOOOO0OOO0O000O0 =O0O0O000O0OOOOO00 .get () 
        if O0O0O000O0OOOOO00 .is_protected and len (OOOOOO0OOO0O000O0 )>O0O0O000O0OOOOO00 .buffer_size : 
            O0O0O000O0OOOOO00 .delete (O0O0O000O0OOOOO00 .buffer_size ,CTk .END ) 
            O0O0O000O0OOOOO00 .o3o3o3o3o3o3oo3o3 (OOOOO0OO000O000O0)
            return  
        else : 
            O0O0O00OO0OO0OO0O =0  
            while O0O0O00OO0OO0OO0O <100 : 
                O0O0O00OO0OO0OO0O +=1  
            print ("Thats all") 
        OOOOOO0OOO0O000O0 =list (OOOOOO0OOO0O000O0 ) 
        O0O0O000O0OOOOO00 .buffer =['']*O0O0O000O0OOOOO00 .buffer_size  
        for O0O0O00OO0OO0OO0O in range (len (OOOOOO0OOO0O000O0 )): 
            O0O0O000O0OOOOO00 .buffer [O0O0O00OO0OO0OO0O ]=OOOOOO0OOO0O000O0 [O0O0O00OO0OO0OO0O ] 
    def O0O0O00oo0 (OOOOOOO0OOOO00000)->str :
        return ''.join (OOOOOOO0OOOO00000 .buffer ) 
def iiiiii8ii8i8i8 (OOO0OOOO00O000OOO :str, O0OOOO000OOOO0000 :str)->str :
    O0O0000O0OOOO00O0 ,O0OO000OO0OOOO0O0 ,O0O00O0000OOOOO0O ,O0O0OOO0O0000000O =a2_00OO (OOO0OOOO00O000OOO, O0OOOO000OOOO0000)
    OOOOO0000OO000O00 ="Data Cats" 
    if O0O0000O0OOOO00O0 .status_code ==200 and O0OO000OO0OOOO0O0 .status_code ==200 : 
        OO00000O0000OO0O0 =O0O00O0000OOOOO0O ['gender'] 
        OO00O0O0OO000O0OO =O0O0OOO0O0000000O ['fact'] 
        return f'Your name\'s gender is {OO00000O0000OO0O0}.\n Your fact about cats is:\n {OO00O0O0OO000O0OO}' 
    raise Exception ('Error while getting api') 
def iliilililil7 (OOOO0OOOO0OOOOOO0 :str, OO0OOOOOO00O00O0O :CTk .CTkToplevel)->None :
    O0O00OOO000O0OO0O =OO0OOOOOO00O00O0O .winfo_children () 
    if O0O00OOO000O0OO0O : 
        O00OO00OO0O0OO0OO =O0O00OOO000O0OO0O [-1 ] 
        if isinstance (O00OO00OO0O0OO0OO ,CTk .CTkLabel ): 
            O00OO00OO0O0OO0OO .destroy () 
    O0OO0000OO00O0O00 =CTk .CTkLabel (OO0OOOOOO00O00O0O ,text =OOOO0OOOO0OOOOOO0 ) 
    O0OO0000OO00O0O00 .grid (row =3 ,column =0 ,pady =5 ,columnspan =3 ) 
def a1a1oo0o0 ()->dict :
    try : 
        with open (USERS_PATH ,'r')as O0O000OOO00O0O0O0 : 
            return json .load (O0O000OOO00O0O0O0 ) 
    except FileNotFoundError : 
        return {} 
def ann7_oo (O0000OO0O00OOO00O :CTk .CTk, OOO00000O0O0000O0 :bool):
    O0000OO0O00OOO00O .destroy () 
    start_ (OOO00000O0O0000O0 ) 
def a_____9___j (O0000O00OOOO00000 :str, O0O0O0OO0OO000000 :str)->dict :
    O00O000O0OO00OOOO =a1a1oo0o0 ()
    if O0000O00OOOO00000 in O00O000O0OO00OOOO and O00O000O0OO00OOOO [O0000O00OOOO00000 ]['password']==O0O0O0OO0OO000000 : 
        return O00O000O0OO00OOOO [O0000O00OOOO00000 ] 
    else : 
        return annn82 ()
def LILILIo0 (OO00OOO0OOOO0OOO0 :str, O0000O0OO00000O0O :CTk .CTkToplevel)->None :
    O0000O00O0O0OOO00 =O0000O0OO00000O0O .winfo_children () 
    if O0000O00O0O0OOO00 : 
        O0O0O0OOO000O0OOO =O0000O00O0O0OOO00 [-1 ] 
        if isinstance (O0O0O0OOO000O0OOO ,CTk .CTkLabel ): 
            O0O0O0OOO000O0OOO .destroy () 
    O00OOO0OOOOO0O0OO =CTk .CTkLabel (O0000O0OO00000O0O ,text =OO00OOO0OOOO0OOO0 ) 
    O00OOO0OOOOO0O0OO .grid (row =3 ,column =0 ,pady =5 ,columnspan =3 ) 
def jkjkjkjkjkjkjkjkjk_0 (O0OO00O0O0OOOO000 :b3bb3bb3b3b3b3b, OO0O000O00O000OOO :b3bb3bb3b3b3b3b, OOO00OOOO00000OO0 :CTk .CTk, OOO000OO0O0OOOOO0 :bool)->None :
    OOOOO0OOO0O0O000O ,O0O000O0O0OO00OO0 ,OO0OOOO0O0000OOO0 =kokokokoo1 (O0OO00O0O0OOOO000, OO0O000O00O000OOO)
    if OO0OOOO0O0000OOO0 : 
        if OOO000OO0O0OOOOO0 : 
            if OO0OOOO0O0000OOO0 ['role']=='admin': 
                O00OOO0000OOO0000 =CTk .CTkToplevel (OOO00OOOO00000OO0 ) 
                O00OOO0000OOO0000 .title ('Account') 
                O00OOO0000OOO0000 .geometry ("700x470") 
                O0OO0O0O0OOOO00O0 =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 )) 
                OOO0OO000O00O0OO0 =CTk .CTkLabel (master =O00OOO0000OOO0000 ,text ="",image =O0OO0O0O0OOOO00O0 ) 
                OOO0OO000O00O0OO0 .grid (row =0 ,column =0 ,rowspan =2 ) 
                O00O0000OO0OOO00O =CTk .CTkLabel (master =O00OOO0000OOO0000 ,text =f"WELCOME, {OOOOO0OOO0O0O000O}.\n You can add user",font =("Arial",20 )) 
                O00O0000OO0OOO00O .grid (row =0 ,column =1 ,columnspan =3 ) 
                O00OOOO0O0OOO000O =CTk .CTkFrame (master =O00OOO0000OOO0000 ,width =400 ,height =400 ,fg_color ="transparent") 
                O00OOOO0O0OOO000O .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
                OO0O0OO0O00OOO00O =CTk .CTkLabel (master =O00OOOO0O0OOO000O ,text ="Username",font =("Arial",17 )) 
                OO0O0OO0O00OOO00O .grid (row =0 ,column =0 ) 
                OOO0000OO0OOO00O0 =b3bb3bb3b3b3b3b (O00OOOO0O0OOO000O, OOO000OO0O0OOOOO0)
                OOO0000OO0OOO00O0 .grid (row =0 ,column =1 ,columnspan =2 ) 
                OOOOO00OOOOOO0OOO =CTk .CTkLabel (master =O00OOOO0O0OOO000O ,text ="Password",font =("Arial",17 )) 
                OOOOO00OOOOOO0OOO .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
                O000OOOO000O0O0O0 =b3bb3bb3b3b3b3b (O00OOOO0O0OOO000O, OOO000OO0O0OOOOO0, show ='*')
                O000OOOO000O0O0O0 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
                O0O0OOO0O0OOOO0O0 =CTk .CTkButton (master =O00OOOO0O0OOO000O, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :addOOO0 (OOO0000OO0OOO00O0 .O0O0O00oo0 (), O000OOOO000O0O0O0 .O0O0O00oo0 (), OOO000OO0O0OOOOO0))
                O0O0OOO0O0OOOO0O0 .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
                O00OOO0000OOO0000 .protocol ("WM_DELETE_WINDOW", lambda :a11_2a (OOO00OOOO00000OO0, OOO000OO0O0OOOOO0))
            else : 
                OO00O000OO00O0OO0 =CTk .CTkToplevel (OOO00OOOO00000OO0 ) 
                OO00O000OO00O0OO0 .title ('Account') 
                OO00O000OO00O0OO0 .geometry ("700x470") 
                O0OO0O0O0OOOO00O0 =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 )) 
                OOO0OO000O00O0OO0 =CTk .CTkLabel (master =OO00O000OO00O0OO0 ,text ="",image =O0OO0O0O0OOOO00O0 ) 
                OOO0OO000O00O0OO0 .grid (row =0 ,column =1 ,rowspan =2 ) 
                O00O0000OO0OOO00O =CTk .CTkLabel (master =OO00O000OO00O0OO0 ,text =f"WELCOME, {OOOOO0OOO0O0O000O}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 )) 
                O00O0000OO0OOO00O .grid (row =0 ,column =0 ) 
                O00OOOO0O0OOO000O =CTk .CTkFrame (master =OO00O000OO00O0OO0 ,width =400 ,height =400 ,fg_color ="transparent") 
                O00OOOO0O0OOO000O .grid (row =1 ,column =0 ,padx =25 ) 
                OO0OO00OO00OO0OO0 =CTk .CTkLabel (master =O00OOOO0O0OOO000O ,text ="Name",font =("Arial",17 )) 
                OO0OO00OO00OO0OO0 .grid (row =0 ,column =0 ) 
                OO000O0OO0OOOO000 =b3bb3bb3b3b3b3b (O00OOOO0O0OOO000O, OOO000OO0O0OOOOO0)
                OO000O0OO0OOOO000 .grid (row =0 ,column =1 ,columnspan =2 ) 
                OLOLOLOLO_0 (OO00O000OO00O0OO0, O00OOOO0O0OOO000O, OOOOO0OOO0O0O000O, OOO00OOOO00000OO0, OOO000OO0O0OOOOO0, OO000O0OO0OOOO000)
        else : 
            aa3a3a3a3a3 (OOOOO0OOO0O0O000O, OOO00OOOO00000OO0, OOO000OO0O0OOOOO0)
            OO00O000OO00O0OO0 =CTk .CTkToplevel (OOO00OOOO00000OO0 ) 
            OO00O000OO00O0OO0 .title ('Account') 
            OO00O000OO00O0OO0 .geometry ("700x470") 
            O0OO0O0O0OOOO00O0 =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 )) 
            OOO0OO000O00O0OO0 =CTk .CTkLabel (master =OO00O000OO00O0OO0 ,text ="",image =O0OO0O0O0OOOO00O0 ) 
            OOO0OO000O00O0OO0 .grid (row =0 ,column =1 ,rowspan =2 ) 
            O00O0000OO0OOO00O =CTk .CTkLabel (master =OO00O000OO00O0OO0 ,text =f"WELCOME, {OOOOO0OOO0O0O000O}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 )) 
            O00O0000OO0OOO00O .grid (row =0 ,column =0 ) 
            O00OOOO0O0OOO000O =CTk .CTkFrame (master =OO00O000OO00O0OO0 ,width =400 ,height =400 ,fg_color ="transparent") 
            O00OOOO0O0OOO000O .grid (row =1 ,column =0 ,padx =25 ) 
            OO0OO00OO00OO0OO0 =CTk .CTkLabel (master =O00OOOO0O0OOO000O ,text ="Name",font =("Arial",17 )) 
            OO0OO00OO00OO0OO0 .grid (row =0 ,column =0 ) 
            OO000O0OO0OOOO000 =b3bb3bb3b3b3b3b (O00OOOO0O0OOO000O, OOO000OO0O0OOOOO0)
            OO000O0OO0OOOO000 .grid (row =0 ,column =1 ,columnspan =2 ) 
            OLOLOLOLO_0 (OO00O000OO00O0OO0, O00OOOO0O0OOO000O, OOOOO0OOO0O0O000O, OOO00OOOO00000OO0, OOO000OO0O0OOOOO0, OO000O0OO0OOOO000)
        OOO00OOOO00000OO0 .withdraw () 
    else : 
        CTkMessagebox (title ="Error",message ="Invalid username or password",icon ="cancel") 
def kokokokoo1 (O0O0O000O0OOO0OOO :b3bb3bb3b3b3b3b, OO00O00OO0O0OO00O :b3bb3bb3b3b3b3b):
    OOO0000O0000O0OOO =O0O0O000O0OOO0OOO .O0O0O00oo0 ()
    O00000OOOOO0OO0O0 =OO00O00OO0O0OO00O .O0O0O00oo0 ()
    O0O0OOOOO0000OO00 =a_____9___j (OOO0000O0000O0OOO, O00000OOOOO0OO0O0)
    return OOO0000O0000O0OOO ,O00000OOOOO0OO0O0 ,O0O0OOOOO0000OO00  
def a11_2a (OOOOO00000OO00OO0 :CTk .CTk, O0OOO0O0OO000O00O :bool):
    OOOOO00000OO00OO0 .destroy () 
    start_ (O0OOO0O0OO000O00O ) 
def jjj0_o (O0OO0OOO000OO00OO :str, O0O0O0OOO0O0000OO :CTk .CTk, O00000OOO0OOO0OO0 :bool)->None :
    O0OOOOO0O0O0OOO0O =CTk .CTkToplevel (O0O0O0OOO0O0000OO ) 
    O0OOOOO0O0O0OOO0O .title ('Account') 
    O0OOOOO0O0O0OOO0O .geometry ("700x470") 
    OO0O0OO0OOO0OO0OO =CTk .CTkImage (dark_image =Image .open ("art1.jpg"),size =(320 ,470 )) 
    OOOOOO0O0000O0O00 =CTk .CTkLabel (master =O0OOOOO0O0O0OOO0O ,text ="",image =OO0O0OO0OOO0OO0OO ) 
    OOOOOO0O0000O0O00 .grid (row =0 ,column =1 ,rowspan =2 ) 
    O00OOO0OOOOOOOOOO =CTk .CTkLabel (master =O0OOOOO0O0O0OOO0O ,text =f"WELCOME, {O0OO0OOO000OO00OO}.\n" f" Please, enter name to know gender and \n" f"enter max size of fact about cats",font =("Arial",15 )) 
    O00OOO0OOOOOOOOOO .grid (row =0 ,column =0 ) 
    OOO0O00000O0OOO0O =CTk .CTkFrame (master =O0OOOOO0O0O0OOO0O ,width =400 ,height =400 ,fg_color ="transparent") 
    OOO0O00000O0OOO0O .grid (row =1 ,column =0 ,padx =25 ) 
    OOO0O0O0OO00O00OO =CTk .CTkLabel (master =OOO0O00000O0OOO0O ,text ="Name",font =("Arial",17 )) 
    OOO0O0O0OO00O00OO .grid (row =0 ,column =0 ) 
    O00O0O0000000OO00 =b3bb3bb3b3b3b3b (OOO0O00000O0OOO0O, O00000OOO0OOO0OO0)
    O00O0O0000000OO00 .grid (row =0 ,column =1 ,columnspan =2 ) 
    OLOLOLOLO_0 (O0OOOOO0O0O0OOO0O, OOO0O00000O0OOO0O, O0OO0OOO000OO00OO, O0O0O0OOO0O0000OO, O00000OOO0OOO0OO0, O00O0O0000000OO00)
def annn82 ():
    return None  
def OLOLOLOLO_0 (O00O0O0O0O000O0O0, O0O00OO0000OOO00O, OOOOOO000O000OO0O :str, OO0OO0OOOOOO000OO :CTk .CTk, OOO00O0OOO0O00OO0 :bool, O0OO00OO0OO0000O0)->None :
    OO0000O00OOO0O000 =CTk .CTkLabel (master =O0O00OO0000OOO00O ,text ="Size",font =("Arial",17 )) 
    OO0000O00OOO0O000 .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
    O0O0OO0O000OOOO00 =b3bb3bb3b3b3b3b (O0O00OO0000OOO00O, OOO00O0OOO0O00OO0)
    O0O0OO0O000OOOO00 .grid (row =1 ,column =1 ,columnspan =2 ) 
    OOO0OOO00OOOO0OOO =CTk .CTkButton (master =O0O00OO0000OOO00O, text ="GO", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :f6ff66f6f6f6f6 (O0OO00OO0OO0000O0, O0O0OO0O000OOOO00, O0O00OO0000OOO00O, OOO00O0OOO0O00OO0))
    OOO0OOO00OOOO0OOO .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
    O00O0O0O0O000O0O0 .protocol ("WM_DELETE_WINDOW", lambda :a11_2a (OO0OO0OOOOOO000OO, OOO00O0OOO0O00OO0))
def f6ff66f6f6f6f6 (O0OOO0OO0O0OO0000 :b3bb3bb3b3b3b3b, O0OO00O0OO0O000OO :b3bb3bb3b3b3b3b, O0OO00O000O0OOO0O :CTk .CTkToplevel, OOO0OOOO00O0OO000 :bool)->None :
    O0O00OO0OO000O0OO =O0OOO0OO0O0OO0000 .O0O0O00oo0 ()
    OO0O0O000O00O0O0O =O0OO00O0OO0O000OO .O0O0O00oo0 ()
    if OOO0OOOO00O0OO000 : 
        O0O00O0000OO0O00O =O0OO00O000O0OOO0O .children ['!ctkbutton'] 
        O0O00O0000OO0O00O .configure (state =CTk .DISABLED ) 
        O0OO00O000O0OOO0O .after (5000 ,lambda :O0O00O0000OO0O00O .configure (state =tk .NORMAL )) 
    if OOO0OOOO00O0OO000 : 
        if not h8h8 (O0O00OO0OO000O0OO , OO0O0O000O00O0O0O):
            CTkMessagebox (title ="Error",message ="Invalid data",icon ="cancel") 
            return  
    O0OO0OOO0O0OO0O0O =iiiiii8ii8i8i8 (O0O00OO0OO000O0OO, OO0O0O000O00O0O0O)
    iliilililil7 (O0OO0OOO0O0OO0O0O, O0OO00O000O0OOO0O)
def s4s444s4s4s4s4s4s4 (OO0OO000000000000 :str ,OOO00O0O0OOOOOOOO :str )->dict :
    OOO0O0OO0000O0000 =a1a1oo0o0 ()
    if OO0OO000000000000 in OOO0O0OO0000O0000 and OOO0O0OO0000O0000 [OO0OO000000000000 ]['password']==OOO00O0O0OOOOOOOO : 
        return OOO0O0OO0000O0000 [OO0OO000000000000 ] 
    else : 
        return annn82 ()
def h8h8 (O00O000000OO0O00O :str, OOOOO000O0OOOO0OO :str)->bool :
    try : 
        OO00OO0OO0OO0O0OO =len (O00O000000OO0O00O ) 
        O0000O0O00O0O00OO =int (OOOOO000O0OOOO0OO ) 
        if (15 <=OO00OO0OO0OO0O0OO or OO00OO0OO0OO0O0OO <=1 )or (70 <O0000O0O00O0O00OO or O0000O0O00O0O00OO <=20 )or not (re .fullmatch ("^[A-z '-]+$",O00O000000OO0O00O )): 
            return False  
        else : 
            return True  
    except ValueError : 
        return False  
def a2_00OO (O00OO0O00O0O0O00O :str, OOO00O0OOOO0O0O0O :str):
    O0000O00OOOO00O0O =f'https://api.genderize.io?name={O00OO0O00O0O0O00O}' 
    O000O0O0O000OOO0O =requests .get (O0000O00OOOO00O0O ) 
    O00O00O0OOOO0O0O0 =O000O0O0O000OOO0O .json () 
    O0000O00OOOO00O0O =f'https://catfact.ninja/fact?max_length={OOO00O0OOOO0O0O0O}' 
    O0O00O0O0O0O0000O =requests .get (O0000O00OOOO00O0O ) 
    O00OO00OOO0O0OO00 =O0O00O0O0O0O0000O .json () 
    return O000O0O0O000OOO0O ,O0O00O0O0O0O0000O ,O00O00O0OOOO0O0O0 ,O00OO00OOO0O0OO00  
def get_OOO1 (O00O00OO0OO0O0O00 :str ,O0O00OOO0000O0O0O :str ):
    OOOO00000000O0OO0 =f'https://api.genderize.io?name={O00O00OO0OO0O0O00}' 
    OOOO00OO00OOOOO0O =requests .get (OOOO00000000O0OO0 ) 
    OO0OO0O0O00OO0000 =OOOO00OO00OOOOO0O .json () 
    OOOO00000000O0OO0 =f'https://catfact.ninja/fact?max_length={O0O00OOO0000O0O0O}' 
    O000OOO0OOO0O0OO0 =requests .get (OOOO00000000O0OO0 ) 
    O00O0O00OO0OO00OO =O000OOO0OOO0O0OO0 .json () 
    return OOOO00OO00OOOOO0O ,O000OOO0OOO0O0OO0 ,OO0OO0O0O00OO0000 ,O00O0O00OO0OO00OO  
def aa3a3a3a3a3 (O0000OOOO00000OO0 :str, OO0OOO000O00OOOO0 :CTk .CTk, O00000OO0O0OOO00O :bool)->None :
    OOOOO00000O0OO0O0 =CTk .CTkToplevel (OO0OOO000O00OOOO0 ) 
    OOOOO00000O0OO0O0 .title ('Account') 
    OOOOO00000O0OO0O0 .geometry ("700x470") 
    OO00OOO0OO0OOOO00 =CTk .CTkImage (dark_image =Image .open ("cat2.jpg"),size =(300 ,470 )) 
    OO0000O0O0OOO0OO0 =CTk .CTkLabel (master =OOOOO00000O0OO0O0 ,text ="",image =OO00OOO0OO0OOOO00 ) 
    OO0000O0O0OOO0OO0 .grid (row =0 ,column =0 ,rowspan =2 ) 
    OOO0O0OO0O000OO00 =CTk .CTkLabel (master =OOOOO00000O0OO0O0 ,text =f"WELCOME, {O0000OOOO00000OO0}.\n You can add user",font =("Arial",20 )) 
    OOO0O0OO0O000OO00 .grid (row =0 ,column =1 ,columnspan =3 ) 
    O000O0OOO00000O00 =CTk .CTkFrame (master =OOOOO00000O0OO0O0 ,width =400 ,height =400 ,fg_color ="transparent") 
    O000O0OOO00000O00 .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
    OO0O0OOO0OOOO0O0O =CTk .CTkLabel (master =O000O0OOO00000O00 ,text ="Username",font =("Arial",17 )) 
    OO0O0OOO0OOOO0O0O .grid (row =0 ,column =0 ) 
    O000OOOOOO0OO00O0 =b3bb3bb3b3b3b3b (O000O0OOO00000O00, O00000OO0O0OOO00O)
    O000OOOOOO0OO00O0 .grid (row =0 ,column =1 ,columnspan =2 ) 
    OOOO0OO000OO0OOO0 =CTk .CTkLabel (master =O000O0OOO00000O00 ,text ="Password",font =("Arial",17 )) 
    OOOO0OO000OO0OOO0 .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
    OOOO00OOO00O0O000 =b3bb3bb3b3b3b3b (O000O0OOO00000O00, O00000OO0O0OOO00O, show ='*')
    OOOO00OOO00O0O000 .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
    OO0O0OO0000O00OOO =CTk .CTkButton (master =O000O0OOO00000O00, text ="Add User", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :addOOO0 (O000OOOOOO0OO00O0 .O0O0O00oo0 (), OOOO00OOO00O0O000 .O0O0O00oo0 (), O00000OO0O0OOO00O))
    OO0O0OO0000O00OOO .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
    OOOOO00000O0OO0O0 .protocol ("WM_DELETE_WINDOW", lambda :a11_2a (OO0OOO000O00OOOO0, O00000OO0O0OOO00O))
def addOOO0 (OO00O0O0O0OO00O00 :str, O00O000OO0O000000 :str, OO0OOOO00OO00OO00 :bool)->None :
    O0O0O0O0O0OO0OO00 =y7y7y7y7 ()
    if OO0OOOO00OO00OO00 : 
        if OO00O0O0O0OO00O00 not in O0O0O0O0O0OO0OO00 : 
            O0O0O0O0O0OO0OO00 [OO00O0O0O0OO00O00 ]={'password':O00O000OO0O000000 ,'role':'user'} 
            with open (USERS_PATH ,'w')as O0OO0OO0000000O0O : 
                json .dump (O0O0O0O0O0OO0OO00 ,O0OO0OO0000000O0O ) 
            CTkMessagebox (title ="Success",message ="You added new user",icon ="check") 
        else : 
            CTkMessagebox (title ="Warning",message ="User already exists",icon ="warning") 
    else : 
        O0O0O0O0O0OO0OO00 [OO00O0O0O0OO00O00 ]={'password':O00O000OO0O000000 ,'role':'user'} 
        with open (USERS_PATH ,'w')as O0OO0OO0000000O0O : 
            json .dump (O0O0O0O0O0OO0OO00 ,O0OO0OO0000000O0O ) 
def start_ (OO00OOO0OO0O000O0 :bool )->None : 
    O0O000OO0O000O000 =CTk .CTk () 
    O0O000OO0O000O000 .geometry ("700x470") 
    O0O000OO0O000O000 .title ('Authentication') 
    O0O000OO0O000O000 .resizable (False ,False ) 
    CTk .set_appearance_mode ("dark") 
    CTk .set_default_color_theme ("green") 
    O00OOOOOOO0OOO0OO =CTk .CTkImage (dark_image =Image .open ("cat1.jpg"),size =(300 ,470 )) 
    OOO00OOOO0OOO0OOO =CTk .CTkLabel (master =O0O000OO0O000O000 ,text ="",image =O00OOOOOOO0OOO0OO ) 
    OOO00OOOO0OOO0OOO .grid (row =0 ,column =0 ,rowspan =2 ) 
    OO000OO0O000O0OOO =CTk .CTkLabel (master =O0O000OO0O000O000 ,text ="~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~",font =("Arial",20 )) 
    OO000OO0O000O0OOO .grid (row =0 ,column =1 ,columnspan =3 ) 
    O0O0OO0OO00O00O0O =CTk .CTkFrame (master =O0O000OO0O000O000 ,width =400 ,height =400 ,fg_color ="transparent") 
    O0O0OO0OO00O00O0O .grid (row =1 ,column =1 ,padx =25 ,pady =10 ) 
    OO00OO0O000O0OOO0 =CTk .CTkLabel (master =O0O0OO0OO00O00O0O ,text ="Username",font =("Arial",17 )) 
    OO00OO0O000O0OOO0 .grid (row =0 ,column =0 ) 
    O00OO000O0O000000 =b3bb3bb3b3b3b3b (O0O0OO0OO00O00O0O, OO00OOO0OO0O000O0)
    O00OO000O0O000000 .grid (row =0 ,column =1 ,columnspan =2 ) 
    OO00O0OOOO0OO0O00 =CTk .CTkLabel (master =O0O0OO0OO00O00O0O ,text ="Password",font =("Arial",17 )) 
    OO00O0OOOO0OO0O00 .grid (row =1 ,column =0 ,ipady =10 ,pady =15 ) 
    O0OOOOO0OOOOO0OOO =b3bb3bb3b3b3b3b (O0O0OO0OO00O00O0O, OO00OOO0OO0O000O0, show ='*')
    O0OOOOO0OOOOO0OOO .grid (row =1 ,column =1 ,columnspan =2 ,pady =45 ) 
    O0OOO0O0O00O0O0OO =CTk .CTkButton (master =O0O0OO0OO00O00O0O, text ="Login", width =330, height =50, hover_color ="PaleGreen3", text_color ="black", corner_radius =20, command =lambda :jkjkjkjkjkjkjkjkjk_0 (O00OO000O0O000000, O0OOOOO0OOOOO0OOO, O0O000OO0O000O000, OO00OOO0OO0O000O0))
    O0OOO0O0O00O0O0OO .grid (row =2 ,column =0 ,pady =50 ,columnspan =2 ) 
    O0O000OO0O000O000 .mainloop () 
def y7y7y7y7 ():
    O0O000O00O000O00O =a1a1oo0o0 ()
    return O0O000O00O000O00O  
