---
toc: true
url: tulane_bioinf_18
covercopy:
priority: 10000
date: 2022-03-24 13:26:26
title: "Deep Learning (Classes notes)"
ytitle: "Deep Learning (Classes notes)"
description: "Basic knowledge and concepts for Artificial Neural Network"
excerpt: "Basic knowledge and concepts for Artificial Neural Network"
tags: [Classes, Bioinformatics, Tulane Classes]
category: [Notes, Class, Tulane, Bioinformatics]
cover: "https://www.hood.edu/sites/default/files/styles/width_720/public/content/program/hero/istock_56013860_molecule_computer_2500.jpg?itok=L8YHtcy2"
thumbnail: "https://cdn.iconscout.com/icon/premium/png-256-thumb/bioinformatics-2355481-1985942.png"
---

# 1
## Lecture 18: Neural Networks

:dog:

***ANN***, also called =="artificial neural net"== or =="neural net"==, represents one of the most popular and promising areas of artificial intelligence (AI) research. An ANN is an ==abstract computational model==, inspired by the structure of central nervous systems

01) ==Network structures==: An ***ANN*** may have either a recurrent or nonrecurrent structure
02) ==Parallel processing ability==: Each neuron in the ANN is a processing element interconnections between neurons have a parallel structure
03) ==Distributed memory==: The network does not store information in a **central memory**. The values in the **weights** (the connections) form a long-term memory
04) ==Fault tolerance ability==: The network’s parallel processing ability and distributed memory make it relatively fault tolerant
05) ==Collective solution==: A conventional computer processes programmed instructions sequentially and one at a time
06) ==Learning ability==: An ANN, especially the nonrecurrent one, is capable of applying learning rules to develop models of processes while adapting the network to the changing environment and discovering useful knowledge implicit in received data

### Development

Source: [thinkautomation: Milestones in artificial intelligence](https://www.thinkautomation.com/histories/milestones-in-artificial-intelligence/)

1943: The first ANN → 1948: First autonomous robots → 1955: Official term and academic recognition → 1964: The first chatbot → 1969: Backpropagation → 1970: First ‘intelligent’ robot → 1978: Voice-activated technology → 1981: Commercialised AI → 1989: Chess victories: defeating masters → 1996: Chess victories: defeating the world champion → 1998: Widespread introduction: Furby and machine learning → 2001: A.I. Artificial Intelligence →  2010: Jeopardy! win → 2011: Voice assistant → 2016: Winning at Go


### (ANN) Learning Major Types

01) ==Supervised Learning==: the desired outputs for a set of training examples with class labels are provided to the neural network; thus, it learns by learning from training examples in the train set
02) ==Unsupervised learning==: no training examples are provided, and therefore, no evaluation of performance provided to the network
03) ==Reinforcement learning==: a hybrid method, the neural network is given a scalar evaluation signal instead of being told the desired output, and evaluations can be made intermittently


|![Deep learning and machine learning as subsections of artificial intelligence](https://www.researchgate.net/publication/328367178/figure/fig1/AS:962674179440669@1606530818662/Deep-learning-and-machine-learning-as-subsections-of-artificial-intelligence.png)|
|:-:|
|[© Matthew E. Dilsizian; 2018](https://www.researchgate.net/publication/328367178_Machine_Meets_Biology_a_Primer_on_Artificial_Intelligence_in_Cardiology_and_Cardiac_Imaging)|
|![Artificial neural network components and (b) multilayer perceptron. ](https://www.researchgate.net/profile/Haroldo-Campos-Velho/publication/323453569/figure/fig1/AS:598990714314752@1519821923069/a-Artificial-neural-network-components-and-b-multilayer-perceptron.png)|
|[© Rosangela Cintra](https://www.researchgate.net/publication/323453569_Data_Assimilation_by_Artificial_Neural_Networks_for_an_Atmospheric_General_Circulation_Model)|
|![Cornell College: Cheat Sheets for AI](https://static.docsity.com/documents_first_pages/2020/02/04/4fb2147aec6fa6f752500e1e2587f695.png)|
|[© Cornell College](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjn0dqlid_2AhUEd98KHT39A5QQFnoECAYQAQ&url=https%3A%2F%2Fmoodle.cornellcollege.edu%2Fpluginfile.php%2F195933%2Fmod_forum%2Fattachment%2F49071%2FML%2520cheatsheets_compressed.pdf%3Fforcedownload%3D1&usg=AOvVaw0cXkhSZwsWZWmQnfx_igp4)|

More infor: [Cornell College: Cheat Sheets for AI, Neural Networks, Machine Learning, Deep Learning & Big Data, click to download](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjn0dqlid_2AhUEd98KHT39A5QQFnoECAYQAQ&url=https%3A%2F%2Fmoodle.cornellcollege.edu%2Fpluginfile.php%2F195933%2Fmod_forum%2Fattachment%2F49071%2FML%2520cheatsheets_compressed.pdf%3Fforcedownload%3D1&usg=AOvVaw0cXkhSZwsWZWmQnfx_igp4)


### FFNN and FBNN

|![](https://ars.els-cdn.com/content/image/1-s2.0-S2213138821004264-gr2.jpg)|
|:-:|
|[© AnhTuan Hoang; 2021](https://www.sciencedirect.com/science/article/pii/S2213138821004264#f0010)|


### Perceptron

- A ==perceptron==, coined by Frank Rosenblatt in 1958, is originally defined as **a single artificial processing neuron with an activation threshold, adjustable weights and bias** [^Zafeiris_2018]
- A perceptron ==**refers to a single node**== in a neural network, such that in an input layer, these nodes (i.e., perceptrons) **receive input values** (also called input signals) that **quantify** the characteristics of each data object, and these input values are **multiplied by the respective weights** assigned to them to produce a summed value, which is **evaluated** according to a threshold value obtained from the activation function to determine the output value[^Lee_2018]
- In a single-layer perceptron, this output value is the prediction value. In a multi-layer perceptron, it is used as the input value for another perceptron layer[^Lee_2018]

*[Perceptron]: 感知器

[^Zafeiris_2018]:Zafeiris D, Rutella S, Ball GR. An Artificial Neural Network Integrated Pipeline for Biomarker Discovery Using Alzheimer's Disease as a Case Study. Comput Struct Biotechnol J. 2018;16:77-87.
[^Lee_2018]: Lee D-G, Jang Y, Seo YS. Intelligent Image Synthesis for Accurate Retinal Diagnosis. Electronics 2020;9:767.


***Multi-Layer Perceptron (MLP)***

*[MLP]: multi-layer perceptron
*[FFNN]: feed forward neural networks

- A ==multi-layer perceptron (MLP)== with **backpropagation (BP)** learning algorithm, also called multi-layer FFNN.
- An MLP comprises 3 layers: input, hidden, and output
- All neurons from one layer are fully connected to neurons in the adjacent layer. These **connections** are represented as **weights**. The weights play an important role in **propagation** of the signal in a neural network. The propagation which can be either single or multiple

- The learning algorithm of an MLP involves a forward feed (also called forward-propagation) step followed by a backpropagation (BP; also called backward-propagation) step, such that the input first is propagated through the neural network and the output computed. Then the error between the computer output and the correct output, in the form of a cost function, is propagated backward from the output to the input to adjust the weights (i.e., connection intensities). There are several methods that can be applied for backpropagation (BP), and among them, gradient descent method is the most popular

### Major Activation Functions in ANN

==What is Activation function==: [**An Activation Function decides whether a neuron should be activated or not**. This means that it will decide whether the neuron’s input to the network is important or not in the process of prediction using simpler mathematical operations.](https://www.v7labs.com/blog/neural-networks-activation-functions)

|![A node of ANN](https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d2424009416f21db643e21_Group%20807.jpg)|
|:-:|
|[© V7 labs](https://www.v7labs.com/blog/neural-networks-activation-functions)|

The steps of the ANN: input → weighted → Transform (Function) → Active (Function)

Table: [TizianoZarra; 2018](https://www.sciencedirect.com/science/article/pii/S016041201931791X)

| Activation Function     | Formula     | Strength/s|Weakness/es| 	Range	| Reference/s|
| :------------- | :------------- |:- |:-|:-|:-|
| Logistic Sigmoid (LS)   | $f(x)=\frac{1}{1+e^ {-x}}$ |• smooth <br>• continuously differentiable |     possibility to get stuck in the training<br>• slow convergence| (0, 1)| [Rojas, 1996](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0435), [Chen et al., 2015](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0085)|
|Hyperbolic Tangent| $f(x)=\frac{1-e^ {-2x}}{1+e^ {-2x}}$ |the derivative is more steep that LS (i.e., scaled LS) Differentiable at all points|vanishing gradient issues and low gradient| (−1, 1)|[Pushpa and Manimala, 2014](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0410), [Theodoridis, 2015](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0505)|
| Radial basis function or Gaussian Function| $f(x)= exp(-\frac{(x-c)^ 2}{r^ 2})$ | • good when finer control is required over the activation range|• computational time consuming due to the calculation of Euclidean distance|(0, 1)|[Sibi et al., 2013](https://www.sciencedirect.com/science/article/pii/S016041201931791X#bib571); [Faqih et al, 2017](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0130)|
|Rectified Linear Unit Function (ReLU)| $f(x)=0\ for\ x<0;x\ for\ x ≥0$ |• good estimator<br>• can combine with other functions<br>• can activate all neurons at the same time|• non-differentiable at zero and unbounded.<br>• it can create dead neurons because gradients for negative input are zero.|(0, ∞)|[Xu et al., 2015](https://www.sciencedirect.com/science/article/pii/S016041201931791X#bib573); [Kessler and Mach, 2017](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0220)|
|Maxout Function or Leaky ReLU| $max(w_ 1 ^T x + b_ 1, w_ 2 ^ Tx + b_ 2)$ | • speeds up the training<br>• no dying ReLU units (i.e., 0 output”|• become saturated for large negative values|(−∞, ∞)| [Xu et al., 2015](https://www.sciencedirect.com/science/article/pii/S016041201931791X#bib573)|
|Swish Function| $f(x)=x×sigmoid(x)$ |• smooth and non-monotonic function which outperformed ReLU on deep networks| • computationally expensive| (−∞, ∞)|[Nwankpa et al., 2018](https://www.sciencedirect.com/science/article/pii/S016041201931791X#b0375)|




|![](https://miro.medium.com/max/1400/1*p_hyqAtyI8pbt2kEl6siOQ.png)|
|:-:|
|[© SAGAR SHARMA; 2017](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)|


### Forward Feed back and Backpropagation

|![](https://dnd.or.kr/ArticleImage/0196DND/dnd-17-83-g005-l.jpg)|![](https://dnd.or.kr/ArticleImage/0196DND/dnd-17-83-g006-l.jpg)|
|:-:|:-:|
|Forward Feed Step|Backpropagation (BP) Step|
Source: [© Han SH; 2018](https://dnd.or.kr/search.php?where=aview&id=10.12779/dnd.2018.17.3.83&code=0196DND&vmode=PUBREADER)


### Gradient Descent

|![Gradient Descent](http://cdn-images-1.medium.com/max/800/1*NRCWfdXa7b-ak2nBtmwRvw.png)|
|:-:|
|[© primo.ai](http://primo.ai/index.php?title=Gradient_Descent_Optimization_%26_Challenges)|

- The gradient descent identifies the lowest point, i.e., the global cost minimum, of a cost function by taking iterative steps to adjust the weights starting from an arbitrarily chosen initial weight[^Han_2018].

- The gradient descent shall take many "epochs" (i.e., training cycles) to find the global cost minimum, rather than a local cost minimum, starting from an arbitrarily chosen initial weight[^Burney_2004].

[^Han_2018]: Han SH, Kim KW, Kim S, Youn YC. Artificial Neural Network: Understanding the Basic Concepts without Mathematics. Dement Neurocogn Disord. 2018;17:83-89.
[^Burney_2004]: Burney SMA, Jilani TA, Ardil C. A comparison of first and second order training algorithms for artificial neural networks. Int. J. Comput. Intelligence, 2004;1:176-184.


### Advantages and Disadvantages

- Advantages
  1) ANNs do not rely on data to be **normally distributed**, an assumption of classical parametric analysis methods
  2) ANNs are able to process data containing **complex (non-linear) relationships** and interactions that are often too difficult or complex to interpret by conventional linear methods
  3) ANNs are **fault tolerant**, i.e., they have the ability of handling noisy or fuzzy information, whilst also being able to endure data which is incomplete or contains missing values
  4) ANNs are capable of **generalization**, so they can interpret information which is different to that of the training data, thus representing a ‘real-world’ solution to a given problem by their ability to predict future cases or trends based on what they have previously seen.
- Disadvantages
  1) The ANN model obtained could be difficult to **interpret**
  2) Training of ANNs can potentially be **time-consuming**, depending on the complexity of the data being modelled
  3) As the # of hidden layers required to capture the features of the data increases, so does the time taken for training to complete. As such, **only one or two hidden layers** are commonly used.
  4) **Overfitting** may be a problem, which is a memorization of the training examples causing the ANN to perform poorly on future examples
  5) It is **not always apparent** how an ANN reaches a solution, and because of this, an ANN model has been referred to as a "black box" approach
  6) the quality of an ANN model ouput is highly dependent upon **the quality of the input data**



## Lecutre 19: Deep Learning

### Outliers
- Advanced Concepts in Neural Networks
	- Cost Functions
	- Activation Functions
	- Learning Rates and Overfitting
	- Stochastic Gradient Descent (SGD) and Parallelization

- Convolutional Neural Networks
- Recurrent Neural Networks


What is Deep learning: ==Deep learning is a NN with >1 hidden layer==

### Loss Functions

Which measures how well the model goes.
- Binary Cross Entropy Loss
- Mean Squared Error Loss


###  Activation Functions

Go back to looking above.
- ReLUs VS Sigmoid Activation Functions
	- ReLUs replace everything below thebias threshold to zero and don’tremap coordinates to (-1 to 1)
	- Sigmoids have a problem ofvanishing gradients where higherabsolute input values no longer increment output values
	- Sparser representation - highproportion of neurons output a 0
	- ReLUs converge much faster

- Multiple Sigmoids are Incompatiblewith Deep Learning
	- Derivative of sigmoid function is always «1, therefore product of gradients drops close to zero for multiple layers

### Learning Rate and Overfitting

|![](https://efxa.files.wordpress.com/2021/04/visualizing-the-loss-landscape-of-neural.png?w=512)|
|:-:|
|[© efxa.org](https://efxa.org/2021/04/17/loss-function-convexity-and-gradient-descent-optimization/)|
Lots of local minima that gradient-descent can get stuck in.

Solution: Setting the learning rate.

#### Memorization and Early Stopping


|![https://miro.medium.com/max/1310/1*ERLrFsyAEqqkPnCdtu1wQA.png](https://miro.medium.com/max/1310/1*ERLrFsyAEqqkPnCdtu1wQA.png)|
|:-:|
|[© Dr. Saptarsi Goswami; 2020](https://towardsdatascience.com/early-stopping-a-cool-strategy-to-regularize-neural-networks-bfdeca6d722e)|
- Goal is to have predictorthat generalizes beyondthe training set
- Early stopping preventsloss of generalization due tomemorization of the training set

#### Regularization I: Dropout
- During training, randomly set some activations to 0
	- Typically "drop" 50% of activations in layer
	- Forces network to not rely on any I node

#### Weight Decay Regularization

- Adds an **additional error**, **proportional** to:
	- Sum of weights (L1 norm)
	- Squared magnitude (L2 norm) of weight vector
	- Elastic net regularization does both L1 and L2

- Penalizing large weights simplifies the model

#### Stochastic Gradient Descent (SGD)

**When you run backpropagation to readjust the weights and biases, should you go through the training set at each iteration?**

No! You can take randomly-sampled mini-batches of the data and compute weight adjustments in parallel across many processors


### Momentum and SGD for learning rate

|![Momentum and SGD for learning rate](https://i.stack.imgur.com/epW89.jpg)|
|:-:|
|[© datascience.stackexchange.com](https://datascience.stackexchange.com/questions/84167/what-is-momentum-in-neural-network)|

- Faster convergence towards local optimum
- Reduced oscillation around steep slopes


### CNN
|![](https://miro.medium.com/max/1400/1*vkQ0hXDaQv57sALXAJquxA.jpeg)|
|:-:|
|![](https://miro.medium.com/max/1052/1*GcI7G-JLAQiEoCON7xFbhg.gif)|
|[© Sumit Saha; 2018](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)|

- CNN Limitations

- Corner cases that occur in real life aren’t found in training sets
	- upturned chair
	- crumpled t-shirt lying on a bed
	- ImageNet has idealized versions of objects in perfect lighting

- Generalization in CNNs occurs in a totally different way than we generalize

- CNNs do not have explicit internal representations of entities and their relationships
	- Capsule Networks are being developed to solve”Picasso problem” for higher-order feature hierarchies


### Recurrent Neural Networks

*[RNN]: Recurrent Neural Networks

Very friendly for time serious data

- A sequence Modeling Problem: Predict the Next Word
	- Fixed window doesn’t work well because long term dependencies need to be modeled
 - Vector of word counts doesn’t work well because counts don’t preserve order

Apply a recurrence relation at every time step to prcess a sequence:
$h_ t = f_ 2 (h_ {t-1}, x_ t)$


**Recurrent Neural Networks Summary**:

- Useful for language modeling and time-series data
	- long short-term memory (LTSM)

- Multiple copies of the network – internal state is passed between these copies

- Signals can propagate through a layer more than once, potentially infinitely

- Data can flow in any direction

### Deep Learning in Biomedical Research



## L20: Deep Learning
====


## Reinforcement Learning

|![](https://www.guru99.com/images/1/082319_0514_Reinforceme2.png)|
|:-:|
|[© Daniel Johnson](https://www.guru99.com/reinforcement-learning-tutorial.html)|

|![](https://www.researchgate.net/profile/Athman-Bouguettaya/publication/317160630/figure/fig2/AS:667604691742749@1536180770838/The-Reinforcement-Learning-Framework.png)|
|:-:|
|[© Hongbign Wang](https://www.researchgate.net/publication/317160630_Integrating_Reinforcement_Learning_with_Multi-Agent_Techniques_for_Adaptive_Service_Composition)|

[Introductions for Matlab](https://www.mathworks.com/campaigns/offers/reinforcement-learning-with-matlab-ebook.html?gclid=Cj0KCQjwl7qSBhD-ARIsACvV1X1ZYlSWTdJc-Rj1tAfhXD23OzP8EzNJNzrrxwAX6iQWYUUSzTIuqEcaAjU_EALw_wcB&ef_id=Cj0KCQjwl7qSBhD-ARIsACvV1X1ZYlSWTdJc-Rj1tAfhXD23OzP8EzNJNzrrxwAX6iQWYUUSzTIuqEcaAjU_EALw_wcB:G:s&s_kwcid=AL!8664!3!378536967499!e!!g!!reinforcement%20learning&s_eid=psn_76888626426&q=reinforcement%20learning)


Reinforcement learning is a machine learning training method based on **rewarding desired behaviors** and/or **punishing undesired ones**. In general, a reinforcement learning agent is able to **perceive and interpret its environment**, take actions and learn through trial and error[Joseph M. Carew,](https://www.techtarget.com/searchenterpriseai/definition/reinforcement-learning).



- Reinforcement learning, also called **neuro-dynamic programming** and **approximate dynamic programming** [^Bertsekas_1996][^Sutton_1998], a goal-oriented algorithm, refers to a class of techniques for training a computational agent (also called controller, robot, or player) to successfully interact with the environment to **attain specifically defined goals**. As an agent takes actions within its environment, an **iterative feedback** looping of reward and state trains the agent during time to better accomplish the goals
- Reinforcement learning learns how to attain **a complex objective** or **maximize along** a particular dimension during many time steps. The key feature is that the agent operates **in a delayed return (i.e., reward) environment**, such that it is not obvious to understand which action leads to which result during many time steps. Thus, reinforcement learning aims at correlating immediate actions with the delayed returns produced by such actions

[^Bertsekas_1996]: Bertsekas DP, Tsitsiklis JN. Neuro-dynamic programming. Athena Scientific, 1996.
[^Sutton_1998]: Sutton RS, Barto AG. Reinforcement learning: An introduction. MIT Press, 1998.


### General Reinforcement Learning Workflow

*[RL]: Reinforcement Learning

- In reinforcement learning (RL), the RL agent solves a sequential decision-making problem by learning new experiences through a trial-and-error approach. An RL agent is trained by its actions interacting with the environment to maximize the cumulative reward resulting from the interactions. Generally, An RL algorithm is modeled and solved based on the Markov decision process (MDP) theory [^Sutton_1998], there is an R packege MDPtoolbox that can be applied to implement MDP
- The learning of an agent is a sequential process, where interactions with the environment occur at discrete time steps t = 0, 1, 2, ...., such that in a typical RL iteration at time step t, the agent receives the environment’s state (i.e., s~t~) and selects an action (a~t~) to interact. The environment responds to the action a~t~ and progresses to a new state s~t+1~ at next iteration at time step t+1
- The reward r~t+1~ that the agent receives for the selected action a~t~ associated with the transition (s~t~, a~t~, s~t+1~) is also determined [^Sutton_1998]. Accordingly, after each RL iteration, the agent updates (state-)value function V(s~t~) and action-value function Q(s~t~, a~t~) based on a control policy π, which is a function that maps s~t~ ∈ S to a~t~ ∈ A, i.e., π: S → A ⇒ a~t~ = π(s~t~) [^Kaelbling_1996]
- The objective of the RL agent is to iteratively learn (i.e., attain) an optimal control policy π* that maximizes the expected umulative reward (i.e., expected return) received


[^Kaelbling_1996]: Kaelbling P, Littman ML, Moore AW. Reinforcement learning: A survey. J Arti. Intell Res., 1996;4:237-285.

### Deep Reinforcement Learning

|![](https://quantdare.com/wp-content/uploads/2018/11/image4-800x365.png)|
|:-:|
|[© Luis Campos; 2018](https://quantdare.com/deep-reinforcement-trading/)|
