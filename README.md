# Exploring Similarity Structures of Documents through Topic Modeling with Latent Dirichlet Allocation and Vector Space Embeddings

The goal of this project is to perform deep comparison of different techniques used for topic identification in Y Combinator (YC) investment data, specifically company descriptions as well as to explore a new technique. The two traditional methods, hierarchical Bayesian models like LDA and clustering based on embedding in a vector space, were found to have limitations. LDA struggles with short texts and identifying main topics when reviews are not coherent, while word co-occurrence-based methods like LDA may fail due to the context-based nature of company descriptions. As a solution, a new technique was experimented with that uses embedding plus clustering to cluster similar topics based on vector representations of the full content of sentences. In this paper we explore different methods for vector representation, including TD-IDF, BERT sentence embedding, and the final method, contextual topic embedding (LDA + BERT). The model was evaluated using coherence in topic modeling and the silhouette score for clustering. The results showed that the contextual topic identification method was the most effective for the YC investment dataset.

## Dataset

Y Combinator investment from 2005 to 2019 - https://www.kaggle.com/datasets/krzysztofpiat/y-combinator-investment-from-2005-to-2019

## References

[1] Ercan Atagün, Bengisu Hartoka, and Ahmet Albayrak. Topic modeling using lda and bert techniques: Teknofest example. In 2021 6th International Conference on Computer
Science and Engineering (UBMK), pages 660-664, 2021.<br />
[2] David M. Blei, A. Ng, and Michael I. Jordan. Latent dirichlet allocation. J. Mach. Learn.Res., 3:993 1022, 2001.<br />
[3] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In Proceedings
of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers),
pages 4171-4186, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics.<br />
[4] Krzysztof Piªat. Y combinator investment from 2005 to 2019, Nov 2019.<br />
[5] Michael Röder, Andreas Both, and Alexander Hinneburg. Exploring the space of topic coherence measures. In Proceedings of the eighth ACM international conference on Web search and data mining, pages 399-408, 2015.<br />
[6] Rita Sevastjanova. Explained, Apr 2016.<br />
[7] Steve Shao. Contextual topic identication, Mar 2020.<br />
[8] Shaheen Syed and Marco Spruit. Full-text or abstract? examining topic coherence scores using latent dirichlet allocation. In 2017 IEEE International Conference on Data Science and Advanced Analytics (DSAA), pages 165-174, 2017.<br />
