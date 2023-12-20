---
toc: true
url: torch_dp
covercopy: <a href='https://towardsdatascience.com/training-deep-neural-networks-9fdb1964b964'>© Ravindra Parmar</a>
priority: 10000
date: 2023-07-03 22:44:14
title: "torch: Start with Deep Learning"
ytitle: "torch: Start with Deep Learning"
description: "torch: Start with Deep Learning"
excerpt: "torch: Start with Deep Learning"
tags: [torch, Deep Learning, Machine Learning]
category: [Python, Data, Machine Learning, Deep Learning]
cover: "https://miro.medium.com/v2/1*N8UXaiUKWurFLdmEhEHiWg.jpeg"
thumbnail: "https://miro.medium.com/v2/1*N8UXaiUKWurFLdmEhEHiWg.jpeg"
---

## Torch: Start with Deep Learning

> Mostly from ChatGPT4

```python
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = nn.Linear(50, 100)  # 隐藏层，接收的输入大小为50，输出的大小为100
        self.relu = nn.ReLU()  # 激活函数
        self.output = nn.Linear(100, 2)  # 输出层，输出的大小为2，对应两个类别

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)
        return x

# 实例化模型
model = Net()

# 首先，我们定义损失函数和优化器。因为我们假设这是一个二分类问题，所以我们使用交叉熵损失（CrossEntropyLoss）。为了优化模型，我们使用随机梯度下降（SGD）
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 接下来，我们生成一些假的训练数据。假设我们有100个样本，每个样本是一个50维的向量：
inputs = torch.randn(100, 50)
labels = torch.randint(0, 2, (100,))  # 随机生成0或1作为标签

# 然后，我们进行一次前向传播、反向传播和权重更新：
# 前向传播

for epochs in range(100):
  outputs = model(inputs)
  loss = criterion(outputs, labels)
  # 反向传播和权重更新
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  print('Loss:', loss.item())

# 这样，你的模型就进行了一次训练。
# 要进行预测，你可以直接使用模型对输入进行前向传播：

# 生成一些假的测试数据
test_inputs = torch.randn(5, 50)
# 前向传播
outputs = model(test_inputs)

# 使用softmax函数得到每个类别的概率，并使用argmax得到预测的类别
_, predicted = torch.max(outputs, 1)

print('Predicted:', predicted)
```


## How to use GPU for training

1. 首先，检查你的系统是否支持CUDA（即GPU计算）：

```python
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)  # 如果你的系统支持CUDA，应该打印出'cuda:0'
```
2. 然后，将模型转移到GPU：
```python
model = Net().to(device)
```
3. 然后，将模型转移到GPU：
```python
for epoch in range(2):  # 进行2个epoch

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)  # 转移到GPU

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:    # 每2000个batch打印一次平均loss值
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
print('Finished Training')
```
4. 同样，当你进行预测时，也需要确保数据被转移到了GPU：
```python
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data[0].to(device), data[1].to(device)  # 转移到GPU
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))
```


## 保存和继续训练

1. 保存整个模型： `torch.save(model, 'model.pth')`
2. 只保存模型参数： `torch.save(model.state_dict(), 'params.pth')`
3. 加载整个模型： `model = torch.load('model.pth')`
4. 只加载模型参数： `model.load_state_dict(torch.load('params.pth'))`

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 以随机梯度下降为例
criterion = torch.nn.CrossEntropyLoss()  # 假设是分类问题
for epoch in range(num_epochs):
    # 清零梯度
    optimizer.zero_grad()
    # 前向传播
    outputs = model(new_data)
    # 计算损失
    loss = criterion(outputs, new_labels)
    # 反向传播
    loss.backward()
    # 更新参数
    optimizer.step()
```

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
