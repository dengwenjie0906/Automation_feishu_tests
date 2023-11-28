import unittest,random,time
from selenium import webdriver
from common import CommonParameterL,element,logfeishu,feishuLoginPage
from  selenium.webdriver.common.keys import Keys


class TestMessage ( unittest.TestCase ):
    u'''测试用例集合,向同事发送消息'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome ()
        cls.driver.maximize_window()
        feishuLoginPage.feishulogin( cls,url=CommonParameterL.feishuurl,phone_number=CommonParameterL.phone_number,password=CommonParameterL.password,driver=cls.driver,uername=CommonParameterL.uername )

    def test_Message_001(self):
        u'''用例1：用例1的操作步骤'''
        logfeishu.Log.info("右上角找到 9 个点")
        element.waitclick(self.driver,5,'//*[@data-icon="DialpadOutlined"]')
        logfeishu.Log.info("点击消息")
        sreach_windows = self.driver.current_window_handle  #当前窗口
        element.waitclick(self.driver,10,"//i[contains(@style,'passport')]")
        handles = self.driver.window_handles  #  获取所有窗口句柄
        for handle in handles:
            if handle !=sreach_windows:
                 self.driver.switch_to.window(handle) #切到这个窗口
                 logfeishu.Log.info("点击通讯录")
                 element.waitclick(self.driver,10,"//section[@class='nav-items']/section[5]")
                 logfeishu.Log.info("点击查询")
                 element.waitclick(self.driver,10,"//div[contains(@class,'quick')]")
                 logfeishu.Log.info("选择已查询的好友")
                 element.waitsend( self.driver,10,"//input[contains(@class,'quick')]",CommonParameterL.seachname )
                 logfeishu.Log.info("点击选择已查询的好友")
                 element.waitclick(self.driver,10,'//*[@class="quickJump_resultContainer"]/div[2]/div')
                 logfeishu.Log.info("进入到好友并进入聊天界面")
                 element.waitclick(self.driver,10,'//*[@class="chatEditor"]/div/div[2]/div[2]/div')
                 text = "学习自动化自动发消息哈哈" + str(bytes.fromhex(f'{random.randint(0xb0, 0xf7):x}{random.randint(0xa1, 0xf9):x}').decode('gb2312') + "系列" + str(random.randint(0xa1, 0xf9))) #发消息内容
                 logfeishu.Log.info("输入信息发送")
                 element.waitsends(self.driver,10,'//*[@class="chatEditor"]/div/div[2]/div[2]/div//*/p',text)
                 logfeishu.Log.info("信息发送")
                 element.waitsends(self.driver,10,'//*[@class="chatEditor"]/div/div[2]/div[2]/div//*/p',Keys.ENTER)
                 logfeishu.Log.info("验证发送消息是否成功")
                 messagetext="//*[contains(text(),'{}')]".format(text)
                 chatEditortext=element.wait(self.driver,10,messagetext)
                 if chatEditortext.text in text:
                     logfeishu.Log.info("发送成功")
                 else:
                     logfeishu.Log.warning("发送消息失败")
            else:
                self.driver.close()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit ()


if __name__ == "__main__":
    unittest.main ()
