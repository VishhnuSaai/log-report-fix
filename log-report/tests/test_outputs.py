import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth computed independently from the fixed access.log baked into the
# environment image (environment/data/access.log). The log is static and
# deterministic, so these values never change between runs.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT_PATH.exists(), "no /app/report.json found"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_exists():
    """The agent must write /app/report.json."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"


def test_report_is_valid_json_object():
    """report.json must parse as a JSON object with the required keys."""
    data = _load_report()
    assert isinstance(data, dict), "report.json must contain a JSON object"
    required_keys = {"total_requests", "unique_ips", "top_path"}
    assert required_keys <= data.keys(), f"missing keys: {required_keys - data.keys()}"


def test_total_requests_correct():
    """total_requests must equal the true number of log lines (6)."""
    data = _load_report()
    assert isinstance(data["total_requests"], int), "total_requests must be an int"
    assert data["total_requests"] == EXPECTED_TOTAL_REQUESTS, (
        f"expected total_requests={EXPECTED_TOTAL_REQUESTS}, got {data['total_requests']}"
    )


def test_unique_ips_correct():
    """unique_ips must equal the true count of distinct client IPs (3)."""
    data = _load_report()
    assert isinstance(data["unique_ips"], int), "unique_ips must be an int"
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {data['unique_ips']}"
    )


def test_top_path_correct():
    """top_path must identify the most-requested path ('/index.html')."""
    data = _load_report()
    assert isinstance(data["top_path"], str), "top_path must be a string"
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {data['top_path']!r}"
    )


def test_source_log_untouched():
    """The agent must not modify the original /app/access.log."""
    original = Path("/app/access.log").read_text()
    expected_line_count = 6
    assert len(original.strip().splitlines()) == expected_line_count, (
        "access.log line count changed — the source log must not be modified"
    )