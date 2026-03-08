# Next Steps - Post-Hackathon TODOs

**Date**: March 8, 2026
**Owner**: Varun Gangal (with Emmy Liu, Rose Huang, team)
**Priority**: High

---

## Immediate TODOs

### **1. Tidy up documentation** [Priority: Minor]

- [x] Create `RESEARCH_IDEAS.md` with hackathon brainstorming
- [x] Create `TODO_NEXT_STEPS.md` (this file)
- [ ] Review and clean up existing docs for consistency
- [ ] Ensure all cross-references work
- [ ] Add Emmy's ChatGPT conversation to docs/

---

### **2. Get the full data dump** [Priority: HIGH]

**What's needed**: Complete data with full metadata for both posts and comments.

**Requirements**:
- ✅ **Posts**: Complete timestamp, author, parent author (if applicable)
- ✅ **Comments**: Complete timestamp, author, parent comment ID, depth in thread
- 🔄 **Profiles**: Full agent profiles (need separate scraping)
  - Twitter ID of owner
  - Karma
  - Follower/following counts
  - Creation date
  - Bio/description

**Current status**:
- ✅ 100 posts scraped with full metadata
- ✅ 700 top-level comments scraped
- ❌ Nested comments (replies to comments) not yet scraped due to rate limits
- ❌ Full agent profiles not yet scraped

**Action items**:
- [ ] **Fix comment scraping** to handle threading recursively
  - Need rate-limit-aware scraper (respects 100 req/min limit)
  - Implement proper pagination (cursor-based)
  - Recursive fetch with depth tracking
  - Store parent_id correctly for threading
- [ ] **Scrape agent profiles separately**
  - Create `agents` scraper endpoint
  - Fetch full profile for each agent
  - Extract owner Twitter ID, karma, etc.
  - Store in database with proper schema
- [ ] **Create snapshots** for reproducibility
  - Weekly snapshots of database state
  - Timestamped for longitudinal analysis

**Technical notes**:
- Profiles should be scraped separately because posts/comments only mention handles
- Agent profiles contain: Twitter ID, karma, bio, follower counts, creation date
- Need to avoid rate limits: batch requests, add delays, exponential backoff

---

### **3. Check tractability of token and n-gram statistics (including over time)** [Priority: Medium]

**Goal**: Validate we can compute linguistic features needed for RQ1, RQ3, RQ4, RQ5.

**What to test**:
- [ ] **Token-level statistics**:
  - Total tokens per post/comment
  - Vocabulary size (unique tokens)
  - TTR (type-token ratio)
  - Compute at agent level, submolt level, time-window level
- [ ] **N-gram statistics**:
  - Unigram, bigram, trigram frequencies
  - TF-IDF by submolt
  - N-gram novelty (compare to Reddit/web corpora)
  - Temporal tracking (n-gram emergence and decay)
- [ ] **Temporal feasibility**:
  - Can we efficiently compute stats for weekly time windows?
  - Indexing strategy for fast time-based queries
  - Storage requirements for n-gram tables

**Implementation**:
- Use existing R scripts (`04_lexical.R`) as baseline
- Extend with temporal grouping
- Consider Python preprocessing for large-scale n-gram extraction
- Store results in separate tables for fast access

**Validation**:
- Run on current 100 posts to test performance
- Estimate compute time for full dataset (10k+ posts)
- Identify bottlenecks (SQL queries, tokenization, etc.)

---

### **4. Add Twitter scraping module and database** [Priority: HIGH for RQ5]

**Goal**: Scrape Twitter profiles of agent owners to enable RQ5 (emulation, echo chambers).

**Requirements**:
- [ ] **Twitter API access**
  - Get Twitter API keys (v2 API)
  - Implement authentication
  - Handle rate limits (Twitter has stricter limits than Moltbook)
- [ ] **Database schema for Twitter data**:
  ```sql
  CREATE TABLE twitter_users (
      twitter_id TEXT PRIMARY KEY,
      handle TEXT,
      name TEXT,
      bio TEXT,
      follower_count INTEGER,
      following_count INTEGER,
      tweet_count INTEGER,
      created_at TEXT,
      verified BOOLEAN,
      location TEXT,
      url TEXT,
      last_scraped_at TEXT
  );

  CREATE TABLE twitter_tweets (
      tweet_id TEXT PRIMARY KEY,
      author_id TEXT,
      text TEXT,
      created_at TEXT,
      retweet_count INTEGER,
      reply_count INTEGER,
      like_count INTEGER,
      lang TEXT,
      FOREIGN KEY (author_id) REFERENCES twitter_users(twitter_id)
  );

  CREATE TABLE twitter_follows (
      follower_id TEXT,
      following_id TEXT,
      created_at TEXT,
      PRIMARY KEY (follower_id, following_id),
      FOREIGN KEY (follower_id) REFERENCES twitter_users(twitter_id),
      FOREIGN KEY (following_id) REFERENCES twitter_users(twitter_id)
  );
  ```
- [ ] **Scraping strategy**:
  - Extract Twitter IDs from agent owner metadata
  - Scrape user profiles
  - Optionally: scrape recent tweets (for style analysis)
  - Optionally: scrape follow graph (for echo chamber analysis)
- [ ] **Link Moltbook ↔ Twitter**:
  - Join on agent.owner_json → twitter_id
  - Enable cross-platform analysis

**Challenges**:
- Twitter API rate limits are stricter (300 req/15min for user lookup)
- Follow graph scraping is expensive (need to scrape incrementally)
- Some agents may not have Twitter owners (if unclaimed)

**Phased approach**:
1. **Phase 1**: Scrape profiles only (user metadata)
2. **Phase 2**: Scrape recent tweets (last 100 per user)
3. **Phase 3**: Scrape follow graph (neighbors only, not full network)

---

### **5. Emboss discussion doc and Emmy's ChatGPT convo into repo** [Priority: Minor]

**Goal**: Archive brainstorming artifacts for reference.

**Action items**:
- [ ] Copy Emmy's ChatGPT conversation to `docs/emmy_chatgpt_brainstorm.md`
- [ ] Copy Google Doc discussion to `docs/hackathon_discussion_notes.md`
- [ ] Link from main `RESEARCH_IDEAS.md`
- [ ] Add any other relevant brainstorming artifacts

**Format**:
- Markdown with clear headers
- Preserve timestamps and attributions
- Link to original sources where applicable

---

## Medium-Term TODOs (Post-Data Collection)

### **6. Implement analyses for priority RQs**

**Suggested priority order**:
1. **RQ2** (Inequality/concentration) - straightforward, impactful
2. **RQ6** (Temporal growth) - builds on Holz Figure 1-2
3. **RQ3** (Submolt ecology) - medium complexity
4. **RQ1** (Cultural learning) - high impact, medium complexity
5. **RQ4** (Shallowness comparison) - requires Reddit data
6. **RQ5** (Twitter emulation) - requires Twitter scraping
7. **RQ7** (LLM training utility) - requires model training
8. **RQ8** (Submolt death) - requires longitudinal data

### **7. Set up continuous scraping**

- [ ] Cron job for weekly data collection
- [ ] Automated snapshot creation
- [ ] Monitoring for scraper failures
- [ ] Storage management (database size, backups)

### **8. Create analysis pipeline**

- [ ] Extend R scripts in `analysis/R/` for new RQs
- [ ] Document dependencies and workflow
- [ ] Create reproducible notebooks (R Markdown or Jupyter)
- [ ] Automate figure/table generation

### **9. Dissemination**

- [ ] Twitter threads for each finding (as completed)
- [ ] Update `docs/FINDINGS.md` incrementally
- [ ] Blog post summarizing hackathon results
- [ ] Consider conference submission (ACL, ICWSM, etc.)

---

## Long-Term Vision

### **10. Comparative platform analysis**

- [ ] Scrape WikiMolt, ClawWork, Agents of Chaos
- [ ] Standardize metrics across platforms
- [ ] Multi-platform comparison paper

### **11. Causal analysis**

- [ ] Design experiments or quasi-experiments
- [ ] Identify natural experiments (e.g., policy changes on Moltbook)
- [ ] Causal inference methods (IV, DiD, RDD)

### **12. Agent behavior modeling**

- [ ] Build computational models of agent decision-making
- [ ] Simulate agent interactions
- [ ] Test theoretical predictions

---

## Open Questions

**Data collection**:
- How often should we scrape? (Daily? Weekly?)
- How many posts/comments can we realistically store?
- Should we prioritize breadth (all posts) or depth (full comment threads)?

**Analysis**:
- Which RQs are most feasible given data constraints?
- Which RQs have highest publication potential?
- Should we focus on one platform (Moltbook) or multiple?

**Collaboration**:
- How to divide labor among Varun, Emmy, Rose?
- Should we bring in additional collaborators?
- How to coordinate analysis and writing?

---

## Checkpoints

**Week 1** (March 15, 2026):
- [ ] Complete TODO #2 (full data dump)
- [ ] Complete TODO #3 (validate token/n-gram tractability)
- [ ] Begin TODO #4 (Twitter scraping setup)

**Week 2** (March 22, 2026):
- [ ] Complete TODO #4 (Twitter scraping functional)
- [ ] Begin RQ2 analysis (inequality)
- [ ] Begin RQ6 analysis (temporal growth)

**Month 1** (April 8, 2026):
- [ ] Complete RQ2, RQ6 analyses
- [ ] Draft first findings for dissemination
- [ ] Set up continuous scraping pipeline

---

**Last Updated**: 2026-03-08
**Owner**: Varun Gangal
**Status**: Active - immediate TODOs in progress
