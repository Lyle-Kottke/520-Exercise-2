import io
import importlib
import pytest
import signal

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


#load the benchmark data
input_output={   "inputs": [     "mew  ",     "wuffuw  ",     "qqqqqqqq  ",     "ijvji  ",     "iiiiiii  ",     "wobervhvvkihcuyjtmqhaaigvvgiaahqmtjyuchikvvhvrebow  ",     "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  ",     "wobervhvvkihcuyjtmqhaaigvahheoqleromusrartldojsjvy  ",     "ijvxljt  ",     "fyhcncnchyf  ",     "ffffffffffff  ",     "fyhcncfsepqj  ",     "ybejrrlbcinttnicblrrjeby  ",     "yyyyyyyyyyyyyyyyyyyyyyyyy  ",     "ybejrrlbcintahovgjddrqatv  ",     "oftmhcmclgyqaojljoaqyglcmchmtfo  ",     "oooooooooooooooooooooooooooooooo  ",     "oftmhcmclgyqaojllbotztajglsmcilv  ",     "gxandbtgpbknxvnkjaajknvxnkbpgtbdnaxg  ",     "gggggggggggggggggggggggggggggggggggg  ",     "gxandbtgpbknxvnkjaygommzqitqzjfalfkk  ",     "fcliblymyqckxvieotjooojtoeivxkcqymylbilcf  ",     "fffffffffffffffffffffffffffffffffffffffffff  ",     "fcliblymyqckxvieotjootiqwtyznhhvuhbaixwqnsy  ",     "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr  ",     "rajccqwqnqmshmerpvjyfepxwpxyldzpzhctqjnstxyfmlhiy  ",     "a  ",     "abca  ",     "aaaaabaaaaa  ",     "aba  ",     "asaa  ",     "aabaa  ",     "aabbaa  ",     "abcdaaa  ",     "aaholaa  ",     "abcdefghijka  ",     "aaadcba  ",     "aaaabaaaa  ",     "abaa  ",     "abcbaa  ",     "ab  ",     "l  ",     "aaaabcaaaa  ",     "abbaaaaaabba  ",     "abaaa  ",     "baa  ",     
"aaaaaaabbba  ",     "ccbcc  ",     "bbbaaab  ",     "abaaaaaaaa  ",     "abaaba  ",     "aabsdfaaaa  ",     "aaaba  ",     "aaabaaa  ",     "baaabbb  ",     "ccbbabbcc  ",   
  "cabc  ",     "aabcd  ",     "abcdea  ",     "bbabb  ",     "aaaaabababaaaaa  ",     "bbabbb  ",     "aababd  ",     "abaaaa  ",     "aaaaaaaabbba  ",     "aabca  ",     "aaabccbaaa  ",     "aaaaaaaaaaaaaaaaaaaab  ",     "babb  ",     "abcaa  ",     "qwqq  ",     "aaaaaaaaaaabbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaa  ",     "aaab  ",     "aaaaaabaaaaa  ",     "wwuww  ",     "aaaaabcbaaaaa  ",     "aaabbbaaa  ",     "aabcbaa  ",     "abccdefccba  ",     "aabbcbbaa  ",     "aaaabbaaaa  ",     "aabcda  ",     "abbca  ",     "aaaaaabbaaa  ",     "sssssspssssss  ",     "sdnmsdcs  ",     "aaabbbccbbbaaa  ",     "cbdbdc  ",     "abb  ",     "abcdefaaaa  ",     "abbbaaa  ",     "v  ",     "abccbba  ",     "axyza  ",     "abcdefgaaaa  ",     "aaabcdaaa  ",     "aaaacaaaa  ",     "aaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaa  ",     "abbbaa  ",     "abcdee  ",     "oom  ",     "aabcaa  ",     "abba  ",     "aaca  ",     "aacbca  ",     "ababa  ",     "abcda  ",     "cccaaccc  ",     "aaabcda  ",     "aa  ",     "aabaaaa  ",     "abbaaaa  ",     "aaabcbaaa  ",     "aabba  ",     "xyxx  ",     "aaaaaaaaaaaabc  ",     "bbaaaabb  ",     "aaabaa  ",     "sssssabsssss  ",     "bbbaaaabbb  ",     "abbbbaaaa  ",     "wwufuww  ",     "oowoo  ",     "cccaccc  ",     "aaa  ",     "bbbcc  ",     "abcdef  ",     "abbba  ",     "aab  ",     "aaba  ",     "azbyaaa  ",     "oooooiooooo  ",     "aabbbbbaaaaaa  "  
 ],   "outputs": [     "3  ",     "5  ",     "0  ",     "4  ",     "0  ",     "49  ",     "0  ",     "50  ",     "7  ",     "10  ",     "0  ",     "12  ",     "23  ",     "0  ",     "25  ",     "30  ",     "0  ",     "32  ",     "35  ",     "0  ",     "36  ",     "40  ",     "0  ",     "43  ",     "0  ",     "49  ",     "0  ",     "4  ",     "10  ",     "2  ",     "4  ",     "4  ",     "5  ",     "7  ",     "7  ",     "12  ",     "7  ",     "8  ",     "4  ",     "6  ",     "2  ",     "0  ",    
 "10  ",     "11  ",     "5  ",     "3  ",     "11  ",     "4  ",     "7  ",     "10  ",     "5  ",     "10  ",     "5  ",     "6  ",     "7  ",     "8  ",     "4  ",     "5  ",     "6  ",     "4  ",     "14  ",     "6  ",     "6  ",     "6  ",     "12  ",     "5  ",     "9  ",     "21  ",     "4  ",     "5  ",     "4  ",     "48  ",     "4  ",     "12  ",     "4  ",     "12  ",     "8  ",     "6  ",     "11  ",     "8  ",     "9  ",     "6  ",     "5  ",     "11  ",     "12  ",     "8  ",   
  "13  ",     "6  ",     "3  ",     "10  ",     "7  ",     "0  ",     "7  ",     "5  ",     "11  ",     "9  ",     "8  ",     "42  ",     "6  ",     "6  ",     "3  ",     "6  ",     "3  ",     "4  ",     "6  ",     "4  ",     "5  ",     "7  ",     "7  ",     "0  ",     "7  ",     "7  ",     "8  ",     "5  ",     "4  ",     "14  ",     "7  ",     "6  ",     "12  ",     "9  ",     "9  ",     "6  ",     "4  ",     "6  ",     "0  ",     "5  ",     "6  ",     "4  ",     "3  ",     "4  ",     "7  ",     "10  ",     "13  "   ] }
#test functions
@pytest.mark.parametrize("input_str,expected_output", zip(input_output["inputs"], input_output["outputs"]))
def test_problem_dynamic(monkeypatch, capsys, input_str, expected_output):
    
    def test(solution):
      args = input_str.split()
      parsed_args = []
      for a in args:
          parsed_args.append(str(a).replace(" ", ""))

      sol = solution.solve(*parsed_args)

      result = int(expected_output)
      assert sol == result

    test(importlib.import_module("solutions.solution1"))
    test(importlib.import_module("solutions.solution2"))
    test(importlib.import_module("solutions.solution3"))
    test(importlib.import_module("solutions.solution4"))