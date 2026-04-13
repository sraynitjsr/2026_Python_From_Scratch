def variables_data_types():
    print("\n" + "="*60)
    print("SECTION 1.2: VARIABLES AND DATA TYPES")
    print("="*60 + "\n")
    
    # ========================================
    # 1.1 VARIABLES
    # ========================================
    print("--- 1.1 VARIABLES ---\n")
    
    # Variable naming rules and conventions
    print("✓ Variable Naming:")
    user_name = "Tufan"              # Snake_case (Python convention)
    age = 25                          # Descriptive names
    is_learning = True                # Boolean naming
    MAX_SCORE = 100                   # Constants in UPPERCASE
    print(f"  user_name = '{user_name}' (snake_case)")
    print(f"  age = {age}")
    print(f"  is_learning = {is_learning}")
    print(f"  MAX_SCORE = {MAX_SCORE} (constant)\n")
    
    # Variable assignment and reassignment
    print("✓ Variable Assignment & Reassignment:")
    score = 50
    print(f"  Initial score: {score}")
    score = 75  # Reassignment
    print(f"  After reassignment: {score}\n")
    
    # Multiple assignment
    print("✓ Multiple Assignment:")
    x, y, z = 10, 20, 30
    print(f"  x, y, z = 10, 20, 30 → x={x}, y={y}, z={z}")
    a = b = c = 100
    print(f"  a = b = c = 100 → a={a}, b={b}, c={c}\n")
    
    # Variable scope demonstration
    print("✓ Variable Scope:")
    global_var = "I'm global"
    
    def demo_scope():
        local_var = "I'm local"
        print(f"  Inside function - local_var: '{local_var}'")
        print(f"  Inside function - global_var: '{global_var}'")
    
    demo_scope()
    print(f"  Outside function - global_var: '{global_var}'")
    print(f"  (local_var doesn't exist outside the function)\n")
    
    # Global keyword demonstration
    print("✓ Using 'global' Keyword:")
    print("  (Modifying a variable from outer scope without global causes error)")
    
    def show_global_example():
        # This would create a new local variable named 'global_var'
        # But with 'global', it modifies the outer one
        global global_var
        global_var = "Modified globally!"
        print(f"  Inside function with global: '{global_var}'")
    
    show_global_example()
    print(f"  Outside function after modification: '{global_var}'\n")
    
    # Nonlocal keyword
    print("✓ Using 'nonlocal' Keyword:")
    
    def outer():
        outer_var = 10
        
        def inner():
            nonlocal outer_var
            outer_var = 20
            print(f"  Inner function changed outer_var to: {outer_var}")
        
        inner()
        print(f"  Outer function sees outer_var as: {outer_var}")
    
    outer()
    print()
    
    # ========================================
    # 1.2 DATA TYPES - NUMBERS
    # ========================================
    print("--- 1.2 DATA TYPES: NUMBERS ---\n")
    
    # Integers
    print("✓ Integers (int):")
    num_int = 42
    negative_int = -100
    large_int = 1_000_000  # Underscores for readability
    print(f"  num_int = {num_int}, type: {type(num_int)}")
    print(f"  negative_int = {negative_int}")
    print(f"  large_int = {large_int:,} (formatted with commas)\n")
    
    # Floats
    print("✓ Floating Point (float):")
    num_float = 3.14159
    scientific = 2.5e3  # 2.5 × 10^3 = 2500
    print(f"  num_float = {num_float}, type: {type(num_float)}")
    print(f"  scientific notation: 2.5e3 = {scientific}\n")
    
    # Complex numbers
    print("✓ Complex Numbers (complex):")
    num_complex = 3 + 4j
    print(f"  num_complex = {num_complex}, type: {type(num_complex)}")
    print(f"  Real part: {num_complex.real}")
    print(f"  Imaginary part: {num_complex.imag}\n")
    
    # Type conversion
    print("✓ Type Conversion (Numbers):")
    x_int = int(3.9)           # Float to int (truncates)
    y_float = float(5)         # Int to float
    z_str = str(42)            # Int to string
    print(f"  int(3.9) = {x_int}")
    print(f"  float(5) = {y_float}")
    print(f"  str(42) = '{z_str}' (type: {type(z_str)})\n")
    
    # Numeric operations
    print("✓ Numeric Operations:")
    a, b = 10, 3
    print(f"  a = {a}, b = {b}")
    print(f"  Addition: {a} + {b} = {a + b}")
    print(f"  Subtraction: {a} - {b} = {a - b}")
    print(f"  Multiplication: {a} * {b} = {a * b}")
    print(f"  Division: {a} / {b} = {a / b}")
    print(f"  Floor Division: {a} // {b} = {a // b}")
    print(f"  Modulus: {a} % {b} = {a % b}")
    print(f"  Exponentiation: {a} ** {b} = {a ** b}\n")
    
    # Operator precedence
    print("✓ Operator Precedence:")
    result = 2 + 3 * 4 ** 2
    print(f"  2 + 3 * 4 ** 2 = {result}")
    print(f"  (Follows: ** → * → +)\n")
    
    # ========================================
    # 1.3 DATA TYPES - STRINGS
    # ========================================
    print("--- 1.3 DATA TYPES: STRINGS ---\n")
    
    # Creating strings
    print("✓ Creating Strings:")
    str_single = 'Single quotes'
    str_double = "Double quotes"
    str_triple = '''Triple quotes
can span multiple
lines'''
    print(f"  Single quotes: '{str_single}'")
    print(f"  Double quotes: \"{str_double}\"")
    print(f"  Triple quotes:\n{str_triple}\n")
    
    # String indexing
    print("✓ String Indexing:")
    text = "Python"
    print(f"  text = '{text}'")
    print(f"  text[0] = '{text[0]}' (first character)")
    print(f"  text[-1] = '{text[-1]}' (last character)")
    print(f"  text[2] = '{text[2]}'\n")
    
    # String slicing
    print("✓ String Slicing:")
    print(f"  text[0:3] = '{text[0:3]}' (characters 0, 1, 2)")
    print(f"  text[2:] = '{text[2:]}' (from index 2 to end)")
    print(f"  text[:4] = '{text[:4]}' (from start to index 3)")
    print(f"  text[::2] = '{text[::2]}' (every 2nd character)")
    print(f"  text[::-1] = '{text[::-1]}' (reversed)\n")
    
    # String immutability
    print("✓ String Immutability:")
    original = "Hello"
    print(f"  Strings cannot be changed in place")
    print(f"  original = '{original}'")
    print(f"  To 'change', create new string: original.replace('H', 'J') = '{original.replace('H', 'J')}'")
    print(f"  Original unchanged: '{original}'\n")
    
    # String concatenation and repetition
    print("✓ String Concatenation & Repetition:")
    first = "Hello"
    last = "World"
    print(f"  '{first}' + ' ' + '{last}' = '{first + ' ' + last}'")
    print(f"  'Ha' * 3 = '{'Ha' * 3}'\n")
    
    # Escape characters
    print("✓ Escape Characters:")
    print(f"  Newline: 'Line1\\nLine2' →")
    print(f"Line1\nLine2")
    print(f"  Tab: 'Name\\tAge' → Name\tAge")
    print(f"  Backslash: 'C:\\\\path' → C:\\path")
    print(f"  Quote: 'He said \\'Hi\\'' → He said 'Hi'\n")
    
    # Raw strings
    print("✓ Raw Strings:")
    path = r"C:\new\test"
    print(f"  r'C:\\new\\test' = '{path}' (backslashes not escaped)\n")
    
    # String methods
    print("✓ Common String Methods:")
    sample = "  Python Programming  "
    print(f"  original = '{sample}'")
    print(f"  .upper() = '{sample.upper()}'")
    print(f"  .lower() = '{sample.lower()}'")
    print(f"  .strip() = '{sample.strip()}'")
    print(f"  .replace('Python', 'Java') = '{sample.replace('Python', 'Java')}'")
    print(f"  .split() = {sample.split()}")
    print(f"  len(sample) = {len(sample)}\n")
    
    # ========================================
    # 1.4 DATA TYPES - BOOLEAN
    # ========================================
    print("--- 1.4 DATA TYPES: BOOLEAN ---\n")
    
    # Boolean values
    print("✓ Boolean Values:")
    is_active = True
    is_deleted = False
    print(f"  is_active = {is_active}, type: {type(is_active)}")
    print(f"  is_deleted = {is_deleted}\n")
    
    # Boolean type conversion
    print("✓ Boolean Type Conversion:")
    print(f"  bool(1) = {bool(1)}")
    print(f"  bool(0) = {bool(0)}")
    print(f"  bool('text') = {bool('text')}")
    print(f"  bool('') = {bool('')}\n")
    
    # Truthy and Falsy values
    print("✓ Truthy and Falsy Values:")
    print(f"  Falsy values: False, 0, 0.0, '', [], {{}}, None")
    print(f"  bool(0) = {bool(0)}")
    print(f"  bool('') = {bool('')}")
    print(f"  bool([]) = {bool([])}")
    print(f"  Truthy: Everything else!")
    print(f"  bool(1) = {bool(1)}")
    print(f"  bool('any text') = {bool('any text')}\n")
    
    # None type
    print("✓ None Type:")
    result = None
    print(f"  result = {result}, type: {type(result)}")
    print(f"  None represents 'no value' or 'null'\n")
    
    # ========================================
    # 1.5 PRACTICAL EXAMPLES
    # ========================================
    print("--- 1.5 PRACTICAL EXAMPLES ---\n")
    
    # Type checking
    print("✓ Type Checking:")
    value = 42
    print(f"  value = {value}")
    print(f"  type(value) = {type(value)}")
    print(f"  isinstance(value, int) = {isinstance(value, int)}")
    print(f"  isinstance(value, str) = {isinstance(value, str)}\n")
    
    # String formatting
    print("✓ String Formatting (f-strings):")
    name = "Alice"
    age = 30
    height = 5.6
    print(f"  f'Name: {name}, Age: {age}, Height: {height}ft'")
    print(f"  → Name: {name}, Age: {age}, Height: {height}ft")
    print(f"  f'{height:.1f}' = {height:.1f} (1 decimal place)\n")
    
    # format() method
    print("✓ String Formatting (.format() method):")
    template = "Hello {}, you are {} years old"
    print(f"  '{template}'.format('{name}', {age})")
    print(f"  → {template.format(name, age)}\n")
    
    # Old-style formatting
    print("✓ Old-Style Formatting (% operator):")
    print(f"  'Name: %s, Age: %d' % ('{name}', {age})")
    print(f"  → Name: %s, Age: %d\n" % (name, age))
    
    print("="*60)
    print("✅ SECTION 1.2 COMPLETE")
    print("="*60 + "\n")
