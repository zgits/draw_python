#coding utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open("test.txt",encoding="utf-8").read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)

wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
