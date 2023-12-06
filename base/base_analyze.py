import os

import yaml


def analyze_data(file_name, key):
    """
    根据文件解析数据
    :param file_name: 数据文件名
    :param key: 数据的key
    :return:
    """

    with open(r".%sdata%s%s.yaml" % (os.sep, os.sep, file_name), "r",encoding="utf-8") as f:
        data_list = list()
        data_list.extend(yaml.safe_load(f)[key].values())
        return data_list

def settings_read_yaml(n,k):
    settings_yaml_path="./data/config.yaml"
    # 打开文件
    with open(settings_yaml_path,"r",encoding="utf-8") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        try:
            #判断传入的n是否在存在
            if n in data.keys():
                return data[n][k]
            else:
                print(f"n：{n}不存在")
        except Exception as e :
            print(f"key值{e}不存在")