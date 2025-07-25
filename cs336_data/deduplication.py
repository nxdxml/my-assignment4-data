import os
import hashlib
from collections import defaultdict
from pathlib import Path

def exact_line_deduplication(input_files: list[os.PathLike], output_directory: os.PathLike):
    # 第一步：统计每一行的哈希出现频次
    line_hash_counts = defaultdict(int)

    for file_path in input_files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n") # 取出末尾换行符
                # hexdigest() 转成人类可读状态
                line_hash = hashlib.md5(line.encode("utf-8")).digest()
                line_hash_counts[line_hash] += 1

    # 第二步：对每个文件输出只包含唯一行的新版本
    os.makedirs(output_directory, exist_ok=True)    

    for file_path in input_files:
        file_name = Path(file_path).name
        output_path = Path(output_directory) / file_name

        with open(file_path, "r", encoding="utf-8") as in_f, \
             open(output_path, "w", encoding="utf-8") as out_f:
            for line in in_f:
                line = line.rstrip("\n")
                line_hash = hashlib.md5(line.encode("utf-8")).digest()
                if line_hash_counts[line_hash] == 1:
                    out_f.write(line + "\n")



def minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    raise NotImplementedError
