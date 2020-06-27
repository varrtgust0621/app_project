# Page setting_page.py 文件
from Base.base import Base
from Page.pageElements import PageElements

# 设置页面操作的业务方法类
class SettingPage(Base): # 继承父类Base类

    # 初始化方法
    def __init__(self):
        # 继承父类初始化方法
        super().__init__()

    # 点击搜索按钮方法  直接使用父类的点击方法
    def click_search_btn(self):
        """ 点击搜索按钮 """
        self.click_ele(PageElements.search_btn_id)
