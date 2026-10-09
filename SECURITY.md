# Security policy

## Supported versions

The project is in its initial development stage. Security fixes, when applicable,
are made on the current `main` branch. There are no released versions yet.

## Reporting a vulnerability

If GitHub private vulnerability reporting is available for this repository, use
**Security → Advisories → Report a vulnerability** to submit a private report.

If that option is unavailable, open an issue requesting a private reporting
channel from [@tao1272](https://github.com/tao1272). Do not include vulnerability
details, exploit code, credentials, or personal data in the public issue.

A useful private report includes:

- The affected commit or version and environment.
- A description of the vulnerability and its impact.
- Minimal reproduction steps and any suggested mitigation.

Please allow the maintainer to investigate and address the issue before publishing
technical details. There is no guaranteed response time at this stage.

## Credentials and local artifacts

API tokens and other secrets belong in local environment variables or an ignored
`.env` file. Do not commit credentials, private match data, or sensitive notebook
outputs. If a token is exposed, revoke it at its provider before removing it from
the repository.
