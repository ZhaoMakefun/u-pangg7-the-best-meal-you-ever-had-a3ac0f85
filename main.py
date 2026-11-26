#!/usr/bin/env python3
# The best meal ever had, told in a single sentence: tomato soup
# and grilled cheese at grandmother's table on a rainy October
# evening, windows steaming, her pretending not to watch.
# This script checks the sentence fits the rules and writes it out.

import os
from pathlib import Path

SENTENCE = "The best meal I ever had was my grandmother's tomato soup and grilled cheese on a rainy October evening, eaten at her kitchen table while the windows steamed and she pretended not to watch me finish."
CEILING = 200

sentence = SENTENCE.strip()
if not sentence:
    raise ValueError("sentence must not be empty")
if len(sentence) > CEILING:
    raise ValueError(f"sentence is {len(sentence)} characters; limit is {CEILING}")
# One sentence means one line: no carriage returns or newlines allowed.
if any(ch in sentence for ch in "\r\n"):
    raise ValueError("sentence must be a single line")
sentence.encode("utf-8")
target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
target_dir.mkdir(parents=True, exist_ok=True)
target_dir.joinpath("entry.txt").write_text(sentence, encoding="utf-8")
