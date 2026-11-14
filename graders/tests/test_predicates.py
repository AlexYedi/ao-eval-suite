"""Seeded tests for every code predicate (PREREG.md section 9: every regex is tested on a
seeded fixture before sign). Run: python3 -m unittest discover -s graders/tests"""
import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from predicates import grade  # noqa: E402

CASES = {
    # type: [(text, expected verdict), ...]
    "T1": [("We leveraged the spec.", "fail"), ("This unlocks scale.", "fail"),
           ("Real synergies here.", "fail"), ("The partner ecosystem grew.", "fail"),
           ("A disruptive idea.", "fail"), ("They use the spec to ship faster.", "pass"),
           ('She called it "the ecosystem" twice.', "blind")],
    "T2": [("AI-powered digital transformation leveraging cutting-edge solutions.", "blind")],
    "T3": [("This is a game-changer.", "fail"), ("A game changing panel.", "fail"),
           ("Revolutionary work.", "fail"), ("Excited to announce my panel.", "fail"),
           ("I’m excited to moderate.", "fail"), ("I am excited to host.", "fail"),
           ("Next Thursday I'm moderating a panel.", "pass")],
    "T4": [("A true thought leader.", "fail"), ("Visionary founder Helena.", "fail"),
           ("An industry-leader in fraud.", "fail"), ("She built and sold a payments company.", "blind")],
    "T5": [("Great talk! Let's connect.", "fail"), ("Loved your talk on forecasts.", "fail"),
           ("This was amazing.", "fail"), ("Your spreadsheet point changed how I see trust.", "blind")],
    "T6": [("I'm curious how you test it.", "fail"), ("I’d love to hear your take.", "fail"),
           ("I am wondering about cost.", "fail"), ("Where does this break first?", "pass")],
    "T7": [("Hi Celeste, saw you were on a podcast.", "fail"), ("Noticed you're speaking Wednesday.", "fail"),
           ("I saw that you rebuilt territories.", "fail"),
           ("Hi Celeste! I'm at RevOps Exchange Wednesday. I saw you're speaking.", "fail"),
           ("I'm rebuilding territory plans around usage data too. See you Wednesday.", "pass"),
           ("I'm at RevOps Exchange Wednesday. Rebuilding territories too. Later I noticed you're on it.", "pass")],
    "T8": [("Your survey of 400 leaders stuck with me.", "fail"), ("62% is wild.", "fail"),
           ("Sixty-two percent? Wild. 62 percent.", "fail"), ("Your one-manual-field idea is smart.", "blind")],
}

class TestCodeGraders(unittest.TestCase):
    def test_cases(self):
        for t, cases in CASES.items():
            for text, want in cases:
                with self.subTest(type=t, text=text):
                    self.assertEqual(grade(t, text)[0], want)

    def test_empty_and_refusal_are_never_pass(self):
        for t in CASES:
            self.assertEqual(grade(t, "")[0], "indeterminate")
            self.assertEqual(grade(t, "I can't help with that.")[0], "indeterminate")

if __name__ == "__main__":
    unittest.main()
