# for reviewer y2cT (6/3)
We thank reviewer for the careful review and constructive suggestion—especially the suggestion on highlighting the reasons for kernel choice and latent space dimension. We address the comments below( C: comments; R: responses): 

>C1:"  It seems a bit unclear how you chose your kernels. Were other options considered and proved to be not as good? How were those specific kernels chosen?"
<!-- 2 points, on the seasonal factors, is efficent, on the trend factor, Matern is suffient and resoanable, other kernel is hard become state-space cloased form -->
R1:  Good point!  In BayOTIDE, we model two main functional factors: seasonal and trend components. For the seasonal factor, the choice of the periodic kernel was quite natural and straightforward as we required a function that could model periodic signals effectively.

Regarding the trend factor, indeed, several kernels, like square-exponential (SE) kernel, could have been considered to capture cpmplex patterns in the latent space. We opted for the Matérn kernel for two reasons: 
- **Flexibility and Strength**: Matérn kernel allows for additional control over the function's smoothness with parameters $\nu$ (line 127-128, left column). The sampled functions from the Matérn kernel are $\nu$ times differentiable in the mean-square sense, providing the capability to adjust the function's behavior according to the data. For example, with different values of  $\nu$, the Matérn kernel can model functions ranging from non-differentiable to infinitely differentiable, offering more versatility than the commonly used SE kernel. The SE kernel, while popular, restricts sampled functions to be infinitely differentiable, which can be overly restrictive for certain datasets. Other often-used kernels, such as the linear kernels or the expenential kernels, is either too simple or a special case of the Matérn kernel. We  evaluate how differnt smoothness of kernels fit the real-world data in Figure (d)-(f).

- **Analytical Tractability with State-Space GP**: As the stationary kernel, Matérn kernel  has a concise and closed-form state-space representation (as detailed in Appendix 1, equations 25-26), enabling us to derive efficient online inference algorithms. In contrast, while some non-stationary kernels may offer more powerful modeling capabilities, they do not easily lend themselves to a state-space model representation, complicating subsequent inference processes.

We thank reviewer to point out this, and we will add this explanation to the revised manuscript.


>C2: "How would your model perform if you used different parameters for these dimensions($D_r, D_s$)?"

R2: Good point! First, we actually show the sensitivity of the model to the latent space dimension in the experiments (Figure 2 (d)) by varing the latent space dimension ($D_r+D_s$) from 5 to 60. To further investigate the impact of the latent space dimension on the model performance, **we conduct extra experiments** on guangzhou-traffic dataset(observed ratio = $70\%$) by varying the latent space dimension and report the results in the follwoing tables:

---
|  Test CRPC   | $D_r$ = 5 |   $D_r$ = 10 |     $D_r$ = 20 |    $D_r$ = 30 |  $D_r$ = 40 |      
| :---        |            ---: |---:  | ---:  | ---:  | ---:  | 
|  $D_s= 3$     |   0.068    | 0.064   | 0.061   | 0.057   |0.056 |
| $D_s= 5$   |   0.067    | 0.063   | 0.059   | 0.056   |0.055 |
| $D_s= 10$    |   0.066    | 0.063  | 0.058   | 0.053   |0.053 |
| $D_s= 20$     |   0.081    | 0.074   | 0.065   | 0.059   |0.058 |

We can found that the increasing the latent space dimension, especially the trend factor dimension ($D_r$), can improve the model performance. However, the improvement is not linear and the model may suffer from overfitting when the latent space dimension is too large. Too high seasonal factor dimension ($D_s$) may also lead to overfitting and degrade the model performance. We will add this analysis to the revised manuscript to highlight the impact of the latent space dimension on the model performance.

# for reviewer  TmRT (6/3)

We thank reviewer for the careful review and constructive suggestion. We address the comments below( C: comments; R: responses): 

> C1:"The numbers of trend factors and seasonal factors are important parameters, but the analysis is insufficient. More experiments and analysis might be better."
<!-- highlight and add exp -->

R1: Good point! We do agree more experiments and analysis on the latent space dimension are necessary to better understand the model's behavior. We have conducted sensitivity analysis on the latent space dimension in the experiments (Figure 2 (d)) by varying the latent space dimension ($D_r+D_s$) from 5 to 60, and **we add extra experiments** on guangzhou-traffic dataset(observed ratio = $70\%$) by varying the latent space dimension and report the results. **Please refer to the response R2 to reviewer y2cT for the detailed results and discussion.**


> C2:  "why to conduct assumptions with Gassian prior and Gamma prior in the function (9) and (12), rather than other distributions?"

R2: Good question! We choose Gaussian and Gamma as priors and approximated distributions for the following reasons:

- for equation (9): The Gaussian prior is a common choice for the latent factors in GP models. It is consistent with the Gaussian data likelihood, and increases the model's robustness and interpretability. The Gamma distribution is most commonly used prior for the inverse noise variance in GP regression. It is a conjugate prior to the Gaussian likelihood and has a closed-form posterior, which simplifies the inference process.

- for equation (12): The equation (12) is the pre-step to conduct conditional Expectation
Propagation(CEP). In general, to conduct EP, we need to introduce an exponential-family (EF) approximation for each non-EF term in the joint probability, so as to obtain a closed-form posterior approximation in the exponential family. Here we adopt the Gaussian-Gamma approximation because: 
    - it decouples the weights, factor states, and inverse noise variance in the likelihood into EF terms (Gaussian and Gamma), which is essential for CEP inference, 
    - its structure is simple and efficient for
computation and updates. More important, it's is consistent with the Gaussian and Gamma posterior approximation (see Eq. 11) in the main text, which allows us to derive a closed-form online update with message passing and merging.(Eq. 13-14). Other distributions may not have these properties, making the inference process more complex and less efficient.

Thanks for the question, we will highlight the meaning and role of Gamma and Gaussian distributionsin our paper.

> C3: " What problems might arise from the approximations of mean-field and conditional Expectation Propagation, and how does they influence the effectiveness of the model?"
<!-- 1. approximation -->

R3: 
We appreciate your insightful question regarding the potential challenges posed by the mean-field and conditional Expectation Propagation (EP) approximations in our model. Below, we address these concerns and elucidate how we mitigate their impacts:

1. **Mean-field Approximation**:

   The mean-field approximation is one of the most common approaches in Bayesian inference, enabling us to decouple all random variables to achieve feasible inference. This decoupling might overlook some complex correlations between variables, potentially affecting the model's capacity. However, it's crucial to highlight that despite adopting the mean-field approximation, our posterior estimation is not a fully-factorized trivial case. We treat the channel-wise weight $u_d$ as a multivariate Gaussian distribution(Equation 9, 11 and 14). This approach allows us to capture the dependencies between different factors across channels, mitigating some of the capacity loss due to the approximation. This strategic choice balances the trade-off between computational feasibility and the retention of significant correlations within the model.

2. **Conditional EP and EP Inference**:

   EP and its conditional variant perform fixed-point iterations to optimize an energy function, akin to solving a mini-max problem. When convergence is achieved, it signifies reaching a stationary point of that energy function. Although EP theoretically does not guarantee convergence due to its fixed-point iteration nature—similar to Newton's algorithm—in practice, it often converges smoothly. The original paper [1] on EP provides an analysis guaranteeing at least one fixed point. A known aspect of EP is that divergence, though rare, can act as a practical indicator that the chosen approximation family might poorly match the exact posterior. This signal can serve as a valuable debugging tool. In our experiments, we observed no divergence instances in our method using CEP, indicating a well-matched approximation family and reliable convergence in practice.

[1]:Minka, Thomas P. "Expectation propagation for approximate Bayesian inference." Proceedings of the Seventeenth conference on Uncertainty in artificial intelligence. 2001.

> C4: "Typo ay  “Employing”."

R4: Thanks for pointing out the typo and we do appreaite it your detailed review. We will correct it in the revised manuscript.


# for reviewer xqnS (6/4):

We thank reviewer for the careful review and constructive suggestion. We address the comments below( C: comments; R: responses): 


> C1:  "authors should consider some causality-based method like"
> > <!-- easy -->
R1: Thanks for the suggestion and the awesome references! Causality-based methods are indeed powerful tools for modeling time series data with disentangled representation learning (DRL)
, especially when the data exhibits causal relationships. We will add the discussion on causality-based methods and  their potential applications in the revised manuscript.


> C2: Can the proposed method address the cases where these two factors are dependent? Please justify it.
> 
R2: Good question! The answar is tricky: **No but Yes** for the following reasons:

- **No**: On the **latent space and prior side** , we applied the independent GPs priors for the trend and seasonal factors (Eq 6 and Eq 8) , assuming that they are *independent*. This assumption simplifies the model and inference process, making it more tractable and efficient, and results in *fully independent* latent factors. 

- **Yes**: On the **obsevation space (data) and inference side**, the trend and seasonal factors are combined through the weights $u_d$ (Eq 9), which are channel-wise dependent. The weights $u_d$ are modeled as a multivariate Gaussian distribution, and its approximate posterior: $q(u^d|D_{t_n})=N(m_n^d,V_n^d)$ (line 187, below eq 11) is updated in a online manner during the inference. The learned covariance matrix $V_n^d$ can directly **reflect the dependency between the functional factors**. In this sense, the models enable finner-grained and *channle-wise dependency* between the trend and seasonal factors to better fit the data.  

We will add this explanation to the revised manuscript to clarify the model's capability in capturing the dependency between the trend and seasonal factors.


> C3: "theoretical analysis like boundary analysis to show how accurate this method can achieve by probabilistic interpolation method 


R3: Thanks for the suggestion! As the BayOTIDE can give the closed-form predictive distributions of factors $V(t^*)$ and weights $U$ at arbitrary time points, the imputation result can be seen as randon variable $V^{T}(t^*)U$, which is the dot prodct of the two multi-var Gaussian distributions with non-identical covariance matrices. There is no explict form for such distribution, but we can explore the distribution's properties, like empirical variance and higher-order moments by Monte Carlo simulation., to analyze the imputation accuracy and boundary analysis. 

> C4: how to simulate the online setting with offline datasets?


R4: We feed the observed data into the model in a sequential manner, following the order of the initial timestamps. The model updates the posterior distribution of the latent factors and weights at each step. At preset steps, we evaluate the model's performance by imputating all missing values in series with current weight and factors, and calculate the imputation accuracy. This procedure is shown in Figure 2(a) and line 366-383 in main text. We will add detailed explanation to the revised manuscript to clarify the online setting.

> C5: "how do the future values in the imputation task benefit reconstructing the trend and season factors?"

R5: Good point! The crucai point to improve the historical imputation with future values is the *RTS-smoothing step* (line 239, left column, and last setp in Algorithem 1). The RTS-smoothing step is a backward pass that refines the latent factors by incorporating future information. This process is aimed to capture the long-term dependencies in the time series data and improving the imputation accuracy. We highlight that the RTS-smoothing step will not revisit the observed data but only refine the latent factors in the latent space—thus not violating the online setting.

We also conduct extra experiments to show the impact of future values on the imputation accuracy. We run the BayOTIDE model on guangzhou-traffic dataset with observed ratios $= 70\%$ and different trend factor dimensions, and compare the imputation accuracy with and without RST-smoothing step. The results are shown in the following table:

---
|  Test RMSE ($D_s= 10$)  | $D_r$ = 3 | $D_r$ = 5 |   $D_r$ = 10 |     $D_r$ = 20 |    $D_r$ = 30 |  $D_r$ = 40 |      
| :---        |    ---: |---:  | ---:  | ---:  | ---:  |  ---:  |
|  W/ RST-smoothing     |  5.14    | 4.56   | 4.26   | 4.09  |3.74 | 3.75 |
| W/O RST-smoothing  |   5.19    | 4.65   | 4.37   | 4.17   |3.91 | 3.92 |

We can see that the RTS-smoothing step can improve the imputation accuracy, especially when the trend factor dimension is large. 


