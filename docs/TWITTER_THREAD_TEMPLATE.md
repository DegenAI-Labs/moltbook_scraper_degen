# Twitter Thread Template

Template for sharing findings in Dimitrios Papaillopoulos style.

---

## Thread Structure

**Tweet 1: Hook**
🧵 New results on [Platform]: [Surprising finding]

We analyzed [N agents/posts/comments] from [platform/timeframe] and found [punchline].

Quick thread 👇

---

**Tweet 2-3: Context**
Background: [Brief context on what we're studying]

Building on @[DavidHoltz or relevant researcher]'s work showing [baseline finding], we asked: [our research question]

[Optional: Include screenshot/image of platform or motivation]

---

**Tweet 4-6: Key Findings** (1 finding per tweet)
**Finding 1**: [Punchline sentence]

[Embed visualization]

[1-2 sentences of interpretation]

---

**Finding 2**: [Punchline sentence]

[Embed visualization]

[1-2 sentences of interpretation]

---

**Finding 3**: [Punchline sentence]

[Embed visualization]

[1-2 sentences of interpretation]

---

**Tweet 7-8: Methods & Replicability**
Methods: [Brief description of approach]

Sample: N = [value] [agents/posts/comments]
Time period: [dates]
Analysis: [key technique]

All code & data available: [GitHub link]

---

**Tweet 9: Comparison/Context**
How does this compare to [human networks / other platforms / expectations]?

[Key comparison statistic or insight]

[Optional: Small comparison visualization]

---

**Tweet 10: Implications**
Why this matters: [2-3 sentences on implications]

Open questions:
- [Question 1]
- [Question 2]

---

**Tweet 11: Credits & Links**
Collaboration with @[Emmy], @[Rose], and @[others]

Enabled by coding agents (Claude Code) - this kind of rapid exploration wasn't feasible before.

📊 Replication package: [GitHub link]
📄 Full writeup: [Blog/Notion link]

/end

---

## Example Thread (Hypothetical)

**Tweet 1**:
🧵 New results on Moltbook (AI-agent social network): Agents exhibit *faster* meme diffusion than humans—but with 10x less semantic drift.

We analyzed 50k posts from 3k agents over 10 days. Quick thread 👇

**Tweet 2**:
Background: Moltbook is a Reddit-like platform where ONLY AI agents post, comment, and form communities.

@davidholtz's seminal paper showed shallow conversations and templated content. We asked: how do ideas spread?

**Tweet 3**:
**Finding 1**: Viral phrases spread 3.2x faster on Moltbook than on Reddit (median time-to-peak: 4 hours vs 13 hours).

[Plot: Diffusion curves comparing Moltbook vs Reddit]

Agents don't sleep—posting is 24/7, accelerating cascades.

**Tweet 4**:
**Finding 2**: But Moltbook memes stay *on-topic*. Semantic drift (measured via sentence embeddings) is 0.08 vs 0.82 on Reddit.

[Plot: Coherence decay over diffusion hops]

Agents don't inject personal tangents—they template and replicate.

**Tweet 5**:
**Finding 3**: Top 5% of agents account for 71% of meme initiations—even more concentrated than human influencers (42% on Twitter).

[Plot: Lorenz curve of meme origination]

Agent popularity compounds faster due to algorithmic consistency.

**Tweet 6**:
Methods:
- Burst detection (Kleinberg) for emerging phrases
- Diffusion trees (reply chains)
- Semantic similarity (Sentence-BERT)

N = 50,314 posts, 3,147 agents
Time: Jan 27 - Feb 6, 2026

Code: github.com/[repo]/findings/meme_diffusion.ipynb

**Tweet 7**:
Why this matters: Agent networks exhibit *hyper-efficient* information spread but *low creativity*.

This could be useful (rapid coordination) or problematic (echo chambers, misinformation cascades).

Open Qs: Do multi-agent owners coordinate? Can we detect manipulation?

**Tweet 8**:
Collaboration with @EmmyLiu, @RoseHuang, @DegenAILabs

Enabled by Claude Code—we went from raw scrape to full analysis in 48 hours. The Papaillopoulos model of rapid research dissemination works!

📊 Replication: github.com/[repo]
📄 Writeup: [link]

/end

---

## Visualization Best Practices

**For Twitter**:
- High-resolution PNG (min 1200px width)
- Clear axis labels (readable on mobile)
- Minimal text on plot (put context in tweet)
- Use colorblind-friendly palettes
- Annotate key points directly on plot
- Save as 16:9 or 4:3 aspect ratio (Twitter-friendly)

**R Code for Twitter-Ready Plots**:
```r
library(ggplot2)
library(scales)

# Set high DPI
ggsave("plot.png", width = 8, height = 5, dpi = 300)

# Use large text
theme_set(theme_minimal(base_size = 16))

# Colorblind-friendly palette
scale_color_brewer(palette = "Set2")
```

**Python Code for Twitter-Ready Plots**:
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_context("talk")  # Larger text
plt.figure(figsize=(10, 6), dpi=300)

# Save high-res
plt.savefig("plot.png", dpi=300, bbox_inches='tight')
```

---

## Hashtags to Consider

- #AIResearch
- #AgenticAI
- #Moltbook
- #ComputationalSocialScience
- #NetworkScience
- #NLP
- #MachineLearning

**Don't overuse**: 2-3 hashtags max, only in final tweet.

---

**Last Updated**: 2026-03-08
