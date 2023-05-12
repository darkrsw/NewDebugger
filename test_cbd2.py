import yaml
from CondBreakDebugger import CondBreakDebugger
from utils import next_inputs, clear_next_inputs

def test_debug_pyyaml():
    clear_next_inputs()
    next_inputs(["break token.value == 'company'", "continue",  "attr token, value, 'mycompany'", "continue"])
    document = """
---
# A sample yaml file
company: spacelift
domain:
 - devops
 - devsecops
tutorial:
  - yaml:
      name: "YAML Ain't Markup Language"
      type: awesome
      born: 2001
  - json:
      name: JavaScript Object Notation
      type: great
      born: 2001
  - xml:
      name: Extensible Markup Language
      type: good
      born: 1996
author: omkarbirade
published: true
                """
    with CondBreakDebugger() as debugged:
        data = yaml.load(document, Loader=yaml.FullLoader)

    print(data)
    assert ("company" not in data) is True
    assert (data["mycompany"] == "spacelift")
