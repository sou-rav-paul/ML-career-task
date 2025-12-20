# Day 6 Function Modularity
### DEEP DIVE : Theory : The Stack Scope
When a function is called, Python creates a 'Stack Frame' in memory. All variables created inside the Python live there. When the fucnction live there. When the function returns, the frame is destroyed. <b>LGEB Rule</b> : Python sreaches for variable in this order : Local -> Enclosing -> Global -> Built-in

---

```python
def calculate_area(radius: float ) -> float:
  '''Return area of circle. Input float'''
  if radius < 0 :
    return 0
  return 3.14 * (radius **2)
# Main Execution
r = 5
print(calculate_area(r))

```
---
### DEEP DIVE : Micro-Challenge : The Scope Fortrss 

**Goal:** Create a global variable x=10. Write a function `change_x()` that sets `x = 20` inside it. Print x outside the function.      
**Observation:** It prints 10, not 20.     
**The Mechanics:** This demonstrates **Local vs. Global Scope**. When you write `x=20` inside a function, Python creates a **new local variable** named 'x' inside the function's stack
frame. It does NOT touch the global 'x'. To modify the global , you would need the `global` keyword (but avoid this in productions!)

 
  ---

  ### DIVE DIVE : Micro-Challenge : The Pure Return
  **Goal:** Write a function `add(a,b)` that prints the sum but returns nothing. Assign the result to a variable `res=add(5 , 5)` . Print `res`.     
**Observation :** It prints `None` . 
**The Mechanics:** Every Python function returns something. If you do not explicitly write `return value` , Ptyhon implicitly execute `return None` at the end .        

**Best Practice:** Functions should calculate and return values . The calling code shuould decide whether to print them.
---

### DEEP DIVE : Micro-Challenge : The Default Gateway
**Goal:** Write a function `connect(port=3302)` that prints 'Connecting to [port]'. Call it once whth no arguments, and once with `5432`  
**The Mechanics:** This uses **Default Argument**. When Python defines the function, it stores 3306 in memory . If the caller provides no argument , Python grabs this stored default . This allows for flexible APIs where common settings are optional . 
