# \[Leet-code] 146. LRU Cache

![](https://img.shields.io/static/v1?label=DSA\&message=Linked%20List\&color=informational\&labelColor=21223e) ![](https://img.shields.io/static/v1?label=DSA\&message=Hash%20Map\&color=informational\&labelColor=21223e) ![](https://img.shields.io/static/v1?label=Difficulty\&message=Easy\&color=success\&labelColor=21223e)&#x20;

### Problem Description

{% embed url="https://leetcode.com/problems/lru-cache/" %}

### Overview

Design a data structure that follows the constraints of a [**Least Recently Used (LRU) cache**](https://en.wikipedia.org/wiki/Cache\_replacement\_policies#LRU).

Implement the `LRUCache` class:

* `LRUCache(int capacity)` Initialize the LRU cache with a **positive** size `capacity`.
* `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
* `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

#### Examples

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

### Discussion

In the first impression maybe we try to solve this problem using mark array. Mark array could be a solution. Let's try to solve this using mark array

Let's say LRU cache size is **4.**

* 1st element is 1
* 2nd element is 2
* 3rd element is 5
* 4th element is 0

Now how do you track the order of coming? You can use another mark array for the order. But in this case, you have to change the order of all other elements. That means you need to traverse the mark array and it will cost $$O(n)$$​time-complexity. But we need to do this in $$O(1)$$​.

**Solution:** We can do this using a **Linked list** & **Hash map.** We will keep the node inside the **hash map** along with the **value.** In the linked list we can delete elements from any position we need. We will keep the **head,** **tail node** & **size** of the cache. Then if any number comes, we check into the **hash map.** If it is found in the **hash map** then we **return the value** and move that node **at first** of the **linked list** and thus it will become the **most recently** used value. If the cache limit is going to overflow then the **tail** will be **deleted** and the **previous node** of the **tail** will be the present **tail.**

***
