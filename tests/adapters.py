from __future__ import annotations

import os
from typing import Any

from cs336_data.extract_text import extract_text_from_html_bytes
from cs336_data.identify_language import identify_language
from cs336_data.mask_pii import mask_emails, mask_ips, mask_phone_numbers
from cs336_data.classify_sth import classify_nsfw, classify_quality, classify_toxic_speech
from cs336_data.gopher_quality_filters import gopher_quality_filters
from cs336_data.deduplication import exact_line_deduplication, minhash_deduplication

# done
def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    return extract_text_from_html_bytes(html_bytes=html_bytes)

# done
def run_identify_language(text: str) -> tuple[Any, float]:
    return identify_language(text)

# done
def run_mask_emails(text: str) -> tuple[str, int]:
    return mask_emails(text)

# done
def run_mask_phone_numbers(text: str) -> tuple[str, int]:
    return mask_phone_numbers(text)

# done
def run_mask_ips(text: str) -> tuple[str, int]:
    return mask_ips(text)

# done
def run_classify_nsfw(text: str) -> tuple[Any, float]:
    return classify_nsfw(text)

# done
def run_classify_toxic_speech(text: str) -> tuple[Any, float]:
    return classify_toxic_speech(text)

# done
def run_classify_quality(text: str) -> tuple[Any, float]:
    return classify_quality(text)

# done
def run_gopher_quality_filter(text: str) -> bool:
    return gopher_quality_filters(text)

# done
def run_exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    return exact_line_deduplication(input_files=input_files,output_directory=output_directory)


def run_minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    return minhash_deduplication(input_files=input_files,
                                 num_hashes=num_hashes,
                                 num_bands=num_bands,
                                 ngrams=ngrams,
                                 jaccard_threshold=jaccard_threshold,
                                 output_directory=output_directory)
