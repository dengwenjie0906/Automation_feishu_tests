import sys,os,unittest
base=os.path.dirname(os.path.dirname(os.path.dirname(__file__))).replace("\\","/")
sys.path.append(base)
from BeautifulReport  import BeautifulReport
from tomorrow import threads
from common.element import *

casepath = os.path.abspath(base+"/scripts").replace("\\","/")  # 存在脚本的路径
reportpath=os.path.abspath(base+"/report").replace("\\","/")  #报告路径



def add_case(case_path=casepath, rule="test_*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover

@threads(1)   #开多少个线程
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='feishuReport.html', description='飞书-前台自动化测试报告', log_path=reportpath)

def shopstartrunner():
    cases = add_case()
    for i in cases:
        run(i)

if __name__ == "__main__":
    shopstartrunner()



