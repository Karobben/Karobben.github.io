

[Zebra Fish](https://www.nature.com/articles/s41598-021-92854-0#Sec15)
[B-SOiD](https://www.nature.com/articles/s41467-021-25420-x#Sec10)
# YoloFly: A Machine Learning Interactive Software for Flies' Social Behavior Annotation

exampel paper [A hierarchical 3D-motion learning framework for animal spontaneous behavior mapping ](https://www.nature.com/articles/s41467-021-22970-y)

## Abstract

Animal behavior is time-series data that is both hierarchical and dynamic. Social interaction behavior would elevate the dimension to another level. Even with well-trained researchers, stereotypes and bias in behavior annotation are difficult to avoid. Consequently, if we were to leave this task to computer vision, not only would the bias be eliminated, but scientists would also be relieved of grunt work. Among the various behaviors that can be analyzed, drosophila is a popular model due to the numerous advantages it offers. But traditionally, different tools are required for video detection, data processing, statistics, modeling, and visualization in fly behavior research because the platforms are fragmented. Here, we provide a comprehensive solution for flies’ social behaviors, from a row video to a grading model to an interaction network. We also wrote a GUI interface to provide a zore-coding experience to facilitate research. Finally, we demonstrate that this framework is able to display the different social behaviors that are preferential among genotypes. With the grading model, we can also evaluate the rescue level by their behaviors. (Otherwise, it shows the capability to detect very unique-abnormal phenotypes). As a result, this platform has a great deal of potential for use in various types of social behavior, such as evaluating behavior changes and disease models.

Other works are based on different software and even personal write scripts to make statistics which makes the results between the different groups harder to compare. So, here we developed a one for all solution for accelerating the study of behavior with minimal investment. A pre-trained model using Yolov5 could detect flies and their corresponding behavior with high efficiency. After that, our pipeline could easily visualize the behavior statistics, behavior flows, social network, and their index. It could also illustrate the complicated multilayer behavior flow to monitor decision preference. We also implied scripts for personalizing the graphics and videos for helping study behavior in more ways.

to elaborate and present the interactions between flies in a group and the data. With this method, we are able to track the individual from beginning to end, recording its movement, the flies it interacted with, the properties of the interaction, and the consequence of the interactions. With these results, we can dig the information about the group, the interaction, and/or the flies, etc. This system could imply digging more new behaviors, the relationship between behavior and/or may be connected with the genes or medical treatments. (With this method, we can not only explain two paired flies but also detected and present more complicated interactions in a group).

Based on the results from the YoloFly, we transformed the raw location data into well described social interaction matrix for each fly in the single frame level. Then, a sliding window was applied based on the described data. Flies' behavior was finally quantified and the differences between flies were compared based on the sliding window in a time like 5 mins or 10 mins. The model was built based on the different genotypes. Finally, we used this model to evaluate the early tumor sample which is not showing very different from our controls. On the other hand, the level of the tumors could be evaluated based on confidence.

## Introduction

<!-- widely used of fly model -->
Drosophila model was widely used in wide range of areas like Microbiome[^douglas2018drosophila][^ludington2020drosophila], drug addiction[^kaun2012drosophila], neurodegenerative disease[^sang2005drosophila], Parkinson's disease[^whitworth2011drosophila], etc. Among them, behavior model was well studied because of well founded and easily be observed behaviors like aggressive behaviors[^yamamoto2014neuroethology] and courtship behavior[^chen2002fighting].


[^sang2005drosophila]: @article{sang2005drosophila, title={Drosophila models of neurodegenerative disease}, author={Sang, Tzu-Kang and Jackson, George R}, journal={NeuroRx}, volume={2}, number={3}, pages={438--446}, year={2005}, publisher={Springer} }
[^whitworth2011drosophila]: @article{whitworth2011drosophila, title={Drosophila models of Parkinson's disease}, author={Whitworth, Alexander J}, journal={Advances in genetics}, volume={73}, pages={1--50}, year={2011}, publisher={Elsevier} }


[^douglas2018drosophila]: @article{douglas2018drosophila, title={The Drosophila model for microbiome research}, author={Douglas, Angela E}, journal={Lab animal}, volume={47}, number={6}, pages={157--164}, year={2018}, publisher={Nature Publishing Group} }
[^ludington2020drosophila]: @article{ludington2020drosophila, title={Drosophila as a model for the gut microbiome}, author={Ludington, William B and Ja, William W}, journal={PLoS Pathogens}, volume={16}, number={4}, pages={e1008398}, year={2020}, publisher={Public Library of Science San Francisco, CA USA} }
[^kaun2012drosophila]: @article{kaun2012drosophila, title={Drosophila melanogaster as a model to study drug addiction}, author={Kaun, Karla R and Devineni, Anita V and Heberlein, Ulrike}, journal={Human genetics}, volume={131}, number={6}, pages={959--975}, year={2012}, publisher={Springer} }



<!-- fly behavior model -->

Mechanisms of fruit fly behavior were well explained[^kadow2019state]
[^kadow2019state]: @article{kadow2019state, title={State-dependent plasticity of innate behavior in fruit flies}, author={Kadow, Ilona C Grunwald}, journal={Current opinion in neurobiology}, volume={54}, pages={60--65}, year={2019}, publisher={Elsevier} }


Though the exist of emotion behavior in invertibrates like droisophila was widly debated, some scholar still believe that there are evidence show that Drosophila has emotions. Professor David J. Anderson[^anderson2014framework] talked the emotional mechanism based on the Wing gesture and repeated behaviors of drosophila. Other emotion related behavior like aggression[^hoopfer2016neural] and autism[^shpigler2017deep] shows that drosophila could have basic emotions like other animals. Other behaviors like addiction[^philyaw2022use][^kaun2011drosophila], locomotor activities, aggressive, etc are be connected with emotions.

[^kaun2011drosophila]: @article{kaun2011drosophila, title={A Drosophila model for alcohol reward}, author={Kaun, Karla R and Azanchi, Reza and Maung, Zaw and Hirsh, Jay and Heberlein, Ulrike}, journal={Nature neuroscience}, volume={14}, number={5}, pages={612--619}, year={2011}, publisher={Nature Publishing Group} }

[^philyaw2022use]: @article{philyaw2022use, title={The Use of Drosophila to Understand Psychostimulant Responses}, author={Philyaw, Travis James and Rothenfluh, Adrian and Titos, Iris}, journal={Biomedicines}, volume={10}, number={1}, pages={119}, year={2022}, publisher={Multidisciplinary Digital Publishing Institute} }

[^anderson2014framework]: @article{anderson2014framework, title={A framework for studying emotions across species}, author={Anderson, David J and Adolphs, Ralph}, journal={Cell}, volume={157}, number={1}, pages={187--200}, year={2014}, publisher={Elsevier} }

[^hoopfer2016neural]: @article{hoopfer2016neural, title={Neural control of aggression in Drosophila}, author={Hoopfer, Eric D}, journal={Current Opinion in Neurobiology}, volume={38}, pages={109--118}, year={2016}, publisher={Elsevier} }

[^shpigler2017deep]: @article{shpigler2017deep, title={Deep evolutionary conservation of autism-related genes}, author={Shpigler, Hagai Y and Saul, Michael C and Corona, Frida and Block, Lindsey and Ahmed, Amy Cash and Zhao, Sihai D and Robinson, Gene E}, journal={Proceedings of the National Academy of Sciences}, volume={114}, number={36}, pages={9653--9658}, year={2017}, publisher={National Acad Sciences} }

<!-- Social Behavior -->
Among them, social behaviors include shocial index, aggressive behavior, and courtship behavior were closestly studied because of been easy quality and quantity. Blake B. Anderson's team[^anderson2016social] illustrated that different line of drosophila has different preference of Social idstance and activities. Sexcual difference also occurs.


[^anderson2016social]: @article{anderson2016social, title={Social behavior and activity are decoupled in larval and adult fruit flies}, author={Anderson, Blake B and Scott, Andrew and Dukas, Reuven}, journal={Behavioral Ecology}, volume={27}, number={3}, pages={820--828}, year={2016}, publisher={Oxford University Press UK} }


<!-- Present tools -->
For free researchers from the label work, lots of tools and profound sorftware's were been developed. TrackFly desinged an Virtual Reality (VR) for fruit flies to studying free fly[^fry2008trackfly],

[^fry2008trackfly]: @article{fry2008trackfly, title={TrackFly: virtual reality for a behavioral system analysis in free-flying fruit flies}, author={Fry, Steven N and Rohrseitz, Nicola and Straw, Andrew D and Dickinson, Michael H}, journal={Journal of neuroscience methods}, volume={171}, number={1}, pages={110--117}, year={2008}, publisher={Elsevier} }

Drosophila has very classic and easy identifiable behaviors like aggressive-behaviors and courtship-behaviors. Because of this behavior could easily change by altering genes (ummm...) and/or environment(light toxi), they are widely be used as behavior models. Otherwise, some disease related genes which are homologous gene from human could also dramatically change the behavior makes them been an ideal medicine model.  


## Methods

### Model training

We choose Yolov5 as the platform to train our data. We applied **** well annotated pictures with ** flies, ** fly-head, ** chasing, ** wing-extend, and **  grooming. We using the Loni server to train the data with 1280*1280 size, 20 batch size, and 1200 epochs. Before the training, pictures are argument with script "png_argument.py" to generate a set of rotated, dim and brightened, flipped, and mozac masked.

### Tracking and Head-bind

The tracking algorithm is achieved by the nearest position sort between adjacent detected flies. We determined the flies and given IDs for each fly. And then, the position of the flies for the next frame was identified and paired with the all flies from previous frame. The distance of paired was calculated and sorted. The ID was inherited from the previous frame from the first paired showed by following the sorted pair list if the distance is lesser than a given threshold. Otherwise, the flies ID are remained on position from previous frame until there is a Non-ID flies fall into the threshold.

Head-bind is different from the tracking. The head is paired with the flies when it is in the fly-rectangle box. The bind was determined when the pair was unique. When there are two head in one fly-rectangle, we assign the unique pair first. When two flies overlapped together and two head is in the overlap arear, we assign the head to the nearest one.

### Post-data Analysis

#### Grooming, Wing-Extend

Grooming is indipendent behavior. Wine-Extend could have different meanings. During the courtship, wine-extend stands for the affections and which also be interpretered as sing. In male-male aggressive behavior, wing-extend stands for the threads. In somee case, we can also detect the win-extend in the resing and leaping. In some rare case, we can even detect the random wing-extend for the extremely excited flies. Anyway, in the male-male copulation case, we'll detect the flies nearby. When there are flies on the head or side of the wing-extend fly, we define it as singing. When there are only a closing flie on the back of it, we characterize it as wing-thread. When there are no flies arround, we ignore it.

#### Chasing Events, Chaining, and Copulation
Chasing and copulation calibration was achived by identify the flies in the Chasing-rectangle at first. We sort the files on the Chasing-rectangle and find the most overlapped two flies which overlape arear is larger than 80%. If failed, we characterize it as false positive.

In each frame, we calculate the overlap-areas of the Chasing-rectangle and keep the pair when they share more them 30% compared to the small one. After that, we use the data identified above to check the files in those boxes. If there are a shared one and only one fly, we characterize it as chaining.

#### Flies' detect area and the relative position calculation

The direction of the fly was represented by an arrow witch from the center of the fly-rectangle toward the center of the head-rectangle. Two circle was been draw and the intersect points (h1 and h2) of the two circle help to calculated the position of the flies. The positive result would be when the sum of distance from the target flies to the two intersect points (h1 and h2) and head, which given it a fan like scan area.

#### Behavior Description and Sliding Window

After the location data transformed to the summary data like speeds, raltive angles, behaviors was clissified to the Table 1. according the to the dicession tree (Pic?). After the annotation for each fram, 30 frame were choosen for summary to a behavior. The behavior domominent into this window would be sleected to stands for this window. When there are mixed behavior in the window, it would be described as "mix".

#### Aggressive Events
$$
AG_ i = \frac{(1 - \frac{Rest_ i}{Total_ i}) }{ \sqrt{\frac{\sum_ {i=1}^{n}  Total_ i^ 2}{n -1}} }
$$

$$
VA = scale(Dis_ {aw})
$$



$$
Z = \frac{x_ i- \mu}{\sigma} = \frac{x_ i - \mu}{ \sqrt{\frac{\sum_ {i=1}^{n}  (x_ i  - \mu )^ 2}{n -1}}}
$$

$$
Z = \frac{x_ i }{ \sqrt{\frac{\sum_ {i=1}^{n} x_ i^ 2}{n -1}}}
$$


Head buds, Aggressive index? Fighting result.
#### Interactive Software
Kivy2

### Variation of the Result

For the perfomance of the fly detection, we compare a few videos with different chasing index and number of the correct flies from the all videos.
For the head-bind, leaping, chasing, sing, copulating, etc, we randomly extract 100 events from video and validate the result manully.


## Result

### customized Model

The model was trained for more than 3 days by using loni server which has 6 GPU nodes and each one has 2 V100 GPUs. We annotate 6 classes which are 'fly', 'fly-head', 'grooming', 'chase', 'singing', and 'copulation' for training. Diffusion matrix (1A) shows the fly hand fly head has the highest grades. Grooming and copulation are lower but still higher than .3 which is acceptable. Annotated videos would show the box which corresponded with classes and fly's ID which is the results of tracking. Motion Kinetics plot illustrates that the activation cycle of flies is around 10 mins. Hence, we select 10 mins around the peak as each sample for the next studies. Some video has been trapped into a few samples by selecting different peaks. Finally, we write the GUI platform to the user-friendly.


### Behavior Statistics

AB: Details of individuals → General statistics


After a minimal calculation, the behavior would be mapped into flies by calculating the overlap region. Visualization of individual behaviors and general statistics could be achieved by implied scripts. Flies and behavior events are recorded as boxes with position and size. Flies and behaviors could be easily achieved by giving corresponded ID while using the visualization scripts (Figure 2A). Except for the individual flies' behavior, we can also visualize Chasing events by giving the Chasing ID. The whole process of Chasing would be visualized in a graph or output as a gif/video. In Drosophila melanogaster, Wing extension could not only mean courtship singing but also threatening. Luckily, the wing extending patterns are different from them. Most differences are in duration and frequency. Figure D shows a pair of fly wing-extending events. The green one is courtship singing to the red one. The red one is threatening the green to expel it. This difference could be used to model the wing-threaten and courtship-sing. This behavior is also variable between different genotypes (Fig2, C).  In those behaviors, another very important courtship behavior is chaining which can not be detected by the pre-trained model. But it would be very easy to tell if there is a fly chasing another one while being chasing. By doing that measurement, we can tell where, when, and how many chaining events happen in each frame(figure2 D). Primary data records the body and head of flies which are used to turn flies into a vector. Now we can calculate the relative position of flies and their chasing preference. After the statistics, we can have general interaction information about each independent experiment based on histograms(Figure 2, E). We can also illustrate the behavior on a plate to find beautiful moving and interaction patterns (Figure 2F). By corresponding the regions on the plate with the center plenty area or food region, we can easily demonstrate the preference of the flies. This could all help us understand the preference of the flies and the difference between treatments.


### Interactoin Network

Flies in a Petri dish shows different. Here we recorded the interactions between all flies in each Petri dish.

- Fly's interaction network: Some flies may never be interested or noticed some flies. But in some cases, flies are more eager to move, to chase/courtship other flies which made the interaction network different between phenotypes. Interaction Times and duration could be used to describe the network index. Here we should that the Difference in ... In GFP, most interaction was actually caused by random exploring. One fly is roaming and had physical contact with another one and ends up leaving in a very short turn.

- Fly's long-duration network: As a result, when we look at long-time Interaction among different genotypes, the difference was dramatic. The differences in an index between Genotypes also show significant differences. Expect Network index, social distance is another well-studied area. In this way, the nearest distance of each fly was recorded and the distance is variety among lines and genotypes.

- Social Index: In our result, .................. Except social distanc, pairwise distance could be also used to illustrate the iinteraction index among flies................... let's see how it worked.
- Center region: Finally, the center. Some studies prefer to put the food at the center. As the result, flies on the center could be recorded as the time they stay on the food. Other research believe that flies has autism related behavior are more sty on the edge of the petridish rather than center, which could also illsutrate the difference between them. In this suty, the circle was auto fit and the percentage of the diameter was by given manully. We can clearly see that ................... do the statistics.

### Behavior

- Behavior decision tree (Figure 4A). Behavior was determined by the logic shown in the tree. Here we designed 21 behavior in total some of them are related to social interaction, and some of them are solo movements only. Unfortunately, we can not tail the difference between aggressive chasing and courtship due to their similarities. On the other hand, aggression and singing could show at the same time on the same individual when one flies in courtship chasing another while being chased by another. In this case, it could express courtship-sing for a while and then wing-threaten to the one on the back. Mixed behavior makes it hard to make a concrete answer for the type of chasing. As a result, most behavior except wing-extend could not tell whether it is courtship-derived or aggressive-derived.
- Afther behaviors are annotated, we then using sliding window to smooth jitter. The window size was been choosed by 30 frame which is one second. After smoothened by sliding window, we still kept some instance behaviors like jump/fly, grooming, and sing. Those behaviors were coud happened in a single frame and are very important for flies.
- Another important thing bothering research is the behavior varity among individuals. Here we impplied a hierarchy clust based on the counts of each behavior from the flies and select the most dominant group for the rest of compairetiong (Figure 4 B2). The same data was dimension-redundant by PCA shows at Fig4 B2 was conresponded with experimental exceptation.
- Aftering the excluding of outliers, the whole behavior map was show in Figure 4 C. The different bewteen groups are visualize and are dromatic among groups. Fig4 C2 and C3 shows the result from Hnf4 and contral group. Here The motion was been seperated into 4 classes, 0 to 4, which is decided by the moving speed of the fly. Color are corresponded to different behaviors. It is clearly viewed that the Hnf4 has more Sing behavior. And purposes color which is resting are also less show in the Hnf4 Group.
- Finally, those data would be different enough by accrosing genotypes. We selected the most different behaviors by the calculate the contribution among GFP and HNF4 group. After that, we selected ....... to build an logistic model whit the score of ****. Now, we can use this model to grading the rescue group and find most of individuals are good enough to be say that they are been rescueted. Also, the results of Umap and hierarchy clust based on the high contribution behaviors are shows the result are highly reliable.

### Bahvior flow, decision make for flies.

Some research studed that the decision pereference of each flies. But most of them stopped at a binary level. Traditionally, they are given flies only two choosies, yes/no, left/right. For example, the Y maze veriflied that flies has left preferencing. The phoneactive gene make flie became aggression when the ligth is one. Very few studies tried a higher level or multiple level of behavior changes. One thing is because previous methods are hard to record different to interprate so complex interactions in a group. As the same time, with the increasing of dimension, the posibilities of combination turns to infinity. Here we shows that the behavior could be present as a multilayer flow whish as poteintial to change the behavior analysis. flies are similar in the first layer of decision making from different genotypes and the different is not significant. But with the increasing of the the flow, the difference was increased and the phenotypes are different.

- Behavior response also has huge different from genotypes to genotypes. Here we present to

### Behaviors Sheet

|Group|Behavior|Abbr. | Description|Citation|
|:-|:-|:-|:-|:-|
|Aggressive/Courtship|√Sing/Wing Threads|ACST| Flappy wings when two flies head against each other|
|Aggressive|Against/Push|PUSH| Two flies head against each other and continue moving ahead with a very small angle|
|Defensive/Courtship|Walk away|DCW| loser in fighting or rejection in courtship|
|Defensive/Courtship|Run away|DCR| loser in fighting or rejection in courtship|
|Defensive/Courtship|fly/leap away|DCF| loser in fighting or rejection in courtship|
|Aggressive/Courtship|Fencing/Touch|ACFT|Two flies' head against to each other|
|Courtship|Chaining|CC|Three or more flies chasing each other to form a chain or circle|
|Defensive/Courtship|Wing Threats|ACWT|Flie is sing when it is been chasing but not target to its head|
|Defensive/Courtship|Do nothing|DCDN|Loser fly doesn't responsible to the aggressive, or female show no clear rejection during courtship|
|Courtship|√(Attempts) Mounting|CM|The male bends its abdomen and (try to) hold the females|
|Aggressive/Courtship|Orientation|ACO |male crab walk to circling the female  without sing|
|Aggressive/Courtship|Orientation with sing|ACOS |male crab walk to circling the female with sing|
|Aggressive/Courtship|√Sing|ACS| Wing movements toward other flies|
|Aggressive/Courtship|√Chasing|ACC|One fly chase after another towards to body or abdomen|
|Aggressive/Courtship|Gentle Tapping/Lick/Push| ACT|male behind/on the side the other with minimal movements|
|Social|Walk/Run/Leap| SCW/SCR/SCL |Walk/Run/Leap in a group||
|Social|Feed| SCF | Eating Foods in a group||
|Social|Resting| SCRT |Not moving; Grooming or Sleep in a group|
|Solo|Walk/Run/Leap| SOW/SOR/SOL |Walk/Run/Leap alone||
|Solo|Feed| SOF| Eating Foods alone||
|Solo|Resting|SORT|Not moving; Grooming or Sleep alone|




Behaviors-sheet reference from Courtship behaviors[^jonsson2011sound][^revadi2015sexual][^yamamoto2014neuroethology] and aggressive behaviors[^chen2002fighting]

[^jonsson2011sound]: @article{jonsson2011sound, title={Sound production during agonistic behavior of male Drosophila melanogaster}, author={Jonsson, Thorin and Kravitz, Edward A and Heinrich, Ralf}, journal={Fly}, volume={5}, number={1}, pages={29--38}, year={2011}, publisher={Taylor \& Francis} }

[^revadi2015sexual]: @article{revadi2015sexual, title={Sexual behavior of Drosophila suzukii}, author={Revadi, Santosh and Lebreton, S{\'e}bastien and Witzgall, Peter and Anfora, Gianfranco and Dekker, Teun and Becher, Paul G}, journal={Insects}, volume={6}, number={1}, pages={183--196}, year={2015}, publisher={Multidisciplinary Digital Publishing Institute} }

[^yamamoto2014neuroethology]: @article{yamamoto2014neuroethology, title={Neuroethology of male courtship in Drosophila: from the gene to behavior}, author={Yamamoto, Daisuke and Sato, Kosei and Koganezawa, Masayuki}, journal={Journal of Comparative Physiology A}, volume={200}, number={4}, pages={251--264}, year={2014}, publisher={Springer} }


[^chen2002fighting]: @article{chen2002fighting, title={Fighting fruit flies: a model system for the study of aggression}, author={Chen, Selby and Lee, Ann Yeelin and Bowens, Nina M and Huber, Robert and Kravitz, Edward A}, journal={Proceedings of the National Academy of Sciences}, volume={99}, number={8}, pages={5664--5668}, year={2002}, publisher={National Acad Sciences} }


### Working Flow The performance of the Models

### Individual behavior

### Paired Analisys

### Group Analysis

- Group behavior
- Classification

### Experiment

### Discussion


## Data Availability
## Code Avaliability
## Additional

## Reference



'''
To recognize the effect of cancer on social behavior, we first use YoloFly to detect and track the fruit flies. We trained a Yolo v2 model with two classes, fly and background. The input size is 640x480 and the training dataset contains around 500 images. After training, we tested the model on some random images and compared it with manual annotation. We did not find any significant difference between the machine learning model or the manual annotation.

To analyze the effect of cancer on social behavior, we compared cancer flies with normal flies. In an experiment, we put two fruit flies in a small cage (10cm x 10cm) for 10 minutes and record how they interact with each other using a camera mounted above the cage. Then we use YoloFly to track every single fly in each frame and generate a csv file that records every position of each fly for 10 minutes (600 frames). Then we developed several simple rules to calculate how far they kept from each other, how much time they stayed together, whether they touched each other or not, etc. After all these data was collected for about 10 groups of flies, we plotted these data into histograms, scatter plots and pie charts to analyze them by hand.
'''
