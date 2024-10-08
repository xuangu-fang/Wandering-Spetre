
 High-level vision-based projects

1. 数字孪生，AI + industy/science

- soft sensor: 软传感器 - 数字化转型的随想 - 王勇的文章 - 知乎
https://zhuanlan.zhihu.com/p/681286081 -- “星尘传感器与念动浮游炮？”

- AI+化工: 热力学建模与优化 聊聊目前化工数字化转型的热力学问题 - 安德鲁威廉的文章 - 知乎 https://zhuanlan.zhihu.com/p/682571957

- AI+全链优化数据集: 化工产业的软测量问题和数据集介绍 - 一块钱买中巴的文章 - 知乎
https://zhuanlan.zhihu.com/p/204921360
https://depts.washington.edu/control/LARRY/TE/download.html#Updated 

- 基于LLM+系统识别/equation discover + 控制/LLM 的集成智能系统
  - ai驱动的 系统识别 + 控制论：
  - https://www.zhihu.com/people/ZhuYucai1/answers
  - https://www.zhihu.com/question/511430750

2. AI + society

- general market/civi simulator: 通用市场/文明模拟器, 心理史学

  - adaptive & generative representation of real-world objects, events, and agents  
  - 工具变量与隐变量
  - LLM fine tunning with Opion Traj. (Yun-Shiuan (Sean) Chuang)

- 后AI时代的失业问题，新的职业和产业是什么？—— 人人都是调查员、研究员、社会复杂数据的贡献者和分析者，社会实验的参与者
  - 为此，需要一种新的社会契约，以保障每个人的基本生活，以及每个人的社会参与权利，以及每个人的社会实验权利
  - 需要新的模型和算法，以及新的社会实验和社会调查方法


- 从 [社会组织学十讲] 中获得的的思路，或可作为 AI for social Science 的 first principle：
    - 社会学中三种分析思路/机制/视角：效率学派，新制度学派（合法性、社会环境），社会网络学派（社会关系、社会结构），其实对应了三种建模思路：内生的驱动（reaction process ）, 外部的驱动（即单位与 “宏观变量” 之间的交互约束）, 结构的驱动（沿网络传播的流）—— 而这三种建模，在ML 这边其实已经有相当丰富和成熟的工具箱了：
        - 内生的效率/随机性：最优化、GP，sampling
        - 外部的约束/环境：attention, transformer， latent variable model, 甚至是因果涌现和宏观变量
        - 结构的传播：graph neural network, tensor network
      - 所以重要的就是找到合适的问题和数据

    - 西蒙的有限理性模型的几个原则：
        - 成对比较 而不是 全局比较
        - “满意”原则 而不是 最大化原则
    - 对让机器更高效推理决策 + 更好地理解和模拟人类社会和历史，都有很多启发


 逆.风暴蝴蝶 (inverse butterfly effect) - 对复杂系统的逆向预测与控制

- 逆向预测与控制的基本思路与方法：
  - deterministic 的方法，由于系统的不稳定性和对初始条件的敏感性，逆向预测是和求解基本是不可能的
  - surrogate model 的方法，通过构建一个系统的在隐空间的近似模型，然后对这个模型进行逆向求解，以及对真实系统的控制
  - diffusion based + Probabilistic + generative model 的方法，通过对系统的随机性和不确定性的建模，以及对系统的生成模型的建模，来进行逆向预测与控制—— 我们并不需要精确地刻画“风暴”的每一个细节，并溯源到蝴蝶，而是将target system - 无数场可能的风暴 - 无数个蝴蝶的关系，建模为一个概率分布，然后通过对这个概率分布的逆向推断，来进行逆向预测与控制

  - update: 
  - 在相空间里的传统建模 （PSR）似乎并不很高效，延迟坐标法的设计有点傻，不如transfomer, 特别是用于时间序列+混沌系统的一些工作，但是一些指标可以参考，比如 Lyaponuv Exponent，基于不变量、operator learning 的一些工作可能参考价值更大 
  - 相关文章：
    - https://arxiv.org/pdf/2402.11463
    - https://arxiv.org/pdf/2408.05177 （没啥特别的，只是说明two-phase training 的思路对于多尺度系统模型有帮助，这也是一种新范式下的数据同化）
    - chatgpt log: https://chatgpt.com/share/67009de3-7524-800c-b0df-c7c8dfe2b347
    - https://zr9558.com/wp-content/uploads/2015/09/time-series-prediction-by-chaotic-modeling-of-nonlinear-dynamical-systems.pdf

