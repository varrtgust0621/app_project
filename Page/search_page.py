# Page search_page.py 文件
from Base.base import Base
from Page.pageElements import PageElements

# 搜索页面操作的业务方法类
class SearchPage(Base):  # 继承父类Base类

    # 初始化方法
    def __init__(self):
        # 继承父类初始化方法
        super().__init__()

    # 输入搜索文本内容方法 直接使用父类的输入文本方法
    def input_search_text(self,text):
        """
        输入搜索文本内容
        :param text: 输入的文本内容
        :return:
        """
        self.input_ele(PageElements.search_input_id,text)

    # 获取搜索结果方法 直接使用父类定位一组元素方法
    def get_search_result(self):
        """ 获取搜索结果内容方法 """
        # 定位搜索结果
        results = self.search_eles(PageElements.search_result_ids)
        # 返回搜索结果文本信息
        return [i.text for i in results]
