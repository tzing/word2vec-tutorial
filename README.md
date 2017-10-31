# 使用 gensim 訓練中文詞向量

[教學文件](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)

## 套件需求

* jieba, 下方為特化供繁中使用之版本
* gensim

    ```bash
    pip install git+https://github.com/APCLab/jieba-tw.git
    pip install gensim
    ```

* [OpenCC](https://github.com/BYVoid/OpenCC) (可更換為任何繁簡轉換套件)

## 訓練流程

1. 取得[中文維基數據](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)

    ```bash
    wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
    ```

2. 將下載後的維基數據置於與專案同個目錄，再使用`wiki_to_txt.py`從 xml 中提取出維基文章

    ```bash
    python wiki_to_txt.py zhwiki-latest-pages-articles.xml.bz2
    ```

3. 使用 OpenCC 將維基文章統一轉換為繁體中文

    ```bash
    opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
    ```

4. 使用`jieba` 對文本斷詞，並去除停用詞

    ```bash
    python segment.py
    ```

5. 使用`gensim` 的 word2vec 模型進行訓練

    ```bash
    python train.py
    ```

6. 測試我們訓練出的模型

    ```bash
    python demo.py
    ```
