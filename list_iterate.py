import time
from collections import namedtuple, deque, defaultdict, Counter
from dataclasses import dataclass
from enum import Enum

def print_all_robust(obj, delay=0.02, visited=None, depth=0, max_depth=50):
    """
    Robust function to extract and print all primitive values from any Python object.
    Handles circular references, deep nesting, custom objects, and edge cases.
    """
    if visited is None:
        visited = set()
    
    # Prevent infinite recursion
    if depth > max_depth:
        print(f"[MAX DEPTH REACHED: {type(obj).__name__}]")
        return
    
    # Handle circular references for mutable objects
    obj_id = id(obj)
    if isinstance(obj, (dict, list, set, tuple)) and obj_id in visited:
        print(f"[CIRCULAR REFERENCE: {type(obj).__name__}]")
        return
    
    if obj is None:
        print("None")
        time.sleep(delay)
    elif isinstance(obj, (str, int, float, bool)):
        print(obj)
        time.sleep(delay)
    elif isinstance(obj, bytes):
        print(f"bytes: {obj.decode('utf-8', errors='replace')}")
        time.sleep(delay)
    elif hasattr(obj, 'values'):  # dict-like objects
        if isinstance(obj, (dict, list, set, tuple)):
            visited.add(obj_id)
        for v in obj.values():
            print_all_robust(v, delay, visited, depth+1, max_depth)
        if isinstance(obj, (dict, list, set, tuple)):
            visited.discard(obj_id)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
        if isinstance(obj, (dict, list, set, tuple)):
            visited.add(obj_id)
        for item in obj:
            print_all_robust(item, delay, visited, depth+1, max_depth)
        if isinstance(obj, (dict, list, set, tuple)):
            visited.discard(obj_id)
    elif hasattr(obj, '__dict__'):  # Custom objects with attributes
        print(f"[Object: {type(obj).__name__}]")
        for attr_name, attr_value in obj.__dict__.items():
            if not attr_name.startswith('_'):  # Skip private attributes
                print_all_robust(attr_value, delay, visited, depth+1, max_depth)
    else:
        print(f"[{type(obj).__name__}: {repr(obj)}]")
        time.sleep(delay)

# ============================================================================
# COMPREHENSIVE DEMO - ALL EDGE CASES
# ============================================================================

print("🚀 COMPREHENSIVE DATA EXTRACTION DEMO 🚀")
print("=" * 60)

# Original test data (your example)
rand = {'ü':'$', '$':'ü', 'aa':'22', 'rr':'ii', '44':'55', 'tt':'88'}
val = {'thing1':'thing2', 'hi':'ho','gosh':{'golly':'goodness', 'blimey':[1, 2, 3, [3.5, 3.6, 3.7, rand, 3.8], 5, 6]}, 'easy':'peasy'}
jk = [0.123, 0.44, 0.55, 1.4, 6]
ppp = [val, val['thing1'], jk]
mv = ['item 1', 'item2', 6, 1, ppp, 2, 44]
t = ['patient zero', val.get('gosh', {}).get('blimey'), 'object x']
original_data = [t, 1, None, None, mv, None, 2, 3, None, "gubbins", val['thing1']]

# Circular references
circular_dict = {'a': 1, 'b': 2}
circular_dict['self'] = circular_dict
circular_list = [1, 2, 3]
circular_list.append(circular_list)

# Custom objects
@dataclass
class Person:
    name: str
    age: int
    skills: list

class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

engineer = Person("Gordon", 42, ["Python", "CATIA", "Problem Solving"])

# Special collections
Point = namedtuple('Point', ['x', 'y', 'z'])
special_data = {
    'deque': deque([1, 2, 3, 4]),
    'defaultdict': defaultdict(list, {'items': [1, 2, 3]}),
    'counter': Counter(['a', 'b', 'a', 'c', 'a']),
    'point': Point(10, 20, 30),
    'status': Status.ACTIVE
}

# Unicode and edge cases
unicode_data = {
    'emoji': '🔧⚙️🚀',
    'chinese': '工程师',
    'math': 'π ≈ 3.14159',
    'special_chars': 'café naïve résumé',
    'bytes': b'binary_data',
    'empty_stuff': {'dict': {}, 'list': [], 'string': ''},
    'numbers': [0, -999, 1e-10, float('inf'), float('nan')],
    'booleans': [True, False]
}

# Deep nesting
deep_structure = {'level': 1}
current = deep_structure
for i in range(2, 15):
    current['next'] = {'level': i, 'data': f'level_{i}_data'}
    current = current['next']

# Real-world scenario
production_data = {
    'system_info': {
        'version': '2.1.0',
        'environment': 'production',
        'features': ['automation', 'monitoring', None]
    },
    'users': [
        engineer,
        {'name': 'Alice', 'role': 'designer', 'active': True},
        {'name': None, 'role': 'tester', 'active': False}
    ],
    'metrics': {
        'uptime': 99.97,
        'errors': 0,
        'performance': [1.2, 0.8, 1.5, None, 2.1]
    },
    'config': special_data
}

# Ultimate test - combine everything
ultimate_test = {
    'original': original_data,
    'circular': [circular_dict, circular_list],
    'unicode': unicode_data,
    'deep': deep_structure,
    'production': production_data,
    'edge_cases': [None, '', 0, False, [], {}]
}

print("\n🎯 EXTRACTING ALL PRINTABLE VALUES...")
print("=" * 60)

start_time = time.time()
print_all_robust(ultimate_test, delay=0.01)  # Fast demo
end_time = time.time()

print("\n" + "=" * 60)
print(f"✅ EXTRACTION COMPLETE!")
print(f"⏱️  Processing time: {end_time - start_time:.3f} seconds")
print(f"🛡️  Handled: Circular refs, Unicode, Custom objects, Deep nesting, Edge cases")
print("=" * 60)