import re

# Test string with multiple HTML-like tags
text = """
<div>Simple example</div>
<span>Multiple <b>nested</b> tags</span>
<p>Another <i>example</i> with <b>multiple</b> inner tags</p>
"""

print("1. Greedy vs Lazy tag matching:")
print("-" * 50)

# Greedy matching (.*) - matches as much as possible
greedy = re.findall('<.*>', text)
print("Greedy '<.*>':")
for match in greedy:
    print(f"  {match}")

# Lazy matching (.*?) - matches as little as possible
lazy = re.findall('<.*?>', text)
print("\nLazy '<.*?>':")
for match in lazy:
    print(f"  {match}")

print("\n2. Getting content between tags:")
print("-" * 50)

# Method 1: Using positive lookbehind and lookahead
content1 = re.findall('(?<=>).*?(?=<)', text)
print("Using lookbehind/lookahead '(?<=>).*?(?=<)':")
for match in content1:
    print(f"  {match}")

# Method 2: Capture group with lazy matching
content2 = re.findall('<[^>]+>(.*?)</[^>]+>', text)
print("\nUsing capture group '<[^>]+>(.*?)</[^>]+>':")
for match in content2:
    print(f"  {match}")

print("\n3. Advanced examples:")
print("-" * 50)

# Match specific tag content
div_content = re.findall('<div>(.*?)</div>', text)
print("Only div content:")
for match in div_content:
    print(f"  {match}")

# Match innermost tags
innermost = re.findall('<([^>]+)>([^<]+)</\\1>', text)
print("\nInnermost tags and their content:")
for tag, content in innermost:
    print(f"  <{tag}>{content}</{tag}>")
