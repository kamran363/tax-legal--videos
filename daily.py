"""Daily runner: pick topic -> build video -> upload to YouTube.

Usage:
    python -m agent.daily --auto --upload --privacy public
    python -m agent.daily --topic "1099"            # test build only
    python -m agent.daily --auto                     # build, no upload
"""
import argparse
import os
import re
import sys


def build_video(topic_data, cfg):
    from script_builder import build_package
    from voiceover import make_voiceovers
    from visuals import make_slides
    from assemble import assemble_video
    from thumbnail import make_thumbnail

    package = build_package(topic_data)
    slug = re.sub(r"[^a-z0-9]+", "-", topic_data["topic"].lower()).strip("-")[:40]
    workdir = os.path.join(cfg["out_dir"], slug)
    os.makedirs(workdir, exist_ok=True)

    print("[1/5] Script ready:", package["title"])
    print("[2/5] Voiceover ...")
    vo = make_voiceovers(cfg, package["sections"], os.path.join(workdir, "audio"))
    print("[3/5] Slides ...")
    slides = make_slides(package["sections"], os.path.join(workdir, "slides"))
    print("[4/5] Assembling video ...")
    video_path = os.path.join(workdir, "video.mp4")
    assemble_video(slides, vo, video_path)
    print("[5/5] Thumbnail ...")
    thumb_path = os.path.join(workdir, "thumbnail.png")
    make_thumbnail(package["title"], thumb_path)
    return package, video_path, thumb_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default="",
                    help="keyword to pick a topic (default: rotate by date)")
    ap.add_argument("--auto", action="store_true")
    ap.add_argument("--upload", action="store_true")
    ap.add_argument("--privacy", default="public",
                    choices=["public", "unlisted", "private"])
    args = ap.parse_args()

    from config import load_config
    from script_builder import pick_topic, find_topic

    cfg = load_config()
    topic_data = find_topic(args.topic) if args.topic else pick_topic()
    print("Topic:", topic_data["topic"])

    package, video_path, thumb_path = build_video(topic_data, cfg)
    print("\nDone! Files:", video_path, thumb_path)

    if args.upload:
        from upload import upload_video
        url = upload_video(
            video_path, package["title"], package["description"],
            package["tags"], privacy=args.privacy, thumbnail_path=thumb_path,
        )
        print("\nUploaded:", url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
