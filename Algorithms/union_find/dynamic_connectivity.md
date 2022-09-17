---
description: Dynamic Connectivity Problem
---

# Union find

**Dynamic connectivity problem:**  Given a set of N objects, connect two objects, or ask if two objects are connected (directly or indirectly).

In [computing](https://en.wikipedia.org/wiki/Computing) and [graph theory](https://en.wikipedia.org/wiki/Graph\_theory), a **dynamically connected** structure is one that maintains information about the connected components of a graph.

It allows items in a larger _**super-set**_ to belong to a common _**sub-set**_, and efficiently answers the question _‘is there a path connecting A to B?’_

> _Given a huge number of connected components in a sub-set, how do we design an efficient data structure that allows us to connect huge amounts of items together and efficiently determine if items are connected ?_

#### Dynamic connectivity introduces the following **abstractions:**

* a set of objects.
* a `union` method, which allows you to _**connect two objects by**_ replacing sets containing two items by their union_**.**_
* a `find` method, which allows you to determine _**if there is a path connecting one object to another by answering the question ‘are two objects in the same set?’.**_

#### Dynamic connectivity also introduces the following **assumptions**:

* _“is connected to”_ is _**r**_**eflexive:** each object is _always connected to itself_.
* _“is connected to”_ is _**s**_**ymmetric:** if **p** is connected to **q**, then **q** is connected to **p**.
* _“is connected to”_ is _**t**_**ransitive:** if **p** is connected to **q** and **q** is connected to **r**, then **p** is connected to **r**.

Finally, dynamic connectivity asserts that one can add and remove items from the graph and that the graph can get very large (hence the title ‘dynamic’).

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 00-37-35 (1).png" alt=""><figcaption><p>Dynamic conneted</p></figcaption></figure>

In the above, we need to find any path of the two given objects.

This seems to be a little problem and can be answered in a minute by a human. But for bigger type problems like we need to find the path in the network hub. eg. is there any path from **p to q**?

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 00-42-06.png" alt=""><figcaption><p>Dynamic connected</p></figcaption></figure>

This is huge and we need a computer program to solve this type of problem.&#x20;

### The real-life examples

* Pixels in a digital photo.&#x20;
* Computers in a network.&#x20;
* Friends in a social network.&#x20;
* Transistors in a computer chip.&#x20;
* Elements in a mathematical set.&#x20;
* Variable names in Fortran program.&#x20;
* Metallic sites in a composite system.

