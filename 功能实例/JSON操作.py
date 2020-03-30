import json

key = ['ORDER_SERVICE_REQ']
value_dict= {"RECORD_SEQUENCE_ID": "2019082610040507902","SOURCEDEVICE_ID": "51","SOURCEDEVICE_TYPE": "84","SOURCEDEVICE_NAME": "流量","ACCESS_TYPE": "1","TOKEN": "954cf7994b3eff143ff1ec9e5d1f0a4d","CONVEYSTRING": "","ORDER_ID": "6800019082600022","ORDER_METHOD": "1","SERVICE_TYPE": "21","MDN": "15600901197","SP_ID": "91639","SP_PRODUCT_ID": "2100079400","SUBSCRIPTION_TIME": "20190826083952","SERVICE_ID": "21000794","DEVELOPER_NAME": "联通在线信息科技有限公司","FEE": "20","EFFECTIVE_START_TYPE": "1","PARA": []}
value = [value_dict]
dict1 = dict(zip(key, value))
###print(dict1)

keys = ['UNI_BSS_HEAD','UNI_BSS_BODY','UNI_BSS_ATTACHED']
values_dict1 = {"APP_ID": "zGLt66zZYw","TIMESTAMP": "2019-08-21 11:30:06 100","TRANS_ID": "20190821113006100335423","TOKEN": "70f95a078b96e641d63dfb4073a06359"}
values_dict2 = {"MEDIA_INFO": ""}
values = [values_dict1,dict1,values_dict2]

dictionary = dict(zip(keys, values))
j = json.dumps(dictionary,ensure_ascii=False)  ###  防止中文乱码

###print(j)

request_str = json.loads(json.dumps(value_dict,ensure_ascii=False))
print(request_str['RECORD_SEQUENCE_ID'])


