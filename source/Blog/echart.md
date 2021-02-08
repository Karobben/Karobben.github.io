---
title: "eChart is fun"
description: "How to start with Echart"
url: echart
---

# eChart is fun

Official examples: [Apache ECharts](https://echarts.apache.org/zh/index.html)

# Install eChart

```bash
git clone https://github.com/apache/echarts.git
```

Than, you can using it as the instructions written by [Quest_sec 2020](https://blog.csdn.net/Quest_sec/article/details/105612523)

# Running it in hexo

```bash
npm install hexo-tag-echarts3 --save
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
