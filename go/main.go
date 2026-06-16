// HawkEye demo — DELIBERATELY VULNERABLE Go sample. Do NOT deploy.
package main

import (
	"crypto/tls"
	"net/http"
	"os/exec"
)

// Hardcoded credential (CWE-798)
const apiToken = "demo-go-api-token-rotate-me-now"
const awsKey = "AKIAIOSFODNN7EXAMPLE"

func insecureClient() *http.Client {
	// TLS verification disabled (CWE-295)
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	return &http.Client{Transport: tr}
}

func ping(host string) ([]byte, error) {
	// OS command injection (CWE-78) — host is attacker-controlled
	return exec.Command("sh", "-c", "ping -c 1 "+host).Output()
}

func main() {
	_ = insecureClient()
	_, _ = ping("127.0.0.1")
}
