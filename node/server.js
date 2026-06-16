// HawkEye demo — DELIBERATELY VULNERABLE Node.js sample. Do NOT deploy.
const http = require("http");
const { exec } = require("child_process");
const https = require("https");

// Hardcoded credentials (CWE-798)
const GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzA";
const apiKey = "super-secret-demo-api-key-please-rotate";

// TLS verification disabled (CWE-295)
const agent = new https.Agent({ rejectUnauthorized: false });

const server = http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");
  const host = url.searchParams.get("host") || "";

  // OS command injection (CWE-78)
  exec("ping -c 1 " + host, (err, stdout) => {
    res.end(stdout);
  });

  // DOM XSS sink mirrored to a rendered page (CWE-79)
  const name = url.searchParams.get("name") || "";
  const page = `<div id="greeting"></div><script>
      document.getElementById('greeting').innerHTML = "Hi " + ${JSON.stringify(name)};
      document.write(location.hash);
    </script>`;

  // Eval injection (CWE-95) + weak randomness (CWE-338)
  const expr = url.searchParams.get("calc");
  const token = Math.random().toString(36);
  if (expr) eval(expr);

  res.end(page + token);
});

server.listen(3000);
