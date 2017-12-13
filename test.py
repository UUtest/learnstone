#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import json
import math

# 使用说明，生成insert语句的sql，alpha环境自己执行，alta环境没有权限提eden给DBA，附件上传sql
# 替换为自己有效的token
token = "HhvkOAlpmrLKzaq-j8YUw2qgTqFd5JQSMMeNljhqBjPmfV_1LAaYdpxbRiOdgGetiPmMltYxla3LRVehKqWFJa-jVsVHwGvzQmdNpBqEZWCBxeXzmLkv7Xy-HbGFJnEQ2dlqc9mY3OeuFXPGs38hhM4t7iufHnSMnxxc0vbKKIkJTU_7dPw9aEef-qYd7zvTsYcYHj_XfpOoRVUKEb8DlbtDz0c11OGzSMcNv-DeTr_npq6gohoGqJ1H-w_zqE9Up3KL4djuADZrzL-Qcn04PayS23GVNLpUrnYkktzYGTeWMF1WalCVttt01TIolXfjal6FNXHjjONsmHVUw3GUiAGBAEERyHrkynb63okyOZXNKlh4bC5eQjdipYqRJIijkX8u8p0zeVfnrENk-zpcWvOi6KpRtsfkF-LzVWGw2D2cvdXg2nq3aD65AVmpTeOUfS0rN1k291R8zvNR-slPKOdSiEma9wIlIOpgHDZE1ebPAUIyFGfTxFqew-Of3qXEBTqXJl3anD5fkwKXWBR_3IeMlM6fvyUmqrIy4sEF5bBQcemv2DUIYWwlfVXWC-nbalUCjxw72siKoWB_ByYVRR1pUSfmofe8w-AVbNsYnf9UCUNBDeMeMFgLYpwH78Y_J9fHhXJVt-Sag8RlyQjSnxRnGUvJ5zpZQevBjVUStdjK-9riJao4UXbzXfcdKx_mRTGkyV_JuujrRX6eDSqVKiey2YnisfxiOD3He-kdAQdbXKt9jTO1ZFgTuuwEssHQNQUzk1aq_5qh3WyKanw_LCSiarDTP2oE_ABZ89WqcsbejBer7nccvKJiegzauVvY91UVaC6A1kV7_W36FA6hFWi1eqY3HJCJE82OQo3afLr1A2nh6XvQ0NxzO4LnsL4Z_nf9__A1qVgfiOojAcNYiWPXCckrGa2-6ZfCufvgw5jNjVThWbv8Jel6baWCZtM9o3wBQtg77VVEmSqLa3ikbg"
command1 = '''curl 'https://console.cloud.elenet.me/role/sql/exec?' -H 'Pragma: no-cache' -H 'Origin: https://console.cloud.elenet.me' -H 'x-authorization-token: '''
command2 = '''' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36' -H 'content-type: application/json' -H 'accept: application/json' -H 'Cache-Control: no-cache' -H 'x-service: dbadmin' -H 'Connection: keep-alive' -H 'Referer: https://console.cloud.elenet.me/dbadmin/database/normal/Rmb_Push_Wg-xy_data' --data-binary '{"group":"normal","db":"Rmb_Push_Wg-xy_data","sql":"'''
command3 = ''';","type":"normal"}' --compressed'''
path = ""
file_str = ""


def executeCurl(sql):
    command = command1 + token + command2 + sql + command3
    r = subprocess.check_output(command, shell=True).decode('utf-8')
    rj = json.loads(r)
    # print(rj)

    return rj['resultPage']


def getCount(sql):
    sql = str(sql).replace("*", "count(*)")
    # sql = sql.replace(" ", "%20")
    print("sql:" + sql)

    result = executeCurl(sql)
    print("------------")
    print(result)
    return result['rows'][0]['count(*)']


def executeSingleSql(sql):
    # sql = sql.replace(" ","%20")
    result = executeCurl(sql)
    columns = result['head']
    rows = result['rows']
    table = result['tables'][0]
    insertLines = ""
    for row in rows:
        insColumn = "("
        insValue = "("
        for column in columns:
            insColumn = insColumn + column + ","
            if (column.__eq__("id")):
                insValue = insValue + "'0',"
            else:
                insValue = insValue + "'" + row[column].replace("'", "\\'") + "',"
        insColumn = insColumn[0: len(insColumn) - 1] + ')'
        insValue = insValue[0: len(insValue) - 1] + ')'
        insertLine = "insert into " + table + " " + insColumn + " values " + insValue
        insertLines = insertLines + insertLine + ";\n"
    return insertLines


def executeSql(sql):
    file_str = ""
    # 1. get table name
    table = executeCurl(sql)['tables'][0]

    # 可以替换为自己的路created_at < DATE_SUB(curdate(),INTERVAL 1 DAY);径指定路径，当然也可以加pwd语句自动生成路径
    path = "/Users/lizhengdao/Desktop/kettle/" + table + "_data.sql"
    # 2. get count
    total = int(getCount(sql))
    print(">>>>>>>>>>>>>>")
    print(total)
    for i in range(0, int(math.ceil(total / 1000))):
        sqlSingle = sql + " order by id asc limit 1000 " + "offset " + str(i * 1000)
        file_str = file_str + executeSingleSql(sqlSingle)
    file = open(path, "wb")
    file.write(bytes(file_str, encoding='utf-8'))
    file.close()


sql_unit_level = '''select * from unit_level where unit_id >0'''
sql_unit_analyzsis = '''select * from unit_analyzsis where unit_id in (2746,3473,4687,3169,4680,5730,3175,55137,54211,43276,38519,4015,4016,60390,60880,72861)'''
sql_shop_analyzsis = "select * from shop_analyzsis where battalion_id in (3473,4015)"
sql_dom_analysis = '''select * from dom_analysis where battalion_id in (3473,4015)'''
sql_visit_record = '''select * from visit_record_count where battalion_id = 4015'''
sql_visit_record_bloc_id = "select * from visit_record_count where bloc_id=4680 and regiment_id!=4016 and battalion_id!=4015 and data_dt > '2017-9-30'"
sql_visit_record_regiment_id = "select * from visit_record_count where regiment_id=4016 and battalion_id!=4015 and data_dt > '2017-9-30'"
sql_visit_record_battalion_id = "select * from visit_record_count where battalion_id=4015 and data_dt > '2017-9-30'"
sql_city_analyzsis = '''select * from unit_analyzsis where bloc_id=4680 and unit_type=%22BU_CITY%22 and shop_level=%22ALL%22 and unit_id > 4680'''
sql_exclusive_shop_analysis = '''select * from exclusive_shop_analysis where battalion_id in (3473,4015)'''
sql_exclusive_unit_analysis = '''select * from exclusive_unit_analysis where unit_id = 4680 or bloc_id = 4680'''
# executeSql(sql_unit_level)
# executeSql(sql_unit_analyzsis)
# executeSql(sql_anomalous_order)
# executeSql(sql_shop_analyzsis)
# executeSql(sql_unit_level)
# executeSql(sql_unit_analyzsis)
executeSql(sql_exclusive_unit_analysis)
executeSql(sql_exclusive_shop_analysis)
# executeSql(sql_dom_analysis)
# executeSql(sql_city_analyzsis)

















