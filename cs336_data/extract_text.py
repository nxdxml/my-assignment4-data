from resiliparse.parse.encoding import detect_encoding
from resiliparse.extract.html2text import extract_plain_text
from fastwarc.warc import ArchiveIterator, WarcRecordType
import gzip
def extract_text_from_html_bytes(html_bytes: bytes) -> str:
    """
    从 HTML 字节串中提取纯文本字符串。
    要求输入必须为 bytes 类型。
    """
    encoding = detect_encoding(html_bytes)
    html_str = html_bytes.decode(encoding, errors="replace")

    return extract_plain_text(html_str)


def main():
    warc_path = "/home/dl/projects/my-assignment4-data/data/CC-MAIN-20250417135010-20250417165010-00065.warc.gz"
    cnt = 0
    with gzip.open(warc_path, "rb") as f:
        for record in ArchiveIterator(f):
        
            # 获取网页正文（HTML 字节串）
            html_bytes = record.reader.read()
            text = extract_text_from_html_bytes(html_bytes)
            print(text)
            cnt += 1
            if cnt >= 5:
                break

if __name__ == "__main__":
    main()

