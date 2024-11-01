from flask import Flask, request, send_file, render_template
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import io
import os
import tempfile

app = Flask(__name__)


# 主页面路由
@app.route('/')
def home():
    return render_template('index.html')


# 词云生成路由
@app.route('/generate-wordcloud', methods=['POST'])
def generate_wordcloud():
    words = request.form['words'].split(',')
    font_file = request.files['font']
    mask_file = request.files['mask']

    # 创建临时文件夹
    with tempfile.TemporaryDirectory() as tempdir:
        # 保存字体文件到临时路径
        font_path = os.path.join(tempdir, font_file.filename)
        font_file.save(font_path)

        # 加载并处理形状图片
        mask = Image.open(mask_file)

        # 创建词频数据
        frequencies = {word.strip(): 100 - i for i, word in enumerate(words)}

        # 使用词云生成器创建词云
        wordcloud = WordCloud(
            font_path=font_path,  # 使用临时字体路径
            background_color="white",
            mask=np.array(mask),
            width=800, height=800
        ).generate_from_frequencies(frequencies)

        # 将生成的词云图转换为 PNG 格式并返回
        img = io.BytesIO()
        wordcloud.to_image().save(img, format='PNG')
        img.seek(0)

    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
