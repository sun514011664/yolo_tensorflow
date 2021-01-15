import os
import xml.etree.ElementTree as ET

#lableing标注完的数据集，原始图像和XML文件
data_path = 'C:\\Users\SWues\PycharmProjects\\tensorflow-yolov3-master\\tensorflow-yolov3-master\data\lableing_data_bilibili'
names_list =["words",]

#获取指定目录下的指定类型的文件名list
def getFileName(path,suffix):
    # 获取指定目录下的所有指定后缀的文件名
    input_template_All=[]
    f_list = os.listdir(path)#返回文件名
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] ==suffix:
            input_template_All.append(i)
    return input_template_All
# print(getFileName(data_path,".xml")) 函数调用示例

xml_list = getFileName(data_path,".xml")

for fp in xml_list:
    root = ET.parse(os.path.join(data_path,fp)).getroot()
