# Base base.py 文件
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver

class Base:

    # 初始化方法，获取app驱动对象
    def __init__(self):
        self.driver = Driver.get_app_driver()

    # 定位单个元素方法 显示等待
    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: (By.?? ,属性值)
        :param timeout: 搜素元素超时时间
        :param poll: 搜索元素间隔时间
        :return:定位到的元素对象
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    # 定位一组元素方法 显示等待
    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: (By.?? ,属性值)
        :param timeout: 搜素元素超时时间
        :param poll: 搜索元素间隔时间
        :return:定位到的元素对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 元素点击方法
    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        元素点击方法
        :param loc: (By.?? ,属性值)
        :param timeout: 搜素元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        self.search_ele(loc,timeout,poll).click()

    # 元素输入内容方法
    def input_ele(self, loc, text, timeout=5, poll=1.0):
        """
        元素输入内容方法
        :param loc: (By.?? ,属性值)
        :param text: 输入的文本内容
        :param timeout: 搜素元素超时时间
        :param poll: 搜索元素间隔时间
        :return:
        """
        # 定位目标元素位置
        input_text = self.search_ele(loc,timeout,poll)
        # 清空原有内容
        input_text.clear()
        # 输入文本内容
        input_text.send_keys(text)


