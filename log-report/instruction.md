There is an access log at /app/access.log. Parse it and write a summary report to
/app/report.json as a JSON object with exactly these keys:

- "total_requests": integer, the total number of log lines in /app/access.log.
- "unique_ips": integer, the number of distinct client IP addresses that appear.
- "top_path": string, the request path (e.g. "/index.html") that appears most often
  across all requests, taken from the request line (the part between the HTTP method
  and the HTTP version, e.g. "GET /index.html HTTP/1.1" -> "/index.html").

Success criteria:
1. /app/report.json exists and contains a single valid JSON object.
2. The object has the keys "total_requests", "unique_ips", and "top_path", with the
   types described above.
3. "total_requests" equals the true number of non-empty lines in /app/access.log.
4. "unique_ips" equals the true number of distinct client IP addresses in
   /app/access.log.
5. "top_path" equals the single most frequently requested path in /app/access.log.
6. /app/access.log is left unmodified.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.