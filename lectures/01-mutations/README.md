<h2 align=center>Week 01: <em>Day 1</em> & Week 02: <em>Day 1</em></h2>

<h1 align=center>Mutations v. Construction</h1>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/0qUtT6k83Go?si=c-pKA-WsWJ57CQjp"><strong><u>Fior di Latte</u></strong></a> by Phoenix (2017).</em></p>

---

## Sections

1. [**A Quick Overview of Python**](#1)
2. [**Mutating An Object v. Creating A New One**](#2)
    1. [**Mutating A List**](#2-1)
    2. [**Creating A New List**](#2-2)

---

<a id="1"></a>

## Part 1: _A Quick Overview of Python_

Alright, before we get into the nitty-gritty of this class, I think we would benefit from a general, bird's-eye review of what you already know about Python. I don't necessarily mean the topics that you've learned in 1114 here, but rather a sort of mental map of the language and how its constituents are grouped together. The way I see it, this is what we have:

| **Category**        | **Details**                                                                   |
|---------------------|-------------------------------------------------------------------------------|
| **Data**            | - Built-in types: `int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`, ... |
|                     | - Programmer-defined types (classes)                                          |
| **Expressions**     | - I/O expressions                                                             |
|                     | - Assignment                                                                  |
|                     | - Arithmetic expressions                                                      |
|                     | - Boolean expressions                                                         |
| **Control Flow**    | - Sequential                                                                  |
|                     | - Branching: `if`, `if-else`, `if-elif-else`                                  |
|                     | - Iterative: `while`, `for`                                                   |
|                     | - Function calls                                                              |
|                     | - Exceptions                                                                  |

<sub>**Figure 1**: A high-level overview of the Python language.</sub>

Everything here should look pretty familiar to us, but I'd like to focus on data types for today's lecture since, as we know, these can be further subdivided into two categories: **mutable** and **immutable** types. As data structures and algorithms is a class that's almost entirely concerned with how efficient our programs are—including with the way we handle memory inside these objects—this seems like a pretty natural way to kick off our journey.

<br>

<a id="2"></a>

## Part 2: _Mutating An Object v. Creating A New One_

As a quick reminder, **mutability** refers to an object's _ability to change in value_ after it has been instantiated. What I mean by this is not, for example, changing the value of a variable from `1` to `2`, but rather changing the value of the `1` `int` object itself (which is, incidentally, not possible, since `int` objects are immutable; it's not as if you can ever change the value of the number 1—one is one forever).

So instead of integers, let's instead turn to the first mutable object we learned about in Python: the `list` type!

<a id="2-1"></a>

### Mutating A List

Let's list out example of list mutation:

1. **Indexed Assignment**: When we have a list with elements in it, we can use indexing in order to _reassign_ the value of one such element with another. For example:

    ```Python
    my_precalc_grades = [91, 87, 41]  # instantiating a list object
    my_precalc_grades[2] = 65         # indexed assignment
    ```

    Note here that, although the value of the immutable `41` was reassigned within the list, this does _not_ make it mutable—we simply replaced it.

    Here's what the memory map looks like for this operation:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
            unused  │ mem_loc a │
                    │———————————│
            91      │ mem_loc b │
                    │———————————│
            87      │ mem_loc c │
                    │———————————│
            41      │ mem_loc d │  <-- to be replaced
                    │———————————│
            unused  │ mem_loc e │
                    │———————————│
                   ~~~~~~~~~~~~~~~
                    
    Step 2 (Assign 65):
                   ~~~~~~~~~~~~~~~
                    │———————————│
            unused  │ mem_loc a │
                    │———————————│
            91      │ mem_loc b │
                    │———————————│
            87      │ mem_loc c │
                    │———————————│
            65      │ mem_loc e │  <-- new reference
                    │———————————│
                   ~~~~~~~~~~~~~~~

    ```

    (Also note that I really should've studied for that pre-calc final exam instead of playing Mass Effect 3 the entire week.)

2. **The `.append(obj: Object) -> None` Method**: One of the most evident benefits of lists being mutable is their ability to grow by having more elements _appended_ to them:

    ```Python
    brit_pop = ["Oasis", "Blur"]  # instantiating a list object
    brit_pop.append("Pulp")       # appending a new str object to it
    ```

    Memory map:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Blur"        │ mem_loc c │
                    │———————————│
           unused   │ mem_loc d │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (Append "Pulp"):
                    ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Blur"        │ mem_loc c │
                    │———————————│
      "Pulp"        │ mem_loc d │  <-- new reference
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

3. **The `.insert(idx: int, obj: Object) -> None` Method**: Similarly, Python allows you to place a new object within a list at any location that you want:

    ```Python
    brit_pop.insert(2, "Suade")           # "Suade" becomes the 2nd element, pushing "Pulp" to the 3rd index
    ```

    Memory map:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Blur"        │ mem_loc c │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (Insert "Suede" at Index 2):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Blur"        │ mem_loc c │
                    │———————————│
      "Suede"       │ mem_loc e │  <-- new reference
                    │———————————│
      "Pulp"        │ mem_loc d │  <-- shifted
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

4. **The `.pop(idx: int = -1) -> Object` Method**: Of course, we can also remove elements from lists. This is commonly done at the end of the list, but not always:

    ```Python
    outlier = brit_pop.pop(1)  # removes the 1st element, "Blur", and returns it
    print(brit_pop)            # ["Oasis", "Suade", "Pulp"]
    ```

    `.pop()` is unusual for `list` methods in that it is one of the few to actually return a value; most `list` methods simply mutate the list _in-place_ and don't return anything. Here, we are doing both.

    Memory map:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Blur"        │ mem_loc c │  <-- to be removed
                    │———————————│
      "Suede"       │ mem_loc e │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (After Removing "Blur"):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
           unused   │ mem_loc c │  <-- removed
                    │———————————│
      "Suede"       │ mem_loc e │  <-- shifted
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

5. **The `reverse() -> None` and `sort() -> None` Methods**: Two very common operations (of whose inner workings we will soon learn about) on collections of objects is order _reversal_ and content _sorting_. These two processes are extremely powerful, and are a lot more involved than a simple Python method might make them seem (but we'll get there):

    ```Python
    brit_pop.reverse()  # reverses the order of the elements in the list

    print(brit_pop)  # ['Pulp', 'Blur', 'Oasis']

    ```

    Memory map:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Suede"       │ mem_loc e │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (After Reverse):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Pulp"        │ mem_loc d │  <-- reversed
                    │———————————│
      "Suede"       │ mem_loc e │  <-- reversed
                    │———————————│
      "Oasis"       │ mem_loc b │  <-- reversed
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

    ```Python
    brit_pop.sort()  # sorts the elements in the list

    print(brit_pop)  # ['Blur', 'Oasis', 'Pulp']
    ```

    Memory map:

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
      "Suede"       │ mem_loc e │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (After Sort):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │  <-- rearranged
                    │———————————│
      "Pulp"        │ mem_loc d │  <-- rearranged
                    │———————————│
      "Suede"       │ mem_loc e │  <-- rearranged
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

    Note that `.sort()` will raise an exception if the objects within the list cannot be compared (i.e. don't have those dunder methods defined). In other words, the following will fail...

    ```Python
    lst = [1, 2, "3"]
    lst.sort()
    ```

    ...with the following error:

    ```
    Traceback (most recent call last):
    File "mutations.py", line 44, in <module>
        lst.sort()
    TypeError: '<' not supported between instances of 'str' and 'int'
    ```

6. **The `.extend(iter: Iterable) -> None` Method**: Instead of using a loop in order to append all of the objects from a list into another list, Python provides a way for us to do this in one line:

    ```Python
    brit_pop.extend(["The Verve", "Radiohead"])  # extends the list with the elements of another list

    print(brit_pop)  # ['Blur', 'Oasis', 'Pulp', 'The Verve', 'Radiohead']
    ```

    ```
    Step 1 (Before):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
      "Suede"       │ mem_loc e │
                    │———————————│
           unused   │ mem_loc f │
                    │———————————│
                   ~~~~~~~~~~~~~~~

    Step 2 (After Extending):
                   ~~~~~~~~~~~~~~~
                    │———————————│
           unused   │ mem_loc a │
                    │———————————│
      "Oasis"       │ mem_loc b │
                    │———————————│
      "Pulp"        │ mem_loc d │
                    │———————————│
      "Suede"       │ mem_loc e │
                    │———————————│
   "The Verve"      │ mem_loc f │  <-- new reference
                    │———————————│
   "Radiohead"      │ mem_loc g │  <-- new reference
                    │———————————│
                   ~~~~~~~~~~~~~~~
    ```

    Note here that _any_ iterable will work here (i.e. `tuple`, `range`, `str`, etc.)

7. **The `+=` Operator**: Although we sometimes call these 'augmented assignment operators', for Python lists, `+=` is simply syntactical sugar for `.extend()`:

    ```Python
    brit_pop += ["The Stone Roses", "The Smiths"]

    print(brit_pop)  # ['Blur', 'Oasis', 'Pulp', 'The Verve', 'Radiohead', 'The Stone Roses', 'The Smiths']
    ```

These being established, let's now look at Python operations that _do not_ mutate a list, but rather create a new one.

<a id="2-2"></a>

### Creating A New List

1. **List literals**: Naturally, creating a new list from scratch is the most obvious example. These are known as _literals_:

    ```Python
    six_moral_tales = ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]
    ```

2. **The `list` Constructor**: One can also create a list using Python's `list` type's constructor:

    ```Python
    six_moral_tales = list(("The Bakery Girl", "Suzanne's Career", "My Night at Maud's"))  # same as above
    ```

    Note here that we're technically creating a `tuple` object and then creating a `list` object out of it.

3. **The `copy.copy(lst: list) -> list` Function**: We can create a _shallow copy_ of a list by calling the `copy` module's `copy()` function.

    ```Python
    french_films = six_moral_tales.copy()  # creates a new list object with the same elements

    print("Copy:", french_films)  # ['The Bakery Girl', "Suzanne's Career", "My Night at Maud's"]
    ```

    Note that shallow copies do _not_ create copies of any mutable objects inside of the copied list.

4. **The `copy.deepcopy(lst: list) -> list` Function**: We can also create a _deep copy_, which _does_ create copies of any mutable objects inside of the copied list:

    ```Python
    french_films = deepcopy(six_moral_tales)  # creates a new list object with the same elements

    print(french_films)  # ['The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]
    ```

5. **List Concatenation (`+`)**: Using the `+` operator between two lists will create a new list containing both of the operand lists' contents:

    ```Python
    french_films = six_moral_tales + ["La Collectionneuse", "Claire's Knee", "Love in the Afternoon"]

    print(french_films)  # ['The Bakery Girl', "Suzanne's Career", "My Night at Maud's", "La Collectionneuse", "Claire's Knee", "Love in the Afternoon"]
    ```

6. **List Repetition (`*`)**: Using the `*` operator between a list and an integer will create a new list containing the original list's contents that many times:

    ```Python
    french_films = six_moral_tales * 2

    print("Repetition:", french_films)  # ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's", "The Bakery", "Suzanne's Career", "My Night at Maud's"]
    ```

7. **List Slicing**: List slicing also creates a new list according to the values used inside of the brackets, `[start:stop:step]`:

    ```Python
    french_films = six_moral_tales[1:]  # creates a new list object with the elements starting from the 2nd index

    print("Slicing:", french_films)  # ["Suzanne's Career", "My Night at Maud's"]
    ```

8. **List Comprehension**: Finally, list comprehension also creates a list, which makes sense since that's exactly what we use it for:

    ```Python
    # list comprehension
    french_films = [film for film in six_moral_tales]  # creates a new list object with the same elements

    print("List comprehension:", french_films)  # ["The Bakery Girl", "Suzanne's Career", "My Night at Maud's"]
    ```

---

Now, the reason why we're making these distinctions early on will become clear as the semester goes along, but it all boils down to the way we measure _efficiency_ of programs:

1. By how _long_ it takes, on average, for a program to execute.
2. By how _much memory space_ it takes, on average, for a program to execute.

We shall soon find out how, why, and how we can measure it.