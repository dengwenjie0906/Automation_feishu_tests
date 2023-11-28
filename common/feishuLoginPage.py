from common import element
from common import logfeishu
log = logfeishu.Log ()

def feishulogin(self,url,phone_number, password,driver,uername):
    """获取的用户名密码登录    """
    element.url(driver,url)
    element.waitclick(driver,10,'//div[@class="hc_Popup-content"]//*[contains(@fill,"#")]')
    element.waitclick(driver,5,"//a[contains(@href,'login')]")

    element.waitclick(driver,10,'//*[contains(@class,"mode")]//*[@fill="none"]')


    element.waitsend(driver,10,'//*[@name="mobile_input"]',phone_number)
    element.waitclick(driver,2,'//*[@role="checkbox"]')
    element.waitclick(driver,5,"//button[contains(@class,'button')]")
    element.waitsend(driver,10,'//*[@name="password_input"]',password)
    element.waitclick(driver,5," //button[contains(@data-test,'pwd')]")
    element.waitassert(driver,20,"//div[contains(@class,'name')]",uername)
    log.info('成功登录系统')




