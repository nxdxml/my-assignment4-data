from typing import Any
import fasttext
import gzip
from fastwarc.warc import ArchiveIterator, WarcRecordType
from cs336_data.extract_text import extract_text_from_html_bytes
from cs336_data.gopher_quality_filters import gopher_quality_filters
from cs336_data.mask_pii import mask_emails, mask_ips, mask_phone_numbers
import fasttext


nsfw_model_path = "/home/dl/projects/my-assignment4-data/data/jigsaw_fasttext_bigrams_nsfw_final.bin" 
nsfw_model = fasttext.load_model(nsfw_model_path)

def classify_nsfw(text: str) -> tuple[Any, float]:
    prediction = nsfw_model.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)

toxic_model_path = "/home/dl/projects/my-assignment4-data/data/jigsaw_fasttext_bigrams_hatespeech_final.bin" 
toxic_model = fasttext.load_model(toxic_model_path)
def classify_toxic_speech(text: str) -> tuple[Any, float]:
    prediction = toxic_model.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)


def classify_quality(text: str) -> tuple[Any, float]:
    model_path = "/home/dl/projects/my-assignment4-data/data/quality_model.bin" 
    model = fasttext.load_model(model_path)
    prediction = model.predict(text.replace("\n", " "), k=1) # 去掉空格，查看1个结果
    label, score = prediction[0][0], prediction[1][0]
    label = label.replace("__label__", "")
    return (label, score)


def main():
    positive_warc_path = "/home/dl/projects/my-assignment4-data/data/subsampled_positive_urls.warc.gz"
    negative_warc_path = "/home/dl/projects/my-assignment4-data/data/CC-MAIN-20250417135010-20250417165010-00065.warc.gz"
    data_size = 2000
    pos_example = 0
    nege_example = 0
    cnt = 0
    # 输出可视化
    # with gzip.open(warc_path, "rb") as f:
    #     for record in ArchiveIterator(f):
        
    #         # 获取网页正文（HTML 字节串）
    #         html_bytes = record.reader.read()
    #         text = extract_text_from_html_bytes(html_bytes)
    #         print(text)
    #         cnt += 1
    #         if cnt >= 30:
    #             break
    train_path = "/home/dl/projects/my-assignment4-data/data/train.txt"
    # positive_path = "/home/dl/projects/my-assignment4-data/data/positive.txt"
    # negative_path = "/home/dl/projects/my-assignment4-data/data/negative.txt"
    with open(train_path, "w") as f:
        for record in ArchiveIterator(gzip.open(positive_warc_path, "rb")):
            html = record.reader.read()
            text = extract_text_from_html_bytes(html)
            if not gopher_quality_filters(text):
                if text.strip():
                    f.write("__label__cc " + text.strip().replace("\n", " ") + "\n")
                    nege_example += 1
                continue
                
            if text.strip():
                f.write("__label__wiki " + text.strip().replace("\n", " ") + "\n")
                pos_example += 1

            cnt += 1
            if cnt >= data_size:
                break
            if pos_example >= 1000:
                break
        cnt = 0

        # 从原始网页中采集
        for record in ArchiveIterator(gzip.open(negative_warc_path, "rb")):
            html = record.reader.read()
            text = extract_text_from_html_bytes(html)
            if text.strip():
                f.write("__label__cc " + text.strip().replace("\n", " ") + "\n")

            cnt += 1
            if cnt >= data_size:
                break
    print(f"pos -> {pos_example} ; nega -> {nege_example}")
    print("开始训练")
    model = fasttext.train_supervised(
        input=train_path,
        epoch=5,
        lr=0.5,
        wordNgrams=2
    )
    model.save_model("/home/dl/projects/my-assignment4-data/data/quality_model.bin")

if __name__ == "__main__":
    main()

