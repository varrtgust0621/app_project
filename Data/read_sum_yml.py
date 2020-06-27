import yaml
import os

def sum_data():
    # 空列表存储数据
    sum_list = []
    # 打开文件
    with open("./data_sum.yaml","r") as f:
        # yaml读取文件
        data = yaml.safe_load(f)
        # print("data:",data)  # 字典格式
        print("values:",data.values())  # 列表格式  存储所有的values
        for i in data.values():
            print("tup:", (i.get("a"), i.get("b"), i.get("c")))
            # 添加元组数据到列表
            sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list

if __name__ == '__main__':
    sum_data()
