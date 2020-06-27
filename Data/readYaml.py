import yaml

with open("./data2.yml","r",encoding="utf-8") as f: # encoding="utf-8" 防止出现编码错误
    # 使用 yaml 加载数据
    data = yaml.safe_load(f)  # 返回字典
    print("返回字典数据:",data)
    print("返回数据类型:",type(data))
    # print("返回数据类型:",type(data.get("value1")))

