# -*- coding: utf-8 -*-
# Improve and use it free !
import wx 
 
class MDIFrame(wx.MDIParentFrame): 
   def __init__(self): 
      wx.MDIParentFrame.__init__(self, None, -1, "VASP", size = (800,600))
#--------------------------------------------------------------------------------------------
#-------------------------------------------- 菜单栏设置
      #panel = wx.Panel(self)  
      #panel.SetBackgroundColour('Black')
      
      menu1 = wx.Menu() 
      menu1.Append(5000, "&INCAR","计算参数文件")
      menu1.Append(5001, "&KINPOINTS","K点设置文件")      
      menu1.Append(5002, "&POSCAR","几何结构信息文件")
      menu1.Append(5003, "&POTCAR","原子赝势文件")    
      menu1.Append(5004, "&Exit","退出程序") 
        
#---------------------------------
      
      menu2 = wx.Menu()
      menu2.Append(5005,"hello1","saysome")
      menu2.Append(5006,"hello2","saysome")
      menu2.Append(5007,"hello3","saysome")
#---------------------------------

      menubar = wx.MenuBar()
      menubar.Append(menu1, "&File")
      menubar.Append(menu2, "&SomeThing")
      
      
#-----------------------------------------------------------
#---------------------------------------------菜单栏事件绑定

      
      self.SetMenuBar(menubar) 
      self.Bind(wx.EVT_MENU, self.OnNewWindow, id = 5000)
      self.Bind(wx.EVT_MENU, self.OnNewWindow1, id = 5001)
      self.Bind(wx.EVT_MENU, self.OnNewWindow2, id = 5002)
      self.Bind(wx.EVT_MENU, self.OnNewWindow3, id = 5003)
      self.Bind(wx.EVT_MENU, self.OnExit, id = 5004)

#--------------------------------------------------创建状态栏
      statusBar = self.CreateStatusBar()
      
      
#-----------------------------------------------------------
#----------------------------------------------菜单栏事件

		
   def OnExit(self, evt): 
      self.Close(True)





      
#---------------------------------------------------------------------------------------------------------INCAR窗口		
   def OnNewWindow(self, evt): 
      win = wx.MDIChildFrame(self, -1, "INCAR", size = (780,510))
      panel = wx.Panel(win)
      #panel.SetBackgroundColour('Black')
      
#---------------------------------------------------------------------------    
#--------------------------------------------------按钮
      
      buttonA = wx.Button(panel, label = 'PRINT', pos = (405,430))      
      buttonB = wx.Button(panel, label = 'SAVE', pos = (510,430))      
      self.Bind(wx.EVT_BUTTON, self.OnClickA,buttonA)
      self.Bind(wx.EVT_BUTTON, self.OnClickB,buttonB)
#--------------------------------------------------文本
      
      text1 = wx.TextCtrl(panel, value="System name", style=wx.TE_MULTILINE,pos=(400, 10), size=(200, 400)) 
      self.Bind(wx.EVT_TEXT_ENTER, self.OnText1, text1)
      
#------------------------------------------------------------------------------------------       
#-------------------------------------------------------------------------------标签
      labelA0 = wx.StaticText(panel, label = "初始参数部分：", pos = (10,10))
      labelA1 = wx.StaticText(panel, label = "SYSTEM", pos = (10,40))      
      labelA2 = wx.StaticText(panel, label = "ISTART", pos = (10,70))#
      labelA3 = wx.StaticText(panel, label = "ICHARG", pos = (10,100))#
      labelA4 = wx.StaticText(panel, label = "PREC",   pos = (10,130))#
      labelA5 = wx.StaticText(panel, label = "LREAL",  pos = (10,160))#
#------------------------------------------------------------------------------------------
      labelB0 = wx.StaticText(panel, label = "自恰迭代部分：", pos = (10,190))
      labelB1 = wx.StaticText(panel, label = "ENCUT", pos = (10,220))      
      labelB2 = wx.StaticText(panel, label = "ISPIN", pos = (10,250))
      labelB3 = wx.StaticText(panel, label = "NELM", pos = (10,280))
      labelB4 = wx.StaticText(panel, label = "EDIFF",   pos = (10,310))
      labelB5 = wx.StaticText(panel, label = "LCHARG",  pos = (10,340))
      labelB6 = wx.StaticText(panel, label = "LWAVE", pos = (10,370))
      labelB7 = wx.StaticText(panel, label = "ISMEAR",   pos = (10,400))
      labelB8 = wx.StaticText(panel, label = "SIGMA",  pos = (10,430))
#------------------------------------------------------------------------------------------
      labelC0 = wx.StaticText(panel, label = "离子驰豫部分：", pos = (200,10))
      labelC1 = wx.StaticText(panel, label = "IBRION", pos = (200,40))#    
      labelC2 = wx.StaticText(panel, label = "ISIF", pos = (200,70))#
      labelC3 = wx.StaticText(panel, label = "NSW", pos = (200,100))
      labelC4 = wx.StaticText(panel, label = "POTIM",   pos = (200,130))
      labelC5 = wx.StaticText(panel, label = "EDIFFG",  pos = (200,160))
#------------------------------------------------------------------------------------------
      labelD0 = wx.StaticText(panel, label = "态密度相关参数设置：", pos = (200,190))
      labelD1 = wx.StaticText(panel, label = "NBANDS", pos = (200,220))      
      labelD2 = wx.StaticText(panel, label = "LORBIT", pos = (200,250))
      labelD3 = wx.StaticText(panel, label = "ICHARG", pos = (200,280))
      labelD4 = wx.StaticText(panel, label = "EMIN",   pos = (200,310))
      labelD5 = wx.StaticText(panel, label = "EMAX",  pos = (200,340))
      labelD6 = wx.StaticText(panel, label = "NEDOS",  pos = (200,370))
#--------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------列表

      
      self.A1=wx.TextCtrl(panel,-1,"",pos=(100,40),size=(80,-1))        #----------SYSTEM
      self.A1.SetInsertionPoint(0)
      self.Bind(wx.EVT_TEXT, self.A1_F, self.A1)


      ListA2 = ['0', '1' , '2']                                         #----------ISTART
      self.chA2 = wx.Choice(panel, -1, (100, 70), choices = ListA2)
      self.Bind(wx.EVT_CHOICE, self.A2_F, self.chA2)


      ListA3 = ['0', '1' , '2',"11","12"]                               #----------ICHARG
      self.chA3 = wx.Choice(panel, -1, (100, 100), choices = ListA3)
      self.Bind(wx.EVT_CHOICE, self.A3_F, self.chA3)
      
      ListA4 = [ 'Low','Medium', 'High', 'Accurate']                    #-----------PREC
      self.chA4 = wx.Choice(panel, -1, (100, 130), choices = ListA4)
      self.Bind(wx.EVT_CHOICE, self.A4_F, self.chA4)

      ListA5 = ['FALSE', 'TRUE', 'ON', 'AUTO']                          #-----------LREAL
      self.chA5 = wx.Choice(panel, -1, (100, 160), choices = ListA5)
      self.Bind(wx.EVT_CHOICE, self.A5_F, self.chA5)
      
#-------------------------------------------------------------

      
      self.B1=wx.TextCtrl(panel,-1,"",pos=(100, 220),size=(80,-1))        #----------ENCUT
      self.B1.SetInsertionPoint(0)
      self.Bind(wx.EVT_TEXT, self.B1_F, self.B1)
      

      self.B2 = wx.SpinCtrl(panel, -1, "", pos=(100, 250),size=(80,-1))  #----------ISPIN
      self.B2.SetRange(1,100)
      self.B2.SetValue(1)
      self.Bind(wx.EVT_SPINCTRL, self.B2_F, self.B2)
      self.Bind(wx.EVT_TEXT, self.B2_F1, self.B2)

      
      ListB3 = ['10', '20', '30', '40', '50', '60','70', '80']
      self.chB3 = wx.Choice(panel, -1, (100, 280), choices = ListB3)
      self.Bind(wx.EVT_CHOICE, self.B3_F, self.chB3)

      ListB4 = ['1E-01', '1E-02', '1E-03', '1E-04', '1E-05', '1E-06','1E-07', '1E-08']
      self.chB4 = wx.Choice(panel, -1, (100, 310), choices = ListB4)
      self.Bind(wx.EVT_CHOICE, self.B4_F, self.chB4)

      ListB5 = ['TRUE', 'FALSE']#
      self.chB5 = wx.Choice(panel, -1, (100, 340), choices = ListB5)
      self.Bind(wx.EVT_CHOICE, self.B5_F, self.chB5)

      ListB6 = ['TRUE', 'FALSE']#
      self.chB6 = wx.Choice(panel, -1, (100, 370), choices = ListB6)
      self.Bind(wx.EVT_CHOICE, self.B6_F, self.chB6)

      ListB7 = ['-5', '-4', '-3', '-2', '-1', '0']#
      self.chB7 = wx.Choice(panel, -1, (100, 400), choices = ListB7)
      self.Bind(wx.EVT_CHOICE, self.B7_F, self.chB7)

      ListB8 = ['0.1', '0.2']#
      self.chB8 = wx.Choice(panel, -1, (100, 430), choices = ListB8)
      self.Bind(wx.EVT_CHOICE, self.B8_F, self.chB8)

#---------------------------------------------------------------      
      ListC1 = ['-1', '0', '1', '2', '3', '4','5', '6', '7', '8']#
      self.chC1 = wx.Choice(panel, -1, (300, 40), choices = ListC1)
      self.Bind(wx.EVT_CHOICE, self.C1_F, self.chC1)

      ListC2 = ['0', '1', '2', '3', '4', '5','6','7']
      self.chC2 = wx.Choice(panel, -1, (300, 70), choices = ListC2)
      self.Bind(wx.EVT_CHOICE, self.C2_F, self.chC2)

      self.C3=wx.TextCtrl(panel,-1,"",pos=(300, 100),size=(80,-1))        #----------ENCUT
      self.C3.SetInsertionPoint(0)
      self.Bind(wx.EVT_TEXT, self.C3_F, self.C3)

      self.C4=wx.TextCtrl(panel,-1,"",pos=(300, 130),size=(80,-1))        #----------ENCUT
      self.C4.SetInsertionPoint(0)
      self.Bind(wx.EVT_TEXT, self.C4_F, self.C4)



      ListC5 = ['1E-01', '1E-02', '1E-03', '1E-04', '1E-05', '1E-06','1E-07', '1E-08']
      self.chC5 = wx.Choice(panel, -1, (300, 160), choices = ListC5)
      self.Bind(wx.EVT_CHOICE, self.C5_F, self.chC5)

#--------------------------------------------------------------

      ListD1 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD1 = wx.Choice(panel, -1, (300, 220), choices = ListD1)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD1)

      ListD2 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD2 = wx.Choice(panel, -1, (300, 250), choices = ListD2)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD2)

      ListD3 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD3 = wx.Choice(panel, -1, (300, 280), choices = ListD3)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD3)

      ListD4 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD4 = wx.Choice(panel, -1, (300, 310), choices = ListD4)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD4)

      ListD5 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD5 = wx.Choice(panel, -1, (300, 340), choices = ListD5)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD5)

      ListD6 = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
      self.chD6 = wx.Choice(panel, -1, (300, 370), choices = ListD6)
      self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.chD6) 

      
      win.Show(True)

#--------------------------------------------------事件1


      
   def OnClickA(self, evt): 
      print("hello")

   def OnClickB(self, evt): 
      print("hi")

   def OnText1 (self ,event):
      print( event.GetString())

      

   def A1_F (self, event):                                         #-----SYSTEM
      print( "SYSTEM = %s\n" % event.GetString() )


   def A2_F(self, event):                                          #-----ISTART                   
      print('ISTART = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def A3_F(self, event):                                          #-----ICHARG                   
      print('ICHARG = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def A4_F (self, event):                                         #-----PREC
      print( 'PREC = %s\n' % event.GetString())


   def A5_F(self, event):                                          #-----LREAL                   
      print('LREAL = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def B1_F (self, event):                                         #-----SYSTEM
      print( "ENCUT = %s\n" % event.GetString() )




     
   def B2_F(self, evt):
      print( 'ISPIN = : %d\n' % self.B2.GetValue())

   def B2_F1(self, evt):
      print( 'ISPIN = %d\n' % self.B2.GetValue())

   def B3_F(self, event):                                          #-----NELM                   
      print('NELM = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def B4_F(self, event):                                          #-----EDIFF                  
      print('EDIFF = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def B5_F(self, event):                                          #-----LCHARG                 
      print('LCHARG = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")
         
   def B6_F(self, event):                                          #-----LWAVE                   
      print('LWAVE = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def B7_F(self, event):                                          #-----ISMEAR                   
      print('ISMEAR = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def B8_F(self, event):                                          #-----SIGMA                   
      print('SIGMA = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")
#----------------------------------------------

   def C1_F(self, event):                                          #-----SIGMA                   
      print('IBRION = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")

   def C2_F(self, event):                                          #-----SIGMA                   
      print('ISIF = %s\n' % event.GetString())
      if event.GetString() == 'one':
         print("well done")   

   def C3_F(self, evt):
      print( 'NSW = %s\n' % self.C3.GetValue())

   def C4_F(self, evt):
      print( 'POTIM = %s\n' % self.C4.GetValue())

   def C5_F(self, event):                                                                               
      print('EDIFFG = %s\n' % event.GetString())
      #self.chA1.Append("A new item")

      if event.GetString() == 'one':
         print("well done")

          
   def EvtChoice(self, event):                                                                               
      print('EvtChoice: %s\n' % event.GetString())
      #self.chA1.Append("A new item")

      if event.GetString() == 'one':
         print("well done")


#------------------------------------------------------------------------------------------  
#---------------------------------------------------------------------------------------------------------KINPOINTS窗口

   def OnNewWindow1(self, evt): 
      win = wx.MDIChildFrame(self, -1, "KINPOINTS")

      panel = wx.Panel(win)
      self.slider=wx.Slider(panel,100,1,1,10,pos=(25,60),size=(250,-1),style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS) 
      self.slider.SetTickFreq(100)
      #self.slider.SetPageSize(10)
      self.Bind(wx.EVT_SLIDER, self.say, self.slider)

      self.sc = wx.SpinCtrl(panel, -1, "", pos=(25, 120))
      self.sc.SetRange(1,100)
      self.sc.SetValue(5)
      self.Bind(wx.EVT_SPINCTRL, self.OnSpin, self.sc)
      self.Bind(wx.EVT_TEXT, self.OnText, self.sc)

      self.basicText=wx.TextCtrl(panel,-1,"",pos=(25,180),size=(175,-1))
      self.basicText.SetInsertionPoint(0)
      self.Bind(wx.EVT_TEXT, self.printme, self.basicText)
      


     
      win.Show(True)

#-------------------------------------------------------------------------事件2
   def say(self, event):
      print('OnSpin: %d\n' % self.slider.GetValue())
      
   def OnSpin(self, evt):
      print( 'OnSpin: %d\n' % self.sc.GetValue())

   def OnText(self, evt):
      print( 'OnText: %d\n' % self.sc.GetValue())

   def printme (self ,event):
      print( 'OnText: %s\n' % self.basicText.GetValue())
#--------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------POSCAR窗口
   def OnNewWindow2(self, evt): 
      win = wx.MDIChildFrame(self, -1, "POSCAR")
      win.Show(True)
#---------------------------------------------------------------------------------------------------------POTCAR窗口      
   def OnNewWindow3(self, evt): 
      win = wx.MDIChildFrame(self, -1, "POTCAR")
      win.Show(True) 
#------------------------------------

 
#-------------------------------------------------------------------------
      
app = wx.App() 
frame = MDIFrame() 
frame.Show() 
app.MainLoop()
