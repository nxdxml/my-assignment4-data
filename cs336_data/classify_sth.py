from typing import Any
import fasttext


def classify_nsfw(text: str) -> tuple[Any, float]:
    model_path = "/home/dl/projects/my-assignment4-data/data/jigsaw_fasttext_bigrams_nsfw_final.bin" 
    model = fasttext.load_model(model_path)
    prediction = model.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)

def classify_toxic_speech(text: str) -> tuple[Any, float]:
    model_path = "/home/dl/projects/my-assignment4-data/data/jigsaw_fasttext_bigrams_hatespeech_final.bin" 
    model = fasttext.load_model(model_path)
    prediction = model.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)


def classify_quality(text: str) -> tuple[Any, float]:
    raise NotImplementedError
