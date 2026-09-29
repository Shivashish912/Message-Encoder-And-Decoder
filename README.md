# Message Encoder and Decoder

A small command-line Python project that turns a message into a copyable coded string and restores it later. The receiver needs only the coded string and, if the sender enabled password checking, the password.

## What it does

- Adds five random letters or digits before and after the reversed message.
- Can attach a password-verification hash to the coded string.
- Decodes a pasted coded string without message IDs or local message/password files.
- Rejects malformed input instead of silently returning a misleading result.

## Tools used

- Python 3.10+ and the Python standard library
- Git for source version control (initialize the repository and commit changes before publishing it)

## Important limitation

Reversing a message and adding random characters is obfuscation, not encryption. The message text remains visible inside the coded string. The optional password check is only a basic gate; the SHA-256 digest is shortened to 12 hexadecimal characters to match the original beginner project, and this is not suitable for protecting sensitive information. Do not use this project to send secrets.

## Requirements

- Python 3.10 or later
- No third-party packages

## Run

From this directory:

```bash
python main.py
```

Choose **1** to encode or **2** to decode. For password-protected strings, share the entire output, including the leading `*` and separator `|`. The recipient pastes it and enters the password. No message ID or local database is used.

## Run the checks

```bash
python -m unittest discover -s tests -v
```

## Publish to GitHub

Initialize a Git repository in this folder, review the files, commit them, and create a GitHub repository for the project. Add your own screenshots to the report only after capturing the program running on your computer.

## Project layout

```text
message-encoder/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── report.md
├── src/message_encoder/
│   ├── __init__.py
│   ├── codec.py
│   ├── password.py
│   ├── message_format.py
│   └── cli.py
└── tests/test_message_encoder.py
```

See [report.md](report.md) for the design, workflow, requirements, test plan, and report sections.
