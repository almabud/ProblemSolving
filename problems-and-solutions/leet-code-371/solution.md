### Discussion:

* Python bit representation is infinite. That means there is no bit limit in python.
In this case let's say for `1` binary in python look like `...00000001`.
For `-1` binary in python is look like `...11111111` which is 2's compliment.

* So, we need to manually limit this bit in python. Let's say we want to limit with 32 bit.
We can do this by using bit mask.

  * 1st create a bit mask of $2^{32}$. That mean all 32 bit should be `1`.

  * We can achive this `mask = 0xffffffff` = `0b11111111111111111111111111111111`

* For limiting the bit's we need to do `&` with the `mask`. This will unset the all bits
those are in the leftside of the `32` bit boundary. For `-1` in python = `1111-11111111111111111111111111111111`
Here, by `-` I represent the boundary. Now if we do `&` with this `-1` = `1111-11111111111111111111111111111111 & 11111111111111111111111111111111`
So, result will be `0000-11111111111111111111111111111111`. All left sided bit's are now unset as we want.

* It will works fine if the `sum` is going to be a `positive integer`. eg. `1-1=0`, `-1+1=0`, `4-1=3`, `-2+4=2`.
Problem start with the `negative` answer. eg. `-3+1=-2`. Why this is a prblem? Let's simmulate this.
  * `-3` = `0b11111111111111111111111111111100` and `1` = `0b00000000000000000000000000000100`

  * `XOR` this two value for the calculating the sum `0b11111111111111111111111111111100 ^ 0b00000000000000000000000000000100 = 0b11111111111111111111111111111100`. carry never be a negative number. So, here forget about the as it will not create any problem.

  * `0b11111111111111111111111111111100` this value is a negative number which will be `4`. But python will treat it as a positive number.
  It is for it's infinite bit limit. In pytho this value look like `0b...0000-11111111111111111111111111111100`. For left side 0's it will
  treat this as a positive number and thus it will produce `4294967295` the sum in decimal. This is not correct value means we are loosing
  information. So, for get the correct value we need to put `..111` to the infinite time before `11111111111111111111111111111100` this value.

  * But how to do this in python? We know that 2's complement of a negative number produce the positive number of the same number. That means
  `sum = 11111111111111111111111111111100` -> 2's compliment = `~x + 1 = 00000000000000000000000000000011 + 1 = 00000000000000000000000000000100`.
  Now this is the positive number  of `sum`. Here is a note that if we used `~` for 1's complement then the value will be wrong again. Because
  all infinite left side `0's` will be now `1`. So here we have to `XOR` the `sum` with the `mask` it will toggle the bit and python left side will be
  untouched.

  * If we make `2's` complement of sum again then the value will be `negative` in python bit. That's we need. So, the expression are for negative numbers conversion is 

  $\sim \{(sum \oplus mask) + 1\} + 1 = \sim (x+1)+1 = \sim x = \sim (sum \oplus mask)$ .


  ```python
  class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python has  infinite  bit limit. So We need to manually limit this to 32bit
        # First we set a mask which binary value will be 2**32 mean 32 number of 1's
        mask = 0xffffffff # this will output '0b11111111111111111111111111111111'
        while b != 0:
            # Calculate the sum
            sum = (a ^ b) & mask
            # Carry
            b = ((a & b) << 1) & mask
            a = sum

            # Check sign bit are set or not. 31th position mean 32 no bit.
            if (a & (1<<31)):
                # Convert the negatic binary to it's actual value in python.a
                a = ~(a ^ mask)

        return a

  ```

  ### Reference:

  * https://wiki.python.org/moin/BitwiseOperators
  * https://www.ibm.com/docs/en/aix/7.1?topic=constants-arithmetic
  * https://en.wikipedia.org/wiki/Ones%27_complement
  * https://www3.ntu.edu.sg/home/ehchua/programming/java/datarepresentation.html
  * https://www.tutorialspoint.com/one-s-complement
  * [geeksforgeeks 1's complement](https://www.geeksforgeeks.org/1s-2s-complement-binary-number/#:~:text=2's%20complement%20of%20a%20binary%20number%20is%201%2C%20added%20to,are%20used%20for%20representing%20magnitude.)
  * https://stackoverflow.com/questions/20766813/how-to-convert-signed-to-unsigned-integer-in-python
  * https://stackoverflow.com/questions/34300336/negative-numbers-to-binary-system-with-python
  * [[This is the main source love this write] https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python](https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python)
