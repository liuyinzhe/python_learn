
# https://zhuanlan.zhihu.com/p/462806946
# https://www.jianshu.com/p/ec35a505ba90
# https://blog.csdn.net/Raider_zreo/article/details/101673853
# https://blog.csdn.net/Raider_zreo/article/details/101380293
import numpy as np
from scipy import stats


data1 = [1,2,3,4,5,6,7,8]
data2 = [3,4,5,6,7,8,9,10]

# 均值
mean = np.mean(data1,data2)

# 方差
variance =np.var(data1,data2)

# 标准差(Standard Deviation) ,与方差的关系：方差=标准差的平方
sd = np.std(data1,data2)

# 方差齐性检验
# levene检验p值大于0.05认为是满足方差齐性的，如果不满足则加一个参数equal_var=False
check_result = scipy.stats.levene(data1,data2)

# 返回值两个，第一个数值，第二个pvalue
print(check_result)
print(check_result.pvalue)

# 单样品T-test
t,p_towTail = stats.ttest_1samp(data1,pop_mean)
# data1是样本数据，pop_mean是总体均值(期望)


# 两独立样品T-test
scipy.stats.ttest_ind(data1,data2, equal_var=False)
# equal_var=False 表示方差非齐性

# 配对样本T-test
scipy.stats.ttest_rel(data1,data2)

# 两样品 秩和检验(Wilcoxon )
stats.wilcoxon(data1,data2) 
stats.mannwhitneyu(data1,data2) # 两样品数量不等


# 卡方检验是用于检验样本实际值与理论值之间是否存在显著差异，原假设是没有显著差异的
import scipy.stats as ss
obs=[107,198,192,125,132,248]
exp=[167]*6
#拒绝域 1%的显著水平,自由度5
#jjy=ss.chi2.isf(0.01,5)
#卡方
kf=ss.chisquare(obs,f_exp=exp).statistic




