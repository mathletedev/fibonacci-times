# fibonacci-times

> Graphing the execution times of different Fibonacci algorithms

## Algorithms

### Recursive

**Time complexity:** `O(n²)`
\
Uses the classic recursive form of the Fibonacci function,

```
F(n) = F(n - 1) + F(n - 2)
```

### Iterative

**Time complexity:** `O(n)`
\
Uses two variables to keep track of the two previous values, adding them together each iteration

### Logical

**Time complexity:** `O(1)`
\
Uses a variation of [Binet's Formula](https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html),

```
F(n) = (φⁿ⁺¹ - (1 - φ)ⁿ⁺¹) / √5
```

## Results

![graph](https://user-images.githubusercontent.com/63214683/174754942-939f13b1-7aa1-4570-b056-d75f29256467.png)
