#!/usr/bin/env python
#_*_coding:utf-8_*_

import re,os,sys,csv
from collections import Counter
pPath = re.sub(r'codes$', '', os.path.split(os.path.realpath(__file__))[0])
sys.path.append(pPath)
from codes import readFasta
import pandas as pd

def AAC(fastas, **kw):
	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	#AA = 'ARNDCQEGHILKMFPSTWYV'
	encodings = []
	header = ['#']
	for i in AA:
		header.append(i)
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		count = Counter(sequence)
		for key in count:
			count[key] = count[key]/len(sequence)
		code = [name]
		for aa in AA:
			code.append(count[aa])
		encodings.append(code)
	return encodings

fastas = readFasta.readFasta("data_test.txt")
#kw=  {'path': "E:\S-sulfenylation11\2018_11_21最新数据\3_特征提取\AAC\\codes",'train':"data_train.txt",'label':"label_train.txt",'order':'ACDEFGHIKLMNPQRSTVWY'}
#kw=  {'path': "D:\\xw\\特征提取\\AAC\\codes",'train':"E:\\S-sulfenylation11\\AAC\\codes\\data_train_p.txt",'label':"E:\\S-sulfenylation11\\AAC\\codes\\label_test.txt",'order':'ACDEFGHIKLMNPQRSTVWY'}
kw=  {'path': "E:\S-sulfenylation11\2018_11_21最新数据\3_特征提取\AAC\\codes",'train':"data_test.txt",'label':"label_train.txt",'order':'ACDEFGHIKLMNPQRSTVWY'}
data_AAC=AAC(fastas, **kw)
#AAC=data_AAC.to_list
AAC=pd.DataFrame(data=data_AAC)
AAC.to_csv('test_AAC_data.csv')

