---
source_kind: url
source_url: "https://en.wikipedia.org/wiki/Mean_reciprocal_rank"
requested_url: "https://en.wikipedia.org/wiki/Mean_reciprocal_rank"
canonical_url: "https://en.wikipedia.org/wiki/Mean_reciprocal_rank"
fetched_at: "unix-ms:1781061435404"
source_hash: 9171ba1efd048efb173b905d98d14230b0afa37e88c9c5940cf222d6099db8df
content_type: "text/html; charset=UTF-8"
---

# Mean reciprocal rank - Wikipedia

Jump to content

Main menu

move to sidebar

hide

Navigation

Main pageContentsCurrent eventsRandom articleAbout WikipediaContact us

Contribute

HelpLearn to editCommunity portalRecent changesUpload fileSpecial pages

Search

Appearance

Donate

Create account

Log in

Personal tools

Donate

Create account

Log in

Contents

move to sidebar

hide

(Top)

1

Example

2

See also

3

References

Toggle the table of contents

Mean reciprocal rank

4 languages

فارسیItalianoРусский中文

Edit links

ArticleTalk

English

ReadEditView history

Tools

move to sidebar

hide

Actions

Read

Edit

View history

General

What links hereRelated changesUpload filePermanent linkPage informationCite this pageGet shortened URL

Print/export

Download as PDFPrintable version

In other projects

Wikidata item

Appearance

move to sidebar

hide

From Wikipedia, the free encyclopedia

Search quality measure in information retrieval

This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.Find sources: "Mean reciprocal rank" – news · newspapers · books · scholar · JSTOR (June 2007) (Learn how and when to remove this message)

The mean reciprocal rank is a statistic measure for evaluating any process that produces a list of possible responses to a sample of queries, ordered by probability of correctness. The reciprocal rank of a query response is the multiplicative inverse of the rank of the first correct answer: 1 for first place, 1⁄2 for second place, 1⁄3 for third place and so on. The mean reciprocal rank is the average of the reciprocal ranks of results for a sample of queries Q:[1][2]

MRR

=

1

|

Q

|

∑

i

=

1

|

Q

|

1

rank

i

.

{\displaystyle {\text{MRR}}={\frac {1}{|Q|}}\sum _{i=1}^{|Q|}{\frac {1}{{\text{rank}}_{i}}}.\!}

where

rank

i

{\displaystyle {\text{rank}}_{i}}

refers to the rank position of the first relevant document for the i-th query.

The reciprocal value of the mean reciprocal rank corresponds to the harmonic mean of the ranks.

Example[edit]

Suppose we have the following three queries for a system that tries to translate English words to their plurals. In each case, the system makes three guesses, with the first one being the one it thinks is most likely correct:

Query

Proposed Results

Correct response

Rank

Reciprocal rank

cat

catten, cati, cats

cats

3

1/3

torus

torii, tori, toruses

tori

2

1/2

virus

viruses, virii, viri

viruses

1

Given those three samples, we could calculate the mean reciprocal rank as

(

1

/

3

+

1

/

2

+

1

)

/

3

=

11

/

18

{\displaystyle (1/3+1/2+1)/3=11/18}

, or approximately 0.61.

If none of the proposed results are correct, the reciprocal rank is 0.[1] Note that only the rank of the first relevant answer is considered, and possible further relevant answers are ignored. If users are also interested in further relevant items, mean average precision is a potential alternative metric.

See also[edit]

Information retrieval

Question answering

References[edit]

^ a b E.M. Voorhees (1999). "Proceedings of the 8th Text Retrieval Conference" (PDF). TREC-8 Question Answering Track Report. pp. 77–82.

^ D. R. Radev; H. Qi; H. Wu; W. Fan (2002). "Evaluating web-based question answering systems" (PDF). Proceedings of LREC.

vteMachine learning evaluation metricsRegression

MSE

MAE

sMAPE

MAPE

MASE

MSPE

RMS

RMSE/RMSD

R2

MDA

MAD

Classification

F-score

P4

Accuracy

Precision

Recall

Kappa

MCC

AUC

ROC

Sensitivity and specificity

Logarithmic loss

Clustering

Silhouette

Calinski–Harabasz index

Davies–Bouldin index

Dunn index

Hopkins statistic

Jaccard index

Rand index

Similarity measure

SMC

DBCV index

Ranking

MRR

NDCG

AP

Computer vision

PSNR

SSIM

IoU

NLP

Perplexity

BLEU

MAUVE

Deep learning

Inception score

FID

Recommender system

Coverage

Intra-list similarity

Similarity

Cosine similarity

Euclidean distance

Pearson correlation coefficient

Confusion matrix

<img src="https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&amp;type=1x1&amp;usesul3=1" alt="" width="1" height="1" style="border: none; position: absolute;">

Retrieved from "https://en.wikipedia.org/w/index.php?title=Mean_reciprocal_rank&oldid=1218582630"

Categories: Summary statisticsInformation retrieval evaluationHidden categories: Articles with short descriptionShort description matches WikidataArticles needing additional references from June 2007All articles needing additional references

This page was last edited on 12 April 2024, at 15:42 (UTC).

Text is available under the Creative Commons Attribution-ShareAlike 4.0 License;

additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

Privacy policy

About Wikipedia

Disclaimers

Contact Wikipedia

Legal & safety contacts

Code of Conduct

Developers

Statistics

Cookie statement

Mobile view

Search

Toggle the table of contents

Mean reciprocal rank

4 languages

Add topic
