# Assessment - Navigation Subsystem

## Project Structure

- `step1_self_trial.py` - Syntax error scoring for corrupted navigation lines
- `step2_self_trial.py` - Autocomplete scoring for incomplete navigation lines

## Setup

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python3 step1_self_trial.py
python3 step2_self_trial.py
```

## Running Tests

```bash
# All tests
python3 -m pytest tests/ -v

# Specific file
python3 -m pytest tests/test_step1_self_trial.py -v
python3 -m pytest tests/test_step2_self_trial.py -v

# Single test class
python3 -m pytest tests/test_step2_self_trial.py::TestSolveTimmyInstruction -v

# With coverage
python3 -m pytest tests/ -v --cov=.
```
