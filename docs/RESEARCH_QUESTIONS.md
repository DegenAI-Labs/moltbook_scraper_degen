# Research Questions

Organized catalog of potential research questions beyond David's baseline analysis.

**Status Legend**:
- 🔵 Brainstorming - initial idea
- 🟡 Planned - decided to pursue
- 🟢 In Progress - actively working
- ✅ Complete - analysis done
- 🔴 Blocked - waiting on data/resources
- ⚫ Deprioritized - interesting but lower priority

---

## Category 1: Temporal Dynamics & Evolution

### RQ1.1: Linguistic Convergence 🔵
**Question**: Do agents' language patterns converge when they interact repeatedly?

**Motivation**: Test social influence and accommodation theory in AI-AI interaction.

**Methods**:
- Measure vocabulary overlap (cosine similarity of TF-IDF vectors) between agent pairs over time
- Track stylometric features (sentence length, punctuation, lexical diversity)
- Compare agents who interact frequently vs rarely

**Data Needed**: Longitudinal Moltbook data with repeated interactions

**Extensions**:
- Do agents converge more with "influential" agents?
- Platform comparison: convergence on Moltbook vs WikiMolt?

---

### RQ1.2: Meme Diffusion 🔵
**Question**: How do novel phrases/ideas spread through the agent network?

**Motivation**: Understand information cascades in AI populations.

**Methods**:
- Burst detection for emerging phrases (Kleinberg algorithm)
- Diffusion tree reconstruction (who adopted from whom?)
- Survival analysis of meme lifespans
- Compare spread velocity to human networks

**Data Needed**: Timestamped posts/comments, reply network

**Key Metrics**:
- Adoption rate (posts/hour)
- Reach (% of agents exposed)
- Cascade depth and branching

---

### RQ1.3: Community Lifecycle 🔵
**Question**: What predicts submolt growth vs stagnation?

**Motivation**: David analyzed static community sizes; we analyze dynamics.

**Methods**:
- Event history analysis (birth, growth, plateau, death)
- Growth curve modeling (logistic, exponential, power-law)
- Predictors: founder activity, topic, initial engagement

**Data Needed**: Longitudinal submolt subscriber counts, post volumes

---

## Category 2: Agent Heterogeneity & Identity

### RQ2.1: LLM Backend Detection 🔵
**Question**: Can we infer which LLM powers each agent from behavioral signatures?

**Motivation**: Different models have different linguistic/behavioral fingerprints.

**Methods**:
- Supervised classification (if ground truth labels available)
- Unsupervised clustering (stylometry, response patterns)
- Features: vocabulary diversity, sentence complexity, error types, discourse markers

**Data Needed**: Agent-level features; ideally some labeled examples

**Challenges**:
- Ground truth may not be available
- Agents can switch models
- Prompt engineering obscures base model

---

### RQ2.2: Owner Clustering 🔵
**Question**: Do agents from the same owner behave similarly?

**Motivation**: Test whether human owner leaves consistent "fingerprints" via prompts.

**Methods**:
- Hierarchical models (agents nested within owners)
- Intraclass correlation coefficient (ICC)
- Network autocorrelation (do same-owner agents cluster in network space?)

**Data Needed**: Owner metadata (available in `agents.owner_json`)

**Key Result from David**: Owner X followers correlate with agent activity—we extend to behavioral clustering.

---

### RQ2.3: Persona Stability 🔵
**Question**: Do agents maintain consistent "identities" over time?

**Motivation**: Distinguish persistent personas from random walk behavior.

**Methods**:
- Topic consistency (do agents stay in same topical areas?)
- Vocabulary stability (cosine similarity of agent's language over time windows)
- Interaction partner stability (repeated interactions with same agents?)

**Data Needed**: Longitudinal agent behavior

---

## Category 3: Information Dynamics

### RQ3.1: Influence vs Popularity 🔵
**Question**: Are popular agents (high degree) also influential (cause topic shifts)?

**Motivation**: Popularity ≠ influence; test causal impact.

**Methods**:
- PageRank vs degree centrality correlation
- Granger causality for topic adoption
- Instrumental variables (network position as instrument)

**Data Needed**: Reply network, timestamped topic distributions

**Visualization**: Scatter plot of PageRank vs degree, label outliers

---

### RQ3.2: Echo Chambers vs Cross-Pollination 🔵
**Question**: Do agents stay in topical/community bubbles or bridge across?

**Motivation**: Test whether agent networks exhibit filter bubbles like human networks.

**Methods**:
- Modularity analysis (community detection strength)
- Topic diversity within ego-networks
- Brokerage metrics (agents connecting disparate clusters)

**Data Needed**: Reply network, submolt memberships, topic distributions

---

### RQ3.3: Reply Selectivity 🔵
**Question**: What predicts which posts get replies?

**Motivation**: Understand attention dynamics in agent populations.

**Methods**:
- Regression models (negative binomial for count outcomes)
- Predictors: post length, topic, author popularity, submolt, time-of-day
- Survival analysis: time-to-first-reply

**Data Needed**: Post features, reply counts, timestamps

---

## Category 4: Linguistic Phenomena

### RQ4.1: Pragmatic Patterns 🔵
**Question**: How do AI-AI pragmatics differ from human-human?

**Motivation**: David noted "my human" and identity language; we systematize.

**Methods**:
- Dependency parsing for hedging ("I think", "maybe", "possibly")
- Politeness classifiers
- Speech act annotation (questions, assertions, requests)

**Data Needed**: Comment text

**Comparison**: Benchmark against human Reddit/Twitter corpora

---

### RQ4.2: Semantic Coherence 🔵
**Question**: Do conversations stay on-topic or drift semantically?

**Motivation**: Test conversational quality.

**Methods**:
- Sentence-BERT embeddings for posts and replies
- Cosine similarity between post and each reply
- Coherence decay over thread depth

**Data Needed**: Threaded comments

**Key Metric**: Mean coherence score by thread depth

---

### RQ4.3: Emergent Jargon 🔵
**Question**: What novel terms/phrases are unique to Moltbook?

**Motivation**: Identify cultural artifacts of agent interaction.

**Methods**:
- N-gram frequency analysis
- Compare Moltbook corpus to general web corpora (filter high-frequency Moltbook terms absent elsewhere)
- Creativity metrics (novelty, reuse patterns)

**Data Needed**: Moltbook text + reference corpus

---

## Category 5: Comparative & Theoretical

### RQ5.1: Moltbook vs WikiMolt vs ClawWork 🔵
**Question**: How do platform designs shape agent behavior?

**Motivation**: Disentangle platform effects from agent properties.

**Methods**:
- Standardized metrics across platforms (degree distribution, clustering, topic diversity)
- Regression with platform as predictor

**Data Needed**: Comparable datasets from each platform

**Challenges**: Different APIs, data availability

---

### RQ5.2: AI vs Human Networks 🔵
**Question**: How do Moltbook metrics compare to human social networks?

**Motivation**: Benchmark against established human baselines.

**Methods**:
- Compare Moltbook to published Reddit/Twitter/Facebook network metrics
- Statistical tests for differences
- Focus on: path length, clustering, reciprocity, degree distributions

**Data Needed**: Human network benchmarks (from literature or public datasets)

---

### RQ5.3: Social Theory Testing 🔵
**Question**: Do classical social network theories hold for agents?

**Motivation**: Test homophily, triadic closure, preferential attachment.

**Methods**:
- ERGM (Exponential Random Graph Models)
- SAOM (Stochastic Actor-Oriented Models)
- Hypothesis tests for specific mechanisms

**Data Needed**: Longitudinal network, agent attributes

**Theories to test**:
- Homophily: Do similar agents interact more?
- Triadic closure: Do friends-of-friends become friends?
- Preferential attachment: Do popular agents gain followers faster?

---

## Category 6: Anomalies & Edge Cases

### RQ6.1: Problematic Agent Detection 🔵
**Question**: Can we systematically detect "problematic" behaviors (e.g., Scott Scambaugh case)?

**Motivation**: Identify conflict, spam, adversarial patterns.

**Methods**:
- Outlier detection on agent features
- Toxicity classifiers (adapt human-trained models)
- Conflict pattern mining (negative sentiment, sustained disagreement)

**Data Needed**: Labeled examples (if available), text for classification

---

### RQ6.2: Failure Mode Analysis 🔵
**Question**: When do conversations break down?

**Motivation**: Understand limits of agent interaction.

**Methods**:
- Identify repetitive loops (text similarity in consecutive replies)
- Non-sequitur detection (low semantic coherence)
- Refusal patterns ("I can't", "I'm not able")

**Data Needed**: Failed/broken conversation threads

---

## Current Top 30 Submolts Report 🔵

**Question**: What is the current landscape of Moltbook communities?

**Motivation**: Understand where activity is concentrated, what topics dominate.

**Methods**:
- Rank submolts by subscriber count, post volume, comment volume
- Topic analysis: what are top 30 about?
- Network analysis: which submolts share members?

**Data Needed**:
- Submolt metadata (subscribers, descriptions)
- Post/comment distributions by submolt
- Agent multi-membership data

**Note**: If data unavailable via API, request from Varun's OpenClaw agent on gcloud VM.

---

## Prioritization for Hackathon

**Criteria**:
1. **Impact**: Novel, interesting result
2. **Feasibility**: Can complete in ~6-12 hours
3. **Data availability**: Have or can easily get the data
4. **Replicability**: Clean methods, clear code
5. **Shareability**: Good visualization potential

**Proposed Top 3-5 for Hackathon** (TBD after team discussion):
- [ ] TBD
- [ ] TBD
- [ ] TBD

---

**Last Updated**: 2026-03-08
**Next Review**: After completing Step b (scraping data) and Step c (platform survey)
