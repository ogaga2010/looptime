def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

def analyze_time_complexity():
    print("Analyzing time complexity of multiply_n_iterations function...")
    print("Time complexity analysis:")
    print("1. Initializing result to 0 takes 0(1) time.")
    print("2. The for loop runs N times, and each iteration takes 0(1) time.")
    print("3. Therefore, the total time complexity is 0(N).")

if __name__ == "__main__":
   # Codingal Usage
   N = 10
   M = 5
   result = multiply_n_iterations(N, M)
   print(f"Result of multiply_n_iterations( {N}, {M} ): {result}")

   # Analyze time complexity
   analyze_time_complexity()