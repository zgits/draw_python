from wordcloud import WordCloud
import matplotlib.pyplot as plt #绘制图像的模块
import jieba #jieba分词

path="斗破苍穹.txt"
f=open(path,"r",encoding="utf-8").read()
cut=" ".join(jieba.cut(f))
mywordCount=WordCloud(
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color="white",
    width=2000,
    height=1700).generate(cut)
plt.imshow(mywordCount)
plt.axis("off")
plt.show()