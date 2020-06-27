# script test_search.py 文件
import pytest
from Base.driver import Driver
from Base.page import Page

# 定义测试类
class Test_Search:

    # 不需要实例化对象了，导入Page类后 ，直接使用

    # 退出app驱动对象
    def teardown_class(self): # 直接使用Driver类中的退出driver方法
        """ 退出driver对象 """
        Driver.quit_app_driver()

    # 点击搜索按钮 只需要点击一次使其进入搜索页面即可
    # 且该方法为依赖函数 所以使用fixture工厂函数
    @pytest.fixture(scope="class",autouse=True)
    def click_search_btn(self):  # 直接使用设置页面点击搜索按钮方法完成
        """ 点击搜索按钮 """
        Page.get_settingpage().click_search_btn()

    # 测试方法
    @pytest.mark.parametrize("search_data, exp_dara",[("1","休眠"),("m","MAC地址"),("i","IP地址")])
    def test_search_text(self,search_data,exp_dara):
        """
        搜索测试方法
        :param search_data: 搜索输入文本内容
        :param exp_dara: 预期结果
        :return:
        """
        # 搜索输入框输入文本内容
        Page.get_searchpage().input_search_text(search_data)
        # 断言预期结果
        assert exp_dara in Page.get_searchpage().get_search_result()


