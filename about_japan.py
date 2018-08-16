# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import csv

def to_dict(keys, values):
    return dict(zip(keys, values))

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

@app.route('/')
def index():
    with open("infos.csv", "r", encoding="utf-8") as f:
        infos = [to_dict(["name", "data"], line) for line in csv.reader(f)]

    return render_template('index.html', infos=infos)

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に