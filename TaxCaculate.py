'''
Created on 2018年10月16日

@author: 沈淋泽
'''
import wx
import decimal

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='hello,Frame', size=(400,300))
        self.initUi()
    
    def initUi(self):
        panel = wx.Panel(self)
        #GridSizer布局 2×4格，5个像素的垂直和水平边距差
        gs = wx.GridSizer(5, 2, 0, 0)
        
        font = wx.Font(10, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.BOLD)
        
        incomingTxt = wx.StaticText(panel,label = '税前月收入：', style=wx.ALIGN_CENTER)
        incomingTxt.SetFont(font)
        gs.Add(incomingTxt,0,wx.ALIGN_CENTER) 
        
        self.incomingInput = wx.TextCtrl(panel)
        gs.Add(self.incomingInput,0,wx.ALIGN_CENTER) 
        
        insuranceTxt = wx.StaticText(panel,label = '五险一金：', style=wx.ALIGN_CENTER)
        insuranceTxt.SetFont(font)
        gs.Add(insuranceTxt,0,wx.ALIGN_CENTER) 
        
        self.insuranceInput = wx.TextCtrl(panel)
        gs.Add(self.insuranceInput,0,wx.ALIGN_CENTER) 
        
        #空白文本占一个单元格
        emptyTxt = wx.StaticText(panel,label = '', style=wx.ALIGN_CENTER)
        gs.Add(emptyTxt,0,wx.ALIGN_CENTER) 
        
        button = wx.Button(panel, label='计算')
        button.Bind(wx.EVT_BUTTON, self.OnClicked)
        gs.Add(button, 0, wx.ALIGN_CENTER)
        
        self.oldTaxTxt = wx.StaticText(panel,label = '旧税率应纳税：0元', style=wx.ALIGN_CENTER)
        self.oldTaxTxt.SetFont(font)
        gs.Add(self.oldTaxTxt, 0, wx.ALIGN_CENTER) 
        
        self.oldIncomeTxt = wx.StaticText(panel,label = '税收收入：0元', style=wx.ALIGN_CENTER)
        self.oldIncomeTxt.SetFont(font)
        gs.Add(self.oldIncomeTxt, 0, wx.ALIGN_CENTER) 
         
        self.newTaxTxt = wx.StaticText(panel,label = '新税率应纳税：0元', style=wx.ALIGN_CENTER)
        self.newTaxTxt.SetFont(font)
        gs.Add(self.newTaxTxt,0,wx.ALIGN_CENTER) 

        self.newIncomeTxt = wx.StaticText(panel,label = '税收收入：0元', style=wx.ALIGN_CENTER)
        self.newIncomeTxt.SetFont(font)
        gs.Add(self.newIncomeTxt, 0, wx.ALIGN_CENTER) 
        
        panel.SetSizer(gs)
    
    def OnClicked(self, event):
        oldTax, oldIncoming, newTax, newIncoming = caculate(self.incomingInput.GetValue(), self.insuranceInput.GetValue())
        self.oldTaxTxt.SetLabelText('旧税率应纳税：'+ oldTax +'元')
        self.oldIncomeTxt.SetLabelText('税收收入：'+ oldIncoming +'元')
        self.newTaxTxt.SetLabelText('新税率应纳税：'+ newTax +'元')
        self.newIncomeTxt.SetLabelText('税收收入：'+ newIncoming +'元')
 
# 应纳税所得额 = 税前收入 - 五险一金 - 起征点
# 应纳税额 = 应纳税所得额 × 税率 - 速算扣除数
def caculate(incoming, insurance):
        #旧税计算
        oldTaxablIncome = float(incoming) - float(insurance) - 3500
        if oldTaxablIncome > 80000:
            oldTax = oldTaxablIncome * 0.45 - 13505
        elif oldTaxablIncome > 55000:
            oldTax = oldTaxablIncome * 0.35 - 5505
        elif oldTaxablIncome > 35000:
            oldTax = oldTaxablIncome * 0.30 - 2755
        elif oldTaxablIncome > 9000:
            oldTax = oldTaxablIncome * 0.25 - 1005
        elif oldTaxablIncome > 4500:
            oldTax = oldTaxablIncome * 0.20 - 555
        elif oldTaxablIncome > 1500:
            oldTax = oldTaxablIncome * 0.10 - 105
        else:
            oldTax = oldTaxablIncome * 0.03 - 0
        oldIncoming = float(incoming) - oldTax
        
        #新税计算
        newTaxablIncome = float(incoming) - float(insurance) - 5000
        if newTaxablIncome>80000:
            newTax = newTaxablIncome*0.45-15160
        elif newTaxablIncome>55000:
            newTax = newTaxablIncome * 0.35 - 7160
        elif newTaxablIncome > 35000:
            newTax = newTaxablIncome * 0.30 - 4410
        elif newTaxablIncome > 25000:
            newTax = newTaxablIncome * 0.25 - 2660
        elif newTaxablIncome > 12000:
            newTax = newTaxablIncome * 0.20 - 1410
        elif newTaxablIncome > 3000:
            newTax = newTaxablIncome * 0.10 - 210
        else:
            newTax = newTaxablIncome * 0.03 - 0
        newIncoming = float(incoming) - newTax
        return str(round(oldTax,2)), str(round(oldIncoming,2)), str(round(newTax,2)), str(round(newIncoming,2))
    
class Application(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True
    
if __name__ == '__main__':
    app = Application()
    app.MainLoop()