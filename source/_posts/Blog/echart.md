---
title: "eChart is fun"
description: "How to start with Echart"
date: 2021-02-01
url: echart
toc: true
excerpt: "Insert Echart into hexo blog!"
tags: [Plot, nCov, Python]
category: [Python, API]
cover: 'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/zh/images/index-home-pie.png'
thumbnail: 'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/zh/images/index-home-pie.png'
priority: 10000
covercopy: '© Apache ECharts'
---

## eChart is fun

Official examples: [Apache ECharts](https://echarts.apache.org/zh/index.html)

请移步[博客](https://karobben.github.io/2021/02/01/Blog/echart/)阅读, 不然只能是一堆乱码...
## Install eChart


```bash
git clone https://github.com/apache/echarts.git
```

Than, you can using it as the instructions written by [Quest_sec 2020](https://blog.csdn.net/Quest_sec/article/details/105612523)

## Running it in hexo

```bash
npm install hexo-tag-echarts3 --save
```

Standard Code model:
```hexo
{% echarts 400 '85%' %}
{% endecharts %}
```

and then, insert codes below
```hexo
{% echarts 400 '85%' %}
{
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['利润', '支出', '收入']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'value'
        }
    ],
    yAxis : [
        {
            type : 'category',
            axisTick : {show: false},
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    series : [
        {
            name:'利润',
            type:'bar',
            itemStyle : {
                normal: {
                    label: {show: true, position: 'inside'}
                }
            },
            data:[200, 170, 240, 244, 200, 220, 210]
        },
        {
            name:'收入',
            type:'bar',
            stack: '总量',
            itemStyle: {
                normal: {
                    label : {show: true}
                }
            },
            data:[320, 302, 341, 374, 390, 450, 420]
        },
        {
            name:'支出',
            type:'bar',
            stack: '总量',
            itemStyle: {normal: {
                label : {show: true, position: 'left'}
            }},
            data:[-120, -132, -101, -134, -190, -230, -210]
        }
    ]
};
{% endecharts %}
```

This is how it looks like from the codes above:

{% echarts 400 '85%' %}
{
   tooltip: {
       trigger: 'axis',
       axisPointer: {            // 坐标轴指示器，坐标轴触发有效
           type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
       }
   },
   legend: {
       data: ['利润', '支出', '收入']
   },
   grid: {
       left: '3%',
       right: '4%',
       bottom: '3%',
       containLabel: true
   },
   xAxis: [
       {
           type: 'value'
       }
   ],
   yAxis: [
       {
           type: 'category',
           axisTick: {
               show: false
           },
           data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
       }
   ],
   series: [
       {
           name: '利润',
           type: 'bar',
           label: {
               show: true,
               position: 'inside'
           },
           emphasis: {
               focus: 'series'
           },
           data: [200, 170, 240, 244, 200, 220, 210]
       },
       {
           name: '收入',
           type: 'bar',
           stack: '总量',
           label: {
               show: true
           },
           emphasis: {
               focus: 'series'
           },
           data: [320, 302, 341, 374, 390, 450, 420]
       },
       {
           name: '支出',
           type: 'bar',
           stack: '总量',
           label: {
               show: true,
               position: 'left'
           },
           emphasis: {
               focus: 'series'
           },
           data: [-120, -132, -101, -134, -190, -230, -210]
       }
   ]
};

{% endecharts %}



## Line chart

```echart

{% echarts 400 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Time',
        nameLocation: "middle",
        nameTextStyle: {fontSize: "2rem"},
        data: [1,2,3,4,5,6,7,]
    },
    yAxis: {
        type: 'value',
        name: "Velacity",
        nameLocation: "middle",
        nameTextStyle: {fontSize: "2rem",
            padding: [0, 0, 20, 0] ,
        },
    },
    series: [{
        data: [150, 230, 270, 285, 290, 295, 297],
        type: 'line'
    }]
};
{% endecharts %}
```


{% echarts 400 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Time',
        nameLocation: "middle",
        nameTextStyle: {fontSize: "2rem"},
        data: [1,2,3,4,5,6,7,]
    },
    yAxis: {
        type: 'value',
        name: "Velacity",
        nameLocation: "middle",
        nameTextStyle: {fontSize: "2rem",
            padding: [0, 0, 20, 0] ,
        },
    },
    series: [{
        data: [150, 230, 270, 285, 290, 295, 297],
        type: 'line'
    }]
};
{% endecharts %}


## Details for Echart

### The name of axis

==info==: In hexo widget, the you can give a `int` value to the `fontSize`. `2rem` is not supported.  
```css
xAxis: {
    type: 'category',
    name: 'Time',
    nameLocation: "middle",
    nameTextStyle: {fontSize: "2rem"},
```


{% echarts 200 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Time',
        nameLocation: "middle",
        nameTextStyle: {fontSize: 30,
          padding: [10, 0, 0, 0]},
        data: [1,2]
    },
    yAxis: {
    },
    series: [{
        data: [0, 20],
        type: 'line'
    }]
};
{% endecharts %}


### Multiple Lines with legend

```css
{% echarts 400 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Time',
        nameLocation: "middle",
        nameTextStyle: {fontSize: 30,
          padding: [10, 0, 0, 0] ,
            },
        data: [0,1,2,3,4,5,6,7,]
    },
    yAxis: {
        type: 'value',
        name: "Velacity",
        nameLocation: "middle",
        nameTextStyle: {fontSize: 30,
            padding: [0, 0, 10, 0] ,
        },
    },
    legend: {
        data: ['Measured Velocity', "Expected Velocity"]
    },
    series: [{
        name: 'Measured Velocity',
        data: [0, 150, 230, 270, 285, 290, 295, 297],
        type: 'line'
    },
    {
        name: "Expected Velocity",
        data: [, 150, 230, 310],
        type: 'line'
    }]
};
{% endecharts %}
```

{% echarts 400 '85%' %}
option = {
    xAxis: {
        type: 'category',
        name: 'Time',
        nameLocation: "middle",
        nameTextStyle: {fontSize: 30,
          padding: [10, 0, 0, 0] ,
            },
        data: [0,1,2,3,4,5,6,7,]
    },
    yAxis: {
        type: 'value',
        name: "Velacity",
        nameLocation: "middle",
        nameTextStyle: {fontSize: 30,
            padding: [0, 0, 10, 0] ,
        },
    },
    legend: {
        data: ['Measured Velocity', "Expected Velocity"]
    },
    series: [{
        name: 'Measured Velocity',
        data: [0, 150, 230, 270, 285, 290, 295, 297],
        type: 'line'
    },
    {
        name: "Expected Velocity",
        data: [, 150, 230, 310],
        type: 'line'
    }]
};
{% endecharts %}


#### lineStyle

<pre>
{
  type: "line",
  smooth: false,

  lineStyle: {type: "dotted",}
}
</pre>

==info==: In hexo chart, you can't assign `lineStyle` directly. But we can include it in `intemStyle`

`lineStyle` in hexo:

```css
itemStyle:{
               normal:{
                   lineStyle:{
                       width:2,
                       type:'dotted'  //'dotted'虚线 'solid'实线
                   }
               }
           },
```


## Bugs

- [ ] can't assign variables before plot

### Barchart

- [ ] can't show labels in serious

exp for labels:
```
label: {
  show: true,
  rotate: 90,
  align: 'left',
  verticalAlign: 'middle',
  position:  'insideBottom',
  formatter: '{c} | {a}',
  distance: 15
},
```
