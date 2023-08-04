We thank all reviewers for their careful and helpful review! 

We are glad that most reviewers agree that SFTL's contributions on novelty("first model to learn factor trajectories under streaming setting"  (vq55), ),  solid method("elegant method and techniques(Dugj)""advantage is computational efficiency(ZhxY), "proposed online method beats many offline models"(vq55)), and fair representation, (“well-written and easy to follow” (DKpV), "clear no-misleading symbols and well written"(Dugj), ).  As a methodogy work focus on general temporal tensor, we also delight to see some comments reconginize its potential and request detailed discussion over boader applications ("Is this method applicable to  this streaming 3D visual(DKpV)", "more detailed explanation over real-world application"(Dugj))

We would like to offer several clarifications for helping review to better understand our paper. 


## 1 Detailed Explanation of Figure 1

Figure 1 demonstrates the workflow of SFTL using an example of a temporal tensor with 3 modes (in real-world data, we can handle tensors with more modes). Different colored boxes contain the factor trajectories of multiple objects in the corresponding mode - for simplicity we only drew one for each mode. The circles and curved arrows on each trajectory represent the Gauss-Markov chain state-space GP prior, as described in line 131-132 of the main paper.

The time axis at the bottom and the data stream blocks represent that at certain timestamps, such as tn+1, we observe parts of the tensor values (denoted by Bn+1 and orange diamonds) - corresponding to line 104-106 of the main paper.

The arrows in various colors from the pink box of τ and the factor trajectory state boxes to the orange diamonds signify that based on the current observations, we update τ and the factor trajectory states in real-time via moment matching, as elaborated in line 180-188 of the main paper.

We will improve the explanation of Figure 1 to make it more accessible to readers. Please let me know if you would like me to modify or refine this explanation. I'm happy to revise it based on your feedback.


## 2 The proposed method is not stricted to single Matern kernels

Our proposed SFTL method is not restricted to only using Matern kernels for the GP priors over factor trajectories. This flexibility comes from two aspects:

The GP prior is placed dimension-wise over each factor (line 96-97, main paper). This enables us to choose GP with arbitrary stationary kernels for different factors and their elements.
As stated in line 28-30, Section A of the appendix, for any stationary kernel, such as SE kernel and RBF kernel, we can follow the same procedure of spectral analysis to construct an equivalent linear time-invariant stochastic differential equation (LTI-SDE) and a state-space prior.
Specifically, we can approximate the inverse spectral density of those kernels using polynomials of ω2 with negative roots, and then follow the steps outlined in the appendix to obtain the LTI-SDE representation.

Therefore, the conversion to a computationally efficient state-space prior is generally applicable beyond Matern kernels. We will highlight this point clearly in the paper to avoid the misconception that our proposed streaming learning framework is restricted to only Matern kernels.

## 3 The usage of state space GP and moment-match is non-trivial
The adoption of state space Gaussian processes (GPs) and moment matching for tensor decomposition is non-trivial. As elaborated in Section 4 and Appendix C, directly applying classical state space GPs and Expectation Propagation (EP) to tensors is infeasible, due to the unique algebraic structure of tensors.

Specifically, each observed tensor entry couples the states of multiple factor trajectories across different modes (see equation (1)), which is more complex than traditional state space models. The multiplicative form of the coupled factor states renders the running posterior intractable. This also makes moment matching in classical EP infeasible.

To address this challenge, we propose innovatively leveraging the chain structure and developing an efficient online filtering algorithm using conditional Expectation Propagation (CEP). This approximates the running posterior of involved factor states as a Gaussian product form. Thereby, we can decouple the factor state chains and conduct standard RTS smoothing independently for each chain.

In summary, the tensor-specific algebraic structure poses unique difficulties for streaming learning based on state space GPs. Our proposed techniques, including adopting conditional EP and deriving closed-form posterior updates, are essential contributions to enable efficient streaming tensor decomposition. We will enhance the paper to provide more details on this non-trivial extension of classical state space GP modeling, to facilitate readers' understanding of our technical novelty.


To summarize, we thank the reviewers for their careful feedback and additional suggestions for evaluation, which will make the paper significantly stronger. We look forward to further discussion, and are happy to answer any questions that might arise.

