# LLM Analysis Quiz Automation

This project solves dynamic quiz tasks served through JavaScript-rendered HTML pages.
The system:
- Loads quiz via headless browser (Playwright)
- Parses and extracts instructions/data
- Uses LLM to interpret tasks
- Performs data processing with pandas/numpy
- Generates visualizations (base64)
- Submits answers to the target endpoint
- Follows multi-step quiz chains

## How to run

### 1. Create Conda Environment
`conda env create -f environment.yml`
`conda activate llmquiz`


### 2. Install Playwright Browsers
`playwright install chromium`


### 3. Start API Server
`uvicorn src.main:app --reload --port 8000`

### 4. Submit a test request
Use the demo endpoint:
`curl -X POST http://localhost:8000/solve -H "Content-Type: application/json" -d '{"email":"test@test.com","secret":"abcd","url":"https://tds-llm-analysis.s-anand.net/demo"}'`


## Repo Layout

- `src/api/` → FastAPI entrypoint + request models  
- `src/solver/` → All logic (scraping, parsing, execution, submit)  
- `src/utils/` → Logging, timing, constants  
- `tests/` → Unit tests  