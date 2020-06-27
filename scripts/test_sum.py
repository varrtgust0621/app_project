import pytest
import os
import yaml
from Base.getData import GetData

# 定义读取yaml数据函数
def sum_data():
    # 空列表存储数据
    sum_list = []
    # 打开文件
    data = GetData.get_yaml_data("data_sum.yaml")
    print("data:",data)  # 字典格式
    # print("values:",data.values())  # 列表格式  存储所有的values
    for i in data.values():
        # print("tup:", (i.get("a"), i.get("b"), i.get("c")))
        # 添加元组数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list

class TestSum:

    # @pytest.mark.parametrize("a,b,c",[(1,2,3),(3,4,5),(4,5,9)])
    @pytest.mark.parametrize("a,b,c",sum_data())
    def test_sum(self,a,b,c):
        """ 判断两个数之和 等于 第三个数 """
        print("\n{}+{}={}".format(a,b,c))
        assert a + b == c