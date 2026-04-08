# 🐍 Python Complete Learning Roadmap
## From Zero to Advanced - Complete Self-Study Guide

---

## 🔰 PHASE 1: BEGINNER LEVEL (Weeks 1-8)

### Week 1-2: Python Fundamentals

#### 1.1 Setting Up Environment
- Installing Python (latest version)
- Setting up IDE (VS Code / PyCharm)
- Understanding Python interpreter
- Running Python scripts (.py files)
- Using Python interactive shell
- Understanding Python virtual environments (venv)
- Installing packages with pip

#### 1.2 Variables and Data Types
- **Variables:**
  - Variable naming rules and conventions
  - Variable assignment and reassignment
  - Multiple assignment
  - Variable scope (local vs global)
  - The `global` and `nonlocal` keywords
  
- **Data Types:**
  - **Numbers:**
    - `int` (integers): whole numbers
    - `float` (floating point): decimal numbers
    - `complex` (complex numbers): 3+4j
    - Type conversion: `int()`, `float()`, `str()`
    - Numeric operations and precedence
  
  - **Strings:**
    - Creating strings (single, double, triple quotes)
    - String indexing and slicing
    - String immutability
    - String concatenation and repetition
    - Escape characters (\n, \t, \\, \', \")
    - Raw strings (r"text")
  
  - **Boolean:**
    - `True` and `False`
    - Boolean type conversion
    - Truthy and Falsy values
    - `None` type

#### 1.3 Operators
- **Arithmetic Operators:**
  - `+` (addition), `-` (subtraction)
  - `*` (multiplication), `/` (division)
  - `//` (floor division), `%` (modulus)
  - `**` (exponentiation)
  
- **Comparison Operators:**
  - `==` (equal), `!=` (not equal)
  - `>`, `<`, `>=`, `<=`
  - Chaining comparisons (1 < x < 10)
  
- **Logical Operators:**
  - `and`, `or`, `not`
  - Short-circuit evaluation
  
- **Assignment Operators:**
  - `=`, `+=`, `-=`, `*=`, `/=`
  - `//=`, `%=`, `**=`
  
- **Identity Operators:**
  - `is`, `is not`
  - Difference between `==` and `is`
  
- **Membership Operators:**
  - `in`, `not in`

#### 1.4 Input and Output
- `print()` function:
  - Multiple arguments
  - `sep` parameter
  - `end` parameter
  - `file` parameter
- `input()` function:
  - Reading user input
  - Type conversion of input
  - Formatting output with f-strings
  - `format()` method
  - Old-style formatting with %

### Week 3-4: Control Flow

#### 2.1 Conditional Statements
- **if Statement:**
  - Basic if syntax
  - Indentation rules
  - Single-line if statements
  
- **if-else Statement:**
  - else block
  - Ternary operator (conditional expression)
  
- **if-elif-else:**
  - Multiple conditions
  - elif chains
  - Nested if statements
  
- **match-case (Python 3.10+):**
  - Pattern matching
  - Case guards
  - Wildcard patterns

#### 2.2 Loops
- **for Loop:**
  - Iterating over sequences
  - `range()` function (start, stop, step)
  - Nested for loops
  - `enumerate()` function
  - `zip()` function
  
- **while Loop:**
  - Basic while syntax
  - Infinite loops and how to avoid them
  - Loop counters
  
- **Loop Control:**
  - `break` statement
  - `continue` statement
  - `pass` statement
  - `else` clause with loops

### Week 5-6: Data Structures

#### 3.1 Lists
- Creating lists
- Accessing elements (indexing)
- Negative indexing
- Slicing lists [start:stop:step]
- **List Methods:**
  - `append()`, `insert()`, `extend()`
  - `remove()`, `pop()`, `clear()`
  - `index()`, `count()`
  - `sort()`, `reverse()`
  - `copy()`
- List concatenation and repetition
- Nested lists (2D lists, matrices)
- List unpacking
- Checking membership with `in`

#### 3.2 Tuples
- Creating tuples
- Tuple with one element (trailing comma)
- Accessing tuple elements
- Tuple immutability
- **Tuple Methods:**
  - `count()`, `index()`
- Tuple packing and unpacking
- Returning multiple values from functions
- Named tuples (collections.namedtuple)

#### 3.3 Sets
- Creating sets
- Set literals vs set() constructor
- **Set Operations:**
  - `add()`, `update()`
  - `remove()`, `discard()`, `pop()`
  - `clear()`
- **Mathematical Set Operations:**
  - Union (`|` or `union()`)
  - Intersection (`&` or `intersection()`)
  - Difference (`-` or `difference()`)
  - Symmetric difference (`^` or `symmetric_difference()`)
  - Subset and superset checks
- Frozen sets (immutable sets)

#### 3.4 Dictionaries
- Creating dictionaries
- Key-value pairs
- Accessing values by key
- Dictionary keys (must be immutable)
- **Dictionary Methods:**
  - `get()`, `setdefault()`
  - `keys()`, `values()`, `items()`
  - `update()`, `pop()`, `popitem()`
  - `clear()`, `copy()`
- Dictionary comprehension (intro)
- Nested dictionaries
- Merging dictionaries (| operator in Python 3.9+)

### Week 7-8: Functions

#### 4.1 Function Basics
- Defining functions with `def`
- Function naming conventions
- Calling functions
- The `return` statement
- Returning multiple values
- Functions without return (returns None)
- Docstrings and documentation

#### 4.2 Function Parameters
- **Positional parameters**
- **Default parameters**
- **Keyword arguments**
- **Arbitrary arguments (*args)**
- **Arbitrary keyword arguments (**kwargs)**
- **Parameter order rules**
- **Positional-only parameters (/ separator)**
- **Keyword-only parameters (* separator)**

#### 4.3 Function Scope
- Local scope
- Global scope
- `global` keyword
- `nonlocal` keyword
- LEGB rule (Local, Enclosing, Global, Built-in)

#### 4.4 Advanced Function Concepts
- **Lambda functions:**
  - Syntax: `lambda args: expression`
  - Use cases
  - Limitations
- **Recursive functions:**
  - Base case and recursive case
  - Common examples (factorial, fibonacci)
  - Recursion depth limit
- **Higher-order functions:**
  - Functions as arguments
  - Functions as return values
  - `map()`, `filter()`, `reduce()`

---

## 🧱 PHASE 2: INTERMEDIATE LEVEL (Weeks 9-20)

### Week 9-10: Advanced Data Structures

#### 5.1 List Comprehensions
- Basic syntax: `[expression for item in iterable]`
- With conditions: `[expr for item in iterable if condition]`
- Nested list comprehensions
- Multiple for clauses
- When to use vs regular loops

#### 5.2 Dictionary Comprehensions
- Syntax: `{key: value for item in iterable}`
- With conditions
- Transforming dictionaries
- Swapping keys and values

#### 5.3 Set Comprehensions
- Syntax: `{expression for item in iterable}`
- Filtering with conditions

#### 5.4 Generator Expressions
- Syntax: `(expression for item in iterable)`
- Memory efficiency vs lists
- When to use generator expressions

#### 5.5 Collections Module
- **Counter:** counting hashable objects
- **defaultdict:** dictionary with default values
- **OrderedDict:** maintaining insertion order
- **deque:** double-ended queue
- **ChainMap:** combining multiple dictionaries

### Week 11-12: String Handling

#### 6.1 String Methods
- **Case methods:**
  - `upper()`, `lower()`, `capitalize()`
  - `title()`, `swapcase()`, `casefold()`
  
- **Search and Replace:**
  - `find()`, `rfind()`, `index()`, `rindex()`
  - `replace()`, `count()`
  - `startswith()`, `endswith()`
  
- **Whitespace:**
  - `strip()`, `lstrip()`, `rstrip()`
  - `split()`, `rsplit()`, `splitlines()`
  - `join()`
  
- **Validation:**
  - `isalpha()`, `isdigit()`, `isalnum()`
  - `isspace()`, `isupper()`, `islower()`
  - `isdecimal()`, `isnumeric()`
  
- **Formatting:**
  - `center()`, `ljust()`, `rjust()`
  - `zfill()`, `expandtabs()`

#### 6.2 String Formatting
- **f-strings (formatted string literals):**
  - Basic: `f"Hello {name}"`
  - Expressions: `f"{2 + 2}"`
  - Format specifiers: `f"{value:.2f}"`
  - Alignment and width
  - Date formatting
  
- **format() method:**
  - Positional arguments
  - Named arguments
  - Format specifications
  
- **% formatting (old style):**
  - Understanding legacy code
  - %s, %d, %f placeholders

#### 6.3 Regular Expressions (re module)
- Pattern matching basics
- `re.match()`, `re.search()`, `re.findall()`
- `re.sub()`, `re.split()`
- Special characters: `.`, `^`, `$`, `*`, `+`, `?`
- Character classes: `[]`, `\d`, `\w`, `\s`
- Groups and capturing
- Compile patterns with `re.compile()`
- Flags: IGNORECASE, MULTILINE, DOTALL

### Week 13-14: File Handling

#### 7.1 File Operations
- **Opening files:**
  - `open()` function
  - File modes: 'r', 'w', 'a', 'x'
  - Binary mode: 'b'
  - Read and write: 'r+', 'w+'
  
- **Reading files:**
  - `read()` - read entire file
  - `readline()` - read one line
  - `readlines()` - read all lines as list
  - Iterating over file object
  
- **Writing files:**
  - `write()` - write string
  - `writelines()` - write list of strings
  
- **File positioning:**
  - `seek()`, `tell()`
  
- **Closing files:**
  - `close()` method
  - Using `with` statement (context manager)

#### 7.2 Working with Paths
- **os.path module:**
  - `join()`, `split()`, `splitext()`
  - `exists()`, `isfile()`, `isdir()`
  - `basename()`, `dirname()`
  - `abspath()`, `realpath()`
  
- **pathlib module (modern approach):**
  - `Path` class
  - Path operations
  - Reading/writing with Path
  - Iterating directories
  - Glob patterns

#### 7.3 Working with Directories
- **os module:**
  - `getcwd()`, `chdir()`
  - `listdir()`, `scandir()`
  - `mkdir()`, `makedirs()`
  - `remove()`, `rmdir()`, `removedirs()`
  - `rename()`, `replace()`
  
- **shutil module:**
  - `copy()`, `copy2()`, `copytree()`
  - `move()`, `rmtree()`

#### 7.4 Working with CSV Files
- **csv module:**
  - `csv.reader()`: reading CSV
  - `csv.writer()`: writing CSV
  - `DictReader`: reading as dictionaries
  - `DictWriter`: writing dictionaries
  - Handling different delimiters
  - Quoting options

#### 7.5 Working with JSON
- **json module:**
  - `json.load()`: read from file
  - `json.loads()`: parse from string
  - `json.dump()`: write to file
  - `json.dumps()`: convert to string
  - Formatting with `indent`
  - Handling custom objects
  - `ensure_ascii` parameter

#### 7.6 Working with Other Formats
- **pickle module:**
  - Serializing Python objects
  - `pickle.dump()`, `pickle.load()`
  - Security considerations
  
- **configparser:**
  - Reading .ini files
  - Writing configuration files

### Week 15-16: Error and Exception Handling

#### 8.1 Exception Basics
- What are exceptions?
- Common built-in exceptions:
  - `SyntaxError`, `IndentationError`
  - `NameError`, `TypeError`, `ValueError`
  - `IndexError`, `KeyError`, `AttributeError`
  - `ZeroDivisionError`, `FileNotFoundError`
  - `ImportError`, `ModuleNotFoundError`

#### 8.2 Handling Exceptions
- **try-except block:**
  - Basic syntax
  - Catching specific exceptions
  - Multiple except blocks
  - Catching multiple exceptions
  - Exception object access with `as`
  
- **try-except-else:**
  - else block execution
  - When to use else
  
- **try-except-finally:**
  - finally block (always executes)
  - Cleanup operations
  
- **try-except-else-finally:**
  - Complete structure
  - Execution order

#### 8.3 Raising Exceptions
- `raise` statement
- Re-raising exceptions
- `raise from` (exception chaining)
- When to raise exceptions

#### 8.4 Custom Exceptions
- Creating exception classes
- Inheriting from Exception
- Adding custom attributes
- Best practices for custom exceptions

#### 8.5 Assertions
- `assert` statement
- When to use assertions
- AssertionError
- Assertions vs exceptions

### Week 17-18: Modules and Packages

#### 9.1 Understanding Modules
- What is a module?
- Importing modules:
  - `import module`
  - `from module import name`
  - `from module import *` (avoid)
  - `import module as alias`
- Module search path (sys.path)
- `__name__` and `__main__`
- Reloading modules (importlib.reload)

#### 9.2 Creating Your Own Modules
- Writing a module file
- Organizing code into modules
- Module documentation
- Private variables (single underscore convention)
- `__all__` list

#### 9.3 Packages
- What is a package?
- `__init__.py` file
- Creating package structure
- Subpackages
- Relative imports
- Absolute imports

#### 9.4 Essential Standard Library Modules

**Mathematics:**
- **math:** mathematical functions
  - `sqrt()`, `pow()`, `ceil()`, `floor()`
  - Trigonometric functions
  - Constants: `pi`, `e`
- **random:** random number generation
  - `random()`, `randint()`, `choice()`
  - `shuffle()`, `sample()`
  - `seed()` for reproducibility
- **statistics:** statistical functions
  - `mean()`, `median()`, `mode()`
  - `stdev()`, `variance()`

**Date and Time:**
- **datetime:**
  - `date`, `time`, `datetime` classes
  - Creating date/time objects
  - Formatting with `strftime()`
  - Parsing with `strptime()`
  - `timedelta` for date arithmetic
- **time:**
  - `time()`, `sleep()`
  - `perf_counter()`, `process_time()`
- **calendar:**
  - Calendar operations
  - Checking leap years

**Itertools:**
- **itertools module:**
  - `count()`, `cycle()`, `repeat()`
  - `chain()`, `compress()`, `dropwhile()`
  - `combinations()`, `permutations()`
  - `product()`, `accumulate()`

**System and OS:**
- **sys:**
  - Command-line arguments (sys.argv)
  - `stdin`, `stdout`, `stderr`
  - `exit()`, `version`
- **platform:**
  - System information
  
**Others:**
- **copy:** `copy()`, `deepcopy()`
- **functools:** `lru_cache()`, `partial()`
- **operator:** operator functions

### Week 19-20: Virtual Environments and Package Management

#### 10.1 Virtual Environments
- Why use virtual environments?
- **venv module:**
  - Creating: `python -m venv env_name`
  - Activating (Windows, Mac, Linux)
  - Deactivating
  - pip in virtual environments
- **virtualenv (alternative)**

#### 10.2 Package Management with pip
- Installing packages: `pip install package`
- Installing specific versions
- Uninstalling: `pip uninstall package`
- Listing installed: `pip list`, `pip freeze`
- Requirements file: `requirements.txt`
  - Creating: `pip freeze > requirements.txt`
  - Installing from: `pip install -r requirements.txt`
- Upgrading pip and packages
- pip vs pip3

---

## ⚙️ PHASE 3: OBJECT-ORIENTED PROGRAMMING (Weeks 21-28)

### Week 21-22: OOP Fundamentals

#### 11.1 Classes and Objects
- Understanding OOP concepts
- Class definition with `class` keyword
- Creating objects (instantiation)
- Instance vs class
- `self` parameter
- Multiple objects from one class

#### 11.2 Attributes
- **Instance attributes:**
  - Defining in `__init__`
  - Accessing with `self`
  - Different attributes for different objects
  
- **Class attributes:**
  - Shared across all instances
  - Accessing via class name
  - Modifying class attributes
  
- **Attribute access:**
  - Dot notation
  - `getattr()`, `setattr()`, `hasattr()`, `delattr()`

#### 11.3 Methods
- **Instance methods:**
  - Regular methods with `self`
  - Accessing instance attributes
  
- **Class methods:**
  - `@classmethod` decorator
  - `cls` parameter
  - Alternative constructors
  
- **Static methods:**
  - `@staticmethod` decorator
  - No self or cls
  - Utility functions
  
- **Special/Magic methods:**
  - `__init__`: constructor
  - `__str__`: string representation
  - `__repr__`: official representation
  - `__len__`, `__getitem__`, `__setitem__`
  - `__call__`: making objects callable

### Week 23-24: OOP Principles

#### 12.1 Encapsulation
- **Access modifiers:**
  - Public attributes (default)
  - Protected attributes (single underscore _)
  - Private attributes (double underscore __)
  - Name mangling
  
- **Properties:**
  - `@property` decorator (getter)
  - `@name.setter` decorator
  - `@name.deleter` decorator
  - Read-only properties
  - Computed properties

#### 12.2 Inheritance
- **Basic inheritance:**
  - Parent/base class
  - Child/derived class
  - `super()` function
  - Overriding methods
  - Extending parent methods
  
- **Types of inheritance:**
  - Single inheritance
  - Multiple inheritance
  - Multilevel inheritance
  - Hierarchical inheritance
  
- **Method Resolution Order (MRO):**
  - Understanding MRO
  - `__mro__` attribute
  - `mro()` method
  - C3 linearization algorithm
  
- **isinstance() and issubclass()**

### Week 25-26: Advanced OOP

#### 12.3 Polymorphism
- Method overriding
- Duck typing in Python
- Operator overloading:
  - `__add__`, `__sub__`, `__mul__`, `__truediv__`
  - `__eq__`, `__lt__`, `__gt__`, etc.
  - `__len__`, `__getitem__`, `__setitem__`
- Abstract base classes:
  - `abc` module
  - `@abstractmethod` decorator
  - Creating interfaces

#### 12.4 Abstraction
- Abstract classes
- Abstract methods
- When to use abstraction
- Designing class hierarchies

#### 12.5 Composition vs Inheritance
- Understanding composition
- When to use composition
- Has-a vs Is-a relationship
- Favor composition over inheritance

### Week 27-28: Design Patterns & Best Practices

#### 13.1 Common Design Patterns
- **Creational Patterns:**
  - Singleton
  - Factory
  - Builder
  
- **Structural Patterns:**
  - Adapter
  - Decorator (beyond Python decorators)
  
- **Behavioral Patterns:**
  - Observer
  - Strategy

#### 13.2 OOP Best Practices
- SOLID principles:
  - Single Responsibility
  - Open/Closed
  - Liskov Substitution
  - Interface Segregation
  - Dependency Inversion
- Writing clean, maintainable code
- Proper use of inheritance
- Avoiding common pitfalls

---

## 🚀 PHASE 4: ADVANCED PYTHON (Weeks 29-40)

### Week 29-30: Iterators and Generators

#### 14.1 Iterators
- **Understanding iteration:**
  - Iterable vs iterator
  - iter() and next() functions
  - StopIteration exception
  
- **Creating custom iterators:**
  - `__iter__()` method
  - `__next__()` method
  - Iterator protocol
  
- **Built-in iterators:**
  - range, enumerate, zip
  - reversed, map, filter

#### 14.2 Generators
- **Generator functions:**
  - `yield` keyword
  - How generators work
  - Generator vs regular function
  - Lazy evaluation
  
- **Generator expressions:**
  - Syntax and usage
  - Memory efficiency
  
- **Advanced generator features:**
  - `send()` method
  - `throw()` method
  - `close()` method
  - Generator pipelines
  
- **yield from:**
  - Delegating to subgenerators
  - Flattening nested iterables

### Week 31-32: Decorators

#### 15.1 Function Decorators
- **Basics:**
  - Functions as first-class objects
  - Nested functions
  - Returning functions
  - Closure concept
  
- **Simple decorators:**
  - Creating a basic decorator
  - @ syntax sugar
  - Wrapping functions
  
- **Decorators with arguments:**
  - functools.wraps()
  - Preserving metadata
  
- **Practical decorators:**
  - Timing functions
  - Logging
  - Authentication/Authorization
  - Caching/Memoization
  
- **Stacking decorators:**
  - Multiple decorators on one function
  - Order of execution

#### 15.2 Class Decorators
- Decorating classes
- Creating decorator classes
- `__call__` method

#### 15.3 Built-in Decorators
- `@property`, `@classmethod`, `@staticmethod`
- `@functools.lru_cache`
- `@functools.wraps`
- `@dataclasses.dataclass`

### Week 33-34: Context Managers

#### 16.1 Understanding Context Managers
- The `with` statement
- Why use context managers?
- Resource management
- Exception handling in context managers

#### 16.2 Creating Context Managers
- **Class-based approach:**
  - `__enter__()` method
  - `__exit__()` method
  - Handling exceptions in __exit__
  
- **Decorator approach:**
  - `@contextmanager` decorator
  - Using `yield`
  - Try-finally pattern

#### 16.3 Practical Applications
- File handling
- Database connections
- Acquiring and releasing locks
- Temporary state changes
- Custom context managers for your use cases

### Week 35-36: Advanced Topics

#### 17.1 Metaclasses
- What are metaclasses?
- `type` as a metaclass
- Creating custom metaclasses
- `__new__` vs `__init__`
- When to use metaclasses (rarely needed)

#### 17.2 Descriptors
- What are descriptors?
- `__get__`, `__set__`, `__delete__`
- Data vs non-data descriptors
- Properties revisited (built on descriptors)
- Practical uses

#### 17.3 Magic Methods (Comprehensive)
- **Object creation and destruction:**
  - `__new__`, `__init__`, `__del__`
  
- **String representation:**
  - `__str__`, `__repr__`, `__format__`
  
- **Comparison operators:**
  - `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
  
- **Arithmetic operators:**
  - `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`
  - `__mod__`, `__pow__`, `__neg__`, `__pos__`, `__abs__`
  
- **Container emulation:**
  - `__len__`, `__getitem__`, `__setitem__`, `__delitem__`
  - `__contains__`, `__iter__`, `__reversed__`
  
- **Callable objects:**
  - `__call__`
  
- **Attribute access:**
  - `__getattr__`, `__setattr__`, `__delattr__`
  - `__getattribute__`
  
- **Context managers:**
  - `__enter__`, `__exit__`

#### 17.4 Type Hints and Annotations
- **Basic type hints:**
  - Variable annotations
  - Function annotations
  - Return type hints
  
- **typing module:**
  - `List`, `Dict`, `Tuple`, `Set`
  - `Optional`, `Union`, `Any`
  - `Callable`, `Type`
  - `Literal`, `Final`
  - `TypeVar` for generics
  
- **Type checking:**
  - Using mypy
  - Benefits of static type checking
  
- **Advanced typing:**
  - Generic types
  - Protocol (structural subtyping)
  - TypedDict

#### 17.5 Dataclasses
- `@dataclass` decorator
- Automatic `__init__`, `__repr__`, `__eq__`
- Field definitions
- Default values and default_factory
- Frozen dataclasses (immutable)
- Post-init processing

### Week 37-38: Concurrency and Parallelism

#### 18.1 Threading
- **threading module:**
  - Creating threads
  - Thread class
  - `start()`, `join()`, `is_alive()`
  
- **Thread synchronization:**
  - Race conditions
  - Lock
  - RLock (Reentrant Lock)
  - Semaphore
  - Event
  - Condition
  
- **Thread-local data:**
  - threading.local()
  
- **Threading limitations:**
  - Global Interpreter Lock (GIL)
  - When threading is useful
  - I/O-bound vs CPU-bound tasks

#### 18.2 Multiprocessing
- **multiprocessing module:**
  - Process class
  - Creating processes
  - Process vs Thread
  
- **Inter-process communication:**
  - Queue
  - Pipe
  - Manager
  - Shared memory (Value, Array)
  
- **Process pools:**
  - Pool class
  - map(), apply(), starmap()
  
- **When to use multiprocessing:**
  - CPU-bound tasks
  - Bypassing GIL

#### 18.3 Asynchronous Programming
- **Understanding async:**
  - Asynchronous vs synchronous
  - Event loop concept
  - Coroutines
  
- **asyncio module:**
  - `async` and `await` keywords
  - Creating coroutines
  - Running async functions: `asyncio.run()`
  - Creating tasks: `asyncio.create_task()`
  - Gathering tasks: `asyncio.gather()`
  
- **Async context managers and iterators:**
  - `async with`
  - `async for`
  - `__aenter__`, `__aexit__`
  - `__aiter__`, `__anext__`
  
- **Async libraries:**
  - aiohttp (async HTTP)
  - aiofiles (async file I/O)

#### 18.4 Concurrent.futures
- **ThreadPoolExecutor**
- **ProcessPoolExecutor**
- **Future objects**
- **submit() and map()**
- **as_completed()**

### Week 39-40: Performance and Best Practices

#### 19.1 Code Profiling and Optimization
- **Timing code:**
  - timeit module
  - time.perf_counter()
  
- **Profiling:**
  - cProfile module
  - profile module
  - Line profiler
  
- **Memory profiling:**
  - memory_profiler
  - tracemalloc module
  
- **Optimization techniques:**
  - Using built-in functions
  - List comprehensions vs loops
  - Generator expressions
  - Local variables
  - Avoiding global lookups
  - String concatenation best practices

#### 19.2 Algorithm Complexity
- **Big O notation:**
  - O(1), O(log n), O(n), O(n log n), O(n²)
  - Time vs space complexity
  
- **Analyzing Python operations:**
  - List operations complexity
  - Dictionary operations complexity
  - Set operations complexity
  
- **Choosing right data structure:**
  - When to use list vs tuple vs set
  - When to use dict vs list

#### 19.3 Python Best Practices (PEP 8)
- **Code layout:**
  - Indentation (4 spaces)
  - Maximum line length
  - Blank lines
  
- **Naming conventions:**
  - Variables: snake_case
  - Constants: UPPER_CASE
  - Classes: PascalCase
  - Private: _leading_underscore
  
- **Comments and docstrings:**
  - When to comment
  - Docstring formats (Google, NumPy, reStructuredText)
  
- **Pythonic code:**
  - EAFP vs LBYL
  - Using enumerate instead of range(len())
  - Using zip for parallel iteration
  - Unpacking sequences
  - Using context managers

#### 19.4 Debugging Techniques
- **Print debugging:**
  - Strategic print statements
  - Pretty printing with pprint
  
- **Logging:**
  - logging module
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Configuring loggers
  - File logging
  - Format strings
  
- **Python debugger (pdb):**
  - Setting breakpoints
  - Stepping through code
  - Inspecting variables
  - pdb commands: n, s, c, l, p, q
  
- **IDE debugging:**
  - VS Code debugger
  - PyCharm debugger
  - Breakpoints and watches

#### 19.5 Testing
- **unittest module:**
  - TestCase class
  - Test methods (test_*)
  - Assertions: assertEqual, assertTrue, assertRaises
  - setUp() and tearDown()
  - Test suites and runners
  
- **pytest:**
  - Simple test functions
  - Fixtures
  - Parametrized tests
  - Mocking with pytest-mock
  - Test discovery
  
- **doctest:**
  - Writing tests in docstrings
  - Running doctests
  
- **Test-Driven Development (TDD):**
  - Red-Green-Refactor cycle
  - Benefits of TDD
  
- **Code coverage:**
  - coverage.py
  - Measuring test coverage
  - Coverage reports

---

## 🌐 PHASE 5: SPECIALIZATION PATHS (Weeks 41+)

Choose your path based on career goals. Each path requires 3-6 months of dedicated learning.

### 🧠 PATH A: DATA SCIENCE & MACHINE LEARNING

#### Week 41-44: NumPy (Numerical Python)
- **Arrays:**
  - Creating arrays: array(), zeros(), ones(), empty()
  - arange(), linspace()
  - Array dimensions and shape
  - Reshaping arrays
  - Data types (dtype)
  
- **Array operations:**
  - Element-wise operations
  - Broadcasting
  - Mathematical functions
  - Aggregations: sum(), mean(), std(), min(), max()
  
- **Indexing and slicing:**
  - Basic indexing
  - Slicing multi-dimensional arrays
  - Boolean indexing
  - Fancy indexing
  
- **Array manipulation:**
  - Concatenation and stacking
  - Splitting arrays
  - Transposing
  - Sorting
  
- **Linear algebra:**
  - Matrix operations
  - Dot product
  - Eigenvalues and eigenvectors

#### Week 45-50: Pandas (Data Analysis)
- **Data structures:**
  - Series: 1D labeled array
  - DataFrame: 2D labeled data structure
  - Index and columns
  
- **Creating DataFrames:**
  - From dictionaries
  - From CSV, Excel, JSON
  - From databases
  
- **Data inspection:**
  - head(), tail(), info(), describe()
  - Shape, columns, dtypes
  
- **Indexing and selection:**
  - []: column selection
  - loc[]: label-based
  - iloc[]: position-based
  - Boolean indexing
  
- **Data cleaning:**
  - Handling missing values: isna(), fillna(), dropna()
  - Removing duplicates
  - Data type conversion
  - Renaming columns
  
- **Data transformation:**
  - apply(), map(), applymap()
  - String methods
  - Binning and categorization
  
- **Grouping and aggregation:**
  - groupby() operations
  - Aggregation functions
  - Multiple aggregations
  - Pivot tables and cross-tabulations
  
- **Merging and joining:**
  - concat(): concatenation
  - merge(): SQL-like joins
  - join(): joining on index
  
- **Time series:**
  - DateTime index
  - Resampling
  - Rolling windows
  - Time-based indexing

#### Week 51-54: Data Visualization
- **Matplotlib:**
  - Figure and axes
  - Line plots: plot()
  - Scatter plots: scatter()
  - Bar plots: bar(), barh()
  - Histograms: hist()
  - Customization: colors, labels, titles
  - Subplots
  - Saving figures
  
- **Seaborn:**
  - Statistical plots
  - Distribution plots: distplot(), boxplot(), violinplot()
  - Categorical plots: barplot(), countplot()
  - Relationship plots: scatterplot(), lineplot()
  - Regression plots
  - Heatmaps
  - Styling and themes
  
- **Plotly (interactive):**
  - Interactive plots
  - 3D plots
  - Dashboard creation

#### Week 55-60: Machine Learning (Scikit-learn)
- **ML fundamentals:**
  - Supervised vs unsupervised learning
  - Training and testing sets
  - Cross-validation
  - Overfitting and underfitting
  
- **Data preprocessing:**
  - Feature scaling: StandardScaler, MinMaxScaler
  - Encoding categorical variables
  - Train-test split
  - Handling imbalanced data
  
- **Regression:**
  - Linear Regression
  - Polynomial Regression
  - Ridge and Lasso Regression
  - Evaluation metrics: MSE, RMSE, R²
  
- **Classification:**
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
  - Decision Trees
  - Random Forests
  - Support Vector Machines (SVM)
  - Naive Bayes
  - Evaluation metrics: accuracy, precision, recall, F1-score
  - Confusion matrix
  - ROC curve and AUC
  
- **Clustering:**
  - K-Means
  - Hierarchical clustering
  - DBSCAN
  
- **Dimensionality reduction:**
  - Principal Component Analysis (PCA)
  - t-SNE
  
- **Model selection:**
  - Cross-validation strategies
  - Grid search and hyperparameter tuning
  - Pipeline creation

#### Week 61-70: Deep Learning (Optional)
- **Neural network basics:**
  - Perceptron
  - Activation functions
  - Backpropagation
  - Gradient descent
  
- **TensorFlow/Keras:**
  - Building neural networks
  - Sequential vs Functional API
  - Layers: Dense, Dropout, BatchNormalization
  - Compiling models
  - Training and validation
  - Callbacks
  
- **CNN (Convolutional Neural Networks):**
  - Convolutional layers
  - Pooling layers
  - Image classification
  
- **RNN (Recurrent Neural Networks):**
  - LSTM and GRU
  - Sequence processing
  - Text generation
  
- **PyTorch (alternative):**
  - Tensors
  - Autograd
  - Building models
  - Training loops

---

### 🌍 PATH B: WEB DEVELOPMENT

#### Week 41-44: HTML, CSS, JavaScript Basics
- **HTML:**
  - Document structure
  - Common tags
  - Forms and inputs
  - Semantic HTML
  
- **CSS:**
  - Selectors
  - Box model
  - Flexbox and Grid
  - Responsive design
  
- **JavaScript basics:**
  - Variables and data types
  - Functions
  - DOM manipulation
  - Event handling
  - Fetch API

#### Week 45-52: Django Framework
- **Django setup:**
  - Installation
  - Project structure
  - Settings configuration
  - Apps concept
  
- **Django fundamentals:**
  - **URLs and views:**
    - URL patterns
    - Function-based views
    - Class-based views
    - URL parameters
  
  - **Templates:**
    - Template syntax
    - Template inheritance
    - Template tags and filters
    - Static files
  
  - **Models:**
    - Defining models
    - Field types
    - Relationships: ForeignKey, ManyToMany, OneToOne
    - Migrations: makemigrations, migrate
    - QuerySets and lookups
    - Model methods
  
  - **Forms:**
    - Django forms
    - ModelForms
    - Form validation
    - Handling file uploads
  
  - **Admin interface:**
    - Registering models
    - Customizing admin
    - Admin actions
  
- **Advanced Django:**
  - **User authentication:**
    - User model
    - Login/logout
    - Registration
    - Password reset
    - Permissions and groups
  
  - **Django ORM advanced:**
    - Complex queries
    - Aggregation
    - F() and Q() objects
    - Prefetch and select related
  
  - **Class-based views:**
    - ListView, DetailView
    - CreateView, UpdateView, DeleteView
    - FormView
    - Mixins
  
  - **REST APIs with Django REST Framework:**
    - Serializers
    - ViewSets and Routers
    - Authentication
    - Pagination
    - Filtering and searching
  
  - **Testing in Django:**
    - TestCase
    - Testing views, models, forms
    - Test database
  
  - **Deployment:**
    - Settings for production
    - Static file handling
    - Security settings
    - WSGI and ASGI

#### Week 45-52: Flask Framework (Alternative to Django)
- **Flask basics:**
  - Installation and setup
  - Application factory
  - Routes and views
  - Request and response objects
  
- **Templates:**
  - Jinja2 templating
  - Template inheritance
  - Macros and filters
  
- **Forms:**
  - WTForms integration
  - Form validation
  - CSRF protection
  
- **Database:**
  - SQLAlchemy integration
  - Models and migrations (Flask-Migrate)
  - Queries
  
- **User authentication:**
  - Flask-Login
  - User sessions
  - Password hashing
  
- **RESTful APIs:**
  - Creating API endpoints
  - JSON responses
  - Flask-RESTful extension
  
- **Blueprints:**
  - Modular applications
  - Blueprint registration
  
- **Deployment:**
  - Configuration
  - Production servers (Gunicorn)

#### Week 53-56: Frontend Integration
- **AJAX and fetch:**
  - Asynchronous requests
  - JSON data exchange
  
- **Frontend frameworks (intro):**
  - React basics
  - Vue.js basics
  - Connecting to Python backend
  
- **WebSockets:**
  - Real-time communication
  - Django Channels
  - Flask-SocketIO

#### Week 57-60: APIs and Web Services
- **RESTful API design:**
  - HTTP methods: GET, POST, PUT, DELETE
  - Status codes
  - API versioning
  - Documentation (Swagger/OpenAPI)
  
- **FastAPI:**
  - Modern Python web framework
  - Automatic API documentation
  - Type hints integration
  - Async support
  - Dependency injection
  
- **GraphQL:**
  - GraphQL basics
  - Graphene-Python
  
- **Authentication:**
  - JWT tokens
  - OAuth2
  - API keys

---

### 🤖 PATH C: AUTOMATION & WEB SCRAPING

#### Week 41-44: Web Scraping Fundamentals
- **HTTP and web basics:**
  - How web pages work
  - HTML/CSS/JavaScript understanding
  - Developer tools
  
- **requests library:**
  - GET and POST requests
  - Headers and cookies
  - Session objects
  - Handling responses
  - Query parameters
  
- **BeautifulSoup:**
  - Parsing HTML
  - Navigating the parse tree
  - Finding elements: find(), find_all()
  - CSS selectors: select()
  - Extracting data
  - Handling encoding
  
- **Advanced scraping:**
  - Handling pagination
  - Rate limiting and delays
  - User agents
  - Proxies
  - Scraping ethics and robots.txt

#### Week 45-48: Selenium (Browser Automation)
- **Selenium WebDriver:**
  - Setting up drivers (Chrome, Firefox)
  - Browser control
  - Navigating pages
  
- **Locating elements:**
  - By ID, name, class, tag
  - XPath and CSS selectors
  - find_element vs find_elements
  
- **Interactions:**
  - Clicking elements
  - Sending keys
  - Form submission
  - Dropdowns and selects
  
- **Waits:**
  - Implicit waits
  - Explicit waits
  - Expected conditions
  
- **Advanced features:**
  - Screenshots
  - Headless mode
  - Handling alerts and popups
  - Switching frames and windows
  - Executing JavaScript

#### Week 49-52: File and System Automation
- **Working with files:**
  - Bulk file operations
  - Renaming files
  - Organizing directories
  - File searching
  
- **PDF manipulation:**
  - PyPDF2: reading, merging, splitting PDFs
  - ReportLab: creating PDFs
  
- **Excel automation:**
  - openpyxl: reading/writing Excel
  - Formatting cells
  - Creating charts
  - xlwings: Excel with Python
  
- **Word documents:**
  - python-docx
  - Reading and creating documents
  
- **Email automation:**
  - smtplib: sending emails
  - Email composition
  - Attachments
  - imaplib: reading emails
  
- **Scheduled tasks:**
  - schedule library
  - Cron jobs (Linux/Mac)
  - Task Scheduler (Windows)

#### Week 53-56: Advanced Automation
- **GUI automation:**
  - pyautogui
  - Mouse and keyboard control
  - Screenshot and image recognition
  
- **Database automation:**
  - Automated backups
  - Data migration scripts
  - Report generation
  
- **API interactions:**
  - Automating API calls
  - Data synchronization
  - Webhooks
  
- **Building workflows:**
  - Combining multiple automation tasks
  - Error handling and logging
  - Creating robust scripts

---

### 🎮 PATH D: GAME DEVELOPMENT (Pygame)

#### Week 41-44: Pygame Basics
- **Setup and window:**
  - Installing Pygame
  - Creating game window
  - Game loop concept
  - Frame rate and Clock
  
- **Drawing:**
  - Shapes: rect, circle, line
  - Colors
  - Surfaces
  - Blitting images
  
- **Events:**
  - Event handling
  - Keyboard input
  - Mouse input
  - Quit events

#### Week 45-48: Game Mechanics
- **Sprites:**
  - Sprite class
  - Sprite groups
  - Collision detection
  
- **Movement:**
  - Position and velocity
  - Player control
  - Gravity and physics
  
- **Sound:**
  - Sound effects
  - Background music
  - Volume control

#### Week 49-52: Advanced Game Development
- **Animation:**
  - Sprite sheets
  - Frame animation
  
- **Game states:**
  - Menu screens
  - Pause functionality
  - Game over screens
  
- **Scoring and UI:**
  - Displaying text
  - HUD elements
  - Health bars
  
- **Project:**
  - Build complete game (platformer, shooter, puzzle)

---

### 🔐 PATH E: CYBERSECURITY

#### Week 41-44: Networking Basics
- **Socket programming:**
  - TCP/IP basics
  - Client-server architecture
  - socket module
  - Creating servers and clients
  
- **Network protocols:**
  - HTTP/HTTPS
  - FTP, SSH, Telnet
  - DNS

#### Week 45-48: Security Fundamentals
- **Cryptography:**
  - Hashing: hashlib
  - Encryption/Decryption
  - cryptography library
  - SSL/TLS basics
  
- **Password security:**
  - Password hashing (bcrypt, argon2)
  - Salt and pepper
  - Password strength checking

#### Week 49-54: Penetration Testing
- **Scapy:**
  - Packet crafting
  - Network scanning
  - Packet sniffing
  
- **Port scanning:**
  - Building port scanner
  - Service detection
  
- **Vulnerability assessment:**
  - Common vulnerabilities
  - Scanning tools
  
- **Web security:**
  - SQL injection testing
  - XSS testing
  - CSRF protection

---

## 🗄️ PHASE 6: DATABASE INTEGRATION (Can be done alongside specialization)

### Week 1-2: SQL Fundamentals
- **SQL basics:**
  - SELECT statements
  - WHERE clauses
  - ORDER BY and LIMIT
  - Aggregate functions: COUNT, SUM, AVG, MAX, MIN
  
- **Data manipulation:**
  - INSERT, UPDATE, DELETE
  - Transactions: COMMIT, ROLLBACK
  
- **Joins:**
  - INNER JOIN
  - LEFT/RIGHT JOIN
  - FULL OUTER JOIN
  - Self joins
  
- **Advanced SQL:**
  - Subqueries
  - GROUP BY and HAVING
  - UNION
  - Indexes
  - Views

### Week 3-4: Python Database Integration
- **SQLite:**
  - sqlite3 module
  - Creating databases and tables
  - Executing queries
  - Parameterized queries (preventing SQL injection)
  - Cursor operations
  - Context managers with databases
  
- **MySQL:**
  - mysql-connector-python
  - PyMySQL
  - Connection pooling
  
- **PostgreSQL:**
  - psycopg2
  - Connection management
  
- **Best practices:**
  - Prepared statements
  - Error handling
  - Connection pooling
  - Avoiding SQL injection

### Week 5-6: ORM (Object-Relational Mapping)
- **SQLAlchemy:**
  - Core vs ORM
  - Engine and session
  - Declaring models
  - Relationships: one-to-many, many-to-many
  - Querying with ORM
  - Migrations with Alembic
  
- **Django ORM (if using Django):**
  - Model definition
  - QuerySets
  - Complex queries
  - Transactions

---

## 📦 PHASE 7: DEVELOPMENT TOOLS & ECOSYSTEM

### Version Control (Git & GitHub)
- **Git basics:**
  - init, clone, status
  - add, commit, push, pull
  - Branching and merging
  - Resolving conflicts
  - .gitignore
  
- **GitHub:**
  - Creating repositories
  - Pull requests
  - Issues and project boards
  - Collaboration workflows
  - GitHub Actions (CI/CD basics)

### Development Environment
- **VS Code:**
  - Python extension
  - Linting: pylint, flake8
  - Formatting: black, autopep8
  - Debugging
  - Code navigation
  
- **PyCharm:**
  - Project setup
  - Debugging tools
  - Refactoring tools

### Code Quality
- **Linters:**
  - pylint
  - flake8
  - mypy (type checking)
  
- **Formatters:**
  - black
  - autopep8
  - isort (import sorting)
  
- **Pre-commit hooks:**
  - Setting up pre-commit
  - Running checks before commits

### Documentation
- **Docstrings:**
  - Google style
  - NumPy style
  - Sphinx/reStructuredText
  
- **README files:**
  - Project description
  - Installation instructions
  - Usage examples
  
- **Sphinx:**
  - Generating documentation
  - Read the Docs

### Containerization (Optional Advanced)
- **Docker basics:**
  - What is Docker?
  - Dockerfile
  - Building images
  - Running containers
  - Docker Compose

---

## 💡 PROJECT IDEAS BY LEVEL

### Beginner Projects (Weeks 1-8)
1. **Calculator** - basic arithmetic operations
2. **Number guessing game** - random number, user input
3. **Password generator** - random string generation
4. **To-do list (CLI)** - CRUD operations with files
5. **Simple quiz app** - questions and scoring
6. **Unit converter** - temperature, length, weight
7. **Rock, paper, scissors** - game logic
8. **Mad Libs generator** - string manipulation
9. **Countdown timer** - time module
10. **Simple banking system** - OOP with classes

### Intermediate Projects (Weeks 9-28)
1. **Weather app** - API integration (OpenWeatherMap)
2. **File organizer** - automate file organization
3. **Web scraper** - scrape quotes/news
4. **URL shortener** - database, hash generation
5. **Expense tracker** - file I/O, data analysis with Pandas
6. **Contact management system** - CRUD with SQL
7. **Markdown to HTML converter** - file processing
8. **Password manager** - encryption, database
9. **Blog (Django/Flask)** - full CRUD web app
10. **Chat application** - sockets/websockets
11. **Email sender** - SMTP automation
12. **CSV to JSON converter** - file handling
13. **Plagiarism detector** - string algorithms
14. **Currency converter** - API integration
15. **Task scheduler** - automation with schedule

### Advanced Projects (Weeks 29+)
1. **Machine learning model** - prediction/classification
2. **REST API** - FastAPI/Django REST with authentication
3. **E-commerce website** - full-stack with payment integration
4. **Social media dashboard** - data visualization
5. **Real-time chat app** - WebSockets, async
6. **Image recognition system** - CNN with TensorFlow
7. **Stock market analyzer** - data science, visualization
8. **Recommendation system** - ML algorithms
9. **Automation bot** - Selenium, complex workflows
10. **Portfolio website with CMS** - Django/Flask backend
11. **API aggregator** - combining multiple APIs
12. **Real-time dashboard** - data streaming
13. **Blockchain implementation** - understanding cryptography
14. **AI chatbot** - NLP, machine learning
15. **DevOps pipeline** - CI/CD with Docker

---

## 📚 LEARNING STRATEGY & TIPS

### Daily Study Routine
**Beginner (Weeks 1-8):**
- 1-2 hours daily
- 30 min theory
- 60-90 min coding practice
- Build one mini-project per week

**Intermediate (Weeks 9-28):**
- 2-3 hours daily
- 45 min reading/watching
- 90-120 min hands-on coding
- Work on 2-3 week projects

**Advanced (Weeks 29-40):**
- 3-4 hours daily
- 1 hour deep concepts
- 2-3 hours implementation
- Month-long complex projects

### Problem-Solving Practice
- **Platforms:**
  - HackerRank (beginner-friendly)
  - LeetCode (interview prep)
  - CodeWars (gamified)
  - Project Euler (mathematical)
  - Exercism (mentored)
  
- **Schedule:**
  - Solve 1-2 problems daily (beginner)
  - Solve 2-3 problems daily (intermediate)
  - Participate in contests (advanced)

### Retention Techniques
1. **Code daily** - consistency over intensity
2. **Build projects** - apply concepts immediately
3. **Teach others** - write blogs, create tutorials
4. **Read code** - explore open-source projects on GitHub
5. **Take notes** - maintain a personal wiki
6. **Review regularly** - revisit topics weekly

### Common Pitfalls to Avoid
❌ Tutorial hell - watching without coding
❌ Copying code without understanding
❌ Skipping fundamentals
❌ Not handling errors
❌ Avoiding documentation
❌ Working in isolation
✅ Code along with tutorials
✅ Type every line yourself
✅ Master basics before advancing
✅ Learn debugging early
✅ Read official docs
✅ Join coding communities

### Timeline Guidelines
- **Beginner proficiency:** 2-3 months (consistent practice)
- **Intermediate level:** +3-4 months
- **Advanced concepts:** +2-3 months
- **Specialization mastery:** +3-6 months
- **Total to job-ready:** 10-18 months (depending on goals and pace)

### Weekly Milestones
- **Week 4:** Build a working calculator with error handling
- **Week 8:** Create a file-based to-do app with full CRUD
- **Week 12:** Automate a real task (file organization, web scraping)
- **Week 20:** Build a small web application or data analysis project
- **Week 28:** Ship a complex OOP project
- **Week 40:** Complete advanced project in chosen specialization
- **Week 52:** Portfolio with 5-7 substantial projects

---

## 🎯 FINAL NOTES

### Keys to Success
1. **Consistency beats intensity** - 1 hour daily > 7 hours on Sunday
2. **Build, don't just learn** - projects solidify knowledge
3. **Embrace errors** - debugging teaches more than success
4. **Join communities** - r/learnpython, Python Discord, local meetups
5. **Contribute to open source** - real-world experience
6. **Never stop learning** - Python ecosystem constantly evolves

### After This Roadmap
- **Contribute to open source projects**
- **Build a strong GitHub portfolio**
- **Write technical blogs**
- **Attend Python conferences (PyCon)**
- **Get certified (optional):** PCEP, PCAP, PCPP
- **Apply for jobs/freelance projects**
- **Keep learning** - stay updated with Python release notes

### Resources Organization
- **Official documentation:** python.org/doc
- **PEP (Python Enhancement Proposals):** especially PEP 8, PEP 20 (Zen of Python)
- **Practice platforms:** mentioned above
- **Community:** Stack Overflow, Reddit, Discord servers

---

## 🚀 YOU'RE READY TO START!

This roadmap is comprehensive and self-contained. Follow it sequentially, build projects at every stage, and you'll master Python from scratch. Remember: the journey is more important than the destination. Code daily, stay curious, and enjoy the process!

**Happy Coding! 🐍**

---
