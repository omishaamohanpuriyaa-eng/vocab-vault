#  Vocab Vault - Bidirectional Semantic Lexicon

A lightweight, bidirectional vocabulary graph engine built in Python and Streamlit to assist learners in connecting everyday phrases to nuanced, advanced academic vocabulary.

---

##  The Problem
When learning nuanced vocabulary (e.g., discovering that **"akin to"** means **"similar to"** or **"related to"**), traditional dictionaries only provide one-way definitions. This project models vocabulary as an undirected graph, ensuring that mapping Term A to Term B automatically enables reverse lookup from Term B to Term A.

##  Core Technical Features
- **Bidirectional Adjacency Mapping:** Automatically manages symmetrical adjacency lists in constant average time $\mathcal{O}(1)$.
- **Dynamic Session State:** Real-time search matching and instant graph updates.
- **Streamlit Web Interface:** Responsive web client deployable to any browser.

##  Local Installation