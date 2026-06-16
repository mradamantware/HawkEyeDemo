// HawkEye demo — DELIBERATELY VULNERABLE Rust sample. Do NOT deploy.
use std::process::Command;

fn main() {
    // Hardcoded credentials (CWE-798)
    let api_token = "demo-rust-api-token-rotate-me";
    let aws_key = "AKIAIOSFODNN7EXAMPLE";
    println!("{api_token} {aws_key}");

    // OS command injection (CWE-78) — user input concatenated into a shell call
    let host = std::env::args().nth(1).unwrap_or_default();
    let _ = Command::new("sh").arg("-c").arg(format!("ping -c 1 {host}")).status();

    // Weak hash for integrity (CWE-327): MD5
    let digest = md5::compute(api_token.as_bytes());
    println!("{digest:x}");
}
