---
toc: true
url: idtracker
covercopy: © Karobben
priority: 10000
date: 2023-01-24 16:41:05
title: "IdTrackerAI"
ytitle: "IdTrackerAI"
description: "IdTrackerAI"
excerpt: "IdTrackerAI is an automated tracking software that uses deep learning algorithms to track individual animals in videos, even in challenging conditions such as occlusions and interactions between animals. The software can be used to extract a variety of metrics, including animal trajectories, activity levels, and social behavior, making it a useful tool for behavioral research in fields such as ecology, neuroscience, and psychology. <a title='ChatGPT'>Who sad this?</a>"
tags: [Bioinformatics, Machine Learning]
category: [Biology, Bioinformatics, Software, more]
cover: "https://s1.ax1x.com/2023/01/25/pSt1TnH.png"
thumbnail: "https://s1.ax1x.com/2023/01/25/pSt1TnH.png"
---

## Set up/Install

[Documentation](https://idtracker.ai/en/latest/user_guide/installation.html)

how to install correct pytorch and cuda: https://pytorch.org/get-started/previous-versions/

```bash
conda create -y --name idtrackerai python=3.7 Tensorflow=2.0.0 cudatoolkit=11.3.1 pytorch=1.10.0
conda activate idtrackerai
pip install "idtrackerai[gui]"
```

## General information for utility

![IDtracker.AI](https://s1.ax1x.com/2023/06/28/pCwm69f.png)

As shown above, the interface is very user-friendly. It can be divided into six regions:

1. Video Load
2. Arguments for Tracking
3. Arguments for Object Segmentation:
    - Blob Intensity: This represents the threshold of the targets based on the grey value, which ranges from 0 (dark) to 255 (light).
    - Blob Area: This is the area of the object, measured in pixels.
4. Tracking Related Arguments
5. Number of Objects and their corresponding sizes: Objects that are significantly larger than others usually indicate occlusion from multiple targets.
6. Area to illustrate the segmentation results for the current frame.


First, we use this interface to select the most appropriate parameters and `Save parameters` as a **.toml file. Then, we simply need to run the following command:
```bash
idtrackerai --load mix.toml --track
```
This command will load the parameters from the .toml file and initiate the tracking process.



## Idtracker Data analysis

```python
import numpy as np
import trajectorytools as tt
import matplotlib.pyplot as plt

trajectories_file_path = 'trajectories/trajectories_wo_gaps.npy'
trajectories_dict = np.load(trajectories_file_path, allow_pickle=True).item()
trajectories = trajectories_dict['trajectories']
tr = tt.Trajectories.from_positions(trajectories)


fig, ax_trajectories = plt.subplots(figsize=(5,5))
frame_range = range(13883) 

for i in range(tr.number_of_individuals):
    ax_trajectories.plot(tr.s[frame_range,i,0], tr.s[frame_range,i,1])
    ax_trajectories.set_aspect('equal','box')
    ax_trajectories.set_title('Trajectories',fontsize=24)
    ax_trajectories.set_xlabel('X (BL)',fontsize=24)
    ax_trajectories.set_ylabel('Y (BL)',fontsize=24)
fig.savefig("trajectory2.png")
```


![Trajectory](https://s1.ax1x.com/2023/01/25/pSt1TnH.png)

With video

```python
import cv2
from matplotlib import colors

Palette = ["#B03D3B", "#B86C3D", "#BF8040", "#ACC144", "#78C144", "#47C291", "#478BC2", "#4760C2", "#574BC3", "#834BC3", "#C34BAB", "#C14465", "#DEB59C", "#D7DF9F", "#A7DF9F", "#9FDFD9", "#A3B3E0", "#D0A3E0", "#E2A7CD", "#361712", "#1A3913", "#132B39", "#2D1339", "#391330"]
Num = 0
#V_loc = '/mnt/Ken_lap/Vlog/upload/promE-GFP/20210622_promE-GFP_C0074_Trim.mp4'
V_loc = '/mnt/Ken_lap/Vlog/upload/promE-fru-IR-v330035/20220116-promE-v330035-298d-C0379_Trim-2.mp4'
#V_loc = '/mnt/Ken_lap/Vlog/upload/elav-GS-fru-IR-V330035/20220123C0394_Trim.mp4'

cap=cv2.VideoCapture(V_loc)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (1920,1080))

while (True):
  ret,frame=cap.read()
  for id in range(len(trajectories[0])):
    XY = np.array(trajectories[Num][id], dtype = int)
    C = np.array(colors.to_rgba(Palette[id]))[:-1] * 225
    cv2.putText(frame, str(id) ,(XY[0], XY[1]), cv2.FONT_HERSHEY_COMPLEX, 1, C, 2)

  #cv2.imshow("video",frame)
  Num +=1 
  out.write(frame)
  #if cv2.waitKey(30)&0xFF==ord('q'):
  #    cv2.destroyAllWindows()
  #    break

out.release()
```








```python
import numpy as np
import trajectorytools as tt
import matplotlib.pyplot as plt
import json


F = open("data/csv/20220116-promE-v330035-298d-C0379_Trim-2.mp4_.json", 'r').read()
Dict = json.loads(F)
trajectories = np.array([[Dict[i][ii]['body'][:2] for ii in np.sort([ii for ii in Dict['12'].keys()])] for i in Dict.keys()])
tr = tt.Trajectories.from_positions(trajectories)

fig, ax_trajectories = plt.subplots(figsize=(5,5))
frame_range = range(30*30) 

for i in range(tr.number_of_individuals):
    ax_trajectories.plot(tr.s[frame_range,i,0], tr.s[frame_range,i,1])
    ax_trajectories.set_aspect('equal','box')
    ax_trajectories.set_title('Trajectories',fontsize=24)
    ax_trajectories.set_xlabel('X (BL)',fontsize=24)
    ax_trajectories.set_ylabel('Y (BL)',fontsize=24)
    ax_trajectories.set_aspect(.5)


fig.savefig("20220123C0394_Trim_30.png")


import cv2
from matplotlib import colors

Palette = ["#B03D3B", "#B86C3D", "#BF8040", "#ACC144", "#78C144", "#47C291", "#478BC2", "#4760C2", "#574BC3", "#834BC3", "#C34BAB", "#C14465", "#DEB59C", "#D7DF9F", "#A7DF9F", "#9FDFD9", "#A3B3E0", "#D0A3E0", "#E2A7CD", "#361712", "#1A3913", "#132B39", "#2D1339", "#391330"]
V_list = {"20210622_promE-GFP_C0074_Trim.mp4": '/mnt/8A26661926660713/Vlog/upload/promE-GFP/20210622_promE-GFP_C0074_Trim.mp4',
    "20220116-promE-v330035-298d-C0379_Trim-2.mp4": '/mnt/8A26661926660713/Vlog/upload/promE-fru-IR-v330035/20220116-promE-v330035-298d-C0379_Trim-2.mp4',
    "20220123C0394_Trim.mp4": '/mnt/8A26661926660713/Vlog/upload/elav-GS-fru-IR-V330035/20220123C0394_Trim.mp4'}


def Video_output(Video, V_loc):
  loc = [i for i in os.listdir("data/csv") if Video in i and "json" in i][0]
  F = open("data/csv/" + loc , 'r').read()
  Dict = json.loads(F)
  trajectories = np.array([[Dict[i][ii]['body'][:2] for ii in np.sort([ii for ii in Dict['12'].keys()])] for i in Dict.keys()])
  tr = tt.Trajectories.from_positions(trajectories)

  Num = 0
  cap=cv2.VideoCapture(V_loc)
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(Video + "_30.avi", fourcc, 20.0, (1920,1080))
  
  List = []
  while Num <= 900:
    ret,frame=cap.read()
    List += [trajectories[Num]]
    List = List[-100:]
    for Trace in List:
      for id in range(len(Trace)):
        XY = np.array(Trace[id]  * (1920, 1080), dtype = int)
        C = np.array(colors.to_rgba(Palette[id]))[:-1] * 225
        cv2.putText(frame, "." ,(XY[0], XY[1]), cv2.FONT_HERSHEY_COMPLEX, 1, C, 2)

    Trace = List[-1]
    for id in range(len(Trace)):
      XY = np.array(Trace[id]  * (1920, 1080), dtype = int)
      C = np.array(colors.to_rgba(Palette[id]))[:-1] * 225
      cv2.putText(frame, str(id) ,(XY[0], XY[1]), cv2.FONT_HERSHEY_COMPLEX, 1, C, 2)

    cv2.imshow("video",frame)
    Num +=1 
    out.write(frame)
    if cv2.waitKey(30)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        out.write(frame)
        break
  cv2.destroyAllWindows()
  out.write(frame)



for Video in V_list.keys():
    Video_output(Video, V_list[Video])
```


































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
