#!/usr/bin/env python3
"""fb_text_poster.py — Posts the next toddler text post to the Facebook Page.

  1. Reads PAGE_ID and FB_PAGE_TOKEN from the environment.
  2. Picks the next template from text_posts.py (rotates via posted_text.json).
  3. Publishes via POST /{page_id}/feed with the message.
"""

import json
import os
import sys
from pathlib import Path

import requests

API_VERSION = "v26.0"

BASE_DIR = Path(__file__).resolve().parent
POSTED_FILE = BASE_DIR / "posted_text.json"


def log(msg: str) -> None:
    print(f"[fb_text_poster] {msg}", flush=True)


def load_posted() -> list:
    if POSTED_FILE.exists():
        try:
            return json.loads(POSTED_FILE.read_text())
        except Exception:
            log("WARNING: posted_text.json unreadable, starting fresh")
    return []


def save_posted(posted: list) -> None:
    POSTED_FILE.write_text(json.dumps(posted))


def post_text(page_id: str, token: str, message: str) -> str:
    url = f"https://graph.facebook.com/{API_VERSION}/{page_id}/feed"
    r = requests.post(url, data={"access_token": token, "message": message}, timeout=60)
    data = r.json()
    if r.status_code != 200 or "id" not in data:
        raise RuntimeError(f"text post failed: {r.status_code} {data}")
    log(f"Published! post_id={data['id']}")
    return str(data["id"])


def main() -> int:
    page_id = os.environ.get("PAGE_ID", "").strip()
    token = os.environ.get("FB_PAGE_TOKEN", "").strip()
    if not page_id or not token:
        log("ERROR: PAGE_ID and FB_PAGE_TOKEN env vars are required")
        return 2

    sys.path.insert(0, str(BASE_DIR))
    from text_posts import make_post, post_count

    posted = load_posted()
    idx = len(posted) % post_count()
    message = make_post(seed=len(posted))

    try:
        pid = post_text(page_id, token, message)
    except Exception as e:
        log(f"ERROR: {e}")
        return 1

    posted.append({"index": idx, "post_id": pid})
    save_posted(posted)
    log(f"Posted template #{idx} ({len(posted)} total).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
