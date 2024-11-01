from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 准备词汇和词频数据
words = [
    #此处填充需要制作的词语(词语需要英文双引号&&一定要用英文逗号隔开!!!)
]
frequencies = {word: 100 - i for i, word in enumerate(words)}  # 模拟词频递减

# 确认图像的掩码(需要提供无背景的图形照片)
mask = np.array(Image.open(""))  # 图片绝对路径

# 创建词云
wordcloud = WordCloud(
    font_path="", # 字体绝对路径
    background_color="white",
    mask=mask,
    width=800, height=800
).generate_from_frequencies(frequencies)

# 显示词云
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
