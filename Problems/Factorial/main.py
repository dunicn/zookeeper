n = int(input())
fn = n  # factorial of n
while 1 < n <= 100:
    fn = fn * (n - 1)
    n -= 1
print(fn)
