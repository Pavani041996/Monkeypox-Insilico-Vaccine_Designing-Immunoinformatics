# Monkeypox-Insilico-Vaccine_Designing-Immunoinformatics
# End-to-end computational vaccine design pipeline
# In-Silico Multi-Epitope Vaccine Design Against Monkeypox Virus
# ## Project Status
🚧 Ongoing Project

# This project is currently under active development. Initial stages including epitope prediction and vaccine construct design are completed. Structural modeling (I-TASSER) and downstream validation are in progress.
# This project demonstrates an end-to-end immunoinformatics pipeline for vaccine design, with ongoing efforts in structural modeling and validation.

## Overview
This project focuses on designing a multi-epitope vaccine candidate against Monkeypox virus using immunoinformatics and computational biology approaches.

The workflow integrates epitope prediction, antigenicity screening, and vaccine construct design to identify potential vaccine targets.

## Objectives
- Identify potential antigenic proteins
- Predict CTL, HTL, and B-cell epitopes
- Filter epitopes based on antigenicity, allergenicity, and toxicity
- Design a multi-epitope vaccine construct

## Methods
- Sequence retrieval from NCBI
- Antigenicity prediction using VaxiJen
- Epitope prediction using IEDB tools
- Allergenicity assessment using AllerTOP
- Toxicity prediction using ToxinPred
- Vaccine construct design with linkers and adjuvants

# ## Workflow

1. **Sequence Retrieval**
   - Viral protein sequences were obtained from NCBI GenBank.

2. **Antigenicity Screening**
   - Proteins were screened using VaxiJen to identify potential antigenic targets.

3. **Epitope Prediction**
   - CTL epitopes predicted using NetMHCpan (IEDB)
   - HTL epitopes predicted using IEDB MHC-II tools
   - B-cell epitopes predicted using BepiPred

4. **Epitope Filtering**
   - Antigenicity assessment (VaxiJen)
   - Allergenicity prediction (AllerTOP)
   - Toxicity prediction (ToxinPred)

5. **Epitope Selection**
   - High-scoring, non-allergenic, non-toxic epitopes were selected

6. **Vaccine Construct Design**
   - Selected epitopes linked using appropriate linkers (AAY, GPGPG, KK)
   - β-defensin used as an adjuvant

7. **Structural Modeling (Ongoing)**
   - 3D structure prediction using I-TASSER
   - Model validation and refinement pending
  
## Key Results
- Identified high-confidence antigenic epitopes
- Selected non-allergenic and non-toxic peptides
- Designed multi-epitope vaccine construct
- Integrated immune-relevant epitopes for broad response

## Tools & Technologies

- **Sequence Databases:** NCBI GenBank  
- **Antigenicity:** VaxiJen v2.0  
- **Epitope Prediction:** IEDB (NetMHCpan, BepiPred)  
- **Allergenicity:** AllerTOP  
- **Toxicity:** ToxinPred  
- **Structural Modeling:** I-TASSER (ongoing)  
- **Programming:** Python (data filtering), basic scripting  

## Partial Results

- Identified multiple antigenic proteins with high VaxiJen scores  
- Predicted CTL, HTL, and B-cell epitopes using IEDB tools  
- Filtered epitopes based on:
  - High antigenicity scores
  - Non-allergenic properties
  - Non-toxic profiles  

- Final shortlisted epitopes show strong potential for immune activation  
- Designed a preliminary multi-epitope vaccine construct incorporating selected epitopes and linkers  

- Structural modeling using I-TASSER has been initiated; model refinement and validation are currently in progress...

## Key Highlights

- Integrated immunoinformatics pipeline for rational vaccine design  
- Multi-layer filtering ensures biological relevance of selected epitopes  
- Designed a multi-epitope construct targeting both cellular and humoral immunity
- 
## Limitations
- Structural validation and docking studies are pending  
- Experimental validation required for clinical applicability

## Future Work
- Structural modeling (3D protein structure)
- Molecular docking with immune receptors
- MD simulations and validation

## Author
Pavani Annambhotla
