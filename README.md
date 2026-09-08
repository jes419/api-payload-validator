# api-payload-validator

A lightweight and robust Python utility designed for automated API request payload sanitization, field verification, and data validation.

## Features
* **Required Field Verification:** Ensures all mandatory keys (such as `user_id`, `email`, and `action`) exist in incoming JSON payloads.
* **Data Integrity:** Prevents malformed requests from reaching downstream microservices or databases.
* **Extensible Design:** Easily customizable schemas to fit various API endpoint requirements.

## Tech Stack
* **Language:** Python 3

## Quick Start
1. Clone the repository:
```bash
git clone https://github.com/jes419/api-payload-validator.git
