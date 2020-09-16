# Nested Conditional Statements
---

Nesting is the act of placing programming statements inside another. We can nest if statements to create complex decision trees in our program.

### ```if``` statements within our ```if``` statements

Examine the following format below:

```python

    if boolean_condition1:
        # code here
        
        if boolean_conditionA:
            # code here
        else:
            # code here
            
    elif boolean_condition2:
        # code here
        
        if boolean_conditionB:
            # code here
        elif boolean_conditionC:
            # code here
    else:
        # code here
        if boolean_conditionD:
            # code here
```

This type of conditional statements are called __nested__ conditional statements.
- When a certain condition is True, we can check upon more conditions for the program
- This is only required when the complexity of the condition increases depending on the given problem

### Nested vs Logical Operator

The following two python conditional formats are equivalent.

```python

    if conditionA:
        if conditionB:
            # execute Code here
            print('Hello, World')
```
        vs.
```python

    if conditionA and conditionB:
        # execute Code here
        print('Hello, World')
    
```


```python
# Code Example
# Scholarship Checker based on Average Mark

mark_average = 92

if mark_average >= 90:
    if mark_average < 95:
        print('Your entrance scholarship is: $2000')
    elif mark_average <= 100:
        print('Your entrance scholarship is: $4000')
else:
    print('You are not elligible for an entrance scholarship.')
```

    Your entrance scholarship is: $2000

