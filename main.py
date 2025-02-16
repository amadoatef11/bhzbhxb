from flet import *
import sqlite3



def main(page:Page):
    page.title = "Ahmed"
    page.window.width= 390
    page.window.height = 740
    page.window.top = 1
    page.scroll = "auto"
    page.window.left= 960
    page.bgcolor="white"
    page.theme_mode = ThemeMode.LIGHT


    tname = TextField(label="اسم الطالب",icon=icons.PERSON,rtl=True,height=38)
    tmail = TextField(label="البريد الكتروني",icon=icons.MAIL,rtl=True,height=38)
    tphone = TextField(label="رقم الهتف",icon=icons.PHONE,rtl=True,height=38)
    taddress = TextField(label="العنوان او السكن",icon=icons.LOCATION_CITY,rtl=True,height=38)

    marktext = Text("Marks Student - علامات الطالب",text_align="center",weight="bold")
    mathmatic = TextField(label="رياطيات",width=110,rtl=True,height=38)
    arabic = TextField(label="عربي",width=110,rtl=True,height=38)
    france = TextField(label="فرنسية",width=110,rtl=True,height=38)
    english = TextField(label="انجليزية",width=110,rtl=True,height=38)
    draw = TextField(label="الرسم",width=110,rtl=True,height=38)
    chemistry = TextField(label="كيميا",width=110,rtl=True,height=38)


    page.add(
         Row([
            Text("تطبيقي",size=20,font_family="IBM plex Sans Arabic",color="black")
        ]),
         Row([
             Text("عدد الطلاب المسجلين:",size=20,font_family="IBM plex Sans Arabic",color="blue"),
             Text(" 1",size=20,font_family="IBM plex Sans Arabic",color="black"),
         ],alignment=MainAxisAlignment.CENTER,rtl=True),
        tname,
        tmail,
        tphone,
        taddress,

        Row([
            marktext
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

        Row([
            mathmatic,arabic,france
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

        Row([
            english,draw,chemistry
        ],alignment=MainAxisAlignment.CENTER,rtl=True)
    )

    page.update()
app(main)