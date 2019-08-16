from pyhanlp import *

file_path = "E:/content.txt"  # 需要分词的数据集

with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    seg_list = HanLP.segment(content)  # 分词，含词性标注、命名实体识别
    print(seg_list)  # 输出列表[吃/v, 葡萄/nf, 不/d, 吐/v, 葡萄皮/nz, ，/w, 不吃/v, 葡萄/nf,
    # 倒/vi, 吐/v, 葡萄皮/nz, 。/w, 上海/ns, 自来水/n, 来自/v, 海上/s, 。/w]

    CustomDictionary.add("上海自来水")  # 添加自定义词汇，但是该方法只针对该程序
    seg_list = HanLP.segment(content)
    print(seg_list)  # [吃/v, 葡萄/nf, 不/d, 吐/v, 葡萄皮/nz, ，/w, 不吃/v, 葡萄/nf, 倒/vi,
    # 吐/v, 葡萄皮/nz, 。/w, 上海自来水/nz, 来自/v, 海上/s, 。/w]

    """
    还有一个永久添加用户自定义词典的方法：
    在字典路径下添加自定义的词典，CustomDictionary主词典文本路径是
    Anaconcda3/Lib/site-pakages/pyhanlp/static/data/dictionary/cus
    tom/CustomDictionary.txt，用户可以在此增加自己的词语（不推荐）；
    也可以单独新建一个文本文件，通过配置文件CustomDictionaryPath=da
    ta/dictionary/custom/CustomDictionary.txt; 我的词典.txt;来追加词
    典（推荐），配置文件为E:/Anaconda3/Lib/site-packages/pyhanlp/static/
    hanlp.properties。
    
    具体配置文件的路径可以通过命令 hanlp --version 查看
    """
    
    parse_list = HanLP.parseDependency(content)  # 语法分析
    print(parse_list)


