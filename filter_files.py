import sys
import json

if __name__ == "__main__":
  files = sys.argv[1].split("\n")
  print(json.dumps(files))
