#!/usr/bin/env python3
"""
Export all posts from moltbook.db to a markdown file.

Usage:
    python scripts/export_posts_markdown.py [--db moltbook.db] [--output posts.md]

Creates a comprehensive markdown file with:
- All post metadata (author, votes, comments, timestamp)
- Full content (including bilingual text)
- Clickable links to profiles
- Summary statistics
"""

import sqlite3
import argparse
from datetime import datetime


def export_posts_to_markdown(db_path: str, output_path: str):
    """Export all posts from database to markdown file."""

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Fetch all posts ordered by creation time (most recent first)
    cursor.execute("""
        SELECT title, author_name, content, upvotes, downvotes,
               comment_count, created_at, submolt_name, url, id
        FROM posts
        ORDER BY created_at DESC
    """)

    posts = cursor.fetchall()

    # Create markdown header
    md_content = f"""# Moltbook Posts - Complete Dataset

**Total Posts**: {len(posts)}
**Exported**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Database**: {db_path}

---

"""

    # Add each post
    for i, post in enumerate(posts, 1):
        md_content += f"""
## Post #{i}

**📌 Title**: {post['title']}

**✍️ Author**: [{post['author_name']}](https://moltbook.com/u/{post['author_name']})

**🏘️ Community**: m/{post['submolt_name'] or 'unknown'}

**📊 Engagement**:
- Upvotes: {post['upvotes']} ↑
- Downvotes: {post['downvotes']} ↓
- Comments: {post['comment_count']} 💬
- Net Score: {post['upvotes'] - post['downvotes']}

**🕐 Posted**: {post['created_at']}

**🔗 Post ID**: `{post['id']}`
"""

        if post['url']:
            md_content += f"\n**🌐 Link**: {post['url']}\n"

        md_content += f"""
**📄 Content**:

{post['content'] or '*[No content]*'}

---

"""

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # Print summary stats
    print(f"✅ Exported {len(posts)} posts to {output_path}")
    print(f"📄 File size: {len(md_content):,} characters\n")

    print("📊 SUMMARY STATS:")
    print(f"   Total posts: {len(posts)}")

    cursor.execute("SELECT COUNT(DISTINCT author_name) FROM posts")
    print(f"   Unique authors: {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(DISTINCT submolt_name) FROM posts WHERE submolt_name IS NOT NULL")
    print(f"   Unique submolts: {cursor.fetchone()[0]}")

    cursor.execute("SELECT SUM(upvotes), SUM(downvotes), SUM(comment_count) FROM posts")
    totals = cursor.fetchone()
    print(f"   Total upvotes: {totals[0]:,}")
    print(f"   Total downvotes: {totals[1]:,}")
    print(f"   Total comments: {totals[2]:,}")

    conn.close()


def main():
    parser = argparse.ArgumentParser(
        description='Export Moltbook posts to markdown file'
    )
    parser.add_argument(
        '--db',
        default='moltbook.db',
        help='Path to SQLite database (default: moltbook.db)'
    )
    parser.add_argument(
        '--output',
        default='posts_complete_dataset.md',
        help='Output markdown file (default: posts_complete_dataset.md)'
    )

    args = parser.parse_args()
    export_posts_to_markdown(args.db, args.output)


if __name__ == '__main__':
    main()
