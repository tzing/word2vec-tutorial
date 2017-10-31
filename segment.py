# -*- coding: utf-8 -*-

import jieba
import logging
import os

if os.name != 'nt':
    jieba.enable_parallel(8)

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # load stopwords set
    stopwordset = set()
    with open('dict/stopwords.txt','r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    texts_num = 0

    output = open('wiki_seg.txt','w')
    with open('wiki_zh_tw.txt','r') as content :
        for line in content:
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word +' ')

            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % texts_num)
    output.close()

if __name__ == '__main__':
    main()
