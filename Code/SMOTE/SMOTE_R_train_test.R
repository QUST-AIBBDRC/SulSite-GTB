library(DMwR)
require(xgboost)
require(methods)

#setwd("D:/xw/20180927/融合特征/csv_smote1")
setwd("D:/xw/3_特征提取/AAC/3_SMOTE")
data_train = read.csv("train_AAC_data1.csv",header = F)
data_train$V1=factor(data_train$V1)
train_data_SMOTEdata <- SMOTE(V1~.,data_train,perc.over =678.67,perc.under=114.73)
jishu<-table(train_data_SMOTEdata$V1)


write.csv(train_data_SMOTEdata,file='train_AAC_data1_SMOTEdata.csv')


data_test<- read.csv("test_data.csv",header = F)
data_test$V1=factor(data_test$V1)
test_SMOTEdata <- SMOTE(V1~.,data_test,perc.over =549.54,perc.under=118.2)
test_jishu<-table(test_SMOTEdata$V1)
write.csv(test_SMOTEdata,file='test_SMOTEdata.csv')