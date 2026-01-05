# Epistemic-Canon-Network-Analyzer
Epistemic Canon Network Analyzer
A reproducible framework for the analysis of citation networks and epistemic regimes in Scopus bibliometric data.
# Description: 
This package implements topometric methods to analyze the structure of academic fields through internal citation networks. It facilitates the mapping of symbolic capital and the identification of structural positions within a given scientific discourse.
# Key Analytical Capabilities: 
- ** Canonical Regimes: Characterization of epistemic power structures using network density and clustering coefficients to determine the degree of field consolidation.
- ** Gatekeepers ("Established"): Identification of nodes with high in-degree centrality, representing authors who command significant internal recognition and define the "orthodoxy" of the field.
- ** "Adventurer" Authors: Identification of researchers with high out-degree (high synthesis of existing knowledge) but low in-degree, signaling potential heterodox or emerging contributions that have yet to be canonized.
# Epistemic Inequality: 
- Quantitative measurement of the distribution of symbolic capital within the network using the Gini Coefficient applied to citation distributions.
- Emerging Topics: Longitudinal analysis using TF-IDF vectorization to isolate terms that appear in recent corpora but are absent in historical foundations.
# Installation
# # Core Requirements:
To ensure a reproducible environment (optimized for Google Colab or local Python distributions), the following scientific stack is required:Data Manipulation: pandas, numpyNetwork 
python >= 3.8
pandas >= 1.3.0
numpy >= 1.21.0
networkx >= 2.6.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
scikit-learn >= 0.24.0
scipy >= 1.7.0
openpyxl >= 3.0.0
# Quick Start:
# Clone the repository
git clone https://github.com/your-username/epistemic-canon-analyzer.git
cd epistemic-canon-analyzer

# Install dependencies
pip install -r requirements.txt
# Analysis: 
networkxStatistical Validation: scipyVisualization: matplotlib, seabornNatural Language 
Processing: scikit-learn (for TF-IDF extraction)

# Basic Usage
Minimum Example:
from epistemic_canon_analyzer import EpistemicCanonAnalyzer

# Initialize with Scopus data
analyzer = EpistemicCanonAnalyzer('scopus_export.csv')

# Generate complete analysis report
analyzer.generate_full_report(output_dir='./results')

# Step-by-Step Analysis
1 Build Network: Construct the citation network from internal references.

2 Calculate Metrics: Compute density, clustering, and degree distributions.

3 Validation: Correlate internal in-degree with official Scopus citation counts.

4 Identify Roles: Extract "Gatekeepers" and "Adventurer" authors.

5 NLP Analysis: Extract emerging topics using TF-IDF.

# Input Data Format
The analyzer requires a Scopus CSV export with the following columns:

| Column     | Description                    | Required       |
| ---------- | ------------------------------ | -------------- |
| EID        | Scopus EID (unique identifier) | ✅              |
| Title      | Document title                 | ✅              |
| Authors    | List of authors                | Recommended    |
| Year       | Year of publication            | Recommended    |
| References | Full bibliographic references  | ✅              |
| DOI        | Digital Object Identifier      | Optional       |
| Abstract   | Document abstract              | Optional       |
| Cited by   | Number of citations (Scopus)   | For validation |

# Theoretical Foundations:
The framework operationalizes concepts from the sociology of scientific knowledge, specifically:

- Mertonian Cumulative Advantage: The "Matthew Effect" ($k_{in}$ distribution).
- Bourdieu’s Scientific Field: The struggle for the monopoly of scientific authority.
- Epistemic Closure: Measured through network density ($\delta$) and the clustering coefficient ($C$).

# Citation
@software{epistemic_canon_analyzer,
  author = {María Dolores González Barbado},
  orcid =  {0000-0002-4213-2090},
  title = {Epistemic Canon Network Analyzer},
  year = {2025},
  url = {https://github.com/your-username/epistemic-canon-analyzer},
  version = {1.0.0}
}

# Use Cases
## Academic field analysis
- Identify central and marginal authors
- Detect fragmentation or consolidation
- Evaluate temporal thematic diversity
## Bibliometric studies
- Complement traditional bibliometric indicators
- Compare internal vs. external citations
- Analyze collaboration patterns
- Track paradigm shifts over time

# License
Distributed under the MIT License.

# Author
Name: [María Dolores González Barbado]

Email: mgonzalezbarbado@uoc.edu

ORCID: [0000-0002-4213-2090]

GitHub: @missmew33

# Note: this project is part of my PhD Doctoral Thesis at UOC University @uoc
