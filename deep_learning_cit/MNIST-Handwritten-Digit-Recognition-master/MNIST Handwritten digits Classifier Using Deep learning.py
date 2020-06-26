#!/usr/bin/env python
# coding: utf-8

# # Handwritten Digits Classifier
# 
# 
# 
# 
# 

# 
# 

# In[1]:


import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets, transforms

# Defining transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                              ])
# Downloading and loading the training data
trainset = datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)


# In[4]:


# Building a feed-forward network
model = nn.Sequential(nn.Linear(784, 128),
                      nn.ReLU(),
                      nn.Linear(128, 64),
                      nn.ReLU(),
                      nn.Linear(64, 10),
                      nn.LogSoftmax(dim=1))

criterion = nn.NLLLoss()
images, labels = next(iter(trainloader))
images = images.view(images.shape[0], -1)

logps = model(images)
loss = criterion(logps, labels)


# In[5]:


print('Before backward pass: \n', model[0].weight.grad)

loss.backward()

print('After backward pass: \n', model[0].weight.grad)


# ## Training the network!
# 

# In[6]:


from torch import optim

optimizer = optim.SGD(model.parameters(), lr=0.01)


# In[7]:


print('Initial weights - ', model[0].weight)

images, labels = next(iter(trainloader))
images.resize_(64, 784)

# Clearing the gradients, 
optimizer.zero_grad()

# Forward pass, then backward pass, then update weights
output = model.forward(images)
loss = criterion(output, labels)
loss.backward()
print('Gradient -', model[0].weight.grad)


# In[8]:


# update step 
optimizer.step()
print('Updated weights - ', model[0].weight)


# ### Training for real
# 
# 

# In[9]:


model = nn.Sequential(nn.Linear(784, 128),
                      nn.ReLU(),
                      nn.Linear(128, 64),
                      nn.ReLU(),
                      nn.Linear(64, 10),
                      nn.LogSoftmax(dim=1))

criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003)

# training for 5 epochs

epochs = 5
for e in range(epochs):
    running_loss = 0
    for images, labels in trainloader:
       
        images = images.view(images.shape[0], -1)
    
        
        optimizer.zero_grad()
        
        output = model.forward(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    else:
        print(f"Training loss: {running_loss/len(trainloader)}")


# Now checking out it's predictions.

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import helper

images, labels = next(iter(trainloader))

img = images[0].view(1, 784)

with torch.no_grad():
    logps = model.forward(img)


ps = torch.exp(logps)
helper.view_classify(img.view(1, 28, 28), ps)


# Accurate Prediction
# 
