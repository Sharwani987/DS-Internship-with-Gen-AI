# Bug Report: Note-Taking App

## Overview
A simple Flask app to add and display notes.

## Bugs Found & Fixes

### 1. Wrong method for form data
**Bug:** Used `request.args.get()`  
**Fix:** Replaced with `request.form.get()`

### 2. Missing GET method
**Bug:** Route only allowed POST  
**Fix:** Added `"GET"` to route methods

### 3. Empty notes added
**Bug:** No validation  
**Fix:** Added `if note:` check

## Final Outcome
App works as expected. Notes are added and displayed.
