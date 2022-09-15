from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
from PIL import Image, ImageDraw, ImageFont

from UserInfo import UserInfo
from CenterDetails import CenterDetails
from OxygenBed import OxygenBed
from TestingLabs import TestingLabs
from PlasmaCenter import PlasmaCenter
from VaccineCenter import VaccineCenter
from InjectionsCenter import InjectionsCenter
from QnA import QnA

root = Tk()

root.geometry("1300x1300")
root.title("COVID RELIEF SERVICES")
root.iconbitmap(r'img/logo.ico')
root['bg'] = '#5c84cc'



image1 = Image.open("img/frontpage1.jpg")
image1_resize = image1.resize((1400, 800))
test = ImageTk.PhotoImage(image1_resize)
label1 = Label(root, image=test)
label1.image = test
label1.config(bd=0)
label1.pack(side=BOTTOM)

image1 = Image.open("img/logo.ico")
image1_resize = image1.resize((150, 150))
test = ImageTk.PhotoImage(image1_resize)
label1 = Label(root, image=test)
label1.image = test
label1.config(bd=0)
label1.place(x=600,y=0)

'''image1 = Image.open("whitebg.jpg")
image1_resize = image1.resize((1200, 80))
test = ImageTk.PhotoImage(image1_resize)
label1 = Label(root, image=test)
label1.image = test
label1.config(bd=0)
label1.place(x=150,y=0)'''

#l1 = Label(root, text="NGO", bg='#bcf5bc')
#l1.configure(font=("Sans", 45))
#l1.pack()
l2 = Label(root, text="COVID RELIEF SERVICES", bg='#f2f2f4',fg='black')
l2.configure(font=("Bariol", 50,'bold'))
l2.place(x=280,y=160)

intro="""~We Isolate Now


    So That Next Time We Gather
         

                    Nobody Is Missing~"""


l3 = Label(root, justify=LEFT, padx=10, text=intro, bg='#f2f2f2')
l3.configure(font=("Arca Majora", 15))
l3.place(x=10, y=480)

'''intro1 = """Welcome to our  NGO, Covid Relief Services. 
         Here, we help you find assistance related to all
         Covid-19 medical emergencies.
         We believe that if we fight this virus together, we can defeat it.
         It is crucial to help each other, during these times.
         So, If you want to help the society, you can enroll in 
         our volunteering programmes too."""

l3 = Label(root, justify=LEFT, padx=10, text=intro1, bg='white')
l3.configure(font=("Arca Majora", 15))
l3.place(x=300, y=350)'''


# volunteers window
def openvolunWindow():
    volunWindow = Toplevel(root)  # Toplevel object which will be treated as a new window
    volunWindow.geometry("1300x1300")  # sets dimensions of new window
    volunWindow.title("WELCOME VOLUNTEERS")
    volunWindow.iconbitmap(r'img/logo.ico')
    volunWindow['bg'] = '#bcf5bc'

    image1 = Image.open("img/volunwindow.jpg")
    image1_resize = image1.resize((1400, 1470))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(volunWindow, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=RIGHT)



    registration = """ Do you want to register to be 
      a volunteer at CRS?"""
    l4 = Label(volunWindow, justify=LEFT, padx=10, text=registration, bg='#ffb712')
    l4.configure(font=("Geo Sans Light", 20))
    l4.place(x=250, y=180)

    existing = """ Existing Volunteer?"""
    l44 = Label(volunWindow, justify=LEFT, padx=10, text=existing, bg='#ffb712')
    l44.configure(font=("Geo Sans Light", 20))
    l44.place(x=800, y=180)

    reg = Button(volunWindow, text="Registration Form", height=3, width=25,
                 command=openregistrationWindow)  # a button widget which will open a new window on button click
    reg.place(x=330, y=300)

    l5 = Label(volunWindow, text="Please enter login details", bg='#ffb712')
    l5.configure(font=("Geo Sans Light", 20))
    l5.place(x=780, y=250)

    l6 = Label(volunWindow, text="Username", bg='#ffb712')
    l6.configure(font=("Geo Sans Light", 20))
    l6.place(x=780, y=350)

    username = StringVar()
    username_login_entry = Entry(volunWindow, textvariable=username)
    username_login_entry.place(x=950, y=360)

    l7 = Label(volunWindow, text="Password", bg='#ffb712')
    l7.configure(font=("Geo Sans Light", 20))
    l7.place(x=780, y=450)

    password = StringVar()
    password__login_entry = Entry(volunWindow, textvariable=password, show='*')
    password__login_entry.place(x=950, y=460)
    Label(volunWindow, text="").pack()

    def checklogin():
        user = UserInfo()
        check = user.checkUsername(username.get(), password.get())
        if check == 1: openloginWindow()
        else: 
            l8 = Label(volunWindow, text="Incorrect Username or Password", bg='#bcf5bc')
            l8.configure(fg="red", font=("calibri", 11))
            l8.place(x=780, y=600)

    logbtn = Button(volunWindow, text="Login", width=10, height=1, command=checklogin)
    logbtn.place(x=900, y=550)


# after logging in
def openloginWindow():
    loginWindow = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    loginWindow.geometry("1300x1300")  # sets dimensions of new window
    loginWindow.title("THANK YOU FOR VOLUNTEERING")
    loginWindow.iconbitmap(r'img/logo.ico')
    loginWindow['bg'] = 'black'

    image1 = Image.open("img/loginwindow.jpg")
    image1_resize = image1.resize((700, 470))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(loginWindow, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=RIGHT)

    l8 = Label(loginWindow, text="Which window do you want to access?")
    l8.configure(font=("Geo Sans Light", 20),bg = 'Black', fg = 'White')
    l8.place(x=150, y=300)

    info = Button(loginWindow, text="Covid Resources", height=3, width=25,
                  command=opencovidResources)  # a button widget which will open a new window on button click
    info.place(x=180, y=400)

    res = Button(loginWindow, text="Covid Information", height=3, width=25,
                 command=opencovidInformation)  # a button widget which will open a new window on button click
    res.place(x=400, y=400)


def opencovidResources():
    covidResources = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidResources.geometry("1300x1300")  # sets dimensions of new window
    covidResources.title("THANK YOU FOR VOLUNTEERING")
    covidResources.iconbitmap(r'img/logo.ico')
    #covidResources['bg'] = '#E9967A'

    image1 = Image.open("img/resources.jpg")
    image1_resize = image1.resize((1400, 1400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(covidResources, image=test)
    label1.image = test
    label1.pack()

    cc = Label(covidResources, text="Which window do you want to access?")
    cc.configure(font=("Geo Sans Light", 20, 'bold'))
    cc.place(x=400,y=40)

    c11 = Button(covidResources, text="Centre Details", height=3, width=25,
                 command=opencovidcentreDetails)  # a button widget which will open a new window on button click
    c11.place(x=550, y=120)

    c22 = Button(covidResources, text="Bed Centre", height=3, width=25,
                 command=openBedsdetails)  # a button widget which will open a new window on button click
    c22.place(x=550, y=220)

    c33 = Button(covidResources, text="Testing Labs", height=3, width=25,
                 command=opentestingLabs)  # a button widget which will open a new window on button click
    c33.place(x=550, y=320)

    c44 = Button(covidResources, text="Plasma", height=3, width=25,
                 command=openPlasma)  # a button widget which will open a new window on button click
    c44.place(x=550, y=420)

    c55 = Button(covidResources, text="Injections", height=3, width=25,
                 command=openInjections)  # a button widget which will open a new window on button click
    c55.place(x=550, y=520)

    c66 = Button(covidResources, text="Vaccine", height=3, width=25,
                 command=openVaccine)  # a button widget which will open a new window on button click
    c66.place(x=550, y=620)


output = ""
def opencovidcentreDetails():
    covidcentreDetails = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidcentreDetails.geometry("1300x1300")  # sets dimensions of new window
    covidcentreDetails.title("CENTRE DETAILS")
    covidcentreDetails.iconbitmap(r'img/logo.ico')
    covidcentreDetails['bg'] = '#43aba3'

    image1 = Image.open("img/centre.png")
    image1_resize = image1.resize((1382, 300))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(covidcentreDetails, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=BOTTOM)

    global cname
    global cno
    global cadd
    global ctype
    cname = StringVar()
    cno = StringVar()
    cadd = StringVar()
    ctype = StringVar()

    ccc = Label(covidcentreDetails, text="CENTRE DETAILS", bg='#43aba3')
    ccc.configure(font=("Geo Sans Light", 40))
    ccc.pack()

    cname_lable = Label(covidcentreDetails, text="Centre Name", bg='#43aba3')
    cname_lable.configure(font=("Geo Sans Light", 15))
    cname_lable.place(x=500, y=80)
    cname_entry = Entry(covidcentreDetails, textvariable=cname)
    cname_entry.place(x=720, y=80)

    cno_lable = Label(covidcentreDetails, text="Centre Phone Number", bg='#43aba3')
    cno_lable.configure(font=("Geo Sans Light", 15))
    cno_lable.place(x=500, y=130)
    cno_entry = Entry(covidcentreDetails, textvariable=cno)
    cno_entry.place(x=720, y=130)

    cadd_lable = Label(covidcentreDetails, text="Centre Address", bg='#43aba3')
    cadd_lable.configure(font=("Geo Sans Light", 15))
    cadd_lable.place(x=500, y=180)
    cadd_entry = Entry(covidcentreDetails, textvariable=cadd)
    cadd_entry.place(x=720, y=180)

    ctype_lable = Label(covidcentreDetails, text="Centre Type", bg='#43aba3')
    ctype_lable.configure(font=("Geo Sans Light", 15))
    ctype_lable.place(x=500, y=230)

    def viewSelected():
        choice = var.get()
        global output
        if choice == 1:
            output = "oxygen beds"

        elif choice == 2:
            output = "testing lab"

        elif choice == 3:
            output = "plasma"

        elif choice == 4:
            output = "injection"

        elif choice == 5:
            output = "vaccine"


    var = IntVar()
    ra1 = Radiobutton(covidcentreDetails, text="Bed Centre", variable=var, value=1, command=viewSelected)
    ra1.pack( anchor = W )
    ra1.place(x=720, y=230)
    ra2 = Radiobutton(covidcentreDetails, text="Testing Centre", variable=var, value=2, command=viewSelected)  # , command=viewSelected)
    ra2.pack( anchor = W )
    ra2.place(x=720, y=260)
    ra3 = Radiobutton(covidcentreDetails, text="Plasma Centre", variable=var, value=3, command=viewSelected)  # , command=viewSelected)
    ra3.pack( anchor = W )
    ra3.place(x=720, y=290)
    ra4 = Radiobutton(covidcentreDetails, text="Injection Distributor", variable=var, value=4, command=viewSelected)  # , value=3, command=viewSelected)
    ra4.pack( anchor = W )
    ra4.place(x=720, y=320)
    ra5 = Radiobutton(covidcentreDetails, text="Vaccination Centre", variable=var, value=5, command=viewSelected)  # , value=3, command=viewSelected)
    ra5.pack( anchor = W )
    ra5.place(x=720, y=350)

    def center_details(operation):
        center = CenterDetails()
        if operation == "Add":
            center.insert_center(cname.get(), cno.get(), cadd.get(), output)

        elif operation == "Update":
            center.update_center(cname.get(), cno.get(), cadd.get(), output)
            
        elif operation == "Delete":
            center.delete_center(cname.get())


    add = Button(covidcentreDetails, text="Add", width=10, height=2, bg="#D3D3D3", command=lambda m="Add": center_details(m))
    add.place(x=520, y=420)

    upd = Button(covidcentreDetails, text="Update", width=10, height=2, bg="#D3D3D3", command=lambda m="Update": center_details(m))
    upd.place(x=620, y=420)

    dele = Button(covidcentreDetails, text="Delete", width=10, height=2, bg="#D3D3D3", command=lambda m="Delete": center_details(m))
    dele.place(x=720, y=420)



def openBedsdetails():
    Bedsdetails = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Bedsdetails.geometry("1300x1300")  # sets dimensions of new window
    Bedsdetails.title("BED CENTRE")
    Bedsdetails.iconbitmap(r'img/logo.ico')
    Bedsdetails['bg'] = 'white'

    image1 = Image.open("img/beddetails.jpeg")
    image1_resize = image1.resize((1400, 400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(Bedsdetails, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack()

    global cnorm
    global coxy
    global ctot
    global cnam
    cnorm = StringVar()
    coxy = StringVar()
    ctot = StringVar()
    cnam = StringVar()

    cccc = Label(Bedsdetails, text="BED CENTRE")
    cccc.configure(font=("Geo Sans Light", 30))
    cccc.place(x=550,y=40)

    cnam_lable = Label(Bedsdetails, text="Centre Name", bg='white')
    cnam_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cnam_lable.place(x=500, y=420)
    cnam_entry = Entry(Bedsdetails, textvariable=cnam,bg="#D3D3D3")
    cnam_entry.place(x=700, y=420)

    cnorm_lable = Label(Bedsdetails, text="Normal Beds", bg='white')
    cnorm_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cnorm_lable.place(x=500, y=470)
    cnorm_entry = Entry(Bedsdetails, textvariable=cnorm,bg="#D3D3D3")
    cnorm_entry.place(x=700, y=470)

    coxy_lable = Label(Bedsdetails, text="Oxygen Beds", bg='white')
    coxy_lable.configure(font=("Geo Sans Light", 13,'bold'))
    coxy_lable.place(x=500, y=520)
    coxy_entry = Entry(Bedsdetails, textvariable=coxy,bg="#D3D3D3")
    coxy_entry.place(x=700, y=520)

    ctot_lable = Label(Bedsdetails, text="Total Beds", bg='white')
    ctot_lable.configure(font=("Geo Sans Light", 13,'bold'))
    ctot_lable.place(x=500, y=570)
    ctot_entry = Entry(Bedsdetails, textvariable=ctot,bg="#D3D3D3")
    ctot_entry.place(x=700, y=570)

    def bed_details(operation):
        beds = OxygenBed()
        if operation == "Add":
            beds.insert_beds(cnam.get(), cnorm.get(), coxy.get(), ctot.get())

        elif operation == "Update":
            beds.update_beds(cnam.get(), cnorm.get(), coxy.get(), ctot.get())


    add1 = Button(Bedsdetails, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": bed_details(m))
    add1.place(x=520, y=630)

    upd1 = Button(Bedsdetails, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": bed_details(m))
    upd1.place(x=620, y=630)



def opentestingLabs():
    testingLabs = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    testingLabs.geometry("1300x1300")  # sets dimensions of new window
    testingLabs.title("TESTING LABS")
    testingLabs.iconbitmap(r'img/logo.ico')
    testingLabs['bg'] = 'white'

    image1 = Image.open("img/RTPCR-test-covid.jpg")
    image1_resize = image1.resize((500, 750))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(testingLabs, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=LEFT)

    image1 = Image.open("img/bloodtest.jpg")
    image1_resize = image1.resize((500, 750))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(testingLabs, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=RIGHT)

    global cna
    global ctest

    cna = StringVar()
    ctest = StringVar()

    cccc1 = Label(testingLabs, text="TESTING LABS", bg='white')
    cccc1.configure(font=("Geo Sans Light", 30))
    cccc1.place(x=505,y=50)

    cna_lable = Label(testingLabs, text="Lab Name", bg='white')
    cna_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cna_lable.place(x=550, y=150)
    cna_entry = Entry(testingLabs, textvariable=cna,bg="#D3D3D3")
    cna_entry.place(x=650, y=150)

    ctest_lable = Label(testingLabs, text="Test Name", bg='white')
    ctest_lable.configure(font=("Geo Sans Light", 13,'bold'))
    ctest_lable.place(x=550, y=200)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()

    ra1 = Checkbutton(testingLabs, text="RTPCR TEST", variable=var1,bg="#D3D3D3")  # , command=viewSelected)
    ra1.place(x=650, y=200)
    ra2 = Checkbutton(testingLabs, text="RAPID ANTIGEN TEST", variable=var2,bg="#D3D3D3")  # , command=viewSelected)
    ra2.place(x=650, y=230)
    ra3 = Checkbutton(testingLabs, text="CRP", variable=var3,bg="#D3D3D3")  # , command=viewSelected)
    ra3.place(x=650, y=260)
    ra4 = Checkbutton(testingLabs, text="FERRITIN", variable=var4,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra4.place(x=650, y=290)
    ra5 = Checkbutton(testingLabs, text="DDMIER", variable=var5,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra5.place(x=650, y=310)
    ra6 = Checkbutton(testingLabs, text="CBC", variable=var6,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra6.place(x=650, y=330)
    ra7 = Checkbutton(testingLabs, text="CT SCAN", variable=var7,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra7.place(x=650, y=360)

    def check_button(operation) :
        vars = {"RTPCR TEST":var1.get(), "RAPID ANTIGEN TEST":var2.get(), "CRP":var3.get(), "FERRITIN":var4.get(), "DDMIER":var5.get(), "CBC":var6.get(), "CT SCAN":var7.get()}
        
        test = TestingLabs()
        bg = ""
        for value, key in vars.items():
            if key == 1: bg = bg + value + ", "
        
        if operation == "Add":
            test.insert_tests(cna.get(), bg)

        if operation == "Update":
            test.update_tests(cna.get(), bg)

    add1 = Button(testingLabs, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": check_button(m))
    add1.place(x=510, y=420)

    upd1 = Button(testingLabs, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": check_button(m))
    upd1.place(x=610, y=420)


def openPlasma():
    Plasma = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Plasma.geometry("1300x1300")  # sets dimensions of new window
    Plasma.title("PLASMA DETAILS")
    Plasma.iconbitmap(r'img/logo.ico')
    Plasma['bg'] = 'white'

    image1 = Image.open("img/plasma.jpg")
    image1_resize = image1.resize((900, 1000))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(Plasma, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=LEFT)

    global cname1
    global cblood
    cname1 = StringVar()
    cblood = StringVar()

    ccc = Label(Plasma, text="PLASMA DETAILS", bg='white')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cname1_lable = Label(Plasma, text="Centre Name", bg='white')
    cname1_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cname1_lable.place(x=950, y=150)
    cname1_entry = Entry(Plasma, textvariable=cname1,bg="#D3D3D3")
    cname1_entry.place(x=1100, y=150)

    cblood_lable = Label(Plasma, text="Blood Group", bg='white')
    cblood_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cblood_lable.place(x=950, y=200)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()

    ra1 = Checkbutton(Plasma, text="A+", variable=var1,bg="#D3D3D3")  # , command=viewSelected)
    ra1.place(x=1100, y=200)
    ra2 = Checkbutton(Plasma, text="A-", variable=var2,bg="#D3D3D3")  # , command=viewSelected)
    ra2.place(x=1100, y=230)
    ra3 = Checkbutton(Plasma, text="B+", variable=var3,bg="#D3D3D3")  # , command=viewSelected)
    ra3.place(x=1100, y=260)
    ra4 = Checkbutton(Plasma, text="B-", variable=var4,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra4.place(x=1100, y=290)
    ra5 = Checkbutton(Plasma, text="O+", variable=var5,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra5.place(x=1100, y=320)
    ra6 = Checkbutton(Plasma, text="O-", variable=var6,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra6.place(x=1100, y=350)
    ra7 = Checkbutton(Plasma, text="AB+", variable=var7,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra7.place(x=1100, y=380)
    ra8 = Checkbutton(Plasma, text="AB-", variable=var8,bg="#D3D3D3")  # , value=3, command=viewSelected)
    ra8.place(x=1100, y=410)


    def check_button(operation) :
        vars = {"A+":var1.get(), "A-":var2.get(), "B+":var3.get(), "B-":var4.get(), "O+":var5.get(), "O-":var6.get(), "AB+":var7.get(), "AB-":var8.get()}
        
        plasma = PlasmaCenter()
        bg = ""
        for value, key in vars.items():
            if key == 1: bg = bg + value + ", "
        
        if operation == "Add":
            plasma.insert_tests(cname1.get(), bg)

        if operation == "Update":
            plasma.update_tests(cname1.get(), bg)


    add = Button(Plasma, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": check_button(m))
    add.place(x=970, y=500)

    upd = Button(Plasma, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": check_button(m))
    upd.place(x=1070, y=500)



def openInjections():
    Injections = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Injections.geometry("1300x1300")  # sets dimensions of new window
    Injections.title("INJECTION DETAILS")
    Injections.iconbitmap(r'img/logo.ico')
    Injections['bg'] = 'white'

    image1 = Image.open("img/remdesivir.jpg")
    image1_resize = image1.resize((600, 400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(Injections, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.place(x=0,y=355)

    image1 = Image.open("img/tocilizumab.jpg")
    image1_resize = image1.resize((800, 400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(Injections, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.place(x=600,y=355)

    global cna1
    global cinj1
    global cinj2
    cna1 = StringVar()
    cinj1 = StringVar()
    cinj2 = StringVar()

    ccc = Label(Injections, text="INJECTION DETAILS", bg='white')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cname1_lable = Label(Injections, text="Centre Name", bg='white')
    cname1_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cname1_lable.place(x=450, y=100)
    cname1_entry = Entry(Injections, textvariable=cna1,bg="#D3D3D3")
    cname1_entry.place(x=600, y=100)

    cblood_lable = Label(Injections, text="Injection Name", bg='white')
    cblood_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cblood_lable.place(x=450, y=150)

    ccost1_lable = Label(Injections, text="Cost- ", bg='white')
    ccost1_lable.configure(font=("Geo Sans Light", 13,'bold'))
    ccost1_lable.place(x=700, y=150)
    ccost1_entry = Entry(Injections, textvariable=cinj1,bg="#D3D3D3")
    ccost1_entry.place(x=750, y=150)
    cname1_lable = Label(Injections, text="Cost- ", bg='white')
    cname1_lable.configure(font=("Geo Sans Light", 13,'bold'))
    cname1_lable.place(x=700, y=180)
    cname1_entry = Entry(Injections, textvariable=cinj2,bg="#D3D3D3")
    cname1_entry.place(x=750, y=180)

    var = IntVar()
    ra1 = Radiobutton(Injections, text="Remdesivir", variable=var, value=1,bg="#D3D3D3")  # , command=viewSelected)
    ra1.place(x=600, y=150)

    ra2 = Radiobutton(Injections, text="Tocilizumab", variable=var, value=2,bg="#D3D3D3")  # , command=viewSelected)
    ra2.place(x=600, y=180)

    def check_button(operation):
        inj = InjectionsCenter()
        if var.get() == 1: 
            inj1 = "Remdesivir"
            cost = cinj1.get()
        elif var.get() == 2: 
            inj1 = "Tocilizumab"
            cost = cinj2.get()

        if(operation == "Add"): 
            inj.insert_center(cna1.get(), inj1, cost)

        if(operation == "Update"): 
            inj.update_center(cna1.get(), inj1, cost)


    add = Button(Injections, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": check_button(m))
    add.place(x=520, y=300)

    upd = Button(Injections, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": check_button(m))
    upd.place(x=620, y=300)



def openVaccine():
    Vaccine = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Vaccine.geometry("1300x1300")  # sets dimensions of new window
    Vaccine.title("VACCINATION DETAILS")
    Vaccine.iconbitmap(r'img/logo.ico')
    Vaccine['bg'] = '#179dda'

    image1 = Image.open("img/vaccine.jpg")
    image1_resize = image1.resize((1400, 750))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(Vaccine, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=BOTTOM)

    global cn1
    global cvac1
    global cvac2
    cn1 = StringVar()
    cvac1 = StringVar()
    cvac2 = StringVar()

    ccc = Label(Vaccine, text="VACCINATION DETAILS", bg='#179dda')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.place(x=400,y=30)

    cn1_lable = Label(Vaccine, text="Centre Name", bg='#2eb3eb')
    cn1_lable.configure(font=("Geo Sans Light", 13))
    cn1_lable.place(x=650, y=100)
    cn1_entry = Entry(Vaccine, textvariable=cn1)
    cn1_entry.place(x=800, y=100)

    cblood_lable = Label(Vaccine, text="Vaccine Name", bg='#179dda')
    cblood_lable.configure(font=("Geo Sans Light", 13))
    cblood_lable.place(x=650, y=150)

    ccost1_lable = Label(Vaccine, text="Cost- ", bg='#179dda')
    ccost1_lable.configure(font=("Geo Sans Light", 13))
    ccost1_lable.place(x=900, y=150)
    ccost1_entry = Entry(Vaccine, textvariable=cvac1)
    ccost1_entry.place(x=980, y=150)
    cname1_lable = Label(Vaccine, text="Cost- ", bg='#179dda')
    cname1_lable.configure(font=("Geo Sans Light", 13))
    cname1_lable.place(x=900, y=180)
    cname1_entry = Entry(Vaccine, textvariable=cvac2)
    cname1_entry.place(x=980, y=180)

    var = IntVar()
    ra11 = Radiobutton(Vaccine, text="Covishield", variable=var, value=1,bg="#D3D3D3")  # , command=viewSelected)
    ra11.place(x=800, y=150)

    ra22 = Radiobutton(Vaccine, text="Covaxin", variable=var, value=2,bg="#D3D3D3")  # , command=viewSelected)
    ra22.place(x=800, y=180)

    def check_button(operation):
        vac = VaccineCenter()
        if var.get() == 1: 
            vacn = "Covishield"
            cost = cvac1.get()
        elif var.get() == 2: 
            vacn = "Covaxin"
            cost = cvac2.get()

        if(operation == "Add"): 
            vac.insert_center(cn1.get(), vacn, cost)

        if(operation == "Update"): 
            vac.update_center(cn1.get(), vacn, cost)


    add = Button(Vaccine, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": check_button(m))
    add.place(x=750, y=300)

    upd = Button(Vaccine, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": check_button(m))
    upd.place(x=850, y=300)

    

def opencovidInformation():
    covidInformation = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidInformation.geometry("1300x1300")  # sets dimensions of new window
    covidInformation.title("COVID INFORMATION")
    covidInformation.iconbitmap(r'img/logo.ico')
    covidInformation['bg'] = '#4682B4'

    image1 = Image.open("img/information.png")
    image1_resize = image1.resize((1400, 800))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(covidInformation, image=test)
    label1.image = test
    label1.config(bd=0)
    label1.pack(side=BOTTOM)

    global que
    global ans
    que = StringVar()
    ans = StringVar()

    ccc = Label(covidInformation, text="INFORMATION", bg='#555555')
    ccc.configure(font=("Geo Sans Light", 80))
    ccc.place(x=360,y=30)

    que_lable = Label(covidInformation, text="QUESTION: ", bg='#6a6a6a')
    que_lable.configure(font=("Geo Sans Light", 13,'bold'))
    que_lable.place(x=500, y=500)
    que_entry = Entry(covidInformation, textvariable=que)
    que_entry.place(x=650, y=500)

    ans_lable = Label(covidInformation, text="ANSWER: ", bg='#6a6a6a')
    ans_lable.configure(font=("Geo Sans Light", 13,'bold'))
    ans_lable.place(x=500, y=550)
    ans_entry = Entry(covidInformation, textvariable=ans)
    ans_entry.place(x=650, y=550)

    def check_button(operation):
        qna = QnA()

        if operation == "Add":
            qna.insert_question(que.get(), ans.get())
        if operation == "Update":
            qna.update_question(que.get(), ans.get())
        if operation == "Delete":
            qna.delete_question(que.get())
        

    add = Button(covidInformation, text="Add", width=10, height=2,bg="#D3D3D3", command=lambda m="Add": check_button(m))
    add.place(x=500, y=600)

    upd = Button(covidInformation, text="Update", width=10, height=2,bg="#D3D3D3", command=lambda m="Update": check_button(m))
    upd.place(x=600, y=600)

    dele = Button(covidInformation, text="Delete", width=10, height=2,bg="#D3D3D3", command=lambda m="Delete": check_button(m))
    dele.place(x=700, y=600)


# new volunteers registration window
def openregistrationWindow():
    registrationWindow = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    registrationWindow.geometry("1300x1300")  # sets dimensions of new window
    registrationWindow.title("REGISTRATION FORM")
    registrationWindow.iconbitmap(r'img/logo.ico')
    registrationWindow['bg'] = '#ffa07a'

    image1 = Image.open("img/registrationform.jpeg")
    image1_resize=image1.resize((250,150))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(registrationWindow, image=test)
    label1.image = test
    label1.pack()

    #border_color = Frame(registrationWindow, background="red")

    global username
    global password
    global fname
    global fmiddle
    global flast
    global age
    global add
    global num
    global username_entry
    global password_entry
    global username_info
    global password_info

    username = StringVar()
    password = StringVar()
    fname = StringVar()
    fmiddle = StringVar()
    flast = StringVar()
    age = StringVar()
    add = StringVar()
    num = StringVar()

    def register_user():
        user = UserInfo()
        name = fname.get() + " " + fmiddle.get() + " " + flast.get()
        user.insert_user(name, age.get(), num.get(), add.get(), username.get(), password.get())

        r2 = Label(registrationWindow, text="Registration Success", fg="red", font=("calibri", 11))
        r2.place(x=150, y=600)

    r = Label(registrationWindow, text="REGISTRATION FORM", bg='#ffa07a')
    r.configure(font=("Sans", 20, 'bold'))
    r.pack()
    # r.place(x=50, y=50)

    r1 = Label(registrationWindow, text="Come Volunteer With Us And Help Out Your Local Community",font=('Helvetica', 18, 'bold'), bg='#ffa07a')
    r1.place(x=330, y=200)

    butt = Button(registrationWindow, text="Register", width=10, height=1,bg="#D3D3D3", command=register_user)
    butt.place(x=620, y=650)

    password_lable = Label(registrationWindow, text="Password", bg='#ffa07a')
    password_lable.place(x=550, y=600)
    password_entry = Entry(registrationWindow, textvariable=password, show='*')
    password_entry.place(x=650, y=600)

    username_lable = Label(registrationWindow, text="Username", bg='#ffa07a')
    username_lable.place(x=550, y=550)
    username_entry = Entry(registrationWindow, textvariable=username)
    username_entry.place(x=650, y=550)

    address_lable = Label(registrationWindow, text="Address", bg='#ffa07a')
    address_lable.place(x=550, y=500)
    address_entry = Entry(registrationWindow, textvariable=add)
    address_entry.place(x=650, y=500)

    mobile_lable = Label(registrationWindow, text="Mobile", bg='#ffa07a')
    mobile_lable.place(x=550, y=450)
    mobile_entry = Entry(registrationWindow, textvariable=num)
    mobile_entry.place(x=650, y=450)

    age_lable = Label(registrationWindow, text="Age", bg='#ffa07a')
    age_lable.place(x=550, y=400)
    age_entry = Entry(registrationWindow, textvariable=age)
    age_entry.place(x=650, y=400)

    last_lable = Label(registrationWindow, text="Last Name", bg='#ffa07a')
    last_lable.place(x=550, y=350)
    last_entry = Entry(registrationWindow, textvariable=flast)
    last_entry.place(x=650, y=350)

    middle_lable = Label(registrationWindow, text="Middle Name", bg='#ffa07a')
    middle_lable.place(x=550, y=300)
    middle_entry = Entry(registrationWindow, textvariable=fmiddle)
    middle_entry.place(x=650, y=300)

    first_lable = Label(registrationWindow, text="First Name", bg='#ffa07a')
    first_lable.place(x=550, y=250)
    first_entry = Entry(registrationWindow, textvariable=fname)
    first_entry.place(x=650, y=250)


volunWindow = Button(root, text="Volunteers", height=3, width=25,bg='black',fg='white',
                     command=openvolunWindow)
volunWindow.configure(font=('bold'))# a button widget which will open a new window on button click
volunWindow.place(x=380, y=550)


# viewers window
def openviewWindow():
    viewWindow = Toplevel(root)  # Toplevel object which will be treated as a new window
    viewWindow.geometry("1300x1300")  # sets dimensions of new window
    viewWindow.title("WELCOME VIEWERS")
    viewWindow.iconbitmap(r'img/logo.ico')
    viewWindow['bg'] = '#bcf5bc'

    image1 = Image.open("img/resources.jpg")
    image1_resize = image1.resize((1400, 1400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(viewWindow, image=test)
    label1.image = test
    label1.pack()

    '''image1 = Image.open("viewers1.jpeg")
    image1_resize = image1.resize((400, 1400))
    test = ImageTk.PhotoImage(image1_resize)
    label1 = Label(viewWindow, image=test)
    label1.image = test
    label1.place(x=0,y=351)'''

    l2 = Label(viewWindow, text="COVID RELIEF SERVICES", bg='#bc0103', fg='black')
    l2.configure(font=("Bariol", 50, 'bold'))
    l2.place(x=250, y=40)

    intro1 = """Welcome to our  NGO, Covid Relief Services.
    
The coronavirus pandemic is leaving millions of people sick,

unemployed, and struggling to make ends meet.

Thankfully, there are many things you can do to help 

make a difference in your community from the safety of your home.
    
Here, we help you find assistance related to all
             
Covid-19 medical emergencies.
             
We believe that if we fight this virus together, we can defeat it.
             
It is crucial to help each other, during these times.
             
So, If you want to help the society, you can enroll in 
             
our volunteering programmes too.

STAY HOME, STAY SAFE."""

    l3 = Label(viewWindow, justify=LEFT, padx=10, text=intro1, bg='#bc0103',fg='white')
    l3.configure(font=("Arca Majora", 15))
    l3.place(x=50, y=150)

    def openBedsdetails1():
        Bedsdetails1 = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        Bedsdetails1.geometry("1300x1300")  # sets dimensions of new window
        Bedsdetails1.title("BED CENTRE")
        Bedsdetails1.iconbitmap(r'img/logo.ico')
        Bedsdetails1['bg'] = '#3420a8'

        ccc = Label(Bedsdetails1, text="CENTRE DETAILS", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20,'underline'))
        ccc.pack()

        table = OxygenBed()
        data = table.getdata()

        v = Scrollbar(Bedsdetails1)
        v.pack(side = RIGHT, fill = Y)
        t = Text(Bedsdetails1, width = 5000, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        for row in data:
            t.insert(END,"\n\n\n\tCenter ")
            t.insert(END,"   ")
            t.insert(END, row[0])
            t.insert(END, "\n\n\t")
            t.insert(END,"Address ")
            t.insert(END,"   ")
            t.insert(END, row[5])
            t.insert(END, "\n\n\t")
            t.insert(END,"Phone ")
            t.insert(END,"   ")
            t.insert(END, row[4])
            t.insert(END, "\n\n\t")
            t.insert(END,"Available beds ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n\n\t")
            t.insert(END,"Oxygen beds ")
            t.insert(END,"   ")
            t.insert(END, row[2])
            t.insert(END, "\n\n\t")
            t.insert(END,"Total beds ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n")



        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)

        # cnum_lable = Label(Bedsdetails1, text="Centre 1: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15,'bold','underline'))
        # cnum_lable.place(x=10, y=50)

        # cname_lable = Label(Bedsdetails1, text="Centre Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=100)

        # cname1_lable = Label(Bedsdetails1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=100)

        # cno_lable = Label(Bedsdetails1, text="Centre Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=150)

        # cno1_lable = Label(Bedsdetails1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=150)

        # cadd_lable = Label(Bedsdetails1, text="Centre Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=200)

        # cadd1_lable = Label(Bedsdetails1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=200)

        # cnbeds_lable = Label(Bedsdetails1, text="Normal Beds:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=300)

        # cnbeds1_lable = Label(Bedsdetails1, text="Normal Beds", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=300)

        # cobeds_lable = Label(Bedsdetails1, text="Oxygen Beds:", bg='white')
        # cobeds_lable.configure(font=("Geo Sans Light", 15))
        # cobeds_lable.place(x=10, y=350)

        # cobeds1_lable = Label(Bedsdetails1, text="Oxygen Beds", bg='white')
        # cobeds1_lable.configure(font=("Geo Sans Light", 15))
        # cobeds1_lable.place(x=250, y=350)

        # ctbeds_lable = Label(Bedsdetails1, text="Total Beds:", bg='white',fg='red')
        # ctbeds_lable.configure(font=("Geo Sans Light", 15,'bold'))
        # ctbeds_lable.place(x=10, y=400)

        # ctbeds1_lable = Label(Bedsdetails1, text="Total Beds", bg='white', fg='red')
        # ctbeds1_lable.configure(font=("Geo Sans Light", 15, 'bold'))
        # ctbeds1_lable.place(x=250, y=400)

        # cnum_lable = Label(Bedsdetails1, text="Centre 2: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=500)

        # cname_lable = Label(Bedsdetails1, text="Centre Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=550)

        # cname1_lable = Label(Bedsdetails1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=550)

        # cno_lable = Label(Bedsdetails1, text="Centre Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=600)

        # cno1_lable = Label(Bedsdetails1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=600)

        # cadd_lable = Label(Bedsdetails1, text="Centre Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=650)

        # cadd1_lable = Label(Bedsdetails1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=650)

        # cnbeds_lable = Label(Bedsdetails1, text="Normal Beds:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=700)

        # cnbeds1_lable = Label(Bedsdetails1, text="Normal Beds", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=700)

        # cobeds_lable = Label(Bedsdetails1, text="Oxygen Beds:", bg='white')
        # cobeds_lable.configure(font=("Geo Sans Light", 15))
        # cobeds_lable.place(x=10, y=750)

        # cobeds1_lable = Label(Bedsdetails1, text="Oxygen Beds", bg='white')
        # cobeds1_lable.configure(font=("Geo Sans Light", 15))
        # cobeds1_lable.place(x=250, y=750)

        # ctbeds_lable = Label(Bedsdetails1, text="Total Beds:", bg='white', fg='red')
        # ctbeds_lable.configure(font=("Geo Sans Light", 15, 'bold'))
        # ctbeds_lable.place(x=10, y=800)

        # ctbeds1_lable = Label(Bedsdetails1, text="Total Beds", bg='white', fg='red')
        # ctbeds1_lable.configure(font=("Geo Sans Light", 15, 'bold'))
        # ctbeds1_lable.place(x=250, y=800)




    def opentestingLabs1():
        testingLabs1 = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        testingLabs1.geometry("1300x1300")  # sets dimensions of new window
        testingLabs1.title("TESTING LABS")
        testingLabs1.iconbitmap(r'img/logo.ico')
        testingLabs1['bg'] = '#3420a8'

        '''image1 = Image.open("RTPCR-test-covid.jpg")
        image1_resize = image1.resize((500, 750))
        test = ImageTk.PhotoImage(image1_resize)
        label1 = Label(testingLabs1, image=test)
        label1.image = test
        label1.config(bd=0)
        label1.pack(side=LEFT)'''

        ccc = Label(testingLabs1, text="TESTING LABS", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20, 'underline'))
        ccc.pack()

        table = TestingLabs()
        data = table.getdata()

        v = Scrollbar(testingLabs1)
        v.pack(side = RIGHT, fill = Y)
        t = Text(testingLabs1, width = 5000, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        for row in data:
            t.insert(END,"\n\n\n\tCenter ")
            t.insert(END,"   ")
            t.insert(END, row[0])
            t.insert(END, "\n\n\t")
            t.insert(END,"Address ")
            t.insert(END,"   ")
            t.insert(END, row[3])
            t.insert(END, "\n\n\t")
            t.insert(END,"Phone ")
            t.insert(END,"   ")
            t.insert(END, row[2])
            t.insert(END, "\n\n\t")
            t.insert(END,"Available Tests ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n")


        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)

        # cnum_lable = Label(testingLabs1, text="Lab 1: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=50)

        # cname_lable = Label(testingLabs1, text="Lab Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=100)

        # cname1_lable = Label(testingLabs1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=100)

        # cno_lable = Label(testingLabs1, text="Lab Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=150)

        # cno1_lable = Label(testingLabs1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=150)

        # cadd_lable = Label(testingLabs1, text="Lab Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=200)

        # cadd1_lable = Label(testingLabs1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=200)

        # cnbeds_lable = Label(testingLabs1, text="Available Tests:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=300)

        # cnbeds1_lable = Label(testingLabs1, text="Tests", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=300)



        # cnum_lable = Label(testingLabs1, text="Lab 2: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=700)

        # cname_lable = Label(testingLabs1, text="Lab Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=700)

        # cname1_lable = Label(testingLabs1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=700)

        # cno_lable = Label(testingLabs1, text="Lab Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=750)

        # cno1_lable = Label(testingLabs1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=750)

        # cadd_lable = Label(testingLabs1, text="Lab Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=800)

        # cadd1_lable = Label(testingLabs1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=800)

        # cnbeds_lable = Label(testingLabs1, text="Available Tests:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=850)

        # cnbeds1_lable = Label(testingLabs1, text="Tests", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=850)

    def openPlasma1():
        Plasma1 = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        Plasma1.geometry("1300x1300")  # sets dimensions of new window
        Plasma1.title("PLASMA DETAILS")
        Plasma1.iconbitmap(r'img/logo.ico')
        Plasma1['bg'] = '#3420a8'

        '''image1 = Image.open("plasma.jpg")
        image1_resize = image1.resize((900, 1000))
        test = ImageTk.PhotoImage(image1_resize)
        label1 = Label(Plasma1, image=test)
        label1.image = test
        label1.config(bd=0)
        label1.pack(side=LEFT)'''

        ccc = Label(Plasma1, text="PLASMA DETAILS", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20, 'underline'))
        ccc.pack()

        table = PlasmaCenter()
        data = table.getdata()

        v = Scrollbar(Plasma1)
        v.pack(side = RIGHT, fill = Y)
        t = Text(Plasma1, width = 5000, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        for row in data:
            t.insert(END,"\n\n\n\tCenter ")
            t.insert(END,"   ")
            t.insert(END, row[0])
            t.insert(END, "\n\n\t")
            t.insert(END,"Address ")
            t.insert(END,"   ")
            t.insert(END, row[3])
            t.insert(END, "\n\n\t")
            t.insert(END,"Phone ")
            t.insert(END,"   ")
            t.insert(END, row[2])
            t.insert(END, "\n\n\t")
            t.insert(END,"Blood Groups available ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n")



        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)

        # cnum_lable = Label(Plasma1, text="Centre 1: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=50)

        # cname_lable = Label(Plasma1, text="Centre Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=100)

        # cname1_lable = Label(Plasma1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=100)

        # cno_lable = Label(Plasma1, text="Centre Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=150)

        # cno1_lable = Label(Plasma1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=150)

        # cadd_lable = Label(Plasma1, text="Centre Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=200)

        # cadd1_lable = Label(Plasma1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=200)

        # cnbeds_lable = Label(Plasma1, text="Available Blood Groups:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=300)

        # cnbeds1_lable = Label(Plasma1, text="blood Group", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=300)



        # cnum_lable = Label(Plasma1, text="Centre 2: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=500)

        # cname_lable = Label(Plasma1, text="Centre Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=550)

        # cname1_lable = Label(Plasma1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=550)

        # cno_lable = Label(Plasma1, text="Centre Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=600)

        # cno1_lable = Label(Plasma1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=600)

        # cadd_lable = Label(Plasma1, text="Centre Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=650)

        # cadd1_lable = Label(Plasma1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=650)

        # cnbeds_lable = Label(Plasma1, text="Available Blood Groups:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=700)

        # cnbeds1_lable = Label(Plasma1, text="Blood Groups", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=700)


    def openInjections1():
        Injections1 = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        Injections1.geometry("1300x1300")  # sets dimensions of new window
        Injections1.title("INJECTION DETAILS")
        Injections1.iconbitmap(r'img/logo.ico')
        Injections1['bg'] = '#3420a8'

        '''image1 = Image.open("remdesivir.jpg")
        image1_resize = image1.resize((600, 400))
        test = ImageTk.PhotoImage(image1_resize)
        label1 = Label(Injections1, image=test)
        label1.image = test
        label1.config(bd=0)
        label1.place(x=0, y=355)'''

        ccc = Label(Injections1, text="INJECTION DETAILS", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20, 'underline'))
        ccc.pack()

        table = InjectionsCenter()
        data = table.getdata()

        v = Scrollbar(Injections1)
        v.pack(side = RIGHT, fill = Y)
        t = Text(Injections1, width = 5000, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        for row in data:
            t.insert(END,"\n\n\n\tCenter ")
            t.insert(END,"   ")
            t.insert(END, row[0])
            t.insert(END, "\n\n\t")
            t.insert(END,"Address ")
            t.insert(END,"   ")
            t.insert(END, row[4])
            t.insert(END, "\n\n\t")
            t.insert(END,"Phone ")
            t.insert(END,"   ")
            t.insert(END, row[3])
            t.insert(END, "\n\n\t")
            t.insert(END,"Injection name ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n\n\t")
            t.insert(END,"Cost ")
            t.insert(END,"   ")
            t.insert(END, row[2])
            t.insert(END, "\n")



        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)

            # cnum_lable = Label(Injections1, text="Centre 1: ", bg='white')
            # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
            # cnum_lable.place(x=10, y=50)

            # cname_lable = Label(Injections1, text="Centre Name:", bg='white')
            # cname_lable.configure(font=("Geo Sans Light", 15))
            # cname_lable.place(x=10, y=100)

            # cname1_lable = Label(Injections1, text=" Name", bg='white')
            # cname1_lable.configure(font=("Geo Sans Light", 15))
            # cname1_lable.place(x=250, y=100)

            # cno_lable = Label(Injections1, text="Centre Phone Number:", bg='white')
            # cno_lable.configure(font=("Geo Sans Light", 15))
            # cno_lable.place(x=10, y=150)

            # cno1_lable = Label(Injections1, text="Phone Number", bg='white')
            # cno1_lable.configure(font=("Geo Sans Light", 15))
            # cno1_lable.place(x=250, y=150)

            # cadd_lable = Label(Injections1, text="Centre Address:", bg='white')
            # cadd_lable.configure(font=("Geo Sans Light", 15))
            # cadd_lable.place(x=10, y=200)

            # cadd1_lable = Label(Injections1, text="Address", bg='white')
            # cadd1_lable.configure(font=("Geo Sans Light", 15))
            # cadd1_lable.place(x=250, y=200)

            # cnbeds_lable = Label(Injections1, text="Available Injections:", bg='white')
            # cnbeds_lable.configure(font=("Geo Sans Light", 15))
            # cnbeds_lable.place(x=10, y=300)

            # cnbeds1_lable = Label(Injections1, text="Normal Beds", bg='white')
            # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
            # cnbeds1_lable.place(x=250, y=300)

            # cobeds_lable = Label(Injections1, text="Oxygen Beds:", bg='white')
            # cobeds_lable.configure(font=("Geo Sans Light", 15))
            # cobeds_lable.place(x=10, y=350)

            # cobeds1_lable = Label(Injections1, text="Oxygen Beds", bg='white')
            # cobeds1_lable.configure(font=("Geo Sans Light", 15))
            # cobeds1_lable.place(x=250, y=350)

            # cnum_lable = Label(Injections1, text="Centre 2: ", bg='white')
            # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
            # cnum_lable.place(x=10, y=500)

            # cname_lable = Label(Injections1, text="Centre Name:", bg='white')
            # cname_lable.configure(font=("Geo Sans Light", 15))
            # cname_lable.place(x=10, y=550)

            # cname1_lable = Label(Injections1, text=" Name", bg='white')
            # cname1_lable.configure(font=("Geo Sans Light", 15))
            # cname1_lable.place(x=250, y=550)

            # cno_lable = Label(Injections1, text="Centre Phone Number:", bg='white')
            # cno_lable.configure(font=("Geo Sans Light", 15))
            # cno_lable.place(x=10, y=600)

            # cno1_lable = Label(Injections1, text="Phone Number", bg='white')
            # cno1_lable.configure(font=("Geo Sans Light", 15))
            # cno1_lable.place(x=250, y=600)

            # cadd_lable = Label(Injections1, text="Centre Address:", bg='white')
            # cadd_lable.configure(font=("Geo Sans Light", 15))
            # cadd_lable.place(x=10, y=650)

            # cadd1_lable = Label(Injections1, text="Address", bg='white')
            # cadd1_lable.configure(font=("Geo Sans Light", 15))
            # cadd1_lable.place(x=250, y=650)



    def openVaccine1():
        Vaccine1 = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        Vaccine1.geometry("1300x1300")  # sets dimensions of new window
        Vaccine1.title("VACCINATION DETAILS")
        Vaccine1.iconbitmap(r'img/logo.ico')
        Vaccine1['bg'] = '#3420a8'

        '''image1 = Image.open("vaccine.jpg")
        image1_resize = image1.resize((1400, 750))
        test = ImageTk.PhotoImage(image1_resize)
        label1 = Label(Vaccine1, image=test)
        label1.image = test
        label1.config(bd=0)
        label1.pack(side=BOTTOM)'''

        ccc = Label(Vaccine1, text="VACCINATION DETAILS", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20, 'underline'))
        ccc.pack()

        table = VaccineCenter()
        data = table.getdata()

        v = Scrollbar(Vaccine1)
        v.pack(side = RIGHT, fill = Y)
        t = Text(Vaccine1, width = 5000, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        #print(data)
        for row in data:
            t.insert(END,"\n\n\n\tCenter ")
            t.insert(END,"   ")
            t.insert(END, row[0])
            t.insert(END, "\n\n\t")
            t.insert(END,"Address ")
            t.insert(END,"   ")
            t.insert(END, row[4])
            t.insert(END, "\n\n\t")
            t.insert(END,"Phone ")
            t.insert(END,"   ")
            t.insert(END, row[3])
            t.insert(END, "\n\n\t")
            t.insert(END,"Vaccine name ")
            t.insert(END,"   ")
            t.insert(END, row[1])
            t.insert(END, "\n\n\t")
            t.insert(END,"Cost ")
            t.insert(END,"   ")
            t.insert(END, row[2])
            t.insert(END, "\n")



        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)

        # cnum_lable = Label(Vaccine1, text="Centre 1: ", bg='white')
        # cnum_lable.configure(font=("Geo Sans Light", 15, 'bold', 'underline'))
        # cnum_lable.place(x=10, y=50)

        # cname_lable = Label(Vaccine1, text="Centre Name:", bg='white')
        # cname_lable.configure(font=("Geo Sans Light", 15))
        # cname_lable.place(x=10, y=100)

        # cname1_lable = Label(Vaccine1, text=" Name", bg='white')
        # cname1_lable.configure(font=("Geo Sans Light", 15))
        # cname1_lable.place(x=250, y=100)

        # cno_lable = Label(Vaccine1, text="Centre Phone Number:", bg='white')
        # cno_lable.configure(font=("Geo Sans Light", 15))
        # cno_lable.place(x=10, y=150)

        # cno1_lable = Label(Vaccine1, text="Phone Number", bg='white')
        # cno1_lable.configure(font=("Geo Sans Light", 15))
        # cno1_lable.place(x=250, y=150)

        # cadd_lable = Label(Vaccine1, text="Centre Address:", bg='white')
        # cadd_lable.configure(font=("Geo Sans Light", 15))
        # cadd_lable.place(x=10, y=200)

        # cadd1_lable = Label(Vaccine1, text="Address", bg='white')
        # cadd1_lable.configure(font=("Geo Sans Light", 15))
        # cadd1_lable.place(x=250, y=200)

        # cnbeds_lable = Label(Vaccine1, text="Available vaccines:", bg='white')
        # cnbeds_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds_lable.place(x=10, y=300)

        # cnbeds1_lable = Label(Vaccine1, text="vaccines", bg='white')
        # cnbeds1_lable.configure(font=("Geo Sans Light", 15))
        # cnbeds1_lable.place(x=250, y=300)

    def opencovidInformation1():
        covinfo = Toplevel(viewWindow)  # Toplevel object which will be treated as a new window
        covinfo.geometry("1300x1300")  # sets dimensions of new window
        covinfo.title("FAQs")
        covinfo.iconbitmap(r'img/logo.ico')
        covinfo['bg'] = '#3420a8'

        '''image1 = Image.open("vaccine.jpg")
        image1_resize = image1.resize((1400, 750))
        test = ImageTk.PhotoImage(image1_resize)
        label1 = Label(covinfo, image=test)
        label1.image = test
        label1.config(bd=0)
        label1.pack(side=BOTTOM)'''

        ccc = Label(covinfo, text="FAQs", bg='#3420a8')
        ccc.configure(font=("Arial Black", 20, 'underline'))
        ccc.pack()

        table = QnA()
        data = table.getdata()

        v = Scrollbar(covinfo)
        v.pack(side = RIGHT, fill = Y)
        t = Text(covinfo, width = 50, height = 5000, wrap = WORD, yscrollcommand = v.set)
        t.configure(font=("Geo Sans Light", 15), fg='white', bg='#3420a8')

        i=1
        #print(data)
        for row in data:
            t.insert(END,"\n\n\nQuestion :\n ")
            t.insert(END, row[0])
            t.insert(END, "\n\n")
            t.insert(END,"Answer :\n")
            t.insert(END, row[1])
            t.insert(END, "\n")



        t.pack(side=TOP, fill=X)
        v.config(command=t.yview)


    cc = Label(viewWindow, text="Which window do you want to access?",bg="#bc0103",fg='white')
    cc.configure(font=("Geo Sans Light", 20, 'bold'))
    cc.place(x=700, y=150)

    c22 = Button(viewWindow, text="Bed Centre", height=3, width=25,
                 command=openBedsdetails1)  # a button widget which will open a new window on button click
    c22.place(x=750, y=250)

    c33 = Button(viewWindow, text="Testing Labs", height=3, width=25,
                 command=opentestingLabs1)  # a button widget which will open a new window on button click
    c33.place(x=1000, y=250)

    c44 = Button(viewWindow, text="Plasma", height=3, width=25,
                 command=openPlasma1)  # a button widget which will open a new window on button click
    c44.place(x=750, y=350)

    c55 = Button(viewWindow, text="Injections", height=3, width=25,
                 command=openInjections1)  # a button widget which will open a new window on button click
    c55.place(x=1000, y=350)

    c66 = Button(viewWindow, text="Vaccine", height=3, width=25,
                 command=openVaccine1)  # a button widget which will open a new window on button click
    c66.place(x=750, y=450)

    c77 = Button(viewWindow, text="FAQ", height=3, width=25,
                 command=opencovidInformation1)  # a button widget which will open a new window on button click
    c77.place(x=1000, y=450)


viewbtn = Button(root, text="Viewers", height=3, width=25,bg='black',fg='white',
                 command=openviewWindow)  # a button widget which will open a new window on button click
viewbtn.configure(font=('bold'))
viewbtn.place(x=700, y=550)

root.mainloop()