import unittest
from yaml_anchor_lab import inspect_yaml

SAMPLE = """base: &base
  color: teal
item:
  <<: *base
  size: large
"""

class YAMLAnchorLabTests(unittest.TestCase):
    def test_finds_anchor_alias_and_merge(self):
        result = inspect_yaml(SAMPLE)
        self.assertEqual([x["name"] for x in result["anchors"]], ["base"])
        self.assertEqual([x["name"] for x in result["aliases"]], ["base"])
        self.assertEqual(len(result["merge_keys"]), 1)
        self.assertEqual(result["resolved"]["item"]["color"], "teal")

if __name__ == "__main__":
    unittest.main()
