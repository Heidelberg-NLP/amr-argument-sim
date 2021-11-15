# Argument Similarity with AMR

AMR Data and AMR metric implementation description for our paper [Explainable Unsupervised Argument Similarity Rating with Abstract Meaning Representation and Conclusion Generation](https://aclanthology.org/2021.argmining-1.3/), presented at ArgMining 2021.

## Data

For the data, generated conclusions, and AMR parses see `data/`.

## Computing AMR metrics

1. Clone [this repo](https://github.com/flipz357/amr-metric-suite). S2match is denoted "standard" in our paper. For "concept-focused" and "structure focus", (very) few changes are necessary in s2match.py (essentially adding a scalar multiplication and normalisation in compute pool function).

2. Compute pairwise similarity for conclusion pairs and premise pairs. We recommend a high cutoff parameter (e.g., 0.95 as in the paper), to allow score increases only for (near-)paraphrasal concepts.

```
cd amr-metric-suite/py3-Smatch-and-S2match/smatch/
python s2match.py -f <firstamrfile> <secondamrfile> -cutoff 0.95 --ms
```

Note I: S2match is only a small change to its ancestor Smatch (which is more or less S2match with cutoff=1.0), so Smatch will generally return similar results.

Note II: Potentially useful graph alignments can be obtained by adding one or two lines in `s2match.py` main function (the alignment is contained in `best_mapping`).

## Evaluate similarity via classification

1. mix similarities with lambda=0.95.

2. Evaluate against human scores, as contained in `data/UKP_aspect.tsv`. Macro F1: a) fuse 4-way labels to binary label (as described in [Reimers et al. 2019](https://arxiv.org/abs/1906.09821)), then b) use cross-val as described in Reimers for threshold (as also described in Reimers et al). For other evaluation metrics, Pearsonr, Spearmanr, etc. computation is straightforward.

See the example by running

```
cd scripts
./evaluate_all.sh
```


## Help

Please file an issue or contact me [via mail](opitz@cl.uni-heidelberg.de?subject=[GitHub]%Argument%AMR%similarity)
