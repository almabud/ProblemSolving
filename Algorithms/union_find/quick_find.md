# Quick Find

**Quick-find** is known as an **eager** approach to solving the union-find problem.

In programming, **quick-find** is represented by two arrays:

— The first array is the set of items in the graph (size **N**).

— The second array is the set of integer id’s for each item in the graph (also size **N**). This is a mark array.

> Quick-find maintains the invariant that _all connected items must have the same id\[] value._

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 17-53-59 (1).png" alt=""><figcaption></figcaption></figure>

_Here, **0-5** are connected because they have the same value in **id** eg. `id[0] == id[5]`**.** The same goes for **3,4,8** they are connected too as they have also the same id eg. `id[3] == id[4] == id[8]`. This means the **second** array represents whether two points are connected or not. So, We can find the connection between **p & q** just by checking that_

<pre class="language-python"><code class="lang-python"># This for find method
<strong>if id[p] == id[q]:
</strong>    # They are connected
    return True</code></pre>

To merge components containing **p & q** , change all entries whose id equals id\[p] to id\[q] .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 17-53-59.png" alt=""><figcaption><p>Before connecting 1 &#x26; 6</p></figcaption></figure>

Here, `6 & 1` are not connected. Using quick-find, if we connect items `6 & 1` above, all entries with `id[6] = 0` (which is 6’s id value) need to change to `1` (which is 1’s id value). This means we need to change `id[0], id[5] and id[6]`.

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-16-15.png" alt=""><figcaption><p>After connecting 1&#x26;6</p></figcaption></figure>

The main problem in this quick find approach we need to change or access so many values.

### Quick find demo

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-19-15.png" alt=""><figcaption><p>Initial items</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-20-19.png" alt=""><figcaption><p>Initial id</p></figcaption></figure>

_**Step1:**_ Connect `4 to 3.` We need to change the value of `id[4] to id[3].`

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-24-27.png" alt=""><figcaption><p><code>Connect 4-3</code></p></figcaption></figure>

_**Step2:**_ Connect `3 to 8` We need to change the value of **`id[i] == id[3] to id[8]`**.

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-35-53.png" alt=""><figcaption><p>Connect 3-8</p></figcaption></figure>

_**Step3:**_ Connect `6 to 5` We need to change the value of **`id[i] == id[6] to id[5]`**.

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-41-52.png" alt=""><figcaption><p>Connect 6-5</p></figcaption></figure>

_**Step4:**_ Connect `9 to 4`. We need to change the value of `id[i] == id[9] to id[4]` .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-45-18.png" alt=""><figcaption><p>Connect 9-4</p></figcaption></figure>

_**Step5:**_ Connect `2 to 1`. We need to change the value of `id[i] == id[2] to id[1]` .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-47-40.png" alt=""><figcaption><p>Connect 2-1</p></figcaption></figure>

_**Step6:**_ Connect `8 to 9`. They are already connected.

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-51-06.png" alt=""><figcaption><p>Connect 8-9</p></figcaption></figure>

_**Step7:**_ Connect `5 to 0`. We need to change the value of `id[i] == id[5] to id[0]` .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-53-10.png" alt=""><figcaption><p>Connect 5-0</p></figcaption></figure>

_**Step8:**_ Connect `7 to 2`. We need to change the value of `id[i] == id[7] to id[2]` .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-54-48.png" alt=""><figcaption><p>Connect 7-2</p></figcaption></figure>

_**Step9:**_ Connect `6 to 1`. We need to change the value of `id[i] == id[6] to id[1]` .

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-18 18-56-20.png" alt=""><figcaption><p>Connect 6-1</p></figcaption></figure>

### Implementation:

```python
class QuickFindUF:
    mark_list = []

    def __init__(self, size:int):
        # Initialize the mark array index number to value.
        mark_list = [i for i in range(size)]
    
    def is_connected(self, from_number: int, to_number: int) -> bool:
        return self.mark_list[from_number] == self.mark_list[to_number]
    
    def union(self, from_number: int, to_number: int) -> None:
        if self.mark_list[from_number] == self.mark_list[to_number]:
            return
        
        from_value = self.mark_list[from_number]
        to_value = self.mark_list[to_number]
        
        for key, val in enumerate(self.mark_list):
            if val == from_Value:
                self.mark_list[key] = to_Value
```

### Time complexity

In quick find the number of array access for read and write

<figure><img src="../../.gitbook/assets/Screenshot from 2022-09-19 00-36-26.png" alt=""><figcaption></figcaption></figure>

Union is too expensive. It takes $$n^2$$ array accesses to process a sequence of `N` union commands on `N` objects. So the time complexity of the **quick find** is $$n^2$$.

### [Code Link](quick\_find.py)
