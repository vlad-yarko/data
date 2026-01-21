from __future__ import annotations
import re
from typing import List, Iterable

_WORD = re.compile(r"[A-Za-z0-9_]+")

def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())

def words(text: str) -> List[str]:
    return _WORD.findall(normalize(text))


