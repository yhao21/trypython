import pandas as pd
import numpy as np
import statsmodels.api as sm


df = pd.read_csv('dataset_ps_4.csv')
print(df)

target_base = np.array(df.iloc[:,1].values).reshape(10000,1)
data_base = np.array(df.iloc[:,2:9].values)
data_base = np.delete(data_base,3,axis = 1)
data_base = np.delete(data_base,-1,axis = 1)
data_base = np.delete(data_base,0,axis = 1)
region = df.iloc[:,5].values
exp = np.array(df.iloc[:,-1].values).reshape(10000,1)
region_dummy = sm.categorical(region,drop = True)
data_base = np.hstack((data_base,region_dummy,exp))
data_base = np.delete(data_base,-2,axis=1)
data_base_df = pd.DataFrame(data_base)
data_base_df.columns = ['ability','age','female','edu','reg1','reg2','reg3','exp']
# print(data_base_df)



"""(a)"""
sum_data = df.iloc[:,1:].values
#mean
sum_data_mean = [np.mean(sum_data[:,i]) for i in range(sum_data.shape[1])]
sum_data_std = [np.std(sum_data[:,i]) for i in range(sum_data.shape[1])]
sum_data_min = [np.min(sum_data[:,i]) for i in range(sum_data.shape[1])]
sum_data_max = [np.max(sum_data[:,i]) for i in range(sum_data.shape[1])]
items = np.array(['Mean','Std','Min','Max']).reshape((4,1))
stat_sum = pd.DataFrame(np.hstack((items,np.vstack((sum_data_mean,sum_data_std,sum_data_min,sum_data_max)))))
stat_order = ['metrics','earnings','occ','ability','age','region','female','edu','exp']
stat_sum.columns = stat_order
# stat_sum.to_csv('summary.csv')
# print(stat_sum)





"""(b)"""
exp_2 = np.array(data_base_df.iloc[:,-1].values ** 2).reshape((10000,1))
data_b = np.hstack((data_base,exp_2))
data_b_df = pd.DataFrame(data_b)
data_b_df.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2']
# data_b_reg = sm.add_constant(data_b_df)
# machine_b = sm.OLS(target_base,data_b_reg)
# machine_b = machine_b.fit()
# OLS_b = machine_b.summary()
# print(OLS_b)

"""
  x1      x2    x3      x4          x5       x6      x7       x8      x9   x10
ability, age, female, education, region1, region2, region3, region4, exp, exp_2
"""

"""(c)"""
data_c = pd.DataFrame(np.delete(data_b.copy(),0,axis = 1))
data_c.columns = ['age','female','education','region1','region2','region3','exp','exp_2']
data_c_reg = sm.add_constant(data_c)
# machine_c = sm.OLS(target_base,data_c_reg)
# machine_c = machine_c.fit()
# OLS_c = machine_c.summary()
# print(OLS_c)
"""
  x1    x2       x3        x4        x5       x6      x7      x8   x9   
 age, female, education, region1, region2, region3, region4, exp, exp_2
"""


"""(d)"""
occ_dummy = sm.categorical(df.iloc[:,2].values,drop = True)
occ_dummy = np.delete(occ_dummy,-1,axis = 1)
occ_index = ['occ'+str(i) for i in range(52)]
data_d = pd.DataFrame(np.hstack((data_b, occ_dummy)))
data_d.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2']+occ_index
data_d_reg = sm.add_constant(data_d)
# machine_d = sm.OLS(target_base,data_d_reg).fit()
# OLS_d = machine_d.summary()
# print(OLS_d)



"""(e)"""
data_e = pd.DataFrame(np.delete(data_b.copy(),-1,axis = 1))
data_e.columns = ['ability','age','female','education','region1','region2','region3','exp']
data_e_reg = sm.add_constant(data_e)
# machine = sm.OLS(target_base,data_e_reg).fit()
# OLS_e = machine.summary()
# print(OLS_e)



"""(f)"""
exp_3 = exp ** 3
exp_4 = exp ** 4
data_f = pd.DataFrame(np.hstack((data_b,exp_3,exp_4)))
data_f.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2','exp_3','exp_4']
data_f_reg = sm.add_constant(data_f)
# machine_f = sm.OLS(target_base,data_f_reg).fit()
# OLS_f = machine_f.summary()
# print(OLS_f)




"""(g)"""
edu_2 = np.array(df.iloc[:,-2].values ** 2).reshape((10000,1))
data_g = pd.DataFrame(np.hstack((data_b,edu_2)))
data_g.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2','education_2']
data_g = data_g[['ability','age','female','education','education_2','region1','region2','region3','exp','exp_2']]
# data_g_reg = sm.add_constant(data_g)
# machine_g = sm.OLS(target_base,data_g_reg).fit()
# OLS_g = machine_g.summary()
# print(OLS_g)



"""(h)"""
random_index = np.random.randint(0,10000,2000)
data_h = pd.DataFrame(data_b[random_index,:])
data_h.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2']
data_h_reg = sm.add_constant(data_h)
# machine_h = sm.OLS(target_base[random_index,:],data_h_reg).fit()
# OLS_h = machine_h.summary()
# print(OLS_h)



"""(i)"""
# data_i = pd.DataFrame(data_b)
# print(data_i)





"""(j)region 1"""
region_1_index = []
for i in range(10000):
    if region[i] == 1:
        region_1_index.append(i)
data_j_region1 = data_b[region_1_index]
data_j_region1 = np.delete(data_j_region1,5,axis = 1)
data_j_region1 = np.delete(data_j_region1,5,axis = 1)
data_j_region1 = np.delete(data_j_region1,4,axis = 1)
data_j_region1 = pd.DataFrame(data_j_region1)
data_j_region1.columns = ['ability','age','female','education','exp','exp_2']
# data_j_region1_reg = sm.add_constant(data_j_region1)
# machine_j_1 = sm.OLS(target_base[region_1_index],data_j_region1_reg).fit()
# OLS_j_1 = machine_j_1.summary()
# print(OLS_j_1)


"""(j)region2"""
region2_index = [i for i in range(10000) if region[i] == 2]
data_j_region2 = data_b[region2_index]
for x in [4,4,4]:
    data_j_region2 = np.delete(data_j_region2,x,axis = 1)
data_j_region2 = pd.DataFrame(data_j_region2)
data_j_region2.columns = ['ability','age','female','education','exp','exp_2']
data_j_region2_reg = sm.add_constant(data_j_region2)
# machine_j_2 = sm.OLS(target_base[region2_index],data_j_region2_reg).fit()
# OLS_j_2 = machine_j_2.summary()
# print(OLS_j_2)



"""(j)region3"""
region3_index = [i for i in range(10000) if region[i] == 3]
data_j_region3 = data_b[region3_index]
for x in [4,4,4]:
    data_j_region3 = np.delete(data_j_region3,x,axis = 1)
data_j_region3 = pd.DataFrame(data_j_region3)
data_j_region3.columns = ['ability','age','female','education','exp','exp_2']
data_j_region3_reg = sm.add_constant(data_j_region3)
# machine_j_3 = sm.OLS(target_base[region3_index],data_j_region3_reg).fit()
# OLS_j_3 = machine_j_3.summary()
# print(OLS_j_3)




"""(j)region4"""
region4_index = [i for i in range(10000) if region[i] == 4]
data_j_region4 = data_b[region4_index]
for x in [4,4,4]:
    data_j_region4 = np.delete(data_j_region4,x,axis = 1)
data_j_region4 = pd.DataFrame(data_j_region4)
data_j_region4.columns = ['ability','age','female','education','exp','exp_2']
data_j_region4_reg = sm.add_constant(data_j_region4)
machine_j_4 = sm.OLS(target_base[region4_index],data_j_region4_reg).fit()
OLS_j_4 = machine_j_4.summary()
print(OLS_j_4)




"""(k)male"""
gender = df.iloc[:,6].values
male_index = [i for i in range(10000) if gender[i] == 0]
data_k_male = data_b[male_index]
data_k_male_ = np.delete(data_k_male,2,axis = 1)
data_k_male = pd.DataFrame(data_k_male_)
data_k_male.columns = ['ability','age','education','region1','region2','region3','exp','exp_2']
data_k_male_reg = sm.add_constant(data_k_male)
# machine_k_male = sm.OLS(target_base[male_index],data_k_male_reg).fit()
# OLS_k_male = machine_k_male.summary()
# print(OLS_k_male)





"""(k)female"""
female_index = [i for i in range(10000) if gender[i] == 1]
data_k_female = data_b[female_index]
data_k_female_ = np.delete(data_k_female,2,axis=1)
data_k_female = pd.DataFrame(data_k_female_)
data_k_female.columns = ['ability','age','education','region1','region2','region3','exp','exp_2']
data_k_female_reg = sm.add_constant(data_k_female)
# machine_k_female = sm.OLS(target_base[female_index],data_k_female_reg).fit()
# OLS_k_female = machine_k_female.summary()
# print(OLS_k_female)


"""(l)"""
# print(data_b_df)
data_l = pd.DataFrame(np.vstack((data_b,data_b,data_b,data_b,data_b)))
data_l.columns = ['ability','age','female','education','region1','region2','region3','exp','exp_2']
target_l = np.vstack((target_base,target_base,target_base,target_base,target_base))
data_l_reg = sm.add_constant(data_l)
# machine_l = sm.OLS(target_l,data_l_reg).fit()
# OLS_l = machine_l.summary()
# print(OLS_l)
# print(data_l)


















