import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """
    Function: x^3 + 4x = 0
    Root at x = 0, but let's find it using bisection method
    Let's use interval [-2, 2] where f(-2) = -16 and f(2) = 16
    """
    return x**3 + 4*x

def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Bisection method to find root of f(x) = 0

    Parameters:
    f: function
    a, b: interval bounds [a, b] where f(a)*f(b) < 0
    tolerance: stopping criteria
    max_iterations: maximum number of iterations

    Returns:
    root: approximate root
    history: list of iteration data
    """


    if f(a) * f(b) >= 0:
        raise ValueError(f"Function must have opposite signs at a and b. f({a}) = {f(a)}, f({b}) = {f(b)}")

    print("Bisection Method for f(x) = x³ + 4x")
    print("=" * 80)
    print(f"{'Iteration':<10} {'a':<12} {'b':<12} {'midpoint':<12} {'f(midpoint)':<15} {'Error':<12}")
    print("-" * 80)

    history = []
    iteration = 0

    for i in range(max_iterations):
        midpoint = (a + b) / 2
        f_mid = f(midpoint)
        error = abs(b - a)


        history.append({
            'iteration': iteration,
            'a': a,
            'b': b,
            'midpoint': midpoint,
            'f_mid': f_mid,
            'error': error
        })

        print(f"{iteration:<10} {a:<12.8f} {b:<12.8f} {midpoint:<12.8f} {f_mid:<15.8f} {error:<12.8f}")


        if abs(f_mid) < 1e-15:
            print("\n🎯 Exact root found!")
            break


        if error < tolerance:
            print("\n✅ Convergence achieved!")
            break


        if f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

        iteration += 1
    else:
        print("\n⚠️  Maximum iterations reached!")

    return midpoint, history

def plot_function_and_iterations(f, history, root):
    """Plot the function and bisection iterations"""
    x = np.linspace(-2, 2, 400)
    y = f(x)

    plt.figure(figsize=(12, 8))


    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x³ + 4x')
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.7)
    plt.axvline(x=root, color='r', linestyle='--', label=f'Root ≈ {root:.6f}')


    plt.axvline(x=history[0]['a'], color='g', linestyle=':', alpha=0.7, label='Initial interval')
    plt.axvline(x=history[0]['b'], color='g', linestyle=':', alpha=0.7)

    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method: f(x) = x³ + 4x')
    plt.legend()


    plt.subplot(2, 1, 2)
    iterations = [h['iteration'] for h in history]
    errors = [h['error'] for h in history]

    plt.semilogy(iterations, errors, 'ro-', linewidth=2, markersize=6)
    plt.grid(True, alpha=0.3)
    plt.xlabel('Iteration')
    plt.ylabel('Error (log scale)')
    plt.title('Convergence of Bisection Method')

    plt.tight_layout()
    plt.show()

def print_summary(root, history, f):
    """Print summary of results"""
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Equation: x³ + 4x = 0")
    print(f"Initial interval: [{history[0]['a']}, {history[0]['b']}]")
    print(f"Root found: x = {root:.8f}")
    print(f"f(root) = {f(root):.2e}")
    print(f"Number of iterations: {len(history)}")
    print(f"Final error: {history[-1]['error']:.2e}")


    print(f"\nVerification:")
    print(f"f({root:.6f}) = {f(root):.10f}")

def main():
    """Main function to run the bisection method"""


    print("Bisection Method for f(x) = x³ + 4x = 0")
    print("Initial analysis:")
    print(f"f(-2) = {f(-2):.2f} (negative)")
    print(f"f(2) = {f(2):.2f} (positive)")
    print("Since f(-2) < 0 and f(2) > 0, root exists in [-2, 2]")
    print()


    a, b = -2, 2
    tolerance = 1e-6
    max_iterations = 50

    try:

        root, history = bisection_method(f, a, b, tolerance, max_iterations)


        print_summary(root, history, f)


        plot_function_and_iterations(f, history, root)


        print("\n" + "🎯 FINAL RESULTS " + "🎯")
        print(f"📍 Root: {root:.8f}")
        print(f"📊 Iterations: {len(history)}")
        print(f"📏 Final Error: {history[-1]['error']:.2e}")
        print(f"✅ f(root) = {f(root):.2e}")

    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if NameError== "__main__":
    main()