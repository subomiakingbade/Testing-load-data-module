import check
from sequences import fibonacci

def test_fibonacci() -> None:
    """Unit test for function fibonacci."""
    # fibonacci(1) a boundary case. fibonacci's docstring states that n must be
    # positive, so 1 is the smallest integer for which fibonacci must return a
    # correct value.

    check.equal(fibonacci(1), 1)

    # fibonacci(2) is a special case: it can't be calculated from the
    # formula fibonacci(n) = fibonacci(n-1) + fibonacci(n-2).

    check.equal(fibonacci(2), 1)

    # fibonacci(1) and fibonacci(2) should both return 1, but testing only
    # these two cases isn't sufficient to determine if the function is correct.
    # What if fibonacci always returned 1? fibonacci(1) and fibonacci(2) would
    # pass their tests, even though the function isn't correct.
    # We won't detect this flaw unless we have a test where the expected
    # result is an int other than 1.
    # Test fibonacci(3), because 3 is the smallest int for which fibonacci
    # should return a value other than 1.

    check.equal(fibonacci(3), 2)

    # Notice that:
    #   fibonacci(2) = 1 = n - 1
    #   fibonacci(3) = fibonacci(2) + fibonacci(1) = 2 = n - 1
    #   fibonacci(4) = fibonacci(3) + fibonacci(2) = 3 = n - 1
    # We need at least one test that verifies that the function doesn't return
    # n - 1 for all n > 1.

    check.equal(fibonacci(5), 5)
    check.summary()

if __name__ == '__main__':
    test_fibonacci()
