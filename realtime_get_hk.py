import os
from datetime import date

import pandas as pd
import pymysql
import requests

cookies = {
    'xq_a_token': '6125633fe86dec75d9edcd37ac089d8aed148b9e',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}

#
# proxys = {
#     "http": "socks5://127.0.0.1:1080",
#     "https": "socks5://127.0.0.1:1080",
# }


today = date.today().strftime('%Y%m%d')
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "xueqiu", "hk", today)
if not os.path.exists(base_path):
    os.mkdir(base_path)

mysql_cn = pymysql.connect(host='localhost', port=3306, user='quant', passwd='123456', db='quant', charset='utf8')
sql = "select id, biz_date, code, name from stock_hk where biz_date = '2017-09-29' order by code"
df = pd.read_sql(sql, mysql_cn, index_col="id")
code_list = list(df['code'])

# 2018-01-12
code_list += ['06885.HK', '01707.HK', '08437.HK', '08480.HK', '08275.HK', '02337.HK', '08392.HK', '08065.HK']
code_list += ['02225.HK', '06080.HK', '08470.HK', '08436.HK', '02232.HK', '00772.HK', '01720.HK', '08426.HK', '02122.HK']
code_list += ['01337.HK', '08375.HK', '01706.HK', '08400.HK', '08376.HK', '02858.HK', '03358.HK', '01975.HK']
code_list += ['08118.HK', '08373.HK', '08402.HK', '01710.HK', '01997.HK', '08495.HK', '08406.HK', '08429.HK']
code_list += ['01697.HK', '02227.HK', '01475.HK', '01417.HK', '06090.HK', '08385.HK', '00839.HK', '01722.HK']
code_list += ['02022.HK', '08377.HK', '01727.HK', '01789.HK', '08419.HK', '03878.HK', '02708.HK', '08422.HK']
code_list += ['00784.HK', '08485.HK', '01730.HK', '08506.HK', '08501.HK', '03738.HK', '02025.HK', '08350.HK']
code_list += ['08509.HK']
# 2018-01-15
code_list += ['03309.HK']
# 2018-01-16
code_list += ['06158.HK', '08487.HK', '03699.HK', '08285.HK', '02292.HK', '02448.HK', '08493.HK', '08313.HK']
# 2018-01-17
code_list += ['08479.HK', '06182.HK', '08371.HK']
# 2018-01-18
code_list += ['08287.HK', '02139.HK']
# 2018-01-19
code_list += ['01665.HK', '08513.HK', '08043.HK']
# 2018-01-22
code_list += ['02683.HK']
# 2018-01-25
code_list += ['08136.HK', '08395.HK']
# 2018-01-26
code_list += ['08456.HK']
# 2018-01-29
code_list += ['01711.HK']
# 2018-02-02
code_list += ['08450.HK']
# 2018-02-08
code_list += ['06829.HK', '08519.HK']
# 2018-02-09
code_list += ['03319.HK']
# 2018-02-12
code_list += ['08523.HK', '08535.HK', '08473.HK']
# 2018-02-13
code_list += ['08510.HK', '08522.HK', '01729.HK', '01183.HK']
# 2018-02-14
code_list += ['08040.HK', '08379.HK']
# 2018-02-23
code_list += ['08532.HK']
# 2018-02-26
code_list += ['08367.HK']
# 2018-02-27
code_list += ['08526.HK']
# 2018-02-28
code_list += ['08483.HK']
# 2018-03-02
code_list += ['01933.HK']
# 2018-03-05
code_list += ['01621.HK']
# 2018-03-08
code_list += ['02182.HK']
# 2018-03-13
code_list += ['01815.HK']
# 2018-03-14
code_list += ['01737.HK', '01705.HK']
# 2018-03-16
code_list += ['06036.HK', '02377.HK', '02363.HK']
# 2018-03-22
code_list += ['08168.HK']
# 2018-03-23
code_list += ['00807.HK']
# 2018-03-26
code_list += ['02779.HK']
# 2018-03-28
code_list += ['02116.HK', '08401.HK', '01716.HK', '08448.HK']
# 2018-03-29
code_list += ['01735.HK', '08372.HK']
# 2018-04-16
code_list += ['08447.HK', '08451.HK', '08241.HK', '08507.HK']
# 2018-04-18
code_list += ['01726.HK']
# 2018-04-20
code_list += ['08511.HK']
# 2018-04-23
code_list += ['08151.HK']
# 2018-04-27
code_list += ['01671.HK']
# 2018-05-04
code_list += ['08107.HK', '01833.HK']
# 2018-05-09
code_list += ['08527.HK']
# 2018-05-11
code_list += ['01752.HK', '02119.HK', '01750.HK', '01742.HK', '08391.HK']
# 2018-05-16
code_list += ['08521.HK', '08105.HK']
# 2018-05-18
code_list += ['08536.HK']
# 2018-05-29
code_list += ['01598.HK']
# 2018-05-30
code_list += ['08490.HK', '01978.HK']
# 2018-05-31
code_list += ['08545.HK']
# 2018-06-01
code_list += ['01451.HK', '06119.HK']
# 2018-06-07
code_list += ['01757.HK']
# 2018-06-12
code_list += ['08403.HK']
# 2018-06-15
code_list += ['01806.HK', '08357.HK']
# 2018-06-19
code_list += ['06098.HK']
# 2018-06-21
code_list += ['02003.HK']
# 2018-06-26
code_list += ['01916.Hk']
# 2018-06-27
code_list += ['01587.HK', '08146.HK', '01749.HK']
# 2018-06-28
code_list += ['01620.HK']
# 2018-06-29
code_list += ['06100.HK']
# 2018-07-04
code_list += ['01592.HK', '08305.HK']
# 2018-07-05
code_list += ['02262.HK']
# 2018-07-06
code_list += ['01763.HK']
# 2018-07-09
code_list += ['01810.HK', '08223.HK']
# 2018-07-10
code_list += ['08502.HK', '06190.HK']
# 2018-07-11
code_list += ['01746.HK', '01652.HK']
# 2018-07-12
code_list += ['01739.HK', '01996.HK', '06860.HK', '03700.HK', '01760.HK', '01773.HK', '08219.HK', '08140.HK']
# 2018-07-13
code_list += ['01731.HK', '02051.HK', '01775.HK']
# 2018-07-16
code_list += ['01721.HK', '01715.HK', '08540.HK', '08606.HK', '01968.HK']
# 2018-07-18
code_list += ['03302.HK', '08547.HK', '08525.HK', '00797.HK']
# 2018-07-19
code_list += ['08512.HK', '01576.HK']
# 2018-07-20
code_list += ['02048.HK']
# 2018-07-31
code_list += ['01758.HK']
# 2018-08-01
code_list += ['01672.HK']
# 2018-08-03
code_list += ['01765.HK']
# 2018-08-08
code_list += ['06160.HK', '00788.HK']
# 2018-08-13
code_list += ['08475.HK']
# 2018-08-16
code_list += ['01725.HK']
# 2018-08-22
code_list += ['01783.HK']
# 2018-08-27
code_list += ['08210.HK']
# 2018-09-05
code_list += ['08482.HK']
# 2018-09-07
code_list += ['08609.HK']
# 2018-09-10
code_list += ['01615.HK']
# 2018-09-13
code_list += ['08601.HK', '01969.HK']
# 2018-09-14
code_list += ['02552.HK', '02680.HK']
# 2018-09-17
code_list += ['08619.HK']
# 2018-09-20
code_list += ['03690.HK']
# 2018-09-26
code_list += ['06862.HK', '01748.HK']
# 2018-09-27
code_list += ['01911.HK', '01723.HK']
# 2018-09-28
code_list += ['08017.HK', '01787.HK']
# 2018-10-04
code_list += ['01781.HK']
# 2018-10-08
code_list += ['01540.HK']
# 2018-10-09
code_list += ['01809.HK']
# 2018-10-11
code_list += ['01939.HK', '03990.HK', '06111.HK', '01772.HK']
# 2018-10-12
code_list += ['01894.HK', '08042.HK']
# 2018-10-15
code_list += ['08603.HK', '08516.HK']
# 2018-10-16
code_list += ['01741.HK', '08613.HK']
# 2018-10-19
code_list += ['01653.HK', '01825.HK']
# 2018-10-22
code_list += ['08611.HK']
# 2018-10-30
code_list += ['01034.HK']
# 2018-10-31
code_list += ['01801.HK']
# 2018-11-05
code_list += ['01712.HK']
# 2018-11-06
code_list += ['01755.HK']
# 2018-11-07
code_list += ['08259.HK']
# 2018-11-12
code_list += ['03616.HK']
# 2018-11-13
code_list += ['01835.HK']
# 2018-11-19
code_list += ['06890.HK', '02258.HK']
# 2018-11-26
code_list += ['00780.HK']
# 2018-11-27
code_list += ['01761.HK']
# 2018-11-29
code_list += ['01790.HK']



print(code_list)
print(len(code_list))


def get_data(param_str, index):
    result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers)
    # result = requests.get("https://xueqiu.com/v4/stock/quote.json?code=" + param_str, cookies=cookies, headers=headers, proxies=proxys)
    content = result.content.decode(encoding="UTF-8")
    print(content)
    with open(os.path.join(base_path, index + '.json'), 'wb') as f:
        f.write(content.encode('utf-8'))


j = 0
count = 0
param = []
for code in code_list:
    count += 1
    param.append(code[:-3])
    # param.append(code)
    if count == 50:
        j += 1
        get_data(','.join(param), str(j))
        param = []
        count = 0

j += 1
get_data(','.join(param), str(j))

import import_xueqiu_hk
import_xueqiu_hk.import_db()
