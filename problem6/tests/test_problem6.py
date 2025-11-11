import io
import importlib
import pytest
import signal

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


#load the benchmark data
input_output={  "inputs": [    "6 5 RRRRR RRRRR BBBBB BBBBB GGGGG GGGGG ",    "4 3 BRG BRG BRG BRG ",    "6 7 RRRGGGG RRRGGGG RRRGGGG RRRBBBB RRRBBBB RRRBBBB ",    "4 4 RRRR RRRR BBBB GGGG ",    "1 3 GRB ",    "3 1 R G B ",    "4 3 RGB GRB GRB GRB ",    "4 6 GGRRBB GGRRBB GGRRBB RRGGBB ",    "100 3 RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB RGB GRB ",    "3 100 BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG ",   
 "3 1 R R B ",    "3 2 RR BB RR ",    "3 2 RR BG BG ",    "3 2 BB RR BB ",    "3 3 RRR RRR RRR ",    "3 3 GGG GGG GGG ",    "1 3 RGG ",    "4 3 RGR RGR RGR RGR ",    "3 4 RRGG RRGG BBBB ",    "3 3 BRG BRG BRG ",    "3 1 R G R ",    "5 3 BBG BBG BBG BBG BBG ",    "3 3 RRR GGG RRR ",    "1 3 RGR ",    "3 6 RRBBGG RRBBGG RRBBGG ",    "6 6 RRBBGG RRBBGG RRBBGG RRBBGG RRBBGG RRBBGG ",    "4 3 RRR GGG BBB BBB ",    "3 3 RRR BBB RRR ",    "3 1 B R B ",    "1 3 BGB ",    "3 1 B B B ",    "3 4 RRRR BBBB RRRR ",    "1 6 RGGGBB ",    "9 3 BBB BBB BBB GGG GGG GRG RGR RRR RRR ",    "4 4 RGBB RGBB RGBB RGBB ",    "3 3 RBR RBR RBR ",    "1 6 RRRRBB ",    "1 6 RRRRRR ",    "1 6 RRGGGG ",    "4 4 RRRR RRRR RRRR RRRR ",    "3 1 B G B ",    "3 1 R R R ",    "1 9 RRRGGGBBB ",    "1 3 RRR ",    "3 5 RRRRR BBBBB BBBBB ",    "3 3 RRR GGG GGG ",    "1 1 R ",    "3 3 RGR RGR RGR ",    "1 3 GGG ",    "3 3 RBG GBR RGB ",    "3 3 RGB RGB RGB ",    "1 3 BRB ",    "2 1 R B ",    "1 3 RBR ",    "3 5 RRGBB RRGBB RRGBB ",    "5 3 BBR BBR BBR BBR BBR ",    "3 3 RGB RBG RGB ",    "1 2 RB ",    "4 3 BBB BBB BBB BBB ",    "36 6 BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR BBRRRR ",    "4 1 R B G R ",    "13 12 RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR RRRRGGGGRRRR ",    "2 2 RR RR ",    "6 6 RRGGBB GRGGBB RRGGBB RRGGBB RRGGBB RRGGBB ",    "70 3 BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG BGG ",    "4 3 BBG BBG BBG BBG ",    "6 3 BBB GGG RRR BRG BRG BRG ",    "3 6 RRBBGG RBBBGG RBBBGG ",    "6 6 GGGGGG GGGGGG BBBBBB BBBBBB GGGGGG GGGGGG ",    "6 1 R B G R B G ",    "6 5 RRRRR BBBBB GGGGG RRRRR BBBBB GGGGG ",    "6 3 RRR GGG BBB RRR GGG BBB ",    "6 5 RRRRR RRRRR RRRRR GGGGG GGGGG GGGGG ",    "15 28 BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBBB GGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG ",    "21 10 RRRRRRRRRR RRRRRRRRRR RRRRRRRRRR RRRRRRRRRR RRRRRRRRRR RRRRRRRRRR RRRRRRRRRR BBBBBBBBBB BBBBBBBBBB BBBBBGBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB GGGGGGGGGG GGGGGGGGGG GGGGGGGGGG GGGGGGGGGG GGGGGGGGGG GGGGGGGGGG GGGGGGGGGG ",    "3 2 RR GB GB ", 
   "3 2 RG RG BB ",    "6 5 RRRRR RRRRR BBBBB BBBBB RRRRR RRRRR ",    "3 3 RGB GBR BRG ",    "1 3 RBB ",    "3 3 BGR BGR BGR ",    "6 6 RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB ",    "4 2 RR GG RR BB ",    "3 3 RRR RRR GGG ",    "8 6 RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR ",    "3 4 RRRR RRRR GGGG ",    "3 4 RRRR RRRR RRRR ",    "6 1 R R R R R R ",    "1 6 RRBBGG ",    "1 6 RGBRGB ",    "3 4 RRRR GGGG RRRR ",    "3 3 RRB GRG GBB ",    "3 7 RRGGBBB RRGGBBB RRGGBBB ",    "3 1 G R R ",    "2 3 RGG RBB ",    "3 3 RRG GGG BBB ",    "3 3 RGB RBB RGB ",    "3 3 RGR RGB RGB ",    "3 1 B R R ",    "1 3 GRR ",    "4 4 RRRR GGGG BBBB BBBB ",    "1 3 GGR ",    "3 3 RGB GGB RGB ", 
   "3 3 RGR GGG BBB ",    "6 6 RRRRRR GGGGGG GGGGGG GGGGGG BBBBBB BBBBBB ",    "6 6 RRRRRR RRRRRR GGGGGG BBBBBB BBBBBB BBBBBB ",    "3 1 G B R ",    "3 3 GGB RGB RGB ",    "3 3 GRR GGG BBB ",    "6 6 RRRRRR RRRRRR GGGGGG GGGGGG BBBBBB RRRRRR ",    "3 3 RRR GBG BBB ",    "3 8 RRGGBBBB RRGGBBBB RRGGBBBB ",    "2 2 RR GG ",    "3 3 RGB RGR RGB ",    "1 3 RBG ",    "2 6 RRGGBB GGRRBB ",    "6 2 RR GG BB RR GG BB ",    "1 5 RRGGB ",    "1 2 RG ",    "1 6 RGBRBG ",    "1 6 RRRGGB ",    "1 3 RGB ",    "4 3 RRR BBR GBB GGG ",    "6 3 RRR BBB BBB BBB GGG GGG ",    "3 3 RBG RBG RBG ",    "6 3 RRR BBB GGG RRR BBB GGG ",    "1 4 RGBB ",    "6 6 RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR RRRRRR ",    "6 5 RRRRR RRRRR GGGGG GGGGG RRRRR RRRRR ",    "3 3 RGB BRG GBR ",    "6 10 RRRRRRRRRR GGGGGGGGGG BBBBBBBBBB RRRRRRRRRR GGGGGGGGGG BBBBBBBBBB ",    "20 6 RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB RRGGBB ",    "4 1 R G B R ", 
   "1 4 RGBR ",    "2 4 RGBB RRGB "  ],  "outputs": [    "YES ",    "YES ",    "NO ",    "NO ",    "YES ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",   
 "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ", 
   "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    
"NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "NO ",    "YES ",    "NO ",    "NO ",    "NO "  ]}


#test functions
def parse_string(s: str):
    parts = s.strip().split()
    first_num = int(parts[0])
    second_num = int(parts[1])
    strings = parts[2:]
    return [first_num, second_num, strings]

@pytest.mark.parametrize("input_str,expected_output", zip(input_output["inputs"], input_output["outputs"]))
def test_problem_dynamic(monkeypatch, capsys, input_str, expected_output):
    
    def test(solution):
        parsed_args = parse_string(input_str)
        
        sol = solution.solve(*parsed_args)

        result = str(expected_output)
        result = result.replace(" ", "")
        assert sol == result

    test(importlib.import_module("solutions.solution1"))
    test(importlib.import_module("solutions.solution2"))
    test(importlib.import_module("solutions.solution3"))
    test(importlib.import_module("solutions.solution4"))