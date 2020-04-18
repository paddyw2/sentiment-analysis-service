# Sentiment analysis service

### Create virtual environment

`virtualenv venv -p python3 && source venv/bin/activate`

Then restore packages:

`pip install -r requirements.txt`

### Restore model and word index

#### Model
Run `python colab_model.py` and copy `my_model.h5` to `files/`, or copy into a new notebook on [colab.research.google.com](https://colab.research.google.com/) and download saved model from the file section.

#### Word index
Restore word index into `files/`:

 `wget https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json`

### Build image
`docker build -t predict_app_tf:latest .`

### Run service
`docker run --rm -p 8080:8080 predict_app_tf:latest`

### Make API call

POST the following to `localhost:8080/predict`:

```
{
    "text": "[your review text]"
}
```
