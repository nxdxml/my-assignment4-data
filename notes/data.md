

## 观察数据
可以看出数据质量非常的差，充满了无意义的内容，格式分隔符，黄色广告。
``` sh
# 
zcat CC-MAIN-20250417135010-20250417165010-00065.warc.gz | less

# 
zcat CC-MAIN-20250417135010-20250417165010-00065.warc.wet.gz | less
```

尝试从warc文件将其中的html_bytes转为字符串，得到的结果相比.wet多了些空格啥的。

语言识别，使用fastText进行高效的文本分类。

mask掉身份敏感信息。

弄掉色情和有害内容。

根据一些规则提升数据质量。

训练一个质量分类器判断好坏文章
``` sh
# 好数据的来源，从wiki中去10000条外链
zcat enwiki-20240420-extracted_urls.txt.gz | shuf -n 10000 > subsampled_positive_urls.txt

# 抓网页内容并保存为 WARC：
wget --timeout=5 \
  -i subsampled_positive_urls.txt \
  --warc-file=subsampled_positive_urls \
  -O /dev/null

# 太慢了试试并行

cat subsampled_positive_urls.txt | xargs -I{} -P 20 wget \
  --timeout=5 \
  --tries=2 \
  --waitretry=0 \
  -e use_proxy=yes \
  -e http_proxy=http://127.0.0.1:11080 \
  -e https_proxy=http://127.0.0.1:11080 \
  --warc-file=warc_outputs/$(echo {} | md5sum | cut -d' ' -f1) \
  "{}" -O /dev/null
```