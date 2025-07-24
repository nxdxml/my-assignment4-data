
from typing import Any
import fasttext
def identify_language(text: str) -> tuple[Any, float]:
    FASTTEXT_MODEL = fasttext.load_model("/home/dl/projects/my-assignment4-data/data/lid.176.bin")
    prediction = FASTTEXT_MODEL.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    # AssertionError: assert '__label__zh' == 'zh'
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)


    