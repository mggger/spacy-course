import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# 处理文本
doc = ____

# 对识别出的实体进行遍历
for ent in ____.____:
    # 打印实体文本及标注
    print(ent.____, ____.____)
