import re
def gopher_quality_filters(text: str) -> bool:

    # 按行切
    lines = text.strip().splitlines()
    # \w+一个或者多个字符
    words = re.findall(r'\b\w+\b', text)

    # 1 <50 或者 >100'000
    num_words = len(words)
    if num_words < 50 or num_words > 100000:
        return False
    
    # 2 平均词数不在 [3,10]
    avg_len = sum(len(w) for w in words) / num_words
    if avg_len < 3 or avg_len > 10:
        return False

    # 3 >30% 行...结尾
    if lines:
        bad_cnt = sum(1 for l in lines if l.strip().endswith("..."))
        if bad_cnt / len(lines) > 0.3:
            return False

    # 4 >=80% 有字母
    valid_word = sum(
        bool(re.search(r'[a-zA-Z]', w)) for w in words
    )
    if valid_word / len(words) < 0.8:
        return False

    return True