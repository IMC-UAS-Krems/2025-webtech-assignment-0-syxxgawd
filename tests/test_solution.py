import os
import re

def test_webpage_file_exists():
    if not os.path.isfile("webpage.html"):
        print("❌ webpage.html is missing")
        assert False, "❌ webpage.html is missing"
    else:
        print("✅ webpage.html is present")
        assert True, "✅ webpage.html is present"

def test_webpage_contains_heading():
    with open("webpage.html", encoding="utf-8") as f:
        text = f.read()
    assert re.search(r"<h1>.*Hello World.*</h1>", text, re.I), \
        "Expected an <h1>Hello World</h1> heading"



def test_solution_contains_heading():
    if os.path.isfile("webpage.html"):
        with open("webpage.html", encoding="utf-8") as f:
            text = f.read()
        if not re.search(r"<h1>.*Hello\s*World.*</h1>", text, re.I):
            print("❌ Expected an <h1>Hello World</h1> heading, but it is missing")
            assert False, "❌ Expected an <h1>Hello World</h1> heading, but it is missing"
        else:
            print("✅ Expected an <h1>Hello World</h1> heading, it is present")
            assert True, "✅ Expected an <h1>Hello World</h1> heading, it is present"
