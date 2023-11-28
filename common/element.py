import sys,os,glob

import pymysql

base=os.path.dirname(os.path.dirname(__file__)).replace("\\","/")
sys.path.append(base)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import select
import time
from common import logfeishu
log = logfeishu.Log ()

#等待点击
def waitclick(driver,timeout,XPATH):
    time.sleep(1)
    F=WebDriverWait(driver,timeout,2).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    F.click()
    # return F.text

#断言
def waitassert(driver,timeout,XPATH,message,descriptor='操作失败'):
    '''
     :param driver:  驱动浏览器
     :param timeout: 超时时间
     :param XPATH: 元素
     :param message: 判断加载后出现判断
     :return:
     '''
    time.sleep(1)
    F=WebDriverWait(driver,timeout,0.5).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    assert message in F.text,descriptor

#返回值
def waitreturn(driver,timeout,XPATH):
    '''    :param driver:    :param timeout:    :param XPATH:    :return: 文本    '''
    time.sleep(1)
    F=WebDriverWait(driver,timeout,0.5).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    return F.text

#等待元素出现在输入
def waitsend(driver,timeout,XPATH,send):
    time.sleep(1)
    WebDriverWait(driver,timeout,0.5).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    F=driver.find_element(By.XPATH,XPATH)
    F.clear()
    F.send_keys(send)

#等待元素出现在输入
def waitsends(driver,timeout,XPATH,send):
    time.sleep(1)
    WebDriverWait(driver,timeout,0.5).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    F=driver.find_element(By.XPATH,XPATH)
    F.send_keys(send)

#等待元素出现
def wait(driver,timeout,XPATH):
    F=WebDriverWait(driver,timeout,0.5).until(ec.presence_of_element_located((By.XPATH,XPATH)))
    return F

#等待元素出现在输入并清理
def waitclearsend(driver,xpath,send,timeout=10):
    WebDriverWait(driver, timeout, 1).until(ec.presence_of_element_located((By.XPATH, xpath)))
    F = driver.find_element(By.XPATH,xpath)
    F.clear()
    F.send_keys(send)
    return  F

#等待元素出现在输入
def waituntilsend(driver,xpath,send,timeout=10):
    WebDriverWait(driver, timeout, 1).until(ec.presence_of_element_located((By.XPATH, xpath)))
    F = driver.find_element(By.XPATH,xpath)
    F.send_keys(send)
    return  F

#("进入页面判断")
def Judge(driver,timeout,XPATH,string):
    WebDriverWait(driver, timeout,0.5).until(ec.presence_of_element_located((By.XPATH, XPATH)))
    F=driver.find_element(By.XPATH,XPATH)
    if F.is_displayed() ==True:
        F.click()
        log.info("进入【{}】页面成功 : url  ====>  {}".format(string,driver.current_url))
        time.sleep(1)
    else:
        log.error("进入页面失败")
#关闭
def close(driver):
    c = driver.quit()
    return c

#打开url
def url(driver,url):
    u = driver.get(url)
    return u

#id元素
def id(driver,id):
    f =  driver.find_element_by_id(id)
    return f

#xpath元素
def Xpath(driver,xpath):
    f = driver.find_element(By.XPATH,xpath)
    return f

#css元素
def Css(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f

'''定位一组元素封装'''
def findsIdl(driver,id):
    f =  driver.find_elements_by_id(id)

    return f

def findsXpathl(driver,xpath):
    f = driver.find_elements(By.XPATH,xpath)
    return f

def findsCssl(driver,css):
    f = driver.find_elements_by_css_selector(css)
    return f

'''定位元素封装,输入'''
def findsIds(driver,id,send):
    f =  driver.find_element_by_id(id).send_keys(send)
    return f

def findsCsss(driver,css,send):
    f = driver.find_element_by_css_selector(css).send_keys(send)
    return f

'''定位元素封装,点击'''
def findsIdc(driver,id):
    f =  driver.find_element_by_id(id).click()
    return f

def findsXpathc(driver,xpath):
    f = driver.find_element(By.XPATH,xpath).click()
    return f

def findsCsssc(driver,css):
    f = driver.find_element_by_css_selector(css).click()
    return f

def Xpathtext(driver,xpath):
    f=driver.find_element(By.XPATH,xpath).text
    log.info("******{}******".format(f))
    return f

#跳出iframe 框架 进入另一个iframe
def iframe(driver,time,xpath):
    driver.switch_to.default_content()
    driver.switch_to.frame(wait(driver,time, xpath))

#进入iframe 框架
def defaultiframe(driver,time,xpath):
    driver.switch_to.frame(wait(driver,time, xpath))

#鼠标操作  双击
def actionChains(driver,xpath):
    # wait(driver,10,xpath)
    ActionChains(driver).move_to_element(Xpath(driver,xpath)).double_click().perform()



#清除输入框
def clear(driver,xpath):
    wait(driver,10,xpath)
    f=driver.find_element_by_xpath(xpath).clear()
    return f

#显示内容
def target(driver,xpath):
    wait(driver,10,xpath)
    target = Xpath(driver,xpath)
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(2)

# 窗口操作
def handle(driver,xpath):
    sreach_windows = driver.current_window_handle  #当前窗口
    waitclick(driver,20, xpath) #点击当前元素
    handles = driver.window_handles  #  获取所有窗口句柄
    for handle in handles:
        if handle !=sreach_windows:
            driver.switch_to.window(handle) #切到这个窗口

def selects(driver,xpath,index,time=20):
    wait(driver,time,xpath)
    select.Select(Xpath(driver,xpath)).select_by_index(index)

def delfile(path):  #删除文件夹下的所有文件
    fileNames = glob.glob(path + r'\*')
    print(fileNames)
    for fileName in fileNames:
        try:
            os.remove(fileName)
        except:
            try:
                os.rmdir(fileName)
            except:
                delfile(fileName)
                os.rmdir(fileName)


def mysql(sql):
    # 连接数据库
    connection = pymysql.connect(host='xxx', user='xx', password='xxx', db='xxx', port=3307,
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()  # 通过cursor创建游标
    try:
        sqlvalue = sql  # "# 创建sql 语句，并执行
        cursor.execute(sqlvalue)
        result = cursor.fetchone()  # 查询数据库单条数据
        # result = cursor.fetchall() #查询数据库多条数据
        # 提交sql
        connection.commit()
        return result
    except:
        try:
            cursor.execute(sql)
            connection.commit()
        except:
            connection.rollback()
    finally:
        connection.close()#前台查询

