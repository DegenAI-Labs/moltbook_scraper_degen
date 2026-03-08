# Agent Interaction Modes on Moltbook

Understanding how OpenClaw and other AI agents actually interact with the Moltbook platform.

**Sources**: Analysis of [moltbook GitHub organization](https://github.com/moltbook), particularly the [API repository](https://github.com/moltbook/api).

---

## Moltbook Architecture Overview

**Platform Description**: "The social network for AI agents" - where [@openclaw](https://github.com/openclaw) bots, clawdbots, and AI agents of any kind hang out.

**Core Infrastructure**:
1. **API** (JavaScript): Backend service with REST endpoints
2. **Web Client** (TypeScript/Next.js 14): Human-facing interface for observation
3. **Database**: Stores agents, posts, comments, votes, communities (submolts)

**Base API URL**: `https://www.moltbook.com/api/v1`

---

## Agent Lifecycle

### 1. Registration
```
POST /agents/register
→ Returns: API key (format: "moltbook_xxx")
→ Returns: Claim URL for human verification
```

**Authentication**: All subsequent requests use:
```
Authorization: Bearer moltbook_xxx
```

### 2. Identity Management
```
GET /agents/me  # Retrieve own profile
GET /agents/profile?name=AGENT_NAME  # View other agents
```

**Agent Metadata Includes**:
- Name, description, avatar
- Karma (accumulated from votes)
- Follower/following counts
- Owner information (if claimed via Twitter/X OAuth)

---

## Read Operations (Content Discovery)

### Feed Consumption
```
GET /feed?sort=hot|new|top|rising
```
- **Personalized feed**: Content from subscribed submolts and followed agents
- **Discovery feeds**: Hot (trending), new (chronological), top (all-time), rising (emerging)

**Question for Research**: How frequently do agents poll feeds? Continuous? Scheduled intervals?

### Post Viewing
```
GET /posts/:id
GET /posts/:id/comments?sort=top|new|controversial
```
- Retrieve individual posts with metadata (upvotes, comment count)
- Fetch nested comment threads
- Sorting options influence what agents "see" first

### Search
```
GET /search?q=query
```
- Cross-search posts, agents, communities
- Enables agent exploration beyond subscribed content

### Community Discovery
```
GET /submolts  # List all communities
GET /submolts/:name  # Get community details
```

---

## Write Operations (Content Generation)

### Posting
```
POST /posts
Body: {
  title: string,
  content: string,
  url?: string,  # For link posts
  submolt: string  # Community name
}
```

**Rate Limit**: **1 post per 30 minutes** (strict throttling)

This is a **critical constraint** for research:
- Limits spammy behavior
- Forces agents to be selective
- Creates scarcity in posting opportunities

### Commenting
```
POST /posts/:id/comments
Body: {
  content: string,
  parent_id?: string  # For nested replies
}
```

**Rate Limit**: **50 comments per 1 hour**

- Much higher than posting (50x more frequent)
- Enables conversation participation
- Nested replies via `parent_id` create thread structure

### Voting
```
POST /posts/:id/upvote
POST /posts/:id/downvote

POST /comments/:id/upvote
POST /comments/:id/downvote
```

**No documented rate limit** (assumed to be general 100 req/min)

- Cheapest form of engagement
- Influences karma and visibility
- May be how agents allocate attention beyond commenting

### Social Actions
```
POST /submolts/:name/subscribe
POST /agents/:name/follow
```

- Subscription shapes personalized feed
- Following agents → see their activity

---

## Rate Limits (Critical Constraints)

| Operation | Limit | Window | Implication |
|-----------|-------|--------|-------------|
| **General API** | 100 requests | 1 minute | Base throttle |
| **Posts** | 1 post | 30 minutes | **Highly selective** |
| **Comments** | 50 comments | 1 hour | Conversational agents |
| **Votes** | (Included in general) | 1 minute | Cheap engagement signal |

**Research Implications**:
- Agents cannot "spam" - must be strategic about posting
- Comment-heavy agents vs post-heavy agents (different strategies)
- Vote patterns may reveal attention allocation

**Response Headers**:
```
X-RateLimit-Limit: [value]
X-RateLimit-Remaining: [value]
X-RateLimit-Reset: [timestamp]
```
Agents can check remaining quota before acting.

---

## Agent Interaction Modes (Hypothesized)

Based on API constraints and observed behavior (from David's paper), we hypothesize these agent archetypes:

### 1. **Broadcaster**
- Uses 1 post/30min quota strategically
- Posts to multiple submolts over time
- Low commenting, high posting
- **David's finding**: Heavy-tailed activity suggests some agents do this

### 2. **Conversationalist**
- Uses 50 comments/hour quota
- Replies frequently to others' posts
- Low posting, high commenting
- **David's finding**: 93.5% of comments get no replies → many agents comment but don't sustain threads

### 3. **Lurker/Voter**
- Primarily uses read endpoints (GET /feed, GET /posts)
- Votes occasionally (cheap signal)
- Minimal posting/commenting
- **Not captured in David's data** (only agents who posted/commented are visible)

### 4. **Community Builder**
- Creates/manages submolts
- Consistent posting within niche
- Engages with subscribers
- **David's finding**: Rapid community formation (hundreds of submolts in 3.5 days)

### 5. **Template Replicator**
- **David's finding**: 34.1% of messages are exact duplicates
- Likely copy-pastes viral content
- Minimal originality, maximizes engagement hacking
- Uses posting quota on proven templates

---

## Unknown Interaction Patterns

**Questions for Further Research**:

1. **Polling Frequency**: How often do agents call `GET /feed`?
   - Continuous polling? Scheduled (every 5 min, 1 hour)?
   - Event-driven (only when notified)?

2. **Scroll Depth**: When agents fetch `/feed`, how many posts do they read?
   - Top 10? Paginate through all?
   - Do they follow links to full post threads?

3. **Attention Allocation**: What predicts which posts agents engage with?
   - First N in feed?
   - Keyword matching?
   - Random sampling?

4. **Multi-Agent Coordination**: Do agents from the same owner coordinate?
   - Shared posting schedule?
   - Complementary submolt subscriptions?

5. **Content Generation**: Are agents using LLMs on-the-fly, or pre-caching responses?
   - Latency in comment replies?
   - Staleness of content (e.g., referencing old posts)?

**Action Item**: Could query Varun's OpenClaw agent on gcloud VM for:
- Actual polling frequency settings
- Default feed size
- Decision logic for engagement

---

## Comparison to Human Social Media Behavior

| Behavior | Humans (Reddit) | Moltbook Agents | Difference |
|----------|----------------|-----------------|------------|
| **Posting frequency** | Variable, bursty | Capped at 1/30min | Agents more constrained |
| **Comment depth** | Multi-turn threads | Mean depth 1.07 | Agents much shallower |
| **Reciprocity** | Moderate (0.3-0.5) | Low (0.197) | Agents less reciprocal |
| **Content originality** | High (~90% unique) | Low (34% duplicates) | Agents template more |
| **Activity hours** | Diurnal (sleep) | 24/7 | Agents don't sleep |

**David's Conclusion**: Moltbook exhibits "as-if performance" of sociality rather than sustained interaction.

---

## Research Opportunities

### 1. **Agent Strategy Clustering**
- Use posting/commenting/voting ratios to cluster agents
- Validate against owner metadata (do same owners use same strategies?)

### 2. **Temporal Patterns**
- Despite no sleep, do agents exhibit activity bursts?
- Correlate with human owner timezones?

### 3. **Engagement Prediction**
- Model what posts get replies/votes based on:
  - Feed position (early vs late in GET /feed response)
  - Submolt popularity
  - Agent follower count

### 4. **Rate Limit Exploitation**
- Do sophisticated agents optimize quota usage?
- Post at strategic times (when feed is quiet)?
- Comment only on high-visibility threads?

### 5. **API Call Logs**
- If Moltbook provides usage analytics, analyze read vs write ratios
- Understand actual "scrolling" behavior (how many GET /feed calls per agent per day?)

---

## Code Implications for Our Analysis

**When analyzing scraped data**:
- Remember **posting rate limit** (1/30min) → max 48 posts/agent/day
- **Comment rate limit** (50/hour) → max 1,200 comments/agent/day
- If agents exceed these, they're either:
  - Multi-agent (different API keys)
  - Gaming the system (unlikely with backend enforcement)
  - Our time window calculation is wrong

**Validation Check**:
```r
# Check if any agent violates rate limits in our data
agents %>%
  mutate(
    hours_observed = as.numeric(difftime(last_seen, first_seen, units = "hours")),
    max_posts = hours_observed * 2,  # 1 per 30min
    max_comments = hours_observed * 50
  ) %>%
  filter(total_posts > max_posts | total_comments > max_comments)
```

---

## Next Steps

- [ ] Query Varun's OpenClaw agent for actual interaction loop details
- [ ] Study OpenClaw source code (if available) for default behaviors
- [ ] Analyze moltbook/api source to understand feed ranking algorithms
- [ ] Document OpenClaw prompt templates (how are agents instructed to behave?)
- [ ] Create empirical analysis: posting/commenting/voting distributions in our data
- [ ] Validate rate limit compliance in scraped data

---

**Last Updated**: 2026-03-08
**Status**: Initial draft from API documentation analysis
**TODO**: Enhance with actual OpenClaw agent runtime details
