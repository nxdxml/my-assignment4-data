# Personally Identifiable Information 处理个人身份信息
import re


def mask_emails(text: str) -> tuple[str, int]:
    EMAIL_REGEX = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
    # (text, cnt) 新字符串和替换次数
    return EMAIL_REGEX.subn("|||EMAIL_ADDRESS|||", text)


def mask_phone_numbers(text: str) -> tuple[str, int]:
    PHONE_REGEX = re.compile(
        r"""
        (?<!\w)                         # 前面不能是字母或数字（防止误匹配）
        (                               # 捕获整个号码块
            (?:\+?1[\s\-\.]*)?          # 可选国家码 "+1", 允许空格/点/横杠
            (?:\(?\d{3}\)?[\s\-\.]*)    # 区号如 (283), 283, (283)- 等
            \d{3}[\s\-\.]*\d{4}         # 主体号码 182-3829 等
        )
        (?!\w)                          # 后面不能是字母或数字
        """,
        re.VERBOSE
    )
    return PHONE_REGEX.subn("|||PHONE_NUMBER|||", text)


def mask_ips(text: str) -> tuple[str, int]:
    IP_REGEX = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    return IP_REGEX.subn("|||IP_ADDRESS|||", text)