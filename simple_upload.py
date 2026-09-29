#!/usr/bin/env python3
""" Simple YouTube uploader for HealthHub v16.4 Uploads the built video WITHOUT the 0-8h sleep that was killing GitHub runners. Uses YouTube's scheduled publishing (publishAt) for natural timing. """
import os
import sys
import json
import random
from datetime import datetime, timedelta, timezone

def get_authenticated_service():
    """Authenticate with YouTube using OAuth refresh token."""
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    
    client_id = os.environ['YT_CLIENT_ID']
    client_secret = os.environ['YT_CLIENT_SECRET']
    refresh_token = os.environ['YT_REFRESH_TOKEN']
    
    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=client_id,
        client_secret=client_secret,
    )
    # Refresh to get access token
    from google.auth.transport.requests import Request
    creds.refresh(Request())
    
    return build('youtube', 'v3', credentials=creds)

def upload_video(video_path, title, description, tags, privacy='public', schedule_hours=None):
    """Upload video to YouTube with optional scheduled publishing."""
    from googleapiclient.http import MediaFileUpload
    
    youtube = get_authenticated_service()
    
    # Read package info for title/description if not provided
    if not title:
        with open('work/package.json') as f:
            pkg = json.load(f)
            title = pkg.get('title', 'Health Video')
            description = pkg.get('description', '')
            tags = pkg.get('tags', [])
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '27',  # Education
        },
        'status': {
            'privacyStatus': 'private' if schedule_hours else privacy,
        }
    }
    
    # Schedule publishing 0-8h in future (replaces the old sleep)
    if schedule_hours is not None:
        publish_at = datetime.now(timezone.utc) + timedelta(hours=schedule_hours)
        # YouTube requires RFC3339 format
        body['status']['publishAt'] = publish_at.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        print(f"[schedule] Video will publish at {publish_at} (in {schedule_hours:.1f}h)")
    
    # Get thumbnail if exists
    thumb_path = 'work/thumbnail.png'
    
    media = MediaFileUpload(video_path, mimetype='video/mp4', resumable=True)
    
    print(f"[upload] Uploading: {title[:50]}...")
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )
    
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"[upload] {int(status.progress() * 100)}%")
    
    video_id = response['id']
    video_url = f"https://youtu.be/{video_id}"
    print(f"[upload] Done! {video_url}")
    
    # Upload thumbnail
    if os.path.exists(thumb_path):
        print("[upload] Setting thumbnail...")
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumb_path, mimetype='image/png')
        ).execute()
        print("[upload] Thumbnail set!")
    
    return video_url

def main():
    workdir = 'work'
    video_path = os.path.join(workdir, 'video.mp4')
    
    if not os.path.exists(video_path):
        print(f"ERROR: {video_path} not found! Run phase finish first.")
        sys.exit(1)
    
    # Load package for metadata
    pkg_path = os.path.join(workdir, 'package.json')
    title, description, tags = '', '', []
    if os.path.exists(pkg_path):
        with open(pkg_path) as f:
            pkg = json.load(f)
            title = pkg.get('title', '')
            description = pkg.get('description', '')
            tags = pkg.get('tags', [])
    
    # Random 0-8h scheduled publishing (NO SLEEP - uses YouTube's scheduler)
    schedule_delay = random.uniform(0, 8)
    
    url = upload_video(video_path, title, description, tags, 
                       privacy='public', schedule_hours=schedule_delay)
    
    # Save upload state (for duplicate protection)
    with open(os.path.join(workdir, 'uploaded.json'), 'w') as f:
        json.dump({'video_url': url}, f)
    
    print(f"\n✅ Uploaded: {url}")

if __name__ == '__main__':
    main()#!/usr/bin/env python3
""" Simple YouTube uploader for HealthHub v16.4 Uploads the built video WITHOUT the 0-8h sleep that was killing GitHub runners. Uses YouTube's scheduled publishing (publishAt) for natural timing. """
import os
import sys
import json
import random
from datetime import datetime, timedelta, timezone

def get_authenticated_service():
    """Authenticate with YouTube using OAuth refresh token."""
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    
    client_id = os.environ['YT_CLIENT_ID']
    client_secret = os.environ['YT_CLIENT_SECRET']
    refresh_token = os.environ['YT_REFRESH_TOKEN']
    
    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id=client_id,
        client_secret=client_secret,
    )
    # Refresh to get access token
    from google.auth.transport.requests import Request
    creds.refresh(Request())
    
    return build('youtube', 'v3', credentials=creds)

def upload_video(video_path, title, description, tags, privacy='public', schedule_hours=None):
    """Upload video to YouTube with optional scheduled publishing."""
    from googleapiclient.http import MediaFileUpload
    
    youtube = get_authenticated_service()
    
    # Read package info for title/description if not provided
    if not title:
        with open('work/package.json') as f:
            pkg = json.load(f)
            title = pkg.get('title', 'Health Video')
            description = pkg.get('description', '')
            tags = pkg.get('tags', [])
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '27',  # Education
        },
        'status': {
            'privacyStatus': 'private' if schedule_hours else privacy,
        }
    }
    
    # Schedule publishing 0-8h in future (replaces the old sleep)
    if schedule_hours is not None:
        publish_at = datetime.now(timezone.utc) + timedelta(hours=schedule_hours)
        # YouTube requires RFC3339 format
        body['status']['publishAt'] = publish_at.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        print(f"[schedule] Video will publish at {publish_at} (in {schedule_hours:.1f}h)")
    
    # Get thumbnail if exists
    thumb_path = 'work/thumbnail.png'
    
    media = MediaFileUpload(video_path, mimetype='video/mp4', resumable=True)
    
    print(f"[upload] Uploading: {title[:50]}...")
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )
    
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"[upload] {int(status.progress() * 100)}%")
    
    video_id = response['id']
    video_url = f"https://youtu.be/{video_id}"
    print(f"[upload] Done! {video_url}")
    
    # Upload thumbnail
    if os.path.exists(thumb_path):
        print("[upload] Setting thumbnail...")
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumb_path, mimetype='image/png')
        ).execute()
        print("[upload] Thumbnail set!")
    
    return video_url

def main():
    workdir = 'work'
    video_path = os.path.join(workdir, 'video.mp4')
    
    if not os.path.exists(video_path):
        print(f"ERROR: {video_path} not found! Run phase finish first.")
        sys.exit(1)
    
    # Load package for metadata
    pkg_path = os.path.join(workdir, 'package.json')
    title, description, tags = '', '', []
    if os.path.exists(pkg_path):
        with open(pkg_path) as f:
            pkg = json.load(f)
            title = pkg.get('title', '')
            description = pkg.get('description', '')
            tags = pkg.get('tags', [])
    
    # Random 0-8h scheduled publishing (NO SLEEP - uses YouTube's scheduler)
    schedule_delay = random.uniform(0, 8)
    
    url = upload_video(video_path, title, description, tags, 
                       privacy='public', schedule_hours=schedule_delay)
    
    # Save upload state (for duplicate protection)
    with open(os.path.join(workdir, 'uploaded.json'), 'w') as f:
        json.dump({'video_url': url}, f)
    
    print(f"\n✅ Uploaded: {url}")

if __name__ == '__main__':
    main()
