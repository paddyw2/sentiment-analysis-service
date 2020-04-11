# Sentiment analysis service

### Restore model and word index

#### Model
Run `colab_model.py` and copy `my_model.h5` to `files/`, or copy into a new notebook on colab.research.google.com and download saved model from the file section.

#### Word index
Restore word index into `files/`: `wget https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json`

### Build image
`docker build -t predict_app_tf:latest .`

### Run service
`docker run --rm -p 8080:8080 predict_app_tf:latest`
