<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Research articles and documentation on graph community algorithms beyond Leiden for code graphs

There is not yet a widely adopted, purely algorithmic replacement that clearly dominates Leiden on code graphs; instead, recent arXiv work improves Leiden’s performance (parallel and dynamic variants) and embeds it as a component inside richer, often learning-based, community-detection frameworks that could be leveraged for code/dependency graphs. For practical code-graph work, the most promising directions beyond “vanilla” Leiden are (1) high-performance/dynamic Leiden implementations, and (2) hybrid GNN/transformer models that either use Leiden as a teacher or replace modularity with learned clustering objectives while still respecting connectivity.[^1][^2][^3][^4][^6][^7][^8]

Below is a distilled map of what the current arXiv landscape actually offers.

## 1. Faster and dynamic variants of Leiden

These keep the Leiden objective and guarantees but substantially change the implementation and runtime behavior.

- **GVE-Leiden (fast shared-memory Leiden).**
A technical report presents one of the fastest known multicore implementations of Leiden, achieving up to 436× speedup over the original Leiden implementation, 104× over igraph’s Leiden, 8.2× over NetworKit Leiden, and 3× over cuGraph’s GPU Leiden, with throughput around 403M edges/s on a 3.8B-edge graph. This is a direct drop-in for massive graphs, making “Leiden-quality” community detection feasible at web-scale.[^3]
- **Dynamic/Incremental Leiden: ND/DS/DF-Leiden.**
A “Starting Point for Dynamic Community Detection with Leiden” extends three known dynamic strategies (Naive-dynamic, Delta-screening, Dynamic Frontier) to a multicore Leiden, reporting 1.37–1.98× speedups over static Leiden on evolving graphs while maintaining comparable community quality. This is useful when your dependency graph changes in batches and you want to amortize recomputation costs.[^2][^10]
- **HIT-Leiden (Hierarchical Incremental Tree Leiden).**
A more recent paper, “Maintaining Leiden Communities in Large Dynamic Graphs,” analyzes why naive incremental methods can incur essentially unbounded work even for small updates, then introduces HIT-Leiden, which maintains a hierarchical tree structure over Leiden’s supergraphs to bound the affected region per update. On large real-world dynamic graphs it matches state-of-the-art community quality but accelerates updates by up to five orders of magnitude, and they report production deployments that meet strict latency SLAs at high update rates. For something like a live, large code/dependency graph (CI/CD, microservices, or package-level ecosystem), this is the closest thing to a production-grade “Leiden++”.[^4][^11]

**Takeaway for code graphs:** If you like Leiden’s behavior but are hitting performance or dynamism limits, the “improvements” are GVE-Leiden (throughput) and HIT-Leiden / ND-DS-DF Leiden (incremental maintenance), not a change of objective.[^2][^3][^4]

## 2. Learning-based methods that leverage or compete with Leiden

These methods move away from pure combinatorial optimization and embed Leiden into neural pipelines or switch objectives entirely.

### TAS-Com: Leiden as a teacher for a GCN

- **TAS-Com (Topological and Attributive Similarity-based Community detection).**
TAS-Com is a GCN-based method that addresses two issues: (a) GCNs trained to maximize modularity often get stuck in suboptimal partitions, and (b) directly using human-labeled communities may break topological cohesion (disconnected “communities”).[^1]
It uses Leiden in two ways:
    - As a high-quality modularity maximizer to generate community structures used in a novel loss function.
    - To refine human-labeled communities so that each is topologically connected before supervision.[^1]
Experiments show TAS-Com significantly outperforms several state-of-the-art algorithms on multiple benchmarks by balancing modularity against label agreement.[^1]

**Why this is relevant for code graphs:**
You can treat Leiden’s communities on a code graph (e.g., modules, packages, service clusters) as pseudo-labels and train a model that incorporates attributes (types, language constructs, ownership, semantic embeddings) so the learned notion of “community” goes beyond modularity while still inheriting Leiden’s connectivity bias.[^12][^1]

### GIT-CD: GNN + Transformer + clustering (no Leiden inside)

- **Graph Integrated Transformer for Community Detection (GIT-CD).**
GIT-CD combines:
    - A GNN module to capture local graph structure.
    - A transformer module to capture long-range dependencies.
    - A self-optimizing clustering head (K-means + silhouette loss + KL divergence) to refine assignments.[^8]
On benchmark social-network datasets, GIT-CD reportedly outperforms prior models in community-detection quality.[^8]

GIT-CD doesn’t use Leiden; it is effectively a node-embedding + deep clustering pipeline. But methodologically, it points to a pattern: for graphs where long-range relations matter (e.g., call graphs spanning large portions of a codebase), you can move community detection into an embedding space optimized jointly for local and global structure instead of modularity.[^13][^8]

### Surveys: broader design space beyond modularity

- Recent surveys and reviews on community detection and deep graph methods categorize approaches into modularity-based, SBM-based, graphical models, and various deep-learning families (autoencoders, GANs, GCNs).[^14]
They highlight:
    - Stochastic block models and hybrid graphical models as generative alternatives to modularity.
    - Deep representation learning as a way to fuse topology with attributes and then cluster in latent space.[^14]

**Takeaway:**
None of these clearly “dominate Leiden” in a black-box sense on code graphs, but they define two promising augmentation patterns: use Leiden as a teacher (TAS-Com-style) or replace modularity with deep clustering optimized for domain-specific metrics, while still ensuring communities remain connected and interpretable.[^14][^1][^8]

## 3. Community detection specifically on software/code graphs

Here the picture is: everyone uses Leiden (or Louvain) as the baseline; improvements are more about graph construction, edge weighting, and downstream use than about new community algorithms.

### Software ecosystems and dependency graphs

- **PyPI DL package supply chains.**
A recent study builds dependency graphs for TensorFlow and PyTorch sub-ecosystems on PyPI and runs Leiden on pruned graphs, discovering 131 and 100 clusters respectively. They characterize cluster shapes (Arrow/Star/Tree/Forest) and show specialization differences between the two ecosystems. Leiden is the community engine here; the novelty is in how they construct and interpret the graph.[^6]
- **Maven dependency families.**
A TU Delft thesis on “Dependency Families in the Maven Ecosystem” uses both Louvain and Leiden to detect families in a large Maven dependency graph. They note:[^7]
    - Leiden produces better-connected communities and avoids some modularity resolution-limit issues.[^7]
    - However, the empirical improvement over Louvain is modest for their metrics, so they don’t restrict themselves to Leiden only.[^7]
    - More importantly, they find that edge weighting — using a linear combination of parent–child relationships and overlap coefficients rather than either alone — has a much larger effect on community quality than the choice of Louvain vs Leiden.[^7]

**Implication:** For code graphs, how you define edges and weights (e.g., dependency types, co-usage, ref edges, structural similarity) will typically matter more than whether you pick Leiden or a slightly different modularity optimizer.[^6][^7]

### Large code knowledge graphs

- **GraphGen4Code.**
This toolkit builds massive code knowledge graphs (over 2 billion triples from ~1.3M Python files plus related artifacts) intended for search, understanding, and automation tasks. It does not prescribe a specific community algorithm, but its scale demonstrates that you can feasibly apply heavyweight methods (Leiden, SBMs, learned clustering) over large-scale code graphs once constructed.[^12]


### Refactoring and package stability

- A thesis on refactoring software packages models package dependencies as directed graphs extracted from Java bytecode and uses community detection to propose refactoring steps that improve package stability. While the algorithm is not necessarily Leiden, the methodology (community detection → structural refactoring suggestions) is compatible with Leiden and suggests how you could compose a Leiden-based clustering with refactoring heuristics for codebases.[^16]

**Overall:** In code/dependency work, Leiden is used as the baseline community engine; the innovation is mostly in graph modeling, weighting, and downstream interpretation or refactoring.[^16][^6][^12][^7]

## 4. What actually “improves on Leiden” for your use case

From the above, “improvement over Leiden” tends to mean one of the following, rather than a totally new, simple drop-in algorithm:

1. **Same objective, drastically better scalability**
    - GVE-Leiden is the go-to if you’re I/O/CPU bound on huge graphs.[^3]
    - HIT-Leiden and related dynamic methods are the go-to when your graph evolves and you need low-latency updates.[^4][^2]
2. **Same structure guarantees, richer objective via learning**
    - TAS-Com uses Leiden’s communities (and refined human labels) to define a loss that enforces both topological cohesion and attribute similarity, yielding better community detection than either modularity-only GCNs or direct supervised training on raw labels.[^1]
    - This pattern generalizes nicely to code graphs where node attributes (AST nodes, types, ownership, code embeddings) are critical.
3. **New objective class with deep models**
    - GIT-CD and related deep clustering models treat community detection as a representation-learning task, optimized for cluster quality rather than modularity; potentially better when you care more about semantic cohesion than about modularity per se.[^13][^8]
    - Surveys indicate that SBMs, mixed-membership models, and hybrid graphical models can capture overlapping or attribute-rich communities that modularity struggles with.[^14]
4. **Domain-specific graph construction \& weighting**
    - Maven/PyPI work suggests that for software ecosystems, the real gains often come from modeling choices like combining structural relations with usage overlap into edge weights.[^6][^7]
    - For a code graph in your own system, tuning the graph schema and weights (e.g., dependencies, imports, call frequency, dynamic traces) may improve practical utility more than swapping Leiden for a different modularity optimizer.

## 5. Concrete directions you could explore for Gobby/code graphs

Given your use case (code graphs, agents, orchestration), here are some directions that are actually grounded in this literature:

- **If you want drop-in algorithmic upgrades:**
    - Evaluate GVE-Leiden or modern multicore Leiden implementations if your graphs are big enough that igraph’s implementation is a bottleneck.[^3]
    - For streaming or near-real-time code graphs (e.g., project graph updated on each commit), prototype HIT-Leiden-style incremental maintenance instead of recomputing from scratch.[^4][^2]
- **If you want “smarter” communities than modularity:**
    - Use Leiden to generate connected communities on your code/dependency graph, then treat those assignments as pseudo-labels to train a TAS-Com-like GCN that also ingests node attributes and code embeddings.[^12][^1]
    - For code graphs with very long-range relationships, experiment with a GIT-CD-style GNN+transformer encoder and K-means/silhouette loss, using Leiden’s partition as a baseline and evaluation reference.[^8]
- **If you want better practical clusters without ML:**
    - Borrow edge-weighting tricks from the Maven/PyPI work: combine “parent-child” dependency edges with co-usage or overlap metrics, then run Leiden; inspect whether module/package communities line up better with conceptual boundaries.[^6][^7]
- **If you want to go deeper into theory:**
    - Explore SBMs or mixed-membership SBMs for code graphs where overlapping communities (e.g., shared libraries) are common; compare these to Leiden on both modularity and domain metrics like refactoring difficulty or change-coupling.[^14][^16]

***

I generated a longer markdown research note that pulls these references together in a more structured way (background on Leiden, engineering improvements, learning-based methods, and code-graph applications). It’s available as a report artifact you can read alongside the arXiv PDFs themselves.[^1]
<span style="display:none">[^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30]</span>

<div align="center">⁂</div>

[^1]: https://www.arxiv.org/abs/2505.10197

[^2]: https://www.arxiv.org/abs/2312.13936

[^3]: https://arxiv.org/abs/1810.08473

[^4]: https://arxiv.org/pdf/2306.16307.pdf

[^6]: https://arxiv.org/abs/2002.09440

[^7]: https://repository.tudelft.nl/file/File_1af6969f-59a8-4832-8b78-f4462fec8aca

[^8]: https://www.arxiv.org/abs/2601.04367

[^10]: https://leidenalg.readthedocs.io/en/latest/reference.html

[^11]: https://search.r-project.org/CRAN/refmans/igraph/html/cluster_leiden.html

[^12]: https://arxiv.org/abs/2405.11658

[^13]: https://arxiv.org/html/2405.11658v1

[^14]: https://arxiv.org/pdf/2601.08554v4.pdf

[^16]: https://arxiv.org/abs/2601.08554

[^17]: http://arxiv.org/pdf/2309.11798.pdf

[^18]: https://www.arxiv.org/pdf/2101.01669v2.pdf

[^19]: https://arxiv.org/abs/2412.10164

[^20]: https://arxiv.org/abs/2109.03341

[^21]: https://arxiv.org/html/2406.11912v2

[^22]: https://arxiv.org/pdf/1811.10171.pdf

[^23]: https://arxiv.org/abs/2406.08098

[^24]: http://www.arxiv.org/abs/0906.0612

[^25]: https://github.com/vtraag/leidenalg/blob/main/doc/source/intro.rst

[^26]: https://cse.iitkgp.ac.in/~bivasm/cnt_notes/community_review.pdf

[^27]: https://arxiv.org/abs/1704.05826

[^28]: https://www.arxiv.org/pdf/2512.02460.pdf

[^29]: https://arxiv.org/pdf/2406.11912.pdf

[^30]: https://github.com/pitsianis/Leiden.jl
