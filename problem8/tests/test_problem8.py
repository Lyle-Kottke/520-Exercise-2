import io
import importlib
import pytest
import signal

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


#load the benchmark data
input_output={   "inputs": [     "4 6 15  ",     "3 2 7  ",     "6 11 6  ",     "3 12 15  ",     "5 5 10  ",     "6 6 7  ",     "1 1 20  ",     "12 14 19  ",     "15 12 26  ",     "2 4 8  ",     "4 5 30  ",     "4 5 48  ",     "2 17 105  ",     "10 25 282  ",     "6 34 323  ",     "2 47 464  ",     "4 53 113  ",     "6 64 546  ",     "1 78 725  ",     "1 84 811  ",     "3 100 441  ",     "20 5 57  ",     "14 19 143  ",     "17 23 248  ",     "11 34 383  ",     "20 47 568  ",  
   "16 58 410  ",     "11 70 1199  ",     "16 78 712  ",     "20 84 562  ",     "19 100 836  ",     "23 10 58  ",     "25 17 448  ",     "22 24 866  ",     "24 35 67  ",     "29 47 264  ",     "23 56 45  ",     "25 66 1183  ",     "21 71 657  ",     "29 81 629  ",     "23 95 2226  ",     "32 4 62  ",     "37 15 789  ",     "39 24 999  ",     "38 32 865  ",     "32 50 205  ",     "31 57 1362  ",     "38 68 1870  ",     "36 76 549  ",     "35 84 1257  ",     "39 92 2753  ",     "44 1 287  ",     "42 12 830  ",     "42 27 9  ",     "49 40 1422  ",     "44 42 2005  ",     "50 55 2479  ",     "48 65 917  ",     "45 78 152  ",     "43 90 4096  ",     "43 94 4316  ",     "60 7 526  ",     "53 11 735  ",     "52 27 609  ",     "57 32 992  ",     "52 49 421  ",     "57 52 2634  ",     "54 67 3181  ",     "52 73 638  ",     "57 84 3470  ",     "52 100 5582  ",     "62 1 501  ",   
  "63 17 858  ",     "70 24 1784  ",     "65 32 1391  ",     "62 50 2775  ",     "62 58 88  ",     "66 68 3112  ",     "61 71 1643  ",     "69 81 3880  ",     "63 100 1960  ",  
   "73 6 431  ",     "75 19 736  ",     "78 25 247  ",     "79 36 2854  ",     "80 43 1864  ",     "76 55 2196  ",     "76 69 4122  ",     "76 76 4905  ",     "75 89 3056  ",   
  "73 100 3111  ",     "84 9 530  ",     "82 18 633  ",     "85 29 2533  ",     "89 38 2879  ",     "89 49 2200  ",     "88 60 4140  ",     "82 68 1299  ",     "90 76 2207  ",  
   "83 84 4923  ",     "89 99 7969  ",     "94 9 168  ",     "91 20 1009  ",     "93 23 2872  ",     "97 31 3761  ",     "99 46 1341  ",     "98 51 2845  ",     "93 66 3412  ",     "95 76 3724  ",     "91 87 6237  ",     "98 97 7886  ",     "12 17 15  ",     "93 94 95  ",     "27 43 27  ",     "17 43 68  ",     "44 12 12  ",     "44 50 150  ",     "1 1 10000  ",     "2 3 10000  ",     "100 1 10  ",     "3 2 1  ",     "1 1 1  ",     "9 9 10000  ",     "2 3 9995  ",     "3 5 4  ",     "99 98 100  ",     "6 10 2  ",     "1 6 5  ",     "1 4 3  ",     "3 2 3  ",     "1 7 6  ",     "2 3 9871  ",     "10 5 5  ",     "10 8 2  "   ],   "outputs": [     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",  
   "Yes  ",     "No  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "No  ",     "No  ",     "No  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  ",     "Yes  ",     "No  ",     "Yes  ",    
 "No  ",     "No  ",     "No  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "Yes  ",     "No  "   ] }

#test functions
@pytest.mark.parametrize("input_str,expected_output", zip(input_output["inputs"], input_output["outputs"]))
def test_problem_dynamic(monkeypatch, capsys, input_str, expected_output):
    
    def test(solution):
      args = input_str.split()
      parsed_args = []
      for a in args:
          parsed_args.append(int(a))

      sol = solution.solve(*parsed_args)

      result = str(expected_output)
      result = result.replace(" ", "")
      assert sol == result

    test(importlib.import_module("solutions.solution1"))
    test(importlib.import_module("solutions.solution2"))
    test(importlib.import_module("solutions.solution3"))
    test(importlib.import_module("solutions.solution4"))