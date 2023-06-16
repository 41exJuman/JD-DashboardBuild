import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

'''
对京东电商运营数据集进行指标分析以了解用户购物行为特征,为运营决策提供支持建议。
'''

# 设置中文编码和负号显示正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_row', 200)
# 读取数据
user_action = pd.read_csv('./2019JDDATA/jdata_action.csv')
# 选取部分数据进行分析 datatime range(2018-03-30 ~ 2018-04-15)
user_data = user_action[(user_action['action_time'] > '2018-03-30') & (user_action['action_time'] < '2018-04-15')]
# 将筛选部分备份至本地
# user_data.to_csv('user_data.csv', sep = ',')
# 查看原始数据各字段类型
behavior = pd.read_csv('user_data.csv', index_col = 0)
# behavior[:10]
# behavior.info()

# 查看缺失值
behavior.isnull().sum()  # 返回None无缺失值


# 字段处理
# 原始数据中action_time,时间和日期是在一起的,不方便分析,对action_time列进行处理,拆分出日期和时间列,
# 并添加星期字段求出日期对应的星期,方便后续处理
behavior['date'] = pd.to_datetime(behavior['action_time']).dt.date  # 日期
behavior['hour'] = pd.to_datetime(behavior['action_time']).dt.hour  # 时间
behavior['weekday'] = pd.to_datetime(behavior['action_time']).dt.day_name()  # 周
# 去除与分析无关的列
behavior = behavior.drop('module_id', axis = 1)
# 将用户行为标签由数据类型改为用字符表示
behavior_type = {1:'pv', 2:'pay', 3:'fav', 4:'comm', 5:'cart'}
behavior['type'] = behavior['type'].apply(lambda x: behavior_type[x])
behavior.reset_index(drop=True, inplace = True)
behavior.to_csv("new_behavior.csv", sep = ',')
# 查看处理好的数据
# behavior[:10]


