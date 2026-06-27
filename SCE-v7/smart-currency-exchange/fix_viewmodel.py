import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    content = f.read()

lines = content.splitlines()
print(f"Lines: {len(lines)}", flush=True)
print(f"Last 3 lines: {lines[-3:]}", flush=True)

# Count braces
opens = content.count('{')
closes = content.count('}')
diff = opens - closes
print(f"Open: {opens}, Close: {closes}, Diff: {diff}", flush=True)

if diff < 0:
    # Too many closing braces - remove extra from end
    for i in range(abs(diff)):
        # Find last } and remove it
        for j in range(len(lines)-1, -1, -1):
            stripped = lines[j].strip()
            if stripped == '}' or stripped.startswith('}'):
                print(f"Removing extra }} at line {j+1}: {repr(lines[j])}", flush=True)
                if stripped == '}':
                    lines.pop(j)
                else:
                    lines[j] = lines[j].replace('}', '', 1).rstrip()
                    if not lines[j].strip():
                        lines.pop(j)
                break

elif diff > 0:
    # Missing closing braces - add them
    print(f"Adding {diff} closing braces", flush=True)
    for i in range(diff):
        lines.append('}')

result = '\n'.join(lines) + '\n'
with open(filename, 'w') as f:
    f.write(result)

print(f"Fixed. New lines: {len(lines)}", flush=True)
print(f"New last 3: {lines[-3:]}", flush=True)
