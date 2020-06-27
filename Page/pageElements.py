# Page pageElements.py 文件
from selenium.webdriver.common.by import By

# 以页面为单位，存放每个页面的元素
class PageElements:
    """ 管理所有页面的元素"""
    # ------设置页面------
    # 搜索按钮
    search_btn_id = (By.ID,"com.android.settings:id/search")

    # ------搜索页面------
    # 搜索输入框
    search_input_id = (By.ID,"android:id/search_src_text")
    # 搜索显示结果
    search_result_ids = (By.ID,"com.android.settings:id/title")