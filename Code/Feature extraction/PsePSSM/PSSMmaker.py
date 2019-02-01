# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:45:47 2017

@author: Patricia Lee
"""
import os
import re
#一个命令函数，根据pdb文件，使用blast生成pssm文件
def command_pssm(content, output_file,pssm_file):#输入File_in_name，Data_name，pssm_file_name
    #几经周折,使用system方法之后遇到的错误,首先第一个内容执行的可执行文件中不要有绝对路径,
    #所以先提前修改一下默认路径,切换到可执行文件所在目录  
    #-db后面的内容不要有路径,直接写文件名称即可
    #针对该出的语句,修改路径时定位到db文件夹还是bin文件夹都是可以执行的,都行的原因应该是在系统用户变量中我添加上了db的文件路径
    os.chdir(r'D:\blast2.2.27+\bin')
    os.system('psiblast \
              -in_msa %s \
              -db swissprot \
              -num_threads 10 \
              -num_iterations 3 \
              -evalue 0.001 \
              -out %s \
              -out_ascii_pssm %s '%(content,output_file,pssm_file))

#对每个序列进行PSSM打分
def pssm(proseq,outdir):
    inputfile = open(proseq,'r')
    content = ''
    input_file = '' 
    output_file = ''
    pssm_file = ''
    chain_name = []
    for eachline in inputfile:
        if '>' in eachline:
            if len(content):
                temp_file = open(outdir + '\\fasta\\' + chain_name,'w')
                temp_file.write(content)
                temp_file.close()
                input_file = outdir + '\\fasta\\' + chain_name
                output_file = outdir + '\\out\\' + chain_name + '.out'
                pssm_file = outdir + '\\pssm\\' + chain_name + '.pssm'                
                command_pssm(input_file, output_file,pssm_file)
            content = ''
            chain_name = eachline.strip()[1:]
        content +=  ''.join(eachline)
        #print content
        #print chain_name
    if len(content):
        temp_file = open(outdir + '\\fasta\\' + chain_name,'w')
        temp_file.write(content)
        temp_file.close()
        input_file = outdir + '\\fasta\\' + chain_name
        output_file = outdir + '\\out\\' + chain_name + '.out'
        pssm_file = outdir + '\\pssm\\' + chain_name + '.pssm'
        #执行shell命令时如果有要处理的文件,那么文件一定要先关系再去执行,否则shell命令不执行
        #该处的temp_file文件的关闭如果放在最后会导致下面的语句无法正确执行
        command_pssm(input_file, output_file,pssm_file)  
        
    inputfile.close()       
    
#格式化pssm每行数据
def formateachline(eachline):
    #下面一行代码是正则表达式的使用,\s表示匹配任意的空白字符,+又代表匹配1个或多个连续的空白字符
    #要处理的数据中每个数字之间的空白字符布置一个且不止一种,所以要使用下面的正则表达式
    col = re.split('\s+',eachline.strip())[:22]
    column = []
    for c in col:
        column.append(c)
    #返回一个列表,要写入文件时进行相应的处理即可
    return column

def simplifypssm(pssmdir,newdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        if os.path.isfile(pssmdir+'/'+eachfile)and eachfile.endswith('.pssm'):
            with open(pssmdir + '/' + eachfile,'r') as inputpssm:
                with open(newdir + '/' + eachfile,'w') as outfile:
                    count = 0
                    for eachline in inputpssm:
                        count +=1
                        if count <= 3:
                            continue
                        if not len(eachline.strip()):
                            break
                        oneline = formateachline(eachline)
                        for one in oneline[:-1]:
                            outfile.write(one+'\t')
                        outfile.write(oneline[-1]+'\n')
        elif os.path.isdir(pssmdir+'/'+eachfile):
            if not os.path.exists(newdir+'/'+eachfile):
                os.mkdir(newdir+'/'+eachfile)
            simplifypssm(pssmdir+'/'+eachfile,newdir+'/'+eachfile)
                    
#标准的pssm,直接根据标准的pssm滑动
def standardPSSM(window_size,pssmdir,outdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        outfile = open(outdir + '/' + eachfile, 'w') 
        with open(pssmdir + '/' + eachfile, 'r') as inputf:
            inputfile = inputf.readlines()
            for linenum in range(len(inputfile)):
                content = []
                first = [];second = [];third=[];last=[]
                if linenum < window_size/2:
                    for i in range((window_size/2 - linenum)*20):
                        second.append('\t0')
                if window_size/2 - linenum > 0:
                    countline = window_size - (window_size/2 - linenum)
                else:
                    countline = window_size  #get needed line count

                linetemp = 0
                for eachline in inputfile:
                    if linetemp < linenum-window_size/2:
                        linetemp += 1
                        continue
                    if linetemp == linenum:
                        thisline = eachline.split('\t')
                        for j in range(0,2):
                            if j>0:
                                first.append('\t')
                            first.append(thisline[j].strip())
                    if countline > 0:
                        oneline = eachline.split('\t')
                        for j in range(2,len(oneline)):
                            third.append('\t' + oneline[j].strip())
                        countline -=1
                    else:
                        break
                    linetemp += 1
                while countline:
                    for i in range(20):
                        last.append('\t0')
                    countline -=1
                content += first + second + third + last
                outfile.write(''.join(content) + '\n')
        outfile.close()
        
#根据窗口大小,计算出滑动后的20个氨基酸打分值
def computedPSSM(window_size,pssmdir,outdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        outfile = open(outdir + '/' + eachfile, 'w') 
        with open(pssmdir + '/' + eachfile, 'r') as inputf:
            inputfile = inputf.readlines()
            for linenum in range(len(inputfile)):
                content = []
                first = [];second = []
                if window_size/2 - linenum > 0:
                    countline = window_size - (window_size/2 - linenum)
                else:
                    countline = window_size  #get needed line count

                linetemp = 0
                for eachline in inputfile:
                    if linetemp < linenum-window_size/2:
                        linetemp += 1
                        continue
                    if linetemp == linenum:
                        thisline = eachline.split('\t')
                        for j in range(0,2):
                            if j>0:first.append('\t')
                            first.append(thisline[j].strip())
                    if countline > 0: 
                        oneline = eachline.split('\t')[2:len(eachline)]
                        tline = []
                        for i in range(len(oneline)):
                            tline.append(int(oneline[i]))
                        if len(second)==0:
                            second += tline
                        else:
                            second = list(map(lambda x: x[0]+x[1], zip(second, tline)))
                        countline -=1 
                    else:
                        break 
                    linetemp += 1 
                format_second = []
                for i in range(len(second)):
                    format_second.append('\t' + str(second[i]))
                content += first + format_second 
                outfile.write(''.join(content) + '\n')
        outfile.close()

def smoothedPSSM(window_size,pssmdir,outdir):
    standardPSSM(window_size,pssmdir, outdir)



































