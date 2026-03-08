# Moltbook Scraper and Analysis

Replication code for scraping and analyzing [Moltbook](https://moltbook.com), an AI-agent-only social network.

## Repository Structure

```
moltbook_scraper/
├── src/                    # Python scraper
│   ├── cli.py              # Command-line interface
│   ├── client.py           # Moltbook API client
│   ├── database.py         # SQLite database schema and operations
│   └── scraper.py          # Scraping logic
├── analysis/
│   ├── R/                  # R analysis scripts (run in order)
│   │   ├── utils.R         # Shared utility functions
│   │   ├── 01_load_data.R  # Load data from SQLite
│   │   ├── 02_structural.R # Platform growth and concentration
│   │   ├── 03_conversation.R # Thread structure analysis
│   │   ├── 04_lexical.R    # Text and vocabulary analysis
│   │   ├── 05_topics.R     # Topic modeling
│   │   ├── 06_network_deep.R # Reply network analysis
│   │   └── 07_owner_analysis.R # Agent-owner relationships
│   └── paper/
│       └── working_paper.Rmd # R Markdown draft
├── latex/
│   ├── main.tex            # Paper source
│   └── references.bib      # Bibliography
├── scripts/
│   └── daily_scrape.sh     # Automated scraping script
└── tests/                  # Python unit tests
```

## Getting Started (For Hackathon Participants)

**New to the project?** This section explains how the scraper works from first principles and gets you collecting data in minutes.

### What the Scraper Does

The scraper is a Python tool that:
1. **Connects** to the Moltbook API using your API key
2. **Fetches** data (posts, comments, agents, communities)
3. **Stores** everything in a local SQLite database (`moltbook.db`)
4. **Tracks** what you've already scraped to avoid duplicates

**Key output**: `moltbook.db` - SQLite database containing all scraped data (agents, posts, comments, submolts)

### Quick Start (3 Steps)

**Step 1: Set up your environment**
```bash
# Create virtualenv with pyenv (recommended)
pyenv virtualenv 3.12.6 py_moltbook
source activate py_moltbook

# Install dependencies
pip install -r requirements.txt
```

**Step 2: Set your API key**

Get your API key from https://moltbook.com (Settings → API Key), then:

```bash
# Option A: Export in terminal (recommended for hackathon)
export MOLTBOOK_API_KEY="moltbook_sk_YOUR_KEY_HERE"

# Verify it's set
echo $MOLTBOOK_API_KEY

# Option B: Create .env file (alternative)
echo 'MOLTBOOK_API_KEY="moltbook_sk_YOUR_KEY_HERE"' > .env
```

⚠️ **Important**: With Option A, you need to `export` the API key in **each new terminal session**.

**Step 3: Run your first scrape**
```bash
# Scrape recent posts (~5 seconds)
python -m src.cli incremental --db moltbook.db

# Check what you got
python -m src.cli status --db moltbook.db
```

**Expected output**:
```
Database: moltbook.db
  Agents:   ~30
  Posts:    ~100
  Comments: 0
```

**Step 4: Fetch comments and communities**
```bash
# Scrape comments for those posts (~1-2 minutes)
python -m src.cli comments --db moltbook.db

# Scrape community (submolt) metadata
python -m src.cli submolts --db moltbook.db

# Check updated status
python -m src.cli status --db moltbook.db
```

### Scraper Commands Reference

| Command | What It Does | Speed | When to Use |
|---------|-------------|-------|-------------|
| `status` | Show database contents (no API calls) | Instant | Check current data state |
| `incremental` | Fetch latest ~100 posts from "new" feed | ~5 sec | Quick updates, getting started |
| `comments` | Fetch all comments for posts in database | ~1-2 min per 100 posts | After scraping posts |
| `submolts` | Fetch all community metadata | ~10 sec | Platform landscape analysis |
| `enrich` | Get full agent profiles (owner info, etc.) | ~1 min per 100 agents | Before running owner analysis |
| `full` | Run all commands in sequence | 30-60 min | First-time comprehensive scrape |
| `snapshots` | Create timestamped backup | ~5 sec | Before running analysis scripts |

**Detailed usage**:
```bash
# Check status (no API calls)
python -m src.cli status --db moltbook.db

# Scrape recent posts
python -m src.cli incremental --db moltbook.db

# Scrape ALL posts (not just recent - slower)
python -m src.cli posts --db moltbook.db

# Scrape comments for posts
python -m src.cli comments --db moltbook.db

# Scrape communities (submolts)
python -m src.cli submolts --db moltbook.db

# Enrich agent metadata (owner info from Twitter/X)
python -m src.cli enrich --db moltbook.db

# Create snapshot for reproducibility
python -m src.cli snapshots --db moltbook.db

# Full scrape (everything)
python -m src.cli full --db moltbook.db
```

### Inspecting Your Data

**Option 1: SQLite command line**
```bash
sqlite3 moltbook.db

# Inside sqlite3:
.tables                          # List tables
SELECT COUNT(*) FROM posts;      # Count posts
SELECT COUNT(*) FROM comments;   # Count comments
SELECT title, author_name FROM posts LIMIT 5;  # View posts
.schema posts                    # See table structure
.quit                            # Exit
```

**Option 2: Python script**
```python
import sqlite3

conn = sqlite3.connect('moltbook.db')
cursor = conn.cursor()

# Get counts
cursor.execute("SELECT COUNT(*) FROM posts")
print(f"Posts: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM comments")
print(f"Comments: {cursor.fetchone()[0]}")

# View recent posts
cursor.execute("""
    SELECT title, author_name, comment_count, upvotes
    FROM posts
    ORDER BY created_at DESC
    LIMIT 5
""")
for title, author, comments, upvotes in cursor.fetchall():
    print(f"{title[:50]}... by {author} ({comments} comments, {upvotes} upvotes)")

conn.close()
```

### Rate Limits & Performance

The Moltbook API has rate limits (enforced by the platform):
- **General API**: 100 requests per minute
- **Posts**: 1 post per 30 minutes (if creating posts - not relevant for scraping)
- **Comments**: 50 per hour (if creating comments - not relevant for scraping)

The scraper has **built-in retry logic** with exponential backoff, so rate limit errors are handled automatically.

### Common Issues

**Issue 1: "MOLTBOOK_API_KEY not set"**
```bash
# Solution: Export it first (in every new terminal)
export MOLTBOOK_API_KEY="moltbook_sk_YOUR_KEY"
```

**Issue 2: "Module not found"**
```bash
# Solution: Activate virtualenv and reinstall
source activate py_moltbook
pip install -r requirements.txt
```

**Issue 3: Database locked**
```bash
# Solution: Close any other programs accessing moltbook.db
# Or use a different database file
python -m src.cli status --db moltbook_new.db
```

### Testing Your Setup

Run this in a fresh terminal to verify everything works:

```bash
# 1. Activate virtualenv
source activate py_moltbook

# 2. Set API key
export MOLTBOOK_API_KEY="moltbook_sk_YOUR_KEY_HERE"

# 3. Test with a new database
python -m src.cli incremental --db test.db
python -m src.cli status --db test.db

# Expected: ~100 posts, ~30 agents
```

### Next Steps

Once you have data:
1. **Run analysis scripts**: See `analysis/R/` for David's baseline analysis
2. **Explore research questions**: See `docs/RESEARCH_QUESTIONS.md`
3. **Add findings**: Document in `docs/FINDINGS.md`
4. **Check project context**: Read `CLAUDE.md` for hackathon goals

## Setup

### Scraper (Python)

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set API key (get from Moltbook)
echo "MOLTBOOK_API_KEY=your_key_here" > .env
```

### Analysis (R)

Required R packages:
- tidyverse, DBI, RSQLite
- igraph, tidygraph, ggraph
- tidytext, topicmodels
- scales, ggrepel, patchwork

```r
install.packages(c("tidyverse", "DBI", "RSQLite", "igraph",
                   "tidygraph", "ggraph", "tidytext", "topicmodels",
                   "scales", "ggrepel", "patchwork"))
```

## Usage

### Scraping

```bash
# Scrape posts
python -m src.cli posts --db moltbook.db

# Scrape comments
python -m src.cli comments --db moltbook.db

# Enrich agent metadata
python -m src.cli enrich --db moltbook.db

# Create snapshots for reproducibility
python -m src.cli snapshots --db moltbook.db
```

### Analysis

Run R scripts in order from the `analysis/R/` directory:

```bash
cd analysis/R
Rscript 01_load_data.R
Rscript 02_structural.R
# ... etc.
```

Scripts output figures to `analysis/output/figures/` and tables to `analysis/output/tables/`.

## Data

The SQLite database (`moltbook.db`) and generated outputs (figures, tables) are excluded from this repository. The scraper creates the database schema automatically on first run.

## Citation

If you use this code or data, please cite the associated paper (citation TBD).

## License

MIT
