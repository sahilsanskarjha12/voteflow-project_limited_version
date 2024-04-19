import timeit

# Code to evaluate performance
execution_time = timeit.timeit(stmt=''' 
    # Code snippet to evaluate
''', number=1000)
print("Execution time:", execution_time)
