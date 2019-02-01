# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:01:11 2018

@author: Administrator
"""

import PSSMmaker

#PSSMMaker.command_pssm('E:\Blast\db\Cytoplasm_test.fasta','try_once.txt','pssm1.pssm')
proseq=r'D:\xw\0709\pssmprocess\data_raw\data_test.txt'
outdir=r'D:\xw\0709\pssmprocess\data_pssm_test'
PSSMmaker.pssm(proseq,outdir)
