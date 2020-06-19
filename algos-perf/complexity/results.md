## contains
#### 100
hashtables are 20x faster

#### 1K
hashtables are 250x faster

#### 10K
hashtables are 2500x faster

| struct    | time   |
|-----------|--------|
| deque     | 2000ms |
| list      | 2000ms |
| tuple     | 2000ms |
| set       | 30ms   |
| dict      | 30ms   |
| frozenset | 30ms   |

#### 50K
hashtables are 10,000x faster

## iteration @ 10K
| struct    | time  |
|-----------|-------|
| deque     | 0.5ms |
| list      | 0.5ms |
| tuple     | 0.5ms |
| set       | 0.5ms |
| dict      | 0.5ms |
| frozenset | 0.5ms |

## hash
#### 100K
frozenset is 4000x faster than tuple

#### 10K
frozenset is 115x faster than tuple

#### 1K
frozenset is 90x faster than tuple

#### 100
frozenset is 6x faster than tuple

## getting
#### 300K
dict is 13,000x faster than set/frozenset
dict is 5000x faster than deque/list/tuple
deque/list/tuple 2.6x faster than set/frozenset

| struct    | time        (ms)      |
|-----------|-----------------------|
| dict      | 0.000000001 (0.001ns) |
| deque     | 0.000005 (5ns)        |
| list      | 0.000005 (5ns)        |
| tuple     | 0.000005 (5ns)        |
| set       | 0.000013 (13ns)       |
| frozenset | 0.000013 (13ns)       |

#### 100K
dict is 3700x faster than set/frozenset
dict is 1250x faster than deque/list/tuple
deque/list/tuple 3x faster than set/frozenset

| struct    | time        (ms)        |
|-----------|-------------------------|
| dict      | 0.0000000008 (0.0008ns) |
| deque     | 0.000001 (1ns)          |
| list      | 0.000001 (1ns)          |
| tuple     | 0.000001 (1ns)          |
| set       | 0.000003 (3ns)          |
| frozenset | 0.000003 (3ns)          |

#### 30K
dict is 900x faster than set/frozenset
dict is 500x faster than deque/list/tuple
deque/list/tuple 1.5x faster than set/frozenset

| struct    | time        (ms)      |
|-----------|-----------------------|
| dict      | 0.000000001 (0.001ns) |
| deque     | 0.0000005 (0.5ns)     |
| list      | 0.0000005 (0.5ns)     |
| tuple     | 0.0000005 (0.5ns)     |
| set       | 0.0000008 (0.8ns)     |
| frozenset | 0.0000008 (0.8ns)     |

#### 10K
dict is 250x faster than set/frozenset
dict is 150x faster than deque/list/tuple
deque/list/tuple 1.5x faster than set/frozenset

| struct    | time        (ms)      |
|-----------|-----------------------|
| dict      | 0.000000001 (0.001ns) |
| deque     | 0.00000015 (0.15ns)   |
| list      | 0.00000015 (0.15ns)   |
| tuple     | 0.00000015 (0.15ns)   |
| set       | 0.00000025 (0.25ns)   |
| frozenset | 0.00000025 (0.25ns)   |

#### 1K
dict is 25x faster than set/frozenset
dict is 18x faster than deque/list/tuple
deque/list/tuple 1.3x faster than set/frozenset

| struct    | time        (ms)        |
|-----------|-------------------------|
| dict      | 0.0000000008 (0.0008ns) |
| deque     | 0.000000015 (0.015ns)   |
| list      | 0.000000015 (0.015ns)   |
| tuple     | 0.000000015 (0.015ns)   |
| set       | 0.00000002 (0.02ns)     |
| frozenset | 0.00000002 (0.02ns)     |

#### 100
dict is 2.5x faster than the rest

| struct    | time        (ms)        |
|-----------|-------------------------|
| dict      | 0.0000000008 (0.0008ns) |
| deque     | 0.000000002 (0.002ns)   |
| list      | 0.000000002 (0.002ns)   |
| tuple     | 0.000000002 (0.002ns)   |
| set       | 0.000000002 (0.002ns)   |
| frozenset | 0.000000002 (0.002ns)   |

## Initialization
## Extension