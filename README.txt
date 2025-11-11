-Each set of 4 generated solutions are present within each problem folder. For example, problem 1's solutions are located in /problem1/solutions.
-The test cases (baseline + improved) and test scripts (for parsing input and output and passing to solution functions) are located
in problem*/tests/test_problem* for each problem

-How to generate coverage reports locally:
    -Navigate to path of problem you wish to generate for (/problem1 for APPS 31, /problem2 for APPS 32 etc)
    -Run pytest --cov=solutions --cov-branch --cov-report=term-missing
        -The tests coverage table will be generated with each solutions' Stmts, Miss, Branch, and BrPart
        -The line coverage was computed by subtracting Miss from Stmts and then dividing by Stmts
        -the branch coverage was computed by subtracting BrPart from Branch and dividing the result by Branch
            -This strategy sometimes produces different results than what is in the "Cover" column. Regardless this is the correct way to calulate these values
        -If you want to see coverage for an individual solution (like in the Part 1 table) comment out the lines in problem*/tests/test_problem* that
         correspond to the other three solutions you dont want to see in the form test(importlib.import_module("solutions.solution*"))
         (located in the "#test functions" section)