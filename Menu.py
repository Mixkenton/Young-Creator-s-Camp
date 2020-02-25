from tkinter import *
from tkinter import ttk, messagebox
import webbrowser as web
from tkinter.ttk import Notebook
#csv + datetime
import csv
from datetime import datetime 


def wirtetocsv(cpd,cpc):

	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	#print(dt)
	with open('coffee.csv','a',newline='') as f:
		fw = csv.writer(f)

		data = [cpd,cpc,dt]

		fw.writerow(data)
		print('Date was saved')

GUI = Tk()
GUI.geometry('700x550')
GUI.title('บุคคลสำคัญ')
GUI.configure(bg='black')
#GUI.state('zoomed')


mainmenu = Menu(GUI)
#-------------------Menu fil----------------
menufile = Menu(mainmenu, tearoff=0)
menufile.add_command(label='Close',command=GUI.quit)

#------------------Menu about---------------
def about():
	print('Hello I AM MIXKENTON')
	messagebox.showinfo('Hello','ผมคือ gdramix และนี่คือโปรแกรมแรกของผม')

def webpage():
	url = 'https://www.facebook.com/peeranut.sangkhawasee.90'
	web.open(url)

menuabout =Menu(mainmenu,tearoff=0)
menuabout.add_command(label='About Us',command=about)
menuabout.add_command(label='Our Webpage ',command=webpage)



mainmenu.add_cascade(label='File', menu=menufile) # this is a pack of menu 
mainmenu.add_cascade(label='About', menu=menuabout)
GUI.config(menu=mainmenu)

#----------------TAB----------------------
Tab = Notebook(GUI)

tabsell = Frame(Tab)
tabinfo = Frame(Tab)

Tab.add(tabsell, text='บิล เกตส์')

Tab.pack(fill=BOTH, expand =1) #file= x file=y fill=BOTH


#-------------------------------------------------
def Latte():
	name ='วิลเลียม เฮนรี เกตส์ ที่สามรือที่มักเป็นที่รู้จักในชื่อ บิล เกตส์ เป็นนักธุรกิจชาวอเมริกัน \nและหนึ่งในผู้ก่อตั้งบริษัทไมโครซอฟท์ เขากับผู้บุกเบิกด้านคอมพิวเตอร์ส่วนบุคคลคนอื่น ๆ \nได้ร่วมกันเขียนต้นแบบของภาษาอัลแตร์เบสิก'

	text = ": %s "%(name,)
	res.set(text)
	wirtetocsv(name) 

def Esapreso():
	name ="""ปริญญาดุษฎีบัณฑิตกิตติมศักดิ์ จาก มหาวิทยาลัยฮาร์วาร์ด 
	 ปริญญาดุษฎีบัณฑิตกิตติมศักดิ์ จาก มหาวิทยาลัยวาเซดะ  
	 รางวัลเกียรติยศผู้บัญชาการอัศวินแห่งจักรวรรดิบริเตน จากสหราชอาณาจักร ตามประกาศเมื่อปี 
     ปริญญาดุษฎีบัณฑิตกิตติมศักดิ์ จากสถาบันเทคโนโลยีหลวง (Royal Institute of Technology) กรุงสต็อกโฮล์ม ประเทศสวีเดน 
     ติดหนึ่งใน ร้อย อันดับบุคคลสำคัญผู้มีอิทธิพลต่อประชาชนในสื่อต่าง ๆ จากการจัดอันดับของ หนังสือพิมพ์ เดอะ การ์เดียน 
     ติดอันดับบุคคลผู้มีอำนาจ, นิตยสารซันเดย์ ไทม 
     อันดับ สอง ในการจัดอันดับ ร้อย ดาวรุ่ง, นิตยสารอัพไซด์ 
     อันดับ หนึ่ง ในการจัดอันดับ ห้าสิบ ดาวรุ่งในโลกไซเบอร์, นิตยสารไทม 
     อันดับที่ ยี่สิบแปด ใน ร้อย อันดับบุคคลสำคัญผู้มีอิทธิพลในวงการกีฬา, นิตยสารสปอร์ตติง นิวส์ 
     ผู้บริหารระดับสูงแห่งปี, นิตยสารชีฟ เอกเซกคูทีฟ ออฟฟิซเซอร์ 
     นักกีฏวิทยา ได้ตั้งชื่อแมลงวันตอมดอกไม้พันธุ์หนึ่งว่า Eristalis gatesi ตามชื่อของบิล เกตส์ เพื่อเป็นเกียรติแก่เขา"""

	text = ":%s "%(name)
	res.set(text) 
	wirtetocsv(name) 

def Mocha():
	name ="""
	โปรแกรมคอมพิวเตอร์หลายตัว ซึ่งส่วนใหญ่ทำงานบนระบบปฏิบัติการอื่นนอกเหนือจากไมโครซอฟท์ วินโดวส์ 
	ได้อ้างถึงบิล เกตส์ ไม่ทางตรงก็ทางอ้อม โดยส่วนใหญ่จะไม่ค่อยจะอ้างถึงในทางชื่นชมสักเท่าไรนัก ซึ่งในจำนวนนี้มี:
เกมโอเพนซอร์ส XBill ซึ่งมีตัวละครชื่อ "บิล" ใส่แว่นตากรอบหนา กำลังพยายามจะลง วิงโดวส์ (โปรแกรมไวรัสที่ปลอมตัวมาเป็นวินโดวส์)
 บนเครื่องคอมพิวเตอร์ที่ใช้ระบบปฏิบัติการอื่น
เกม Uropa² บน Amiga ที่มีตัวร้ายหลักชื่อว่า "บิล เซแทก" (Setag = Gates สะกดแบบถอยหลัง)
ในเกม Might and Magic VII: For Blood and Honor ผู้เล่นถูกมอบหมายภารกิจหนึ่งให้สังหารตัวละครผู้ชั่วร้ายชื่อว่า 
"วิลเลียม เซแทก" และช่วยเหลือเจ้าหญิงที่ถูกมันจับไป
Arcanum: Of Steamworks and Magick Obscura บน ไมโครซอฟท์ วินโดวส์ ได้มีตัวละครตัวหนึ่งชื่อว่า "กิลเบิร์ต เบตส์
" ผู้ประกอบการผู้มั่งคั่ง ชื่อของตัวละคร "กิล เบตส์" เป็นคำผวนของ "บิล เกตส์" นั่นเอง
ในSpace Quest III: The Pirates of Pestulon เกมแอดเวนเจอร์บนเครื่องคอมพิวเตอร์ส่วนบุคคล ได้กล่าวถึงบริษัทซอฟต์แวร์ชื่อ
 "สกัมซอฟท์" ซึ่งเป็นชื่อล้อเลียนไมโครซอฟท์ คอร์ปอเรชัน ประธานบริษัทผู้ชั่วร้าย เป็นชายร่างเล็ก มีบุคลิกแบบพวกเนิร์ดสวมแว่นตา มีชื่อว่า
  "เอลโม พัก" ผู้ซึ่งมีลักษณะคล้ายคลึงกับบิล เกตส์มาก
โปรแกรมคอมพิวเตอร์สำหรับออกแบบคอมพิวเตอร์ชิป อันเป็นผลิตภัณฑ์ของ Electronic Design Automation ใช้ชื่อว่า "Build Gates" 
(สร้างประตู) ซึ่งประตูในที่นี้หมายถึงประตูตรรกะ (logic gate)
Kill Bill edition เป็นชื่อแผ่นซีดีสำหรับบู้ทลินุกซ์ของ SLAX ซึ่งล้อเลียนภาพยนตร์เรื่อง นางฟ้าซามูไร (Kill Bill) 
ภาพวอลล์เปเปอร์ของผลิตภัณฑ์เป็นรูปตัวทักซ์ (นกเพ็นกวินสัญลักษณ์ของลินุกซ์) ในชุดสีเหลืองคล้ายกับที่นางเอกเรื่องนางฟ้าซามูไรสวมใส่ 
เพื่อที่จะสังหารบิล (เกตส์)
ในวิดีโอเกมมาเฟียของ Illusion Softworks คนชื่อ "วิลเลียม เกตส์" ออกมาปรากฏตัวในฐานะคนขายสินค้าละเมิดลิขสิทธิ์ชาวเคนทักกี
ในเกมกลยุทธ์คลาสสิก Total Annihilation: Core Contingency มีส่วนหนึ่งของเนื้อเมืองในเกมที่มีชื่อว่า "อาคารวิลลี เกตส์" 
ซึ่งถ้าหากผู้เล่นยึดอาคารหลังนี้ได้จะทำแต้มได้มาก
"""
	text = ": %s"%(name)
	res.set(text)
	wirtetocsv(name)  






BLatte = ttk.Button(tabsell, text='จากวิกิพีเดีย สารานุกรมเสรี',command = Latte)
BLatte.grid(row=0,column=0,ipadx=20,ipady=20)

BEsapreso = ttk.Button(tabsell, text='เกียรติประวัติ',command = Esapreso  )
BEsapreso.grid(row=0,column=1,ipadx=20,ipady=20)

BMocha = ttk.Button(tabsell, text='ในซอฟต์แวร์',command = Mocha )
BMocha.grid(row=0,column=2,ipadx=20,ipady=20)


#-------------------------------------------------
FResult = Frame(tabsell)
FResult.place(x=10,y=100)

res = StringVar() #**************
res.set('this is Result')

pc = StringVar()

LResult = Label(FResult, textvariable=res, font=('Angsana New',11,'bold'),fg='black',bg ='gray')
LResult.pack()




#-------------------------------------------------







GUI.mainloop()