# Project Statement

## Project title

Message Encoder and Decoder

## Problem

People may want a simple way to transform a short message into a string that can be copied and later restored. A receiver should be able to use the string directly without access to the sender's computer or a stored message list.

## Aim

Build a beginner-friendly command-line program that reverses a message, adds five random alphanumeric characters at each end, and can optionally attach a password-verification value to the same string.

## Scope

The program supports encoding and decoding text in one local command-line session. Password verification data travels in the coded string. The project does not use message IDs, message databases, network services, or local password storage.

## Intended users

Students learning Python modules, functions, string handling, input validation, and basic automated checks.

## Expected outcome

For valid input, the decoder recovers the original message. Password-protected strings are decoded only after the entered password matches the embedded verification value.

## Limitations

Reversing and padding do not encrypt or conceal the message. The password check is educational and is not a secure access-control or encryption system. It should not be used for sensitive or confidential information.
