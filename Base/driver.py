# Base driver.py 文件
from appium import webdriver

class Driver:
    """ 声明app驱动对象 """
    # 定义app驱动对象
    app_driver = None

    # 类方法，不需要实例化类 可以直接调用
    @classmethod
    def get_app_driver(cls):
        """ 声明app驱动对象 """
        # 当 app_driver 为 None 时：
        if not cls.app_driver:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            # 声明app_driver对象
            cls.app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 返回app驱动对象
        return cls.app_driver

    # 类方法 不需要实例化类  可以直接调用
    @classmethod
    def quit_app_driver(cls):
        """ 退出app驱动对象"""
        # 当app_driver 有值时,退出app驱动对象
        if cls.app_driver:
            cls.app_driver.quit()
            # 重新给app_driver赋值为None
            cls.app_driver = None
