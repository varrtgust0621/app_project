# Base page.py 文件
from Page.setting_page import SettingPage
from Page.search_page import SearchPage

# 返回测试脚本所需要用到的所有页面的实例化对象
class Page:

    # 类级别方法，不需要实例化类 直接调用
    @classmethod
    def get_settingpage(cls):
        """ 返回设置页面实例化对象 """
        return SettingPage()

    # 类级别方法，不需要实例化类 直接调用
    @classmethod
    def get_searchpage(cls):
        """ 返回搜索页面实例化对象 """
        return SearchPage()