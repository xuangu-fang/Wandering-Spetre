# for reviewer FPUc (8/4)
We thank reviewer for the careful review and constructive suggestion—especially the suggestion on highlighting and elaborating the novelty of the proposed method in theoretical and methodological aspects. 

**We follow your suggestion and make a response overview to highlight the novelty and contribution of the proposed method**, which is the top-level post in this forum.  **we regularly refer to the response overview, which is the top-level post in this forum**. We address the comments below:

>C1:" Section 3.2 does not seem to play any role. It looks hardly related."

R1: The state-space GP we introduced in section 3.2  actually plays a key role in the proposed method. We use that state-space GP to model the trend and seasonal components in a continuous and functional manner with linear time cost. The chain structure of the state-space GP also enables the online learning with KF. Specifically, we have to use the chain-structured prior (eq 2 in section 3.2) to replace the full GP prior (eq 7 in section 4.2) in the proposed method (the paragraph under eq7). We apologize for the unclear presentation and will added statements to highlight the role of the state-space GP in the proposed method.

>C2: "Improve presentation quality"

R2: Thanks for the suggestion! We will polish the presentation quality in the revised version. Acutally, it's the fist time we submit this paper to peer-reviewed conference, so we are pretty grateful to get your valuable feedback and will continue to improve the presentation quality in the future :) 


>C3:  "How does the well-known non-identifiability with respect to the unitary transformation in the UV-factorization form (1) take effect on the result?"

R3: Good point! We do acknowledge that non-identifiability of unitary transformation will make learned components(V) and weights(U) lose the nice properties of uniqueness. However, we argue that the losing of non-identifiability is not a big issue in our case. The reason is that the components(V) is assigned with functional priors (GP), and doomed to be non-linear and periodic. Then, even the non-identifiability effect takes place, saying the components(V) are not match the right "scale" but still have the right "shape", the weights(U) will be able to compensate the "scale" effect. Actually, in our simulation study(Section 5.1), we do observe the non-identifiability effect, but when combining learned components(V) and weights(U), we could still get the right trend and seasonal components with the weights (Figure 1, (b)-(e)). We will add statements to clarify this point in the revised version.

>C4: "I am not clear how the almost linear trend could be separated in the result presented in Fig.1. How did the kernel expansion with the GPs produce the linear-looking trend component? What is the intuition behind it?"

R4: Good question! The short answer is that the seperation of linear trend is not learned by the GP, but by the weights(U). Specifically, we set four GP components for $V(t)$ in the simulation study, and the first component is a Matern kernel, and the last three components are periodic kernels. Thus, the seperated linear trends shown in Figure 1 (b)-(e) are actually from one GP kernel (Matern kernel), but with four different weights(U). The intuition behind it is that the different channels of dynamics may share similar trend components, but with different weights. The message passing algorithm in the proposed method is able to learn the channel-wise weight precisely with conditional moment-matching. 

>C5: "Elaborate Bayesian PCA-based imputation and highlight novelty compared with existing methods."

R5: Great point! We just follow your suggestion and add general statements to highlight the novelty of the proposed method in the response overview. Please refer sections **Novelty and contribution on time series imputation side** and  **Novelty and contribution on Bayesian learning side** in the response overview. 

# for reviewer CYA1 (3/2)

Thanks for your comments. Here are our responses. C: comments; R: response.

> C1:"unclear and insufficient descriptions"

R1: Could you please specify which part is unclear and insufficient? We will gladly add statements to clarify the unclear and insufficient parts.

> C2:  "Unclear theoretical support."

R2: The factorization-based formulation of the proposed method is alinged with Bayesian PCA[1], which is a well-known and classical Bayesian method with theoretical support.  The state-space GP prior[2] is known to be highly flexible/expressive for function estimation and has been used in numerous applications, include time series modeling [3]. The EP based inference[4] is also a well-known approximate inference method with theoretical gaurentee on provably convergence. Thus, the proposed method is well-supported by the theoretical results of the above methods.

[1] Bishop, Christopher. "Bayesian pca." Advances in neural information processing systems 11 (1998).
[2] Rasmussen, Carl Edward. "Gaussian processes in machine learning." Summer school on machine learning. Berlin, Heidelberg: Springer Berlin Heidelberg, 2003. 63-71.
[3] Roberts, Stephen, et al. "Gaussian processes for time-series modelling." Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 371.1984 (2013): 20110550.
[4]:Minka, Thomas P. "Expectation propagation for approximate Bayesian inference." arXiv preprint arXiv:1301.2294 (2013).



# for reviewer SiJc (5/3):

> C1: Typos and presentation.

R1: Thanks for the suggestion! We will polish the presentation quality in the revised version. 

> C2: Comparison with online univariate & probabilistic imputation models （state-space model with Kalman filtering）

R2: Good suggestion! We add the comparison with single state-space model (**single-SS**) with Kalman filtering on *traffic-guangzhou* The results are shown in the following table:

| Observed-ratio=70% | RMSE | MAE | CRPS |
| ------ | ---- | --- | --- | 
| **BayOTIDE** | 3.724 | 2.611 |  0.053 | 
| **single-SS** | 5.152 | 4.691 |  0.132 | 

| Observed-ratio=50% | RMSE | MAE | CRPS |
| ------ | ---- | --- | --- | 
| **BayOTIDE** | 3.820 | 2.687 |  0.055 | 
| **single-SS**| 5.558 | 4.821 |  0.173 | 

It's clear that the **single-SS** model is much worse than the proposed method. The reason is that the **single-SS** model is not able to capture the cross-channel dependency, which is crucial for multivariate time series imputation.

> C3: Add multivariate metrics (e.g., energy score [1] and sum CRPS [2])

R3: We do agree that the multivariate metrics are more informative than univariate metrics, but we clarify that the *energy score*[1] will reduce to the *CRPS* ($\beta=m=1$) and *RMSE* ($\beta=2$), which are already included in the paper. For the *sum CRPS* used in [2], it seems to be the sum over the CRPS over all evaluation points. As we report the mean of the CRPS over all evaluation points, the *sum CRPS* will have the same effect as the *CRPS* in our case. However, we do agree that multivariate metrics may help to better understand the performance under multivariate setting, and will investigate it in the future work. 


[1] Gneiting, Tilmann, and Adrian E. Raftery. "Strictly proper scoring rules, prediction, and estimation." Journal of the American Statistical Association 102.477 (2007): 359-378.
[2] Kan, K., Aubet, F. X., Januschowski, T., Park, Y., Benidis, K., Ruthotto, L., & Gasthaus, J. (2022, May). Multivariate quantile function forecaster. In International Conference on Artificial Intelligence and Statistics， 2022

> C4: Add model size discussion

R4: Good point! We take the *traffic-guangzhou* dataset(size: 213 channels, 500 timestamps) as an example, and show the model size comparaion of *BayOTIDE* and *CSDI*[1]—the state-of-the-art probabilistic imputation method.  

 As *BayOTIDE* is a factorization-based method, the model size is determined by the number of components.. Corrsponding to the hyper-parameter setting in Table 4, we set $D_r + D_s = 40$ components. Then the weights U's size is $40 \times 213$, and the components V's size is $40 \times 500 \times 2$(the mean and diag var). Thus, the total model size is $40 \times (213+500 + 500) = 48520$.

*CSDI* is a diffusion-based method, the model size training memory is determined by the number of diffusion steps and the structure of the deep-based score estimator. The default  structure *CSDI*'s(Figure 6 in CSDI paper) includes temporal-feature transformer with 5 layers and 8 heads and fully connected layes . The parameters also incude the embedding(dim=128) of timestamps and features, and the diffusion step embedding. Thus, the total model size is at least $5 \times 16 \times 2 \times (500*3+128*3) +  128 \times (213 + 500) =  388224$. 

Thus, the model size of *BayOTIDE* is much smaller than *CSDI*. The performance gain of *BayOTIDE* over *CSDI* is mainly due to the factorization-based formulation, not the model size. In the *TIDER* paper[2], which take the similar factorization formulation with *BayOTIDE*, the authors reportred the memory usage of TIDER and CSDI (Figure 4 in TIDER paper). The memory usage of TIDER is much smaller than CSDI.

[1]: Tashiro, Yusuke, et al. "Csdi: Conditional score-based diffusion models for probabilistic time series imputation." Advances in Neural Information Processing Systems 34 (2021): 24804-24816.

[2]: LIU, SHUAI, et al. "Multivariate Time-series Imputation with Disentangled Temporal Representations." The Eleventh International Conference on Learning Representations. 2022.


# for reviewer  PJoe (3/3):

Thanks for your comments. Here are our responses. C: comments; R: response.

> C1: More missing rate setting

R1: We agee more missing rate setting will help to better evaluate the performance of the proposed method. However, we argue that , the main contribution of **BayOTIDE**, the first Bayesian online imputation model ,is mainly on the novel methodological and theoretical aspects, instead of the performance gain over large-scale datasets under different missing rate settings. The similar method-driven work in this area, like **CSDI** [ Tashiro, Neurips 2021],  **CSBI** [Chen, ICML 2022],  **TIDER** [Liu, ICRL 2023] all only evaluate the performance under no-more-three missing rate settings.  

Thus, we only evaluate the performance under two missing rate settings in the paper. We will add statements to clarify this point in the revised version.    

> C2: "Only missingness at random is considered."

R2: Good point. We clarify that we actully evaluate the performance under **two** missing pattern settings. 

- The first setting is the **random missing pattern**, which is the most common missing pattern in real-world applications. The table 2 in the paper shows the performance under this missing setting.

 - The second setting is the **all-channel / block-wise missing**, which is similar to the *temporal missing* pattern in the **GP-VAE** paper. We actually use the setting at **Imputation with Irregular timestamps** parts(last section of section 5). During the training, the observations at the irregular timestamps are all masked out. The results are shown in the table 3 and 5.   


>C3: Multi-output GP framework with linear + periodic kernels as baselines.

R3: Good point. We do agree that the multi-output GP with linear + periodic kernels can work well on the simulation study. However, we argue that even with linear + periodic kernels,**multi-output GP can not handle the real-world long time series. It's because the multi-output GP is a full GP, which has $O(T^2N^2)$ space cost and $O(T^3N^3)$ time cost**. where $T$ is channel number and $N$ is the number of timestamps. Thus, it's not scalable to the real-world long time series.

 To make the multi-output GP work on the real-world long time series, we have to **patching** the long time series into short segments, and then train the multi-output GP on each segment (**The segment size is $30 \times 30$ in our experiments**).The patching make the kernel can not capture any long-term dependency, like seasonal dependency, and the performance will be similar or worse than the multi-output GP with RBF kernels. To verify this, we compare the performance of multi-output GP with RBF kernels and multi-output GP with linear + periodic kernels on the *traffic-guangzhou* dataset. The results are shown in the following table:

| Observed-ratio=70% | RMSE | MAE | CRPS |
| ------ | ---- | --- | --- | 
| **BayOTIDE** | 3.724 | 2.611 |  0.053 | 
| **MT-GP-RBF** | 4.471 | 3.223 |  0.082  | 
| **MT-GP-linear+periodic** | 8.673 | 7.224 |  0.252 | 

> C4: MC-study on evaluation

R4: We clarify that we actually use the MC-study on evaluation. We state at the end of the *Baseline and setting* paragraph in section 5.2 that "We repeat all the experiments 5 times and report the average results.". Due to the space limit, we do not report the variance of the results. 



# for reviewer  XZJX (5/3):
We thank reviewer for the careful review and constructive suggestion.We address the comments below:

> C1:Novelty in Bayesian learning side and time series imputation side

R1: Good point! Please refer sections **Novelty and contribution on time series imputation side** and  **Novelty and contribution on Bayesian learning side** in the response overview, which at the top-level post in this forum.

> C2: Notation polish and remove inaccurate statements

R2: We thank reviewer for the careful reading and pointing out the inaccurate statements. We will polish the notation and remove the inaccurate statements in the revised version.

> C3: Why matern kernel?

R3: The state-space GP we used requires the kernel to be a stationary covariance function. The Matern kernel is a strong and well-known stationary covariance function, which is widely used in the GP literature and has a elegant closed-form for the corresponding state-space representation(Section 1.1 and 1.2 in appendix). We can further adjust the smoothness parameter $\nu$ to control the smoothness of the kernel to match the different series.
 It can be further reduced to the widely-used RBF kernel when the smoothness parameter $\nu$ is set to $1/2$.  
 
 Thus, considering the capacty and flexibility of the Matern kernel, and the elegant closed-form of the corresponding state-space representation
 we choose the Matern kernel to model the non-linear trend components in **BayOTIDE**. 

> C4: "Is it possible to incorporate other low-rank GP methods into your framework?"

R4: Very good point! Utilizing other low-rank GP methods, like the classical spase GP with inducing points, is feasible. We just need to run SVI to minimize the ELBO with respect to joint probability (eq 7). However, compared with state-space GP,
 we claim the sparse GP may not ideal for the following reasons:

 - The spase GP with inducing points actually is the low-rank approximation of the corvariance matrix, which is could be low quality when the inducing points are not well-selected. On the contrary, the state-space GP is exactly equivalent to the original GP, which fully preserves the capacity of GPs.

- The ELBO-based SVI for saprse GP is not able to handle the online learning well. On the contrary, the state-space GP, formulated as a chain-structured prior, is able to handle the streaming inference with KF. It's a great advantage for the time series task.

 

