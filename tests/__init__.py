import os

# Keep the test suite hermetic: never fetch live pricing over the network and
# never read a developer's local pricing cache. Tests assert built-in rates.
os.environ.setdefault("CLAUDE_USAGE_DISABLE_PRICING_FETCH", "1")
