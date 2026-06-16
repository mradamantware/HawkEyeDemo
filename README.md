# HawkEyeDemo — deliberately vulnerable multi-language project

⚠️ **This code is intentionally insecure. Do not deploy, run against real data,
or copy any pattern from it.** It exists only to demonstrate
[HawkEye](https://nohathacker.com)'s Source Assessment tab.

Register this repository in HawkEye's **🧬 Source** tab and run **Sync & Scan**.
You should see findings from both engines, with remediation guidance carried
through into the generated report.

## What's in here

| Path | Language | Code-vuln highlights | Supply-chain highlights |
|------|----------|----------------------|--------------------------|
| `python/` | Python  | command injection, SQLi (f-string), `pickle`/`yaml.load`, `eval`, MD5, `verify=False`, hardcoded AWS keys | `requirements.txt` with CVE-bearing pins, unpinned `flask`, malicious `colourama` |
| `node/`   | Node.js | `child_process.exec`, `innerHTML`/`document.write`, `eval`, `Math.random`, `rejectUnauthorized:false`, hardcoded GitHub token | `package.json` with vulnerable `lodash`/`minimist`, `postinstall` curl\|bash, `crossenv` (malicious), `lodahs` (typosquat), floating `request` |
| `go/`     | Go      | `InsecureSkipVerify`, command injection, hardcoded keys | `go.sum` with `dgrijalva/jwt-go` (CVE-2020-26160) |
| `rust/`   | Rust    | command injection, MD5, hardcoded credentials | `Cargo.lock` pinned to RustSec-flagged `time`/`chrono`/`smallvec` |
| `c/`      | C       | `gets`, `strcpy`/`strcat`, `sprintf`, `system()` | — |

## Expected coverage

- **Code scanner (SAST):** secrets, OS command injection, SQL injection, unsafe
  deserialization, weak crypto, DOM XSS, disabled TLS verification, unsafe C memory functions.
- **Supply-chain sensor:** SBOM enumeration across all five manifest types, OSV.dev
  known-CVE matching, typosquat detection, known-malicious denylist, npm install-script
  execution, and floating/unpinned version flags.
