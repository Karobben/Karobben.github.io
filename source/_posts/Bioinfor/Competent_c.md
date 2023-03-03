---
title: "Calcium Competent Cells"
date: 2020/06/29
description: "How to Make Calcium Competent Cells"
url: ca_competent
toc: true
excerpt: "Calcium competent cells are bacterial cells that are treated with calcium chloride to increase their ability to uptake plasmid DNA. The calcium ions disrupt the cell membrane and make it more permeable to DNA, increasing the efficiency of transformation. These cells are commonly used in molecular biology experiments to introduce foreign DNA into bacterial cells. <a title='GhatGPT'>Who said this?</a>"
tags: [Biology, Cell, Wet]
category: [Biology, Wet Protocol]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 6
---

## Making Calcium Competent Cells

```mermaid
graph TB
DH5((DH5α))
LB_p(LB plate)
LB_l(LB starter)

LB(LB 1 L)

Centrifuge2(Centrifuge)

ice(ice bath 20-30 minutes)
ice2(ice bath 20 minutes)
Ca(CaCl2)
CaCl2(85 mM CaCl2, 15% glycero)
Eptube(1.5 ml Ep tube )
     subgraph Day 1
     DH5-->|Streak & over night|LB_p
     end
     subgraph Day 2
     LB_p-->|over night| LB_l
     end
     subgraph Day 3
     LB_l-->|10 ml 37C|LB
     LB-->|OD600 reaches 0.35-0.4|ice
     ice-->|Harvest: 3000g, 15 min, 4C|Centrifuge
     Centrifuge-->|Decant the supernatant|pellet
     MgCl2-->|100 mL resuspend|pellet
     pellet-->|Harvest: 2000g, 15 min, 4C|Centrifuge2
     Centrifuge2-->|Decant the supernatant|pellet2
     Ca-->|100 mL resuspend|pellet2
     pellet2-->ice2
     ice2 --> |Harvest: 2000g, 15 min, 4C|Centrifuge3
     Centrifuge3-->|Decant the supernatant|pellet3
     CaCl2-->|50 mL resuspend|pellet3
     pellet3-->|Harvest: 1000g, 15 min, 4C,Decant the supernatant|pellet4
     CaCl2-->|2 ml|pellet4
     pellet4-->|OD600|200-250
     200-250-->|Aliquot 50 μL|Eptube
     Eptube-->|liquid nitrogen to -80C|Store
     end
```
Preparing for Day 2:

**Chill overnight at 4°C**:
100 mM CaCl2
100 mM MgCl2
85 mM CaCl2, 15% gly  cerol v/v
Centrifuge rotor  


## Day 1

1. Streak out frozen glycerol stock of bacterial cells (Top10, DH5α, etc.) onto an LB plate (<span style="background:salmon">no antibiotics since these cells do not have a plasmid in them</span>). Work sterile. Grow plate overnight at 37°C.



## Day 2
1. **Autoclave**:
1 L LB (or your preferred media)
1 L of 100 mM CaCl2
1 L of 100 mM MgCl2
100 mL of 85 mM CaCl2, 15% glycerol v/v
4 centrifuge bottles and caps
Lots of microfuge tubes

2. **Chill overnight at 4°C**:
100 mM CaCl2
100 mM MgCl2
85 mM CaCl2, 15% glycerol v/v
Centrifuge rotor

3. Prepare starter culture of cells
Select a single colony of E. coli from fresh LB plate and inoculate a 10 mL starter culture of LB (or your preferred media – no antibiotics). Grow culture at 37°C in shaker overnight.

Notes:
• You will have extra CaCl2 and MgCl2. These solutions can be saved and reautoclaved for the next time you make competent cells.
• You can also substitute other media like SOB, 2xYT, etc. for the LB if you prefer.
• All glassware should be detergent free. Presence of detergent reduces
competency of cells.

## Day 3
1. Inoculate 1 L of LB media with 10 mL starter culture and grow in 37°C shaker. Measure the OD600 every hour, then every 15-20 minutes when the OD gets above 0.2.

2. When the OD600 reaches 0.35-0.4, immediately put the cells on ice. Chill the culture for 20-30 minutes, swirling occasionally to ensure even cooling. Place centrifuge bottles on ice at this time.

    <span style="background:salmon">**IMPORTANT NOTES**</span>:
    • It is important not to let the OD get any higher than 0.4. The OD should be carefully monitored and checked often, especially when it gets above 0.2, as the cells grow exponentially. It usually takes about 3 hours to reach an OD of 0.35 when using a 10 mL starter culture.
    • It is also very important to keep the cells at 4°C for the remainder of the procedure. The cells, and any bottles or solutions that they come in contact with, must be pre-chilled to 4°C.

3. (Spin #1) Split the 1 L culture into four parts by pouring about 250 mL into ice cold centrifuge bottles. Harvest the cells by centrifugation at 3000g (~4000 rpm in the Beckman JA-10 rotor) for 15 minutes at 4°C.
4. Decant the supernatant and gently resuspend each pellet in about 100 mL of ice cold MgCl2. Combine all suspensions into one centrifuge bottle. Make sure to prepare a blank bottle as a balance.
5. (Spin #2) Harvest the cells by centrifugation at 2000g (~3000 rpm in the Beckman JA-10 rotor) for 15 minutes at 4°C.
6. Decant the supernatant and resuspend the pellet in about 200 mL of ice cold CaCl2. Keep this suspension on ice for at least 20 minutes. Start putting 1.5 mL microfuge tubes on ice if not already chilled.
7. (Spin #3) Harvest the cells by centrifugation at 2000g (~3000 rpm in the Beckman JA-10 rotor) for 15 minutes at 4°C. At this step, rinse a 50 mL conical tube with ddH2O and chill on ice.
8. Decant the supernatant and resuspend the pellet in ~50 mL of ice cold 85 mM CaCl2, 15% glycerol. Transfer the suspension to the 50 mL conical tube.
9. (Spin #4) Harvest the cells by centrifugation at 1000g (~2100 rpm in the Beckman GH-3.8 rotor) for 15 minutes at 4°C.
10. Decant the supernatant and resuspend the pellet in 2 mL of ice cold 85 mM CaCl2, 15% glycerol. The final OD600 of the suspended cells should be ~ 200-250.
11. Aliquot 50 μL into sterile 1.5 mL microfuge tubes and snap freeze with liquid nitrogen. Store frozen cells in the -80°C freezer.


---
Advocation:

This protocol belongs to [berkeley.edu 2008](http://mcb.berkeley.edu/labs/krantz/protocols/calcium_comp_cells.pdf). I just gently reset part of the sentences.
If there are any offensive behaviors, please contact <a mailto="a591465908@outlook.com">me</a> and I'll delete it
