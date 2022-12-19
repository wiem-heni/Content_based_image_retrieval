import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from feature_extractor import FeatureExtractor
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
size = 1
fe = FeatureExtractor(size)
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".png"))
features = np.array(features)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        query = fe.extract(img)
        dists = np.linalg.norm(features-query, axis=1)
        ids = np.argsort(dists)[:10]
        scs = [(dists[id], img_paths[id]) for id in ids]
        return render_template('index.html', query_path=uploaded_img_path, scores=scs)
    elif request.method == 'GET':
        return render_template('index.html')




if __name__=="__main__":
    app.run("0.0.0.0")
