# -*- coding: utf-8 -*-
import scipy.io as sio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import roc_curve, auc
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.linear_model import OrthogonalMatchingPursuitCV
from sklearn.preprocessing import scale,StandardScaler
from sklearn.preprocessing import normalize,Normalizer
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso,LassoCV
from sklearn.linear_model import ElasticNet,ElasticNetCV
from sklearn.linear_model import LassoLarsCV,LassoLars
from sklearn.feature_selection import VarianceThreshold
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import LinearSVC,SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import utils.tools as utils
from sklearn.metrics import average_precision_score
from dimension_reduction_com1 import lassodimension,logistic_dimension,elasticNet

data_=pd.read_csv(r'label10_ALL_train_SMOTEdata.csv')

data1=np.array(data_)
data2=data1[:,2:]
label1=data1[:,1]	
shu=data2

data_2,mask=lassodimension(shu,label1,alpha=np.array([0.0005]))
train_data=data_2
trainlabel=label1

#data_1=pd.read_csv(r'label10_ALL_test.csv')
data_1=pd.read_csv(r'label10_ALL_test_SMOTEdata.csv')
data11=np.array(data_1)
data22=data11[:,2:]
label=data11[:,1]	
sh=data22
mask1=np.array(mask)

test_data=sh[:,mask1]
testlabel=label

cv_clf = GradientBoostingClassifier(n_estimators=2000,max_depth=6,learning_rate= 0.01,)
row=train_data.shape[0]  
index=[i for i in range(row)]
np.random.shuffle(index)
train_shu=train_data[index,:]
train_label=trainlabel[index]

sepscores=[]
hist=cv_clf.fit(train_shu, train_label)
y_score=cv_clf.predict_proba(test_data)
y_test=utils.to_categorical(testlabel)    
y_class= utils.categorical_probas_to_classes(y_score)
y_test_tmp=testlabel
acc, precision,npv, sensitivity, specificity, mcc,f1 = utils.calculate_performace(len(y_class), y_class, y_test_tmp)

row=y_score.shape[0]
y_score=y_score[np.array(range(1,row)),:]
yscore_sum = pd.DataFrame(data=y_score)
yscore_sum.to_csv('yscore_sum_test.csv')
y_test=y_test[np.array(range(1,row)),:]
ytest_sum = pd.DataFrame(data=y_test)
ytest_sum.to_csv('ytest_sum_test.csv')
ytest_sum=np.array(ytest_sum)
yscore_sum=np.array(yscore_sum)
fpr, tpr, _ = roc_curve(ytest_sum[:,0], yscore_sum[:,0])
roc_auc=auc(fpr, tpr)
lw=2
plt.plot(fpr, tpr, color='darkorange',lw=lw, label='GBDT ROC (area =roc_auc)')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.05])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

aupr=average_precision_score(ytest_sum[:,0], yscore_sum[:,0])
sepscores.append([acc, precision,npv, sensitivity, specificity, mcc,f1,roc_auc,aupr])


result=sepscores
data_csv = pd.DataFrame(data=result)
data_csv.to_csv('Matine_test_result.csv')

colum = ['ACC', 'precision', 'npv', 'Sn', 'Sp','MCC','F1','AUC','aupr']
data_csv = pd.DataFrame(columns=colum, data=result)

data_csv.to_csv(r'test_lasso_0.0005_GBDT.csv')




