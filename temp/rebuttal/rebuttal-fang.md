# for reviewer DKpV

We thank reviewer 8NSa for their careful review! We address the comments below - **we regularly refer to the response overview, which is the top-level post in this forum**::

>“Parameters of the decomposition factor are sampled from a GP with the same kernel. That says that the smoothness of the factor trajectories is assumed to be similar. That might be a restrictive assumption on the data the method is applied for, but it is not discussed.” 

We claim SFTL does not assume all factor trajectories are with similar smoothness, or restrict to model them with GPs with the same kernels. Actually, the GP prior is assigned dimension-wise over each factor (line 96-97, main paper). Thus, it enables the flexibility to choose GPs with arbitrary stationary kernels, and follow the same way to construct an LTI-SDE and state-space prior (line 28-30, section A, appendix), for each element of different factor trajectories.   **Please see section 2 of the response overview** for more detailed explanation.


>Continuity in the latent space of the factors translates to the continuity in the space of the initial tensor values that follow from (1). In practice, a slight change in the factors might hugely affect the initial tensor values and vice versa like streaming point cloud data.  Is this method applicable to the streaming 3D visual data, where the change in scenes might be significant from scene to scene?

We appreciate the reviewer raising this interesting point. We believe SFTL's online updating mechanism can handle reasonably well the case.

Specifically, whenever the observation space exhibits a significant and drastic new pattern change, we would update the factor trajectories in the latent space through the three steps of moment matching, Kalman filtering and RTS smoothing (see the algorithm table in the paper). Among them, Kalman filtering and RTS smoothing fully utilize the historical states as implicit constraints, ensuring the updated factor trajectories remain relatively robust and smooth.

We acknowledge the reviewer's concern and will explore more in-depth in this direction in our future work.

>the trade-off between the decomposition rank and sustaining several Gaussian processes (i.e., better modeling of the factors). The rank R used in the experiments is relatively small.

We appreciate the reviewer's comment. The relatively small rank R used in the experiments is due to the intrinsic low-rank property of our datasets (see details in Section E of Appendix) - either being sparse (e.g. FitRecord) or with fewer factors in each mode (ServerRoom, BeijingAir). The lower rank choices were sufficient to capture their temporal patterns.

We acknowledge the trade-off between the decomposition rank and sustaining several Gaussian processes (i.e. better modeling of the factors) raised by the reviewer. We will experiment with denser and higher-dimensional streaming time-series tensor data, such as streaming point cloud data, in our future work to better investigate this issue. We thank the reviewer for the constructive suggestion.

>why is Gamma distribution used?

The Gamma distribution is the most commonly used prior to model the observation noise of Gaussian likelihoods. Since it belongs to the exponential family as Gaussian does, by using moment matching, we can easily obtain closed-form posterior update formulas( Equation 25, 26 in Appendix ). 

>how are the hyperparameters of the models chosen? Do the data dictate those, or is there a reason for them?

We currently determine the hyperparameters via cross-validation and tuning experiments. We have provided the related sensitivity analysis in the appendix (Section D2) to show the model performance under different hyperparameter settings.

>Why Tensor Train or Tensor Ring decompositions, are not compared to or not used? 

We appreciate the reviewer raising this point. There are two main reasons we have not compared to or used Tensor Train or Tensor Ring decompositions in this work:

1. Our derivations of the closed-form running posterior updates (Section C.2 of Appendix) rely on the specific algebraic structures of CP and Tucker decompositions. Extending them to Tensor Train or Tensor Ring is non-trivial.
2. Among common tensor decomposition methods, CP is the simplest while Tucker is the most complex one with the largest model capacity. Tensor Train and Tensor Ring lie in between CP and Tucker in the trade-off between model capacity and scalability. Given that we have addressed the simplest and most complex cases of CP and Tucker decompositions, we believe it is a natural next step to study Tensor Train and Tensor Ring in our future work.
We agree with the reviewer that comparing with more tensor decomposition forms can further validate the advantage and generalizability of our streaming learning framework. We will explore this direction in our future research.

> A simple baseline would tackle the problem as a regression task. It would be great to add it as a baseline.

Good suggestion. We use the index of modes and timestamps as features to build the regression task.  We applied Baysian Linear Regression(BLR), RBF-kernel support vector machine (RBF-SVM), and simple neural-network(NN) with 3-hiden MLP layers as the regression baselines. The trianing and test setting are aligned with the STFL. Here's the results: 

| RMSE      | FitRecord | ServerRoom     |  BeijingAir-2 |     BeijingAir-3 |    
| :---        |    :----:   |          ---: |---:  | ---:  | 
| BLR      | 0.967 ± 0.003      | 1.164 ± 0.013   | 1.118 ± 0.016   | 1.074 ± 0.028  |
| RBF-SVM   |0.881 ± 0.012        | 1.232 ± 0.002      | 1.052 ± 0.018   | 1.018 ± 0.016   |
| NN   | 0.725 ± 0.024        | 1.431 ± 0.035      | 0.856 ± 0.054   | 0.871 ± 0.022   |
|SFTL-CP   | **0.242 ± 0.006**        | **0.108 ± 0.008**      | **0.15 ± 0.003**   | 0.318 ± 0.008   |
| SFTL-Tucker   | 0.246 ± 0.001        |0.216 ± 0.034     |  0.185 ± 0.029   | **0.278 ± 0.011**  |

We can see the SFTL outperforms all the regression-based methods. On ServerRoom, the non-linear model RBF-SVM and NN seems get trapped by severe overfitting problem. We will add thess baselines into the paper.


# for reviewer vq55

We thank reviewer 8NSa for their careful review! We address the comments below - **we regularly refer to the response overview, which is the top-level post in this forum**::

> Although the problem setting is new in the tensor decomposition field, most techniques used in this work seem standard, such as state-space Gaussian process and expectation propagation.

  **Please see section 3 of the response overview** . The inference over state-space Gaussian process and expectation propagation is non-trival. We used several novel tech to make them fit the streaming tensor task.


>The notations are too complex and hard to follow.

Thanks much for the many detailed and valuable suggestions. We will follow your advice to polish and improve the presentation. 

> In Equation 9, for the first Gaussian distribution, is the variance missing?

Yes and thanks much for pointing out the typo, we will fix it.



# for review Zhxy

We thank reviewer 8NSa for their careful review! We address the comments below - **we regularly refer to the response overview, which is the top-level post in this forum**::

> What are the applications that STL can be used in real-world? Can you please explain the real-world applications?

Please see the Section E of the Appendix, where we listes the detailed information and discrimination of the real-world datasets.

>  Not a big difference is observed between SOTA and the STL on the real-world applications. Can you also add how much gain you provide with STL compared to baselines, e.g. in percent? both in efficiency and accuracy.

Thanks for the valuable suggestion, we list the performence gain of percent over the sub-optimal benchmark on three datasets: 

|  RMSE   | FitRecord |   BeijingAir-2 |     BeijingAir-3 |    
| :---        |            ---: |---:  | ---:  | 
| Sub-optimal  benchmark    | 0.503   | 0.395   |  0.535  |
| SFTL  | 0.424      | 0.248   | 0.439   |
| Performence Gain   |   16%    | 38%   | 19%   |

It's clear the SFTL get significant performence gain over the sub-optimal benchmark. We want to highlight the fact that sub-optimal benchmarks (NONFAT, P-Tucker) are all static method, which will access the data hundreds epochs during the traning, but SFTL is a online model that only access the training data once.

As for the efficiency gain, we conducted the comparation of running time on BeijingAir2 dataset between our methods and BCTT(SOTA method to handle continues-time tensor decomposition) in Section G of appendix. Based on that, we compute the speed-up in persent:  

|  Training Time(Sec)   | R=2 |   R=3 |     R=5 |    R=7 |    
| :---        |            ---: |---:  | ---:  | ---:  | 
| BCTT (benchmark)    | 49.5   | 56.5   |  72.1  | 136.7  |
| SFTL-Tucker  | 32.3      | 35.6   | 43.2   | 59.3   |
| SFTL-CP  | 27.1      | 27.2   | 28.5   | 29.1 |
| Speed-up Tucker   |   55%    | 59%   | 67%   | 131%   |
| Speed-up CP   |   83%    | 107%   | 152%   | 371%   |

We could see a large speed-up of our method with both the CP and Tucker
form. We will add the in-percent gain and highlight it in the paper.

>Can you please add more explanations to Figure 1? 

**Please See the section 1 of the overview for more detailed explanation. **


# for review Dugj

We thank reviewer 8NSa for their careful review! We address the comments below - **we regularly refer to the response overview, which is the top-level post in this forum**::

>I struggled to understand Fig 1. Since there are 3 trajectories in Fig 1, does this correspond to the SFTL for a tensor that has three 3 modes?

Yes, Figure1 use an example of a temporal tensor with 3 modes (in real-world data, we can handle tensors with more modes). We will improve the explanation of Figure 1 to make it more accessible to readers.  Please See the **section 1 of the overview** for more detailed explanation.

>In Algorithm 1, R is not included in Input. That point needs to be clarified.

Thanks for detailed review and pointing out the typo. We will fix it!

>In section 6.1, the word node suddenly appears, but I am unclear what this means. My understanding is that the input to the experiment in section 6.1 is a full-rank 2x2 time-evolving matrix with noise, is this correct?

We appreciate the reviewer raising this point. Yes, your understanding is exactly correct. "node" means the object in the mode, and we will improve this presentation. 


>1. There are some known tricks to reduce the computational complexity of the Gaussian process from O(n^3), such as Inducing Variable Method, Deterministic Training Conditional (DTC) Approximation, and Fully Independent Training Conditional (FITC) Approximation. All of these tricks can be adapted to non-Matern kernels. With these tricks, I think it is possible to achieve fast computations without Hartikainen's elegant tricks. Although the elegant method of this paper is to be evaluated, it is a drawback that there is no comment on this point. 
>2.  The authors appropriately mention in the Appendix that the speedup of the proposed method is only applicable to Matern kernels. It is unfortunate that these techniques are not applicable to non-matern kernels, i.e., RBF kernels.


We appreciate the reviewer carefully reading the appendix section and giving valuable suggestion. To clarify, the technique we used to reduce the computational complexity - the LTI-SDE representation of GP - is not limited to only Matern kernels. In fact, as we stated in line 28-30, Section A of the appendix, for any stationary kernel, such as SE/RBF kernel, we can follow the same procedure to construct an equivalent LTI-SDE and state-space prior.

More specifically, we can approximate the inverse spectral density of those kernels using polynomials of ω2 with negative roots, and then follow the same steps outlined in the appendix to obtain the LTI-SDE representation. Therefore, the speedup of our proposed method is generally applicable beyond Matern kernels. We will update the appendix to further clarify this point. We will also add the dicussion of other tricks to reduce the computational complexity of GPs. 

Please also read the **section 2 of the overview**  for more detailed explanation.












