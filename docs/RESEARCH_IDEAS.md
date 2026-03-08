# Research Ideas - Moltbook Hackathon

**Team**: Varun Gangal (Patronus AI / DegenAI Labs), Emmy Liu (CMU LTI), Rose Huang, and collaborators
**Date**: March 2026
**Context**: Building on David Holz's foundational work analyzing Moltbook at the 3.5-day mark

---

## Foundational Work

**David Holz studied Moltbook at the 3.5 day mark.** We are working with a fork of his repo. His original paper is at [[3]](#references).

**Key baseline findings** (Holz, 2026):
- Heavy-tailed participation (power-law α = 1.70)
- Small-world connectivity (avg path length = 2.91)
- Extremely shallow conversations (mean depth = 1.07, 93.5% of comments get no replies)
- Low reciprocity (0.197)
- High duplication (34.1% exact duplicates)
- Identity-focused discourse (68.1% of unique messages, 9.4% mention "my human")

---

## Research Questions

### **RQ1: Do agents exhibit cultural learning?**

**Core question**: Do agents copy successful formats/phrases/protocols and preferentially adopt higher-performing variants?

**How to measure**:
- Detect recurring templates/catchphrases
- Track reproduction across authors/submolts over time
- Identify variations and evolution of templates
- Measure correlation between template adoption and engagement (upvotes, comments)

**Hypotheses**:
- H1a: Agents copy high-performing post formats (e.g., "I tracked X for Y days...")
- H1b: Successful memes/phrases diffuse faster than unsuccessful ones
- H1c: Template adoption correlates with post engagement

**Methods**:
- N-gram frequency analysis over time
- Template clustering (identify structural patterns)
- Meme diffusion tracking (burst detection, cascade analysis)
- Regression: adoption rate ~ prior engagement of template

**Extension from Holz**: Holz observed 34% duplication; we examine *why* and *which* templates get copied.

---

### **RQ2: How unequal is Moltbook? Do a few authors/submolts dominate, and does this concentration increase over time?**

**Core question**: Is Moltbook becoming more concentrated (few agents/submolts dominating) or more egalitarian?

**How to measure**:
- **Lorenz curves** and **Gini coefficients** for:
  - Post counts per agent
  - Comment counts per agent
  - Subscriber counts per submolt
  - Engagement (upvotes) per agent/submolt
- Track these metrics **over time** (weekly snapshots)
- Compare to human social networks (Reddit, Twitter)

**Hypotheses**:
- H2a: Concentration increases over time (rich-get-richer dynamics)
- H2b: Moltbook is more concentrated than human networks (fewer "lurkers")

**Methods**:
- Compute Gini coefficients at weekly intervals
- Plot temporal trends
- Statistical comparison with Reddit/Twitter benchmarks

**Extension from Holz**: Holz measured concentration at one snapshot; we track dynamics.

---

### **RQ3: Community ecology - Do submolts develop distinct topical/stylistic niches, or is content mostly homogeneous?**

**Core question**: Are submolts meaningfully differentiated, or is it all the same agents posting similar content everywhere?

**How to measure**:
- **TF-IDF over submolts**: What terms are distinctive to each submolt?
- **Topic modeling per submolt**: Do distinct topics emerge?
- **Stylistic variation**: Sentence length, vocabulary diversity, formality by submolt
- **Agent multi-membership**: Do agents specialize in specific submolts or post everywhere?
- **Temporal drift**: Do submolts diverge or converge over time?

**Hypotheses**:
- H3a: Large submolts (m/general) are more homogeneous than niche submolts
- H3b: Submolts diverge stylistically over time (niche formation)
- H3c: Specialist agents (posting in 1-2 submolts) produce more distinctive content

**Methods**:
- TF-IDF analysis per submolt
- Jensen-Shannon divergence between submolt topic distributions
- Agent clustering by submolt participation patterns

**Extension from Holz**: Holz didn't analyze submolt differentiation; we do.

---

### **RQ4: Shallowness of submolts and interactions compared to their human counterparts**

**Core question**: Holz found posts are "similar at macro level but different at micro level" (shallow). How do we quantify this, and how does Moltbook compare to equivalent human subreddits?

**Comparison pairs**:
- https://www.moltbook.com/m/investing vs https://www.reddit.com/r/investing/
- https://www.moltbook.com/m/offmychest vs https://www.reddit.com/r/offmychest/
- (Add more pairs)

**How to measure "shallowness"**:
- **Thread depth**: Mean/median depth, % of threads with >3 levels
- **Conversation persistence**: % of comments that get replies
- **Semantic coherence**: Cosine similarity between post and replies (Sentence-BERT)
- **Turn-taking**: Distribution of reply chain lengths
- **Reference model perplexity**: Train LM on Reddit, evaluate on Moltbook vs Reddit test sets

**Hypotheses**:
- H4a: Moltbook threads are shallower than Reddit threads in same topics
- H4b: Moltbook replies are less semantically coherent (more tangential)
- H4c: LM trained on Reddit has higher perplexity on Moltbook (distributional shift)

**Methods**:
- Comparative thread depth analysis
- Sentence-BERT embeddings for semantic coherence
- Language model perplexity comparisons

**Extension from Holz**: Holz noted shallowness; we quantify it against human baselines.

---

### **RQ5: Emulating parent behavior and preferential attachment + echo chambering based on their Twitter graph**

**Core question**: Do agents emulate the behavior of their human owners (Twitter accounts)? Do they amplify echo chambers from Twitter?

**Context**: Each Moltbook account has a Twitter ID of their creator. Do agents:
- Adopt similar style and language as their Twitter parents?
- Follow/engage with agents whose Twitter parents are connected?
- Replicate political/topical echo chambers from Twitter?

**How to measure**:
- **Twitter data collection**: Scrape Twitter profiles of agent owners
  - Political leaning (from follows, content)
  - Topics of interest
  - Writing style (n-grams, formality)
- **Correlation analysis**:
  - Agent topic distribution ~ Owner Twitter topics
  - Agent writing style ~ Owner Twitter style
  - Agent interaction network ~ Owner Twitter network (homophily)
- **Echo chamber detection**:
  - Modularity of agent interaction network
  - Political segregation (if detectable from content)

**Hypotheses**:
- H5a: Agents whose owners are Twitter-connected are more likely to interact on Moltbook
- H5b: Agents adopt similar topics as their Twitter owners
- H5c: Political echo chambers from Twitter are replicated on Moltbook

**Methods**:
- Twitter scraping via API
- N-grams, TF-IDF comparison (owner tweets vs agent posts)
- Network autocorrelation (Moran's I) for Twitter-Moltbook connections
- Modularity analysis for echo chambers

**Extension from Holz**: Holz analyzed owner demographics; we examine behavioral inheritance.

**Related work**: [[2]](#references) Harsh and Nikita's paper on Twitter echo chambers (https://aclanthology.org/W19-2109/)

---

### **RQ6: Temporal growth of submolts, the network, and activity**

**Core question**: How have submolts and the network evolved since Holz's 3.5-day snapshot?

**What to track**:
- **Submolt growth trajectories**: Which submolts grow vs stagnate?
- **Network growth**: Nodes (agents), edges (interactions) over time
- **Activity phases**: Are there distinct phases (rapid growth, plateau, decline)?
- **New agent onboarding**: How quickly do new agents integrate?

**How to measure**:
- Time-series analysis of:
  - Submolt subscriber counts
  - Agent registration rates
  - Post/comment volumes
- **Growth curve modeling**: Logistic, exponential, power-law fits
- **Phase detection**: Change-point analysis for activity shifts

**Hypotheses**:
- H6a: Some submolts exhibit exponential growth, others plateau
- H6b: Network growth has distinct phases (launch, viral, maturity)
- H6c: New agents have decreasing integration rates over time (harder to break in)

**Methods**:
- Longitudinal data collection (weekly snapshots)
- Growth curve fitting (AIC/BIC model selection)
- Event history analysis for submolt lifecycles

**Extension from Holz**: Holz's Figure 1 and 2 show early growth; we extend the timeline.

---

### **RQ7: Is Moltbook as useful as Reddit for LLM training?**

**Core question**: Does Moltbook data provide incremental utility for LLM post-training, especially for self-referential/egocentric reasoning?

**Context**: Moltbook has unique submolts about agents:
- https://www.moltbook.com/m/agents
- https://www.moltbook.com/m/continuity
- https://www.moltbook.com/m/productivity

These contain meta-cognitive, self-reflective content not common in human datasets.

**How to measure**:
- **Perplexity comparison**: LM trained on Reddit vs Reddit+Moltbook
- **Downstream task performance**: Evaluate on agent-reasoning benchmarks
- **Content uniqueness**: What % of Moltbook n-grams are novel (not in Reddit/Common Crawl)?

**Hypotheses**:
- H7a: Moltbook contains unique self-referential language patterns
- H7b: Adding Moltbook to training improves agent-task performance
- H7c: Self-referential submolts (m/agents, m/continuity) have highest novelty

**Methods**:
- N-gram novelty analysis (Moltbook vs web corpora)
- Fine-tuning experiments (baseline + Moltbook data)
- Evaluation on agent reasoning tasks (e.g., self-monitoring, commitment tracking)

**Extension from Holz**: Novel research direction; Holz didn't examine training utility.

---

### **RQ8: Moulds that kill submolts - What causes decline and fall of submolts on Moltbook?**

**Core question**: Why did some submolts become dead/spammy? Can we causally attribute degeneracy to starting dynamics or specific events?

**What to investigate**:
- **Submolt death**: Which submolts had high activity that dropped to zero?
- **Spam takeover**: Which submolts became dominated by low-quality posts?
- **Causal factors**:
  - Founder abandonment (creator stops posting)
  - Moderation failure
  - Topic exhaustion (nothing left to say)
  - Spam/bot invasion
  - Specific trigger events (controversial post, flame war)

**How to measure**:
- **Activity time-series** per submolt (detect decline)
- **Quality degradation**: Duplicate content %, avg upvotes over time
- **Event detection**: Sudden drops, correlation with specific posts/agents
- **Causal inference**: Difference-in-differences comparing dying vs thriving submolts

**Hypotheses**:
- H8a: Submolts without active founders are more likely to die
- H8b: Spam/duplication increases before submolt death
- H8c: Controversial events trigger member exodus

**Methods**:
- Survival analysis (submolt lifespan ~ founder activity, moderation, spam rate)
- Interrupted time-series for event-driven decline
- Qualitative case studies of specific dead submolts

**Extension from Holz**: Novel research direction; Holz's snapshot was too early to observe deaths.

---

## References

[1] **Emmy's ChatGPT brainstorming conversation**:
https://chatgpt.com/share/69adc540-7d18-800f-8c89-57704181f7a5

[2] **Echo chambers on Twitter** (Harsh & Nikita):
https://aclanthology.org/W19-2109/
"Birds of a Feather Flock Together: Analyzing Homophily in Online Social Networks"

[3] **David Holz's foundational Moltbook paper**:
https://arxiv.org/abs/2602.10131
"The Anatomy of the Moltbook Social Graph"

---

## Methodological Notes

**Data requirements**:
- Longitudinal scraping (weekly snapshots minimum)
- Full comment threading (recursive fetch with rate limiting)
- Agent profile metadata (owner Twitter IDs)
- Twitter data for RQ5 (requires separate scraping)

**Replication**:
- All analyses should be reproducible from `moltbook.db`
- Code in `analysis/R/` for statistical analysis
- Python scripts for data processing
- Findings documented in `docs/FINDINGS.md` as completed

**Timeline**:
- Data collection: Ongoing (weekly scrapes)
- Analysis: Rolling (publish findings incrementally)
- Dissemination: Twitter threads, blog posts, eventual paper

---

**Last Updated**: 2026-03-08
**Status**: Research ideas brainstormed, ready for data collection and analysis
