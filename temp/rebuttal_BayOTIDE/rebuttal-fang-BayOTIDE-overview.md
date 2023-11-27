# Author Response- Clarifications

We thank all reviewers for their careful reading, and detailed and considerate feedback. We are glad to see that almost all reviewers agree that **BayOTIDE** is a well-motivated  work with solid formulation.  

The following are the general clarifications for the reviewers' comments. We also provide detailed responses to each comment in the following sections.

### **1. Novelty and contribution on time series imputation side** 

Though the factorization-based imputation methods are widely appled in general machine learning, like Bayesian PCA and tensor decomposition, and matrix factorization, they are rarely applied in time series imputation. In our knowledge, the most recent work to apply this for time series imputation is **TIDER**[Liu et al., ICLR 2022], which is a matrix factorization-based formulation. The gap there is because:

- Tranditioonal time series models cares more on capturing the temporal dependency, instead of the **cross-channel dependency** and **low-rank structure**. 
  
- Directly applying factorization-based imputation to time series imputation is not feasiable. The time series data is with **inherent temporal continuity**, which is not considered in the factorization-based methods. For example, directly applying Bayesian PCA to time series can not guarantee the learned factors are smooth over time mode.
Even the most recent work **TIDER**, which is a matrix factorization-based formulation, can not guarantee the temporal continuity of the learned trend factors, nor extend to the continuous and functional manner. 

- In short, **it's non-trivial to model a low-rank factorization with constrains of temporal continuity** for applying classical imputation methods in multivar time series.
  
Thus, the proposed method **BayOTIDE** is the **first work to perfectly bridge the gap of low-rank representation and temporal continuity under probabilistic framework**. Firstly, the facorization imputation ensure its scalability and efficiency, even for time series with thousands of channels. Secondly, the usage of state-sapce GP naturally models the temporal dependency in a continuous and functional manner, even allowing Bayesian online inference. 


### **2. Novelty and contribution on Bayesian learning side**

We acknowledge that the fundamental 
Bayesian learning tools used in **BayOTIDE**, like state-space GP, conditional moment-matching, are mature techniques. However, they do not naturally fit in time series imputation. Specifically,

- The state-space GP, along with the Kalman filter, is designed for cases where **one observation cooresponds one latent dynamic**. However, in BayOTIDE, **one observation cooresponds to multiple latent dynamics(components)**. 

- The CEP, is orginally designed for cases where we observe **one obsevation** and then do **entry-wise conditional moment matching**. However, in BayOTIDE, as we observe **batch of observations** every time(values at different channels), we need to enxtend it to handle **batch-wise conditional moment matching**. 

Thus, we  have modified the original CEP to handle the batch-wise moment-matching (eq 9, 32), merging the approx. messages from different channels (eq 10, 11), and then feed latent message factors—alinged with the "observations" in standard state-space model/KF— to the component-wise Kalman filter (eq 12), and update the multiple latent dynamics in a synchronous way. In our knowledge, this is the **first online Bayesian inference framework for multivariate time series**, and it's **quiet different from the original CEP and state-space GP, nor any existing Bayesian learning methods**


###  **3. Experiment Setting**

We thank all the reviewers for their suggestions on enhancing the experiment setting by more baselines, metrics and
 ablation studies. We do agree that the experiment setting can be further improved.

 However, we would like to point out that the **main contribution of our work is on the methodological and formulation side**, which is the **first online Bayesian method** for multivariate time series. We follow the most recent work in this field: **CSDI** [ Tashiro, Neurips 2021],  **CSBI** [Chen, ICML 2022],  **TIDER** [Liu, ICRL 2023] to set up the experiment setting,  and think that the comprarion with the most **offline baselines** is sufficient to show the **effectiveness of the BayOTIDE**. 

 We also add some new experiments based on the reviewers' comments:
 
 - The comparison with single state-space model.
 - The comparison with linear + periodic kernel multi-output GP.
 - The numeinical comparison of the model size between **BayOTIDE** and **CSDI**. 

