from tkinter import *
import tkinter.font as font 
from tkinter import messagebox
from PIL import ImageTk,Image
import csv

root=Tk()

root.title("FOODIE")
root.iconbitmap('C:\PROJECT\EAT.ico')
root.geometry("313x470")

myFont = font.Font(family='Courier', size=10, weight='bold')

def newwindow():
        global nw
        root.withdraw()
        nw=Toplevel(root)
        nw.title("FOODIE")
        nw.iconbitmap("EAT.ico")
        nw.geometry("1530x796")
        back=PhotoImage(file="pistha4.gif")
        p=Label(nw,image=back)
        g=Label(nw,text="FOODIE")
        g.config(font=("Helvetica",65))
        p.place(x=0,y=0) 
        g.place(x=700,y=50)
        logo=PhotoImage(file="EAT1.gif")
        b=Label(image=logo)
        but=Button(nw,image=logo,padx=20,pady=20)
        but.place(x=500,y=50)


        order_but=PhotoImage(file="milagu.gif")
        his_but=PhotoImage(file="sukku.gif")
        img_1=Label(image=order_but)
        img_2=Label(image=his_but)
        mybutton_1=Button(nw,image=order_but,padx=500,pady=450,borderwidth=0,command=new)
        mybutton_2=Button(nw,image=his_but,padx=500,pady=450,borderwidth=0,command=dew)
        mybutton_3=Button(nw,text="Order Now",padx=140,command=new)
        mybutton_3.config(font=("Helvetica",30))
        mybutton_4=Button(nw,text="Bill History",padx=143,command=dew)
        mybutton_4.config(font=("Helvetica",30))
        mybutton_1.place(x=100,y=400)
        mybutton_2.place(x=900,y=400)
        mybutton_3.place(x=100,y=330)
        mybutton_4.place(x=900,y=330) 
        
        
        
        nw.mainloop()
        

def new():
        global nw
        global pw
        nw.withdraw()
        pw=Toplevel(root)
        pw.title("FOODIE")
        pw.iconbitmap("EAT.ico")
        pw.geometry("1530x796")
        sack=PhotoImage(file="pistha4.gif")
        ul=Label(pw,image=sack)
        po=Label(pw,text="FOODIE")
        po.config(font=("Helvetica",65))
        ul.place(x=0,y=0) 
        po.place(x=700,y=50)
        qogo=PhotoImage(file="EAT1.gif")
        bal=Label(image=qogo)
        butto=Button(pw,image=qogo,padx=20,pady=20)
        butto.place(x=500,y=50)


        veg_but=PhotoImage(file="veg.gif")
        nonveg_but=PhotoImage(file="non veg.gif")
        pizzas_but=PhotoImage(file="pizzas.gif")
        burgers_but=PhotoImage(file="burgers.gif")
        icecreams_but=PhotoImage(file="icecreams.gif")
        beverages_but=PhotoImage(file="beverages.gif")
        imge_1=Label(image=veg_but)
        imge_2=Label(image=nonveg_but)
        imge_3=Label(image=pizzas_but)
        imge_4=Label(image=burgers_but)
        imge_5=Label(image=icecreams_but)
        imge_6=Label(image=beverages_but)
        mybut_1=Button(pw,image=veg_but,padx=500,pady=450,borderwidth=0,command=veg)
        mybut_2=Button(pw,image=nonveg_but,padx=500,pady=450,borderwidth=0,command=nonveg)
        mybut_3=Button(pw,image=pizzas_but,padx=500,pady=450,borderwidth=0,command=pizzas)
        mybut_4=Button(pw,image=burgers_but,padx=500,pady=450,borderwidth=0,command=burgers)
        mybut_5=Button(pw,image=icecreams_but,padx=500,pady=450,borderwidth=0,command=icecreams)
        mybut_6=Button(pw,image=beverages_but,padx=500,pady=450,borderwidth=0,command=beverages) 
        mybutton_5=Button(pw,text="VEGETARIAN",padx=80,command=veg)
        mybutton_5.config(font=("Helvetica",10))
        mybutton_6=Button(pw,text="NON VEGETARIAN",padx=64,command=nonveg)
        mybutton_6.config(font=("Helvetica",10))
        mybutton_7=Button(pw,text="PIZZAS",padx=100,command=pizzas)
        mybutton_7.config(font=("Helvetica",10))
        mybutton_8=Button(pw,text="BURGERS",padx=90,command=burgers)
        mybutton_8.config(font=("Helvetica",10))
        mybutton_9=Button(pw,text="ICE CREAMS",padx=81,command=icecreams)
        mybutton_9.config(font=("Helvetica",10))
        mybutton_10=Button(pw,text="BEVERAGES",padx=81,command=beverages)
        mybutton_10.config(font=("Helvetica",10))
        mybutton_11=Button(pw,text="ORDER HISTORY",padx=30,pady=10,command=dew)
        mybutton_11.config(font=("Helvetica",10))
        mybut_1.place(x=50,y=250)
        mybutton_5.place(x=50,y=450)
        mybut_2.place(x=425,y=250)
        mybutton_6.place(x=425,y=450)
        mybut_3.place(x=800,y=250)
        mybutton_7.place(x=800,y=450)
        mybut_4.place(x=1175,y=250)
        mybutton_8.place(x=1175,y=450)
        mybut_5.place(x=425,y=500)
        mybutton_9.place(x=425,y=700)
        mybut_6.place(x=800,y=500)
        mybutton_10.place(x=800,y=700)
        mybutton_11.place(x=1200,y=50)
        
        
        pw.mainloop()
                
        
        
def quantity():
        global qu
        global que
        global fish_items
        global nv_dict
        global nhy
        nhy=fish_items.get(ANCHOR)
        order_item.append(nhy)
        if str(nhy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu=Toplevel(root)
                qu.title("FOODIE")
                qu.iconbitmap("EAT.ico")
                qul1=Label(qu,text=nhy)
                qul2=Label(qu,text="TOTAL PRICE: "+str(nv_dict[nhy])+'  *  ')
                que=Entry(qu)
                qub1=Button(qu,text='ORDER',command=bill_1)
                qub2=Button(qu,text='ORDER MORE',command=bill_16)
                qul1.grid(row=0,column=0,columnspan=2)
                qul2.grid(row=1,column=0)
                que.grid(row=1,column=1)
                qub1.grid(row=2,column=0)
                qub2.grid(row=2,column=1)
                
        

def quantity1():
        global qu1
        global que1
        global egg_items
        global nv_dict
        global eggy
        eggy=egg_items.get(ANCHOR)
        order_item.append(eggy)
        if str(eggy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu1=Toplevel(root)
                qu1.title("FOODIE")
                qu1.iconbitmap("EAT.ico") 
                qul3=Label(qu1,text=eggy)
                qul4=Label(qu1,text="TOTAL PRICE: "+str(nv_dict[eggy])+'  *  ')
                que1=Entry(qu1)
                qub3=Button(qu1,text='ORDER',command=bill_2)
                qub4=Button(qu1,text='ORDER MORE',command=bill_17)
                qul3.grid(row=0,column=0,columnspan=2)
                qul4.grid(row=1,column=0) 
                que1.grid(row=1,column=1)
                qub3.grid(row=2,column=0)
                qub4.grid(row=2,column=1) 
        


def quantity2():
        global qu2
        global que2
        global fn_items
        global nv_dict
        global fny
        fny=fn_items.get(ANCHOR)
        order_item.append(fny)
        if str(fny)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu2=Toplevel(root)
                qu2.title("FOODIE")
                qu2.iconbitmap("EAT.ico")
                qul5=Label(qu2,text=fny)
                qul6=Label(qu2,text="TOTAL PRICE: "+str(nv_dict[fny])+'  *  ')
                que2=Entry(qu2)
                qub5=Button(qu2,text='ORDER',command=bill_3)
                qub6=Button(qu2,text='ORDER MORE',command=bill_18)
                qul5.grid(row=0,column=0,columnspan=2)
                qul6.grid(row=1,column=0) 
                que2.grid(row=1,column=1)
                qub5.grid(row=2,column=0)
                qub6.grid(row=2,column=1) 
        


def quantity3():
        global qu3
        global que3
        global soup_items
        global nv_dict
        global spy
        spy=soup_items.get(ANCHOR)
        order_item.append(spy)
        if str(spy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu3=Toplevel(root)
                qu3.title("FOODIE")
                qu3.iconbitmap("EAT.ico")
                qul7=Label(qu3,text=spy)
                qul8=Label(qu3,text="TOTAL PRICE: "+str(nv_dict[spy])+'  *  ')
                que3=Entry(qu3)
                qub7=Button(qu3,text='ORDER',command=bill_4)
                qub8=Button(qu3,text='ORDER MORE',command=bill_19)
                qul7.grid(row=0,column=0,columnspan=2)
                qul8.grid(row=1,column=0) 
                que3.grid(row=1,column=1)
                qub7.grid(row=2,column=0)
                qub8.grid(row=2,column=1)

def quantity4():
        global qu4
        global que4
        global gravy_items
        global nv_dict
        global gry
        gry=gravy_items.get(ANCHOR)
        order_item.append(gry)
        if str(gry)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu4=Toplevel(root)
                qu4.title("FOODIE")
                qu4.iconbitmap("EAT.ico")
                qul9=Label(qu4,text=gry)
                qul10=Label(qu4,text="TOTAL PRICE: "+str(nv_dict[gry])+'  *  ')
                que4=Entry(qu4)
                qub9=Button(qu4,text='ORDER',command=bill_5)
                qub10=Button(qu4,text='ORDER MORE',command=bill_20)
                qul9.grid(row=0,column=0,columnspan=2)
                qul10.grid(row=1,column=0) 
                que4.grid(row=1,column=1)
                qub9.grid(row=2,column=0)
                qub10.grid(row=2,column=1)

def quantity5():
        global qu5
        global que5
        global mutton_items
        global nv_dict
        global mny
        mny=mutton_items.get(ANCHOR)
        order_item.append(mny)
        if str(mny)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu5=Toplevel(root)
                qu5.title("FOODIE")
                qu5.iconbitmap("EAT.ico")
                qul11=Label(qu5,text=mny)
                qul12=Label(qu5,text="TOTAL PRICE: "+str(nv_dict[mny])+'  *  ')
                que5=Entry(qu5)
                qub11=Button(qu5,text='ORDER',command=bill_6)
                qub12=Button(qu5,text='ORDER MORE',command=bill_21)
                qul11.grid(row=0,column=0,columnspan=2)
                qul12.grid(row=1,column=0) 
                que5.grid(row=1,column=1)
                qub11.grid(row=2,column=0)
                qub12.grid(row=2,column=1)

def quantity6():
        global qu6
        global que6
        global chicken_items
        global nv_dict
        global cny
        cny=chicken_items.get(ANCHOR)
        order_item.append(cny)
        if str(cny)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu6=Toplevel(root)
                qu6.title("FOODIE")
                qu6.iconbitmap("EAT.ico")
                qul13=Label(qu6,text=cny)
                qul14=Label(qu6,text="TOTAL PRICE: "+str(nv_dict[cny])+'  *  ')
                que6=Entry(qu6)
                qub13=Button(qu6,text='ORDER',command=bill_7)
                qub14=Button(qu6,text='ORDER MORE',command=bill_22)
                qul13.grid(row=0,column=0,columnspan=2)
                qul14.grid(row=1,column=0) 
                que6.grid(row=1,column=1)
                qub13.grid(row=2,column=0)
                qub14.grid(row=2,column=1)

def quantity7():
        global qu7
        global que7
        global poultry_items
        global nv_dict
        global pty 
        pty=poultry_items.get(ANCHOR)
        order_item.append(pty)
        if str(pty)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu7=Toplevel(root)
                qu7.title("FOODIE")
                qu7.iconbitmap("EAT.ico")
                qul15=Label(qu7,text=pty)
                qul16=Label(qu7,text="TOTAL PRICE: "+str(nv_dict[pty])+'  *  ')
                que7=Entry(qu7)
                qub15=Button(qu7,text='ORDER',command=bill_8)
                qub16=Button(qu7,text='ORDER MORE',command=bill_23)
                qul15.grid(row=0,column=0,columnspan=2)
                qul16.grid(row=1,column=0) 
                que7.grid(row=1,column=1)
                qub15.grid(row=2,column=0)
                qub16.grid(row=2,column=1)

def quantity8():
        global qu8
        global que8
        global pizzas_items
        global pz_dict
        global pzy
        pzy=pizzas_items.get(ANCHOR)
        order_item.append(pzy)
        if str(pzy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu8=Toplevel(root)
                qu8.title("FOODIE")
                qu8.iconbitmap("EAT.ico")
                qul17=Label(qu8,text=pzy)
                qul18=Label(qu8,text="TOTAL PRICE: "+str(pz_dict[pzy])+'  *  ')
                que8=Entry(qu8)
                qub17=Button(qu8,text='ORDER',command=bill_9)
                qub18=Button(qu8,text='ORDER MORE',command=bill_24)
                qul17.grid(row=0,column=0,columnspan=2)
                qul18.grid(row=1,column=0) 
                que8.grid(row=1,column=1)
                qub17.grid(row=2,column=0)
                qub18.grid(row=2,column=1)

def quantity9():
        global qu9
        global que9
        global combos_items
        global pz_dict
        global cby
        cby=combos_items.get(ANCHOR)
        order_item.append(cby)
        if str(cby)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu9=Toplevel(root)
                qu9.title("FOODIE")
                qu9.iconbitmap("EAT.ico")
                qul19=Label(qu9,text=cby)
                qul20=Label(qu9,text="TOTAL PRICE: "+str(pz_dict[cby])+'  *  ')
                que9=Entry(qu9)
                qub19=Button(qu9,text='ORDER',command=bill_10)
                qub20=Button(qu9,text='ORDER MORE',command=bill_25)
                qul19.grid(row=0,column=0,columnspan=2)
                qul20.grid(row=1,column=0) 
                que9.grid(row=1,column=1)
                qub19.grid(row=2,column=0)
                qub20.grid(row=2,column=1)

def quantity10():
        global qu10
        global que10
        global r_icec
        global ic_dict
        global r_icy
        r_icy=r_icec.get(ANCHOR)
        order_item.append(r_icy)
        if str(r_icy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu10=Toplevel(root)
                qu10.title("FOODIE")
                qu10.iconbitmap("EAT.ico")
                qul21=Label(qu10,text=r_icy)
                qul22=Label(qu10,text="TOTAL PRICE: "+str(ic_dict[r_icy])+'  *  ')
                que10=Entry(qu10)
                qub21=Button(qu10,text='ORDER',command=bill_11)
                qub22=Button(qu10,text='ORDER MORE',command=bill_26)
                qul21.grid(row=0,column=0,columnspan=2)
                qul22.grid(row=1,column=0) 
                que10.grid(row=1,column=1)
                qub21.grid(row=2,column=0)
                qub22.grid(row=2,column=1)

def quantity11():
        global qu11
        global c_icec
        global ic_dict
        global c_icy
        c_icy=c_icec.get(ANCHOR)
        order_item.append(c_icy)
        if str(c_icy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu11=Toplevel(root)
                qu11.title("FOODIE")
                qu11.iconbitmap("EAT.ico")
                qul23=Label(qu11,text=c_icy)
                qul24=Label(qu11,text="TOTAL PRICE: "+str(ic_dict[c_icy])+'  *  ')
                que11=Entry(qu11)
                qub23=Button(qu11,text='ORDER',command=bill_12)
                qub24=Button(qu11,text='ORDER MORE',command=bill_27)
                qul23.grid(row=0,column=0,columnspan=2)
                qul24.grid(row=1,column=0) 
                que11.grid(row=1,column=1)
                qub23.grid(row=2,column=0)
                qub24.grid(row=2,column=1)

def quantity12():
        global qu12
        global que12
        global burgers_items
        global bg_dict
        global bgy
        bgy=burgers_items.get(ANCHOR)
        order_item.append(bgy)
        if str(bgy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu12=Toplevel(root)
                qu12.title("FOODIE")
                qu12.iconbitmap("EAT.ico")
                qul25=Label(qu12,text=bgy)
                qul26=Label(qu12,text="TOTAL PRICE: "+str(bg_dict[bgy])+'  *  ')
                que12=Entry(qu12)
                qub25=Button(qu12,text='ORDER',command=bill_13)
                qub26=Button(qu12,text='ORDER MORE',command=bill_28)
                qul25.grid(row=0,column=0,columnspan=2)
                qul26.grid(row=1,column=0) 
                que12.grid(row=1,column=1)
                qub25.grid(row=2,column=0)
                qub26.grid(row=2,column=1)      

def quantity13():
        global qu13
        global que13
        global veg_items
        global veg_dict
        global vgy
        vgy=veg_items.get(ANCHOR)
        order_item.append(vgy)
        if str(vgy)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu13=Toplevel(root)
                qu13.title("FOODIE")
                qu13.iconbitmap("EAT.ico")
                qul27=Label(qu13,text=vgy)
                qul28=Label(qu13,text="TOTAL PRICE: "+str(veg_dict[vgy])+'  *  ')
                que13=Entry(qu13,width=50)
                qub27=Button(qu13,text='ORDER',command=bill_14)
                qub28=Button(qu13,text='ORDER MORE',command=bill_29)
                qul27.grid(row=0,column=0,columnspan=2)
                qul28.grid(row=1,column=0) 
                que13.grid(row=1,column=1)
                qub27.grid(row=2,column=0)
                qub28.grid(row=2,column=1)


def quantity14():
        global qu14
        global que14
        global beverages_items
        global bvg_dict
        global bry
        bry=beverages_items.get(ANCHOR)
        order_item.append(bry)
        if str(bry)=='':
                messagebox.showerror("ERROR","You have not ordered anything")
        else:
                qu14=Toplevel(root)
                qu14.title("FOODIE")
                qu14.iconbitmap("EAT.ico")
                qul29=Label(qu13,text=vgy)
                qul30=Label(qu13,text="TOTAL PRICE: "+str(bvg_dict[bry])+'  *  ')
                que14=Entry(qu13,width=50)
                qub29=Button(qu13,text='ORDER',command=bill_15)
                qub30=Button(qu13,text='ORDER MORE',command=bill_30)
                qul29.grid(row=0,column=0,columnspan=2)
                qul30.grid(row=1,column=0) 
                que14.grid(row=1,column=1)
                qub29.grid(row=2,column=0)
                qub30.grid(row=2,column=1)
        
                
def back1():
        global veg
        veg.withdraw()
        new()

def back2():
        global nv
        nv.withdraw()
        new()

def back3():
        global pz
        pz.withdraw()
        new()

def back4():
        global bu
        bu.withdraw()
        new()

def back5():
        global ic
        ic.withdraw()
        new()

def back6():
        global br
        br.withdraw()
        new()
                
def bill_1():
        global qu
        global nv_dict
        global nhy
        global order_item
        global que
        physics=que.get()
        no_item=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item))+'\t'+nhy+'\t'+'\t'+(str(physics))+'\t'+(str(nv_dict[nhy]*int(physics)))+'\n')
        f.close()
        qu.withdraw()

def bill_2():
        global qu1
        global nv_dict
        global eggy
        global order_item
        global que1
        physics1=que1.get()
        no_item1=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item1))+'\t'+eggy+'\t'+'\t'+(str(physics1))+'\t'+(str(nv_dict[eggy]*int(physics1)))+'\n')
        f.close()
        qu1.withdraw()

        
def bill_3():
        global qu2
        global nv_dict
        global fny
        global order_item
        global que2
        physics2=que2.get()
        no_item2=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item2))+'\t'+fny+'\t'+'\t'+(str(physics2))+'\t'+(str(nv_dict[fny]*int(physics2)))+'\n')
        f.close()
        qu2.withdraw()
                                                                
def bill_4():
        global qu3
        global nv_dict
        global spy
        global order_item
        global que3
        physics3=que3.get()
        no_item3=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item3))+'\t'+spy+'\t'+'\t'+(str(physics3))+'\t'+(str(nv_dict[spy]*int(physics3)))+'\n')
        f.close()
        qu3.withdraw()        
        
def bill_5():
        global qu4
        global nv_dict
        global gry
        global order_item
        global que4
        physics4=que4.get()
        no_item4=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item4))+'\t'+gry+'\t'+'\t'+(str(physics4))+'\t'+(str(nv_dict[gry]*int(physics4)))+'\n')
        f.close()
        qu4.withdraw()
        
def bill_6():
        global qu5
        global nv_dict
        global mny
        global order_item
        global que5
        physics5=que5.get()
        no_item5=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item5))+'\t'+mny+'\t'+'\t'+(str(physics5))+'\t'+(str(nv_dict[mny]*int(physics5)))+'\n')
        f.close()
        qu5.withdraw()


def bill_7():
        global qu6
        global nv_dict
        global cny
        global order_item
        global que6
        physics6=que6.get()
        no_item6=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item6))+'\t'+cny+'\t'+'\t'+(str(physics6))+'\t'+(str(nv_dict[cny]*int(physics6)))+'\n')
        f.close()
        qu6.withdraw()


def bill_8():
        global qu7
        global nv_dict
        global pty
        global order_item
        global que7
        physics7=que7.get()
        no_item7=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item7))+'\t'+pty+'\t'+'\t'+(str(physics7))+'\t'+(str(nv_dict[pty]*int(physics7)))+'\n')
        f.close()
        qu7.withdraw()
        
def bill_9():
        global qu8
        global pz_dict
        global pzy
        global order_item
        global que8
        physics8=que8.get()
        no_item8=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item8))+'\t'+pzy+'\t'+'\t'+(str(physics8))+'\t'+(str(pz_dict[pzy]*int(physics8)))+'\n')
        f.close()
        qu8.withdraw()
        
def bill_10():
        global qu9
        global pz_dict
        global cby
        global order_item
        global que9
        physics9=que9.get()
        no_item9=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item9))+'\t'+cby+'\t'+'\t'+(str(physics9))+'\t'+(str(pz_dict[cby]*int(physics9)))+'\n')
        f.close()
        qu9.withdraw()

def bill_11():
        global qu10
        global ic_dict
        global r_icy
        global order_item
        global que10
        physics10=que10.get()
        no_item10=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item10))+'\t'+r_icy+'\t'+'\t'+(str(physics10))+'\t'+(str(ic_dict[r_icy]*int(physics10)))+'\n')
        f.close()
        qu10.withdraw()

def bill_12():
        global qu11
        global ic_dict
        global c_icy
        global order_item
        global que11
        physics11=que11.get()
        no_item11=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item11))+'\t'+c_icy+'\t'+'\t'+(str(physics11))+'\t'+(str(ic_dict[c_icy]*int(physics11)))+'\n')
        f.close()
        qu11.withdraw()

def bill_13():
        global qu12
        global bg_dict
        global bgy
        global order_item
        global que12
        physics12=que12.get()
        no_item12=len(order_item)
        f=open("Bill.txt","a+")
        f.write('\n')
        f.write((str(no_item12))+'\t'+bgy+'\t'+'\t'+'\t'+(str(physics12))+'\t'+'\t'+'\t'+(str(bg_dict[bgy]*int(physics12)))+'\n')
        f.close()
        k=open("Bill.txt")
        k_read=k.read()
        k_window=Toplevel(qu12)
        k_window.title("BILL")
        k_lab=Text(k_window,width=100,height=40)
        k_lab.pack()
        k_lab.insert(END,k_read)
        k.close()
        
        qu12.withdraw()

def bill_14():
        global qu13
        global veg_dict
        global vgy
        global order_item
        global que13
        physics13=que13.get()
        no_item13=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item13))+'\t'+vgy+'\t'+'\t'+(str(physics13))+'\t'+(str(veg_dict[vgy]*int(physics13)))+'\n')
        f.close()
        qu13.withdraw()

def bill_15():
        global qu14
        global bvg_dict
        global bry
        global order_item
        global que14
        physics14=que14.get()
        no_item14=len(order_item)
        f=open("Bill.txt","a")
        f.write('\n')
        f.write((str(no_item14))+'\t'+bry+'\t'+'\t'+(str(physics14))+'\t'+(str(bvg_dict[bry]*int(physics14)))+'\n')
        f.close()
        qu14.withdraw()


        
def bill_16():
        global qu
        qu.withdraw()
        
def bill_17():
        global qu1
        qu1.withdraw()
        
def bill_18():
        global qu2
        qu2.withdraw()
        
def bill_19():
        global qu3
        qu3.withdraw()
        
def bill_20():
        global qu4
        qu4.withdraw()

def bill_21():
        global qu5
        qu5.withdraw()

def bill_22():
        global qu6
        qu6.withdraw()

def bill_23():
        global qu7
        qu7.withdraw()

def bill_24():
        global qu8
        qu8.withdraw()

def bill_25():
        global qu9
        qu9.withdraw()

def bill_26():
        global qu10
        qu10.withdraw()

def bill_27():
        global qu11
        qu11.withdraw()

def bill_28():
        global qu12
        qu12.withdraw()

def bill_29():
        global qu13
        qu13.withdraw()
        
def bill_30():
        global qu14
        qu14.withdraw()


        
def dew():
        mw=Toplevel(root)
        mw.title("FOODIE")
        mw.iconbitmap("EAT.ico")
        mw.geometry("1530x796")
        mack=PhotoImage(file="pistha4.gif")
        nl=Label(mw,image=mack)
        go=Label(mw,text="FOODIE")
        go.config(font=("Helvetica",65))
        nl.place(x=0,y=0) 
        go.place(x=750,y=50)
        mogo=PhotoImage(file="EAT1.gif")
        hal=Label(image=mogo)
        sutto=Button(mw,image=mogo,padx=20,pady=20)
        sutto.place(x=600,y=50) 

        mw.mainloop()

def veg():
        global pw
        pw.withdraw()
        global veg1
        global veg_items
        global veg
        veg=Toplevel(root)
        veg.title("FOODIE")
        veg.iconbitmap("EAT.ico")
        veg.geometry("1530x796")
        vegg=PhotoImage(file="pistha4.gif")
        ve=Label(veg,image=vegg)
        vg=Label(veg,text="FOODIE")
        vg.config(font=("Helvetica",65))
        vg1=Label(veg,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        vg1.config(font=("Helvetica",25))
        ve.place(x=0,y=0)
        vg.place(x=750,y=50)
        vg1.place(x=350,y=200)
        vogo=PhotoImage(file="EAT1.gif")
        val=Label(image=vogo)
        vutto=Button(veg,image=vogo,padx=20,pady=20)
        vutto.place(x=600,y=50)
        vutto1=Button(veg,text="BACK",padx=30,pady=10,command=back1)
        vutto1.config(font=("Helvetica",10))
        vutto1.place(x=1400,y=50)
        vutto2=Button(veg,text="VIEW BILL",padx=30,pady=10)
        vutto2.config(font=("Courier",10))
        vutto2.place(x=675,y=700)
        my_scroll=Scrollbar(veg,orient=VERTICAL)
        veg_items=Listbox(veg,width=50,yscrollcommand=my_scroll.set)
        my_scroll.config(command=veg_items.yview)
        veg_items1=Button(veg,text="VEGETARIAN ITEMS",padx=83,command=quantity13)
        veg_items1.config(font=('Helvetica',10))
        veg_items1.place(x=600,y=370)
        veg1=['Idly (2)','Plain Dosai','Masala Dosai','Rava Dosai','Poori (3)','Chapathi','Parotta (2)','Chola Poori','Idly Vadacurry','Rava Idly (2)','Sambar Idly (2)','Plain Dosai','Masala Dosai','Rava Dosai','Spl.Dosai','Onion Dosai','Paper Roast','Meals','Mini Meals','Quick Lunch','Variety Rice','Sambar Rice','Curd Rice','Parcel Mini Meals','Jeera rice','Kashmiri pulao','Plain basbathi fried rice','Schezwan veg fried rice','Schezwan veg noodles','Veg fried rice','Veg.pulao','Vegetable fried noodles','Aloo mutter masala','Baby corn papper onion','Bindi masala','Chettinad vegetable kurma']           
        for items in veg1:
                veg_items.insert(END,items)
        veg_items.place(x=600,y=400)
        my_scroll.pack(side=RIGHT,fill=Y)        
                

        veg.mainloop()


                
        
def nonveg():
        global pw
        pw.withdraw()
        global fish_items
        global egg_items
        global fn_items
        global soup_items
        global gravy_items
        global mutton_items
        global chicken_items
        global poultry_items
        global nv
        nv=Toplevel(root)
        nv.title("FOODIE")
        nv.iconbitmap("EAT.ico")
        nv.geometry("1530x796")
        nack=PhotoImage(file="pistha4.gif")
        nil=Label(nv,image=nack)
        no=Label(nv,text="FOODIE")
        no1=Label(nv,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        no.config(font=("Helvetica",65))
        no1.config(font=("Helvetica",25))
        nil.place(x=0,y=0) 
        no.place(x=750,y=50)
        no1.place(x=350,y=200)
        nogo=PhotoImage(file="EAT1.gif")
        nal=Label(image=nogo)
        nutto=Button(nv,image=nogo,padx=20,pady=20)
        nutto.place(x=600,y=50)
        nutto1=Button(nv,text="BACK",padx=30,pady=10,command=back2)
        nutto1.config(font=("Helvetica",10))
        nutto1.place(x=1400,y=50)
        nutto2=Button(nv,text="VIEW BILL",padx=30,pady=10)
        nutto2.config(font=("Courier",10))
        nutto2.place(x=675,y=730)
        fish_items=Listbox(nv,width=50)
        fish_items1=Button(nv,text="FISH VARIETIES",padx=110,command=quantity)
        fish_items1.place(x=40,y=270)
        egg_items=Listbox(nv,width=50)
        egg_items1=Button(nv,text="EGG",padx=138,command=quantity1)
        egg_items1.place(x=440,y=270)
        fn_items=Listbox(nv,width=50)
        fn_items1=Button(nv,text="FRIED RICE-NOODLES",padx=90,command=quantity2)
        fn_items1.place(x=840,y=270)
        soup_items=Listbox(nv,width=40)
        soup_items1=Button(nv,text="SOUP",padx=103,command=quantity3)
        soup_items1.place(x=1240,y=270)
        gravy_items=Listbox(nv,width=50)
        gravy_items1=Button(nv,text="GRAVY",padx=130,command=quantity4)
        gravy_items1.place(x=40,y=520)
        my_scroll1=Scrollbar(nv,orient=VERTICAL)
        mutton_items=Listbox(nv,width=50,yscrollcommand=my_scroll1.set)
        my_scroll1.config(command=mutton_items.yview)
        mutton_items1=Button(nv,text="MUTTON",padx=123,command=quantity5)
        mutton_items1.place(x=440,y=520)
        my_scroll2=Scrollbar(nv,orient=VERTICAL)
        chicken_items=Listbox(nv,width=50,yscrollcommand=my_scroll2.set)
        my_scroll2.config(command=chicken_items.yview)
        chicken_items1=Button(nv,text="CHICKEN",padx=123,command=quantity6)
        chicken_items1.place(x=840,y=520)
        poultry_items=Listbox(nv,width=40)
        poultry_items1=Button(nv,text="POULTRY",padx=93,command=quantity7)
        poultry_items1.place(x=1240,y=520)
        
        fish=['Vanjiram Fish / Tawa','Fish Roast / Tawa','Fish Curry','Prawn Fry / Masala','Fish Chukka','Nethilli Fish','Prawn 65','Fish 65']
        egg=['Egg Masala','Omelet / Egg Fry','Kalakki / Halfboil']
        friedrice_noodles=['Chicken Fried Rice / Noodles','Egg Fried Rice / Noodles']
        soup=['Chicken Soup','Mutton Soup']
        gravy=['Egg Parotta – Gravy','Egg. Veech Parotta – Gravy','Egg Dosai / Egg Oothappm','Erode Dosai','Empty Biriyani','Empty Biriyani 1/2 ']
        mutton=['Mutton Biriyani','Mutton Biriyani 1/2','Mutton Pallipalayam (Oil Free)','Mutton Nalli Fry / Gravy','Mutton Fry / Chukka','Mutton Gravy / Masala','Mutton Liver Fry / Masala',' Kongu Mutton Curry ','Mutton Kola Urundai','Thalai Fry / Gravy ','Kudal Fry / Gravy','Kaima','Egg Kaima' ,'Brain Fry','Aattukal Paaya']
        chicken=['Chicken Biriyani','Chicken Biriyani 1/2','Chicken Leg Piece Fry','Chicken Manchurian','Chicken Anda Fry','Chicken Masala / Gravy','Pallipalayam Chicken (Oil Free)','Porritha Kozhi Urundai (Kids SPL)','Chicken Lollipop (Kids SPL)',' Kabhab With Bone (Kids SPL)','Boneless Chicken 65 (Kids SPL)','Boneless Fry / Chukka','Chicken Chukka / Curry','Chicken Liver Fry / Masala ']
        poultry=['Kongu Naduchicken Curry','Naduchicken Gravy / Fry / Chukka','Kaadai Roast / Masala / Fry' ]
        for item in fish:
                fish_items.insert(END,item)
        for item in egg:
                egg_items.insert(END,item)
        for item in friedrice_noodles:
                fn_items.insert(END,item)
        for item in soup:
                soup_items.insert(END,item)
        for item in gravy:
                gravy_items.insert(END,item)
        for item in mutton:
                mutton_items.insert(END,item)
        for item in chicken:
                chicken_items.insert(END,item)
        for item in poultry:
                poultry_items.insert(END,item)
        fish_items.place(x=40,y=300)
        egg_items.place(x=440,y=300)
        fn_items.place(x=840,y=300)
        soup_items.place(x=1240,y=300)
        gravy_items.place(x=40,y=550)
        mutton_items.place(x=440,y=550)
        chicken_items.place(x=840,y=550)
        poultry_items.place(x=1240,y=550)
        my_scroll1.pack(side=LEFT,fill=Y)
        my_scroll2.pack(side=RIGHT,fill=Y)
        nv.mainloop()


        
        
def pizzas():
        global pz
        global pw
        pw.withdraw()
        global pizzas_items
        global combos_items
        pz=Toplevel(root)
        pz.title("FOODIE")
        pz.iconbitmap("EAT.ico")
        pz.geometry("1530x796")
        pack=PhotoImage(file="pistha4.gif")
        pl=Label(pz,image=pack)
        po=Label(pz,text="FOODIE")
        po.config(font=("Helvetica",65))
        po1=Label(pz,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        po1.config(font=("Helvetica",25))
        pl.place(x=0,y=0) 
        po.place(x=750,y=50)
        po1.place(x=350,y=200)
        pogo=PhotoImage(file="EAT1.gif")
        pal=Label(image=pogo)
        putto=Button(pz,image=pogo,padx=20,pady=20)
        putto.place(x=600,y=50)
        putto1=Button(pz,text="BACK",padx=30,pady=10,command=back3)
        putto1.config(font=("Helvetica",10))
        putto1.place(x=1400,y=50)
        putto2=Button(pz,text="VIEW BILL",padx=30,pady=10)
        putto2.config(font=("Courier",10))
        putto2.place(x=675,y=700)
        my_scroll3=Scrollbar(pz,orient=VERTICAL)
        pizzas_items=Listbox(pz,width=50,yscrollcommand=my_scroll3.set)
        my_scroll3.config(command=pizzas_items.yview)
        pizzas_items1=Button(pz,text="PIZZAS",padx=125,command=quantity8)
        pizzas_items1.config(font=("Helvetica",10))
        pizzas_items1.place(x=100,y=370)
        combos_items=Listbox(pz,width=50)
        combos_items1=Button(pz,text="COMBOS",padx=118,command=quantity9)
        combos_items1.config(font=("Helvetica",10))
        combos_items1.place(x=1100,y=370)
        pizzas=['African Peri Peri Veg','Aussie Barbecue Veg','Jamaican Jerk Veg','Indi Tandoori Paneer','English Cheddar and Veggies','African Peri Peri Chicken','Aussie Barbecue Chicken','Jamaican Jerk Chicken','Indi Chicken Tikka','English Cheddar and Chicken Sausage','Deluxe Veggie','Veg Extravaganzz','Double Cheese Margherita','Cheese N Corn','Fresh Veggie','Farmhouse','Peppy Paneer','Mexican Green Wave','Veggie Paradise','Paneer Makhani','Margherita','Non Veg Supreme','Chicken Pepperoni','Chicken Dominator','Chicken Golden Delight','Chicken Fiesta','Pepper Barbecue & Onion','Pepper Barbecue Chicken','Chicken Sausage','Specialty Chicken','Roasted Chicken Wings Peri-Peri','Roasted Chicken Wings - Classic','Chicken Meatballs Peri-Peri','Chicken Meatballs Classic','Boneless Chicken Wings Lemon Pepper','Boneless Chicken Wings Peri-Peri','Burger Pizza Classic Veg','Burger Pizza Premium Veg','Burger Pizza Classic Non Veg','White Pasta Italiano Veg','White Pasta Italiano Non Veg','Garlic Breadsticks','Stuffed Garlic Breadsticks','Taco Mexicana Non Veg','Taco Mexicana Veg','Potato Cheese Shots']
        combos=['2 Medium Pizzas (305 each)','2 Medium Pizzas (385 each)','2 Medium Pizzas (450 each)','2 Medium Pizzas (555 each)','2 Regular Pizzas (165 each)','2 Regular Pizzas (205 each)','2 Regular Pizzas (235 each)','2 Regular Pizzas (295 each)']
        for items in pizzas:
                pizzas_items.insert(END,items)
        for items in combos:
                combos_items.insert(END,items)
        pizzas_items.place(x=100,y=400)
        combos_items.place(x=1100,y=400)
        my_scroll3.pack(side=LEFT,fill=Y)

        pz.mainloop()


def burgers():
        global bu
        global pw
        pw.withdraw()
        global burgers_items
        bu=Toplevel(root)
        bu.title("FOODIE")
        bu.iconbitmap("EAT.ico")
        bu.geometry("1530x796")
        back=PhotoImage(file="pistha3.gif")
        bl=Label(bu,image=back)
        bo=Label(bu,text="FOODIE")
        bo.config(font=("Helvetica",65))
        bo1=Label(bu,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        bo1.config(font=("Helvetica",25))
        bl.place(x=0,y=0) 
        bo.place(x=750,y=50)
        bo1.place(x=350,y=200)
        bogo=PhotoImage(file="EAT1.gif")
        bal=Label(image=bogo)
        outto=Button(bu,image=bogo,padx=20,pady=20)
        outto.place(x=600,y=50)
        outto1=Button(bu,text="BACK",padx=30,pady=10,command=back4)
        outto1.config(font=("Helvetica",10))
        outto1.place(x=1400,y=50)
        outto2=Button(bu,text="VIEW BILL",padx=30,pady=10)
        outto2.config(font=("Courier",10))
        outto2.place(x=675,y=700)
        my_scroll4=Scrollbar(bu,orient=VERTICAL)
        burgers_items=Listbox(bu,width=50,yscrollcommand=my_scroll4.set)
        my_scroll4.config(command=burgers_items.yview)
        burger_items1=Button(bu,text="BURGERS",padx=115,command=quantity12)
        burger_items1.config(font=("Helvetica",10))
        burger_items1.place(x=600,y=370)
        burgers=['Veg Whopper','Veg Whopper Combo','Chicken Whopper','Chicken Whopper Combo','Mutton Whopper','Mutton Whopper Combo','Veg Masala Whopper','Veg Masala Whopper Combo','Chicken Masala Whopper','Chicken Masala Whopper Combo','Mutton Masala Whopper','Mutton Masala Whopper Combo','Crispy Veg Burger','Crispy Veg Burger Combo','BK Veggie Burger','BK Veggie Burger Combo','Veg Chilli Cheese Melt Burger','Veg Chilli Cheese Melt Burger Combo','Crispy Veg Supreme Burger','Crispy Veg Supreme Burger Combo','Veg Surpries Burger','Veg Surpries Burger Combo','Paneer King Melt Burger','Paneer King Melt Burger Combo','Crispy Chicken Burger','Crispy Chicken Burger Combo']
        for item in burgers:
                burgers_items.insert(END,item)
        burgers_items.place(x=600,y=400)
        my_scroll4.pack(side=RIGHT,fill=Y)
        bu.mainloop()


def icecreams():
        global ic
        global pw
        pw.withdraw()
        global r_icec
        global c_icec
        ic=Toplevel(root)
        ic.title("FOODIE")
        ic.iconbitmap("EAT.ico")
        ic.geometry("1530x796")
        iack=PhotoImage(file="pistha3.gif")
        il=Label(ic,image=iack)
        io=Label(ic,text="FOODIE")
        io.config(font=("Helvetica",65))
        io1=Label(ic,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        io1.config(font=("Helvetica",25))
        il.place(x=0,y=0) 
        io.place(x=750,y=50)
        io1.place(x=350,y=200)
        iogo=PhotoImage(file="EAT1.gif")
        ial=Label(image=iogo)
        iutto=Button(ic,image=iogo,padx=20,pady=20)
        iutto.place(x=600,y=50)
        iutto1=Button(ic,text="BACK",padx=30,pady=10,command=back5)
        iutto1.config(font=("Helvetica",10))
        iutto1.place(x=1400,y=50)
        iutto2=Button(ic,text="VIEW BILL",padx=30,pady=10)
        iutto2.config(font=("Courier",10))
        iutto2.place(x=675,y=700)
        my_scroll5=Scrollbar(ic,orient=VERTICAL)
        r_icec=Listbox(ic,width=50,yscrollcommand=my_scroll5.set)
        my_scroll5.config(command=r_icec.yview)
        my_scroll6=Scrollbar(ic,orient=VERTICAL)
        c_icec=Listbox(ic,width=50,yscrollcommand=my_scroll6.set)
        my_scroll6.config(command=c_icec.yview)
        r_icecream=['Alphonso Mango','Sitapal','Jack Fruit','Anjeer','Black Grapes','Chikoo','Coffee Walnuts','Guava','Kala Jamun','Lychee','Malai','Roasted Almond','Strawberry','WaterMelon','Anjeer Almond','Belgium Almond','Belgium Chips','Choco Vanilla','Real Bean Vanilla']
        c_icecream=['Gajar Halwa','Fig and Honey','Green Grapes','Black Current','Butter Scotch Walnut','Dry Khajur','Belgium Dark Chocolate','Gulab Jamun','Gulkand','Honey and Banana','Horlicks','Malai Kulfa','Mixed Dry Fruit','Mixed Fruit','Orange','Oreo Chocolate','Pedha','Pineapple','Pomegranate','Thandoi','Paan']
        r_ic_items=Button(ic,text="REGULAR ICECREAMS",padx=77,command=quantity10)
        r_ic_items.config(font=("Helvetica",10))
        r_ic_items.place(x=100,y=370)
        c_ic_items=Button(ic,text="CLASSIC ICECREAMS",padx=80,command=quantity11)
        c_ic_items.config(font=("Helvetica",10))
        c_ic_items.place(x=1100,y=370)
        for items in r_icecream:
                r_icec.insert(END,items)
        for items in c_icecream:
                c_icec.insert(END,items)
        r_icec.place(x=100,y=400)
        c_icec.place(x=1100,y=400)
        my_scroll5.pack(side=LEFT,fill=Y)
        my_scroll6.pack(side=RIGHT,fill=Y)
        ic.mainloop()


def beverages():
        global pw
        pw.withdraw()
        global beverages_items
        br=Toplevel(root)
        br.title("FOODIE")
        br.iconbitmap("EAT.ico")
        br.geometry("1530x796")
        brack=PhotoImage(file="pistha4.gif")
        brl=Label(br,image=brack)
        bro=Label(br,text="FOODIE")
        bro.config(font=("Helvetica",65))
        bro1=Label(br,text="AFTER SELECTION PLEASE CLICK THE ABOVE BUTTON")
        bro1.config(font=("Helvetica",25))
        brl.place(x=0,y=0) 
        bro.place(x=750,y=50)
        bro1.place(x=350,y=200)
        brogo=PhotoImage(file="EAT1.gif")
        bral=Label(image=brogo)
        brutto=Button(br,image=brogo,padx=20,pady=20)
        brutto.place(x=600,y=50)
        brutto1=Button(br,text="BACK",padx=30,pady=10,command=back6)
        brutto1.config(font=("Helvetica",10))
        brutto1.place(x=1400,y=50)
        brutto2=Button(br,text="VIEW BILL",padx=30,pady=10)
        brutto2.config(font=("Courier",10))
        brutto2.place(x=675,y=700)
        my_scroll7=Scrollbar(br,orient=VERTICAL)
        beverages_items=Listbox(br,width=50,yscrollcommand=my_scroll7.set)
        my_scroll7.config(command=beverages_items.yview)
        beverages_items1=Button(br,text="BEVERAGES",padx=107,command=quantity14)
        beverages_items1.config(font=("Helvetica",10))
        beverages_items1.place(x=600,y=370)
        beverage=['Alphonso Mango Milkshake','Arise With Pomegranate','Assam Tea','Aztec single origin Coffee','Café Americano','Café Frappe','Café Latte','Café Mocha','Classic Cappuccino','Cassic Lemonade','Classic Strawberry Milkshake','Cocoa Cookie Milkshake','Cold Cocoa Latte','Cool Blue','Crunchy Frappe','Darjeeling Tea','Dark Frappe','Devils Own','Enliven With Chamomile','Ethiopian single origin Coffee','Eye-opener Espresso','Filter Coffee','Glide With Green Mint','Green Tea']
        for items in beverage:
                beverages_items.insert(END,items)
        beverages_items.place(x=600,y=400)
        my_scroll7.pack(side=RIGHT,fill=Y)       
        br.mainloop()

def process():
        global d
        user=unl.get()
        passw=pwl.get()
        if user=='' or passw=='':
        	messagebox.showerror("ERROR", "You have not entered the username or password")
        elif user not in d :
        	messagebox.showerror("ERROR","Enter a valid username")
        elif user in d and passw!=d[user]:
        		messagebox.showerror("ERROR","Incorrect password")
        elif user in d and passw==d[user]:
        		newwindow()
        		root.withdraw()

        


def popup():
        if naml.get()=='' and phnl.get()=='' and addl.get()=='' and usnl.get()=='' and pasl.get()=='' and cnf_pasl.get()=='':
                messagebox.showerror("ERROR","All the fields are empty")
        elif naml.get()=='' or phnl.get()=='' or addl.get()=='' or usnl.get()=='' or pasl.get()=='' or cnf_pasl=='':
                messagebox.showerror("ERROR","One of the fields is empty")
        elif len(phnl.get())!=10:
                messagebox.showerror("ERROR","Invalid Phone Number")
        elif pasl.get()!=cnf_pasl.get():
                messagebox.showerror("ERROR","Please enter the correct password")
        else:
                s=usnl.get()
                v=cnf_pasl.get()
                d[s]=v
                reg.withdraw()
        

def register():
        global reg
        global naml
        global phnl
        global addl
        global usnl
        global pasl
        global cnf_pasl
        reg=Toplevel(root)
        reg.title("FOODIE-REGISTER")
        reg.iconbitmap("EAT.ico")
        reg.geometry("500x400")
        wgo=PhotoImage(file="pistha.gif")
        wal=Label(reg,image=wgo)
        wal.place(x=0,y=0)
        per=Label(reg,text="FOODIE")
        per.config(font=("Helvetica",25))
        per.place(x=175,y=5)
        gel=PhotoImage(file="EAT2.gif")
        gal=Label(image=gel)
        gutto=Button(reg,image=gel,borderwidth=0)
        gutto.place(x=110,y=5)
        nam=Label(reg,text="NAME")
        nam.place(x=50,y=80)
        phn=Label(reg,text="PHONE NUMBER")
        phn.place(x=50,y=120)
        add=Label(reg,text="ADDRESS")
        add.place(x=50,y=160)
        usn=Label(reg,text="USERNAME")
        usn.place(x=50,y=200)
        pas=Label(reg,text="PASSWORD")
        pas.place(x=50,y=240)
        cnf_pas=Label(reg,text="CONFIRM PASSWORD")
        cnf_pas.place(x=50,y=280)
        naml=Entry(reg)
        naml.place(x=200,y=80)
        phnl=Entry(reg)
        phnl.place(x=200,y=120)
        addl=Entry(reg)
        addl.place(x=200,y=160)
        usnl=Entry(reg)
        usnl.place(x=200,y=200)
        pasl=Entry(reg,show='*')
        pasl.place(x=200,y=240)
        cnf_pasl=Entry(reg,show='*')
        cnf_pasl.place(x=200,y=280)
        reg_but=Button(reg,text="SUBMIT",command=popup)
        reg_but.place(x=175,y=340)
        reg_but['font']=myFont
        reg.mainloop()


        
                                
photo=PhotoImage(file="images.gif")
w=Label(root,image=photo)
w.place(x=0,y=0)



                                        

un=Label(root,text=" USERNAME ")
pw=Label(root,text=" PASSWORD ")
txt=Label(root,text="FOODIE")
txt.config(font=("Helvetica",25))
txt.place(x=120,y=125)
jgo=PhotoImage(file="EAT2.gif")
jal=Label(image=jgo)
jutto=Button(root,image=jgo,borderwidth=0)
jutto.place(x=60,y=125) 
re=Button(root,text="REGISTER",padx=1,pady=1,command=register)
re.place(x=50,y=314)
unl=Entry(root)
pwl=Entry(root,show='*')
sub=Button(root,text=" SUBMIT ",command=lambda:process(),activebackground='red')
msg=Label(text = '',fg = 'red')

re['font']=myFont
sub['font']=myFont


un.grid(row=10,column=0,sticky=W,padx=(50,0),pady=(200,0))
unl.grid(row=10,column=1,padx=(2,0),pady=(200,0))
pw.grid(row=11,column=0,sticky=W,padx=(50,0),pady=10)
pwl.grid(row=11,column=1,padx=10,pady=10)
sub.grid(row=17,column=1,padx=10,pady=30)
msg.grid(row=8,column=1)

d={'gowtham':'sg'}
order_item=[]
nv_dict={'Vanjiram Fish / Tawa':90,'Fish Roast / Tawa':90,'Fish Curry':90,'Prawn Fry / Masala':100,'Fish Chukka':90,'Nethilli Fish':90,'Prawn 65':85,'Fish 65':85,'Egg Masala':55,'Omelet / Egg Fry':50,'Kalakki / Halfboil':50,'Chicken Fried Rice / Noodles':120,'Egg Fried Rice / Noodles':120,'Chicken Soup':25,'Mutton Soup':25,'Mutton Biriyani':120,'Chicken Biriyani':110,'Empty Biriyani':75,'Mutton Biriyani 1/2':60,'Egg Parotta – Gravy':75,'Chicken Biriyani 1/2':55, 'Empty Biriyani 1/2 ':30,'Egg. Veech Parotta – Gravy':70,'Egg Dosai / Egg Oothappam':55,'Erode Dosai':50,'Mutton Pallipalayam (Oil Free)':80,'Mutton Nalli Fry / Gravy':80,'Mutton Fry / Chukka':80,'Mutton Gravy / Masala':80,'Mutton Liver Fry / Masala':80,' Kongu Mutton Curry ':80,'Mutton Kola Urundai':80,'Thalai Fry / Gravy ':80,'Kudal Fry / Gravy':80,'Kaima':80,'Egg Kaima':80,'Brain Fry':80,'Aattukal Paaya':80,'Chicken Leg Piece Fry':75,'Chicken Manchurian':75,'Chicken Anda Fry':75,'Chicken Masala / Gravy':75,'Pallipalayam Chicken (Oil Free)':75,'Porritha Kozhi Urundai (Kids SPL)':75,'Chicken Lollipop (Kids SPL)':75,' Kabhab With Bone (Kids SPL)':75,'Boneless Chicken 65 (Kids SPL)':75,'Boneless Fry / Chukka':75,'Chicken Chukka / Curry':75,'Chicken Liver Fry / Masala ':75,'Kongu Naduchicken Curry':90,'Naduchicken Gravy / Fry / Chukka':90,'Kaadai Roast / Masala / Fry':60}
pz_dict={'African Peri Peri Veg':385,'Aussie Barbecue Veg':450,'Jamaican Jerk Veg':385,'Indi Tandoori Paneer':450,'English Cheddar and Veggies':385,'African Peri Peri Chicken':450,'Aussie Barbecue Chicken':555,'Jamaican Jerk Chicken':555,'Indi Chicken Tikka':555,'English Cheddar and Chicken Sausage':450,'Deluxe Veggie':450,'Veg Extravaganzz':450,'Double Cheese Margherita':305,'Cheese N Corn':305,'Fresh Veggie':305,'Farmhouse':385,'Peppy Paneer':385,'Mexican Green Wave':385,'Veggie Paradise':385,'Paneer Makhani':385,'Margherita':195,'Non Veg Supreme':555,'Chicken Pepperoni':555,'Chicken Dominator':555,'Chicken Golden Delight':450,'Chicken Fiesta':450,'Pepper Barbecue & Onion':385,'Pepper Barbecue Chicken':305,'Chicken Sausage':305,'Specialty Roasted Chicken Wings Peri-Peri':109,'Roasted Chicken Wings - Classic':109,'Chicken Meatballs Peri-Peri':99,'Chicken Meatballs Classic':99,'Boneless Chicken Wings Lemon Pepper':139,'Boneless Chicken Wings Peri-Peri':139,'Burger Pizza Classic Veg':99,'Burger Pizza Premium Veg':129,'Burger Pizza Classic Non Veg':139,'White Pasta Italiano Veg':135,'White Pasta Italiano Non Veg':145,'Garlic Breadsticks':95,'Stuffed Garlic Breadsticks':139,'Chicken Parcel':39,'Veg Parcel':35,'Chocolate Lava Cake':99,'Butterscotch Mousse Cake':90,'Taco Mexicana Non Veg':135,'Taco Mexicana Veg':125,'Potato Cheese Shots':59,'Crunchy Strips':59,'Crinkle Fries':59,'Brownie Fantasy':59,'Classic Combo (Pizza & Drink)':199,'Meal for 1 (Pizza, Drink, Breadsticks)':269,'Meal for 2 (Large Pizza, Drink, Breadsticks)':449,'Pizza Feast (2 Pizza, 2 Drink, 2 Breadsticks)':849,'2 Medium Pizzas (305 each)':199,'2 Medium Pizzas (385 each)':249,'2 Medium Pizzas (450 each)':299,'2 Medium Pizzas (555 each)':399,'2 Regular Pizzas (165 each)':99,'2 Regular Pizzas (205 each)':139,'2 Regular Pizzas (235 each)':179,'2 Regular Pizzas (295 each)':219}
ic_dict={'Alphonso Mango':70,'Sitapal':70,'Jack Fruit':70,'Anjeer':70,'Black Grapes':70,'Chikoo':70,'Coffee Walnuts':70,'Guava':70,'Kala Jamun':70,'Lychee':70,'Malai':70,'Roasted Almond':70,'Strawberry':70,'WaterMelon':70,'Anjeer Almond':70,'Belgium Almond':70,'Belgium Chips':70,'Choco Vanilla':70,'Real Bean Vanilla':70,'Gajar Halwa':80,'Fig and Honey':80,'Green Grapes':80,'Black Current':80,'Butter Scotch Walnut':80,'Dry Khajur':80,'Belgium Dark Chocolate':80,'Gulab Jamun':80,'Gulkand':80,'Honey and Banana':80,'Horlicks':80,'Malai Kulfa':80,'Mixed Dry Fruit':80,'Mixed Fruit':80,'Orange':80,'Oreo Chocolate':80,'Pedha':80,'Pineapple':80,'Pomegranate':80,'Thandoi':80,'Paan':80}
bg_dict={'Veg Whopper':139,'Veg Whopper Combo':238,'Chicken Whopper':149,'Chicken Whopper Combo':248,'Mutton Whopper':219,'Mutton Whopper Combo':318,'Veg Masala Whopper':199,'Veg Masala Whopper Combo':298,'Chicken Masala Whopper':209,'Chicken Masala Whopper Combo':308,'Mutton Masala Whopper':279,'Mutton Masala Whopper Combo':378,'Crispy Veg Burger':39,'Crispy Veg Burger Combo':138,'BK Veggie Burger':79,'BK Veggie Burger Combo':178,'Veg Chilli Cheese Melt Burger':109,'Veg Chilli Cheese Melt Burger Combo':208,'Crispy Veg Supreme Burger':59,'Crispy Veg Supreme Burger Combo':158,'Veg Surpries Burger':99,'Veg Surpries Burger Combo':198,'Paneer King Melt Burger':129,'Paneer King Melt Burger Combo':228,'Crispy Chicken Burger':59,'Crispy Chicken Burger Combo':158,'Crispy Chicken Supreme Burger':79,'Crispy Chicken Supreme Burger Combo':178,'BK Grill Chicken Burger':89,'BK Grill Chicken Burger Combo':188,'Chicken Chilli Cheese Burger':119,'Chicken Chilli Cheese Burger Combo':218,'Chicken Tandoor Grill Burger':149,'Chicken Tandr Grill Burger Combo':248,'Fiery Chicken Burger':149,'Fiery Chicken Burger Combo':248,'King Egg Burger':49,'King Egg Burger Combo':148,'King Egg Burger + Lipton Ice Tea':119,'BK Veggie Burger + Lipton Ice Tea':149,'BK Grill Burger + Lipton Ice Tea':159,'Fries (regular)':70,'Fries (medium)':80,'Fries (large)':90,'Chicken Fries (5 pcs)':80,'Chicken Fries (9 pcs)':13}
veg_dict={'Idly (2)':37,'Plain Dosai':50,'Masala Dosai':75,'Rava Dosai':65,'Poori (3)': 75,'Chapathi': 75,'Parotta (2)':75,'Chola Poori':85,'Idly Vadacurry':55,'Rava Idly (2)':42,'Sambar Idly (2)':40,'Plain Dosai':47,'Masala Dosai':62,'Rava Dosai': 56,'Spl.Dosai': 55,'Onion Dosai':62,'Paper Roast':100,'Meals':115,'Mini Meals':90,'Quick Lunch':90,'Variety Rice':45,'Sambar Rice':45,'Curd Rice':45,'Parcel Mini Meals':82,'Jeera rice':160,'Kashmiri pulao':160,'Plain basbathi fried rice':165,'Schezwan veg fried rice':109,'Schezwan veg noodles':160,'Veg fried rice':145,'Veg.pulao':160,'Vegetable fried noodles':145,'Aloo mutter masala': 136,'Baby corn papper onion': 136,'Bindi masala':126,'Chettinad vegetable kurma':141}
bvg_dict={'Alphonso Mango Milkshake':45,'Arise With Pomegranate':45,'Assam Tea':25,'Aztec single origin Coffee':65,'Café Americano':65,'Café Frappe':65,'Café Latte':65,'Café Mocha':65,'Classic Cappuccino':65,'Classic Lemonade':65,'Classic Strawberry Milkshake':45,'Cocoa Cookie Milkshake':45,'Cold Cocoa Latte':45,'Cool Blue':45,'Crunchy Frappe':45,'Darjeeling Tea':45,'Dark Frappe':45,'Devils Own':45,'Enliven With Chamomile':25,'Ethiopian single origin Coffee':25,'Eye-opener Espresso':25,'Filter Coffee':25,'Glide With Green Mint':45,'Green Tea':25}

root.mainloop()
