---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Multiple Conditions
---

By combining ```if``` and ```else``` we were able to create binary pathways. With another built-in condiitonal keyword, we can create _multiple_ pathways in our code.

### ```elif``` statement

```elif``` is a built-in keyword related to if statements.
- ```elif``` can only exists if there is a related ```if``` statement above it
- ```elif``` can have its own condition, and it will execute its code block if the Boolean condition is True
- After the first if statement, you are allowed to have as many elif statements as you'd like
- It is recommended that your elif's boolean condition is related to the condition that comes before it

Examine the following format:
```python

    if boolean_condition1:
        # code here

    elif boolean_condition2:
        # code here

    elif boolean_condition3:
        # code here

    else:
        # code here
```

__NOTE:__
- if ```boolean_condition1``` is __True__, it will ignore the conditional statements below it
- if ```boolean_condition1``` is __False__, it will check the 2nd condition
- if both ```boolean_condition1``` and ```boolean_condition2``` is __False__, it will check the 3rd condition
- if all the conditions evaluate to __False__, then the else's code block will execute


```python
# Example

age = 14

if age > 17:
    print('You are allowed to watch any movies.')
elif age >= 13:
    print('You can watch any movies with any rating with exception of:')
    print('-- You cannot watch NC-17.')
    print('-- You require parent/adult guaradian supervision to watch R rated movies.')
else:
    print('You can watch G rated movies and you also need parental guidance for PG and PG-13 rated movies.')
```

    You can watch any movies with any rating with exception of:
    -- You cannot watch NC-17.
    -- You require parent/adult guaradian supervision to watch R rated movies.

