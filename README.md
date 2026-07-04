```markdown
```mermaid
graph TD
    %% Inputs
    In1[inputs/student_profile.txt] --> Join
    In2[inputs/job_description.txt] --> Join

    %% Orchestrator
    Join{ } --> Crew[ResumeBuilderCrew]

    %% Agents
    Crew --> Agent1[Expert Resume Strategist]
    Crew --> Agent2[ATS Optimization Expert]
    Crew --> Agent3[Professional Career Coach]

    %% Tasks
    Agent1 --> Task1[Profile & Align Task]
    Agent2 --> Task2[ATS Evaluation Task]
    Agent3 --> Task3[Gap Improvement Task]

    %% Outputs
    Task1 --> Out1[outputs/resume.md]
    Task2 --> Out2[outputs/ats_report.md]
    Task3 --> Out3[outputs/improvement_plan.md]

    %% Styling
    style Crew fill:#f9f,stroke:#333,stroke-width:2px
    style Out1 fill:#bbf,stroke:#333
    style Out2 fill:#bbf,stroke:#333
    style Out3 fill:#bbf,stroke:#333



### 🧠 Agent Roles & Governance:
1. **Expert Resume Strategist (Profiler Agent):** Translates raw academic metrics, projects, and experiences into high-impact, professionally tailored alignments mapped explicitly to the target role.
2. **ATS Optimization Expert (ATS Agent):** Evaluates linguistic and structural elements against industrial parsing software algorithms to flag formatting, semantic gaps, and missing keywords.
3. **Professional Career Coach (Coach Agent):** Identifies programmatic discrepancies between current capabilities and market expectations, framing them into a time-bound actionable sprint.

---

## 📂 Project Structure

```text
ai-resume-builder/
├── inputs/
│   ├── job_description.txt       # Target job posting/requirements
│   └── student_profile.txt       # Raw student resume/skills/projects
├── outputs/
│   ├── ats_report.md             # ATS score and keyword gap analysis
│   ├── improvement_plan.md       # 4-week step-by-step roadmap
│   └── resume.md                 # Tailored, polished markdown resume
├── .env                          # Local environment secrets storage
├── agents.py                     # CrewAI Agent definitions & LLM configuration
├── crew.py                       # Crew pipeline coordination and task matching
├── app.py                       # Orchestration entry point & file stream controller
├── tasks.py                      # Production standards and task definitions
└── pyproject.toml                # Managed environment project dependencies


## 🚀 Installation Guide

This project leverages **`uv`**, an ultra-fast Python package installer and resolver. Because the verified `uv.lock` file is included in this repository, you do not need to manually install or manage individual dependencies. `uv` will sync your environment to the exact project specifications automatically.

### Step 1: Clone the Workspace
Clone the repository and navigate to your project root directory:
```bash
git clone <your-github-repo-url>
cd ai-resume-builder
Step 2: Configure Environment Variables
Create a .env file in the root of your directory to secure your Gemini API Key:

Code snippet


GEMINI_API_KEY=your_actual_gemini_api_key_here
Step 3: Install and Sync Dependencies
Simply run the sync command. uv will read the committed uv.lock file and construct your virtual environment with the precise version matches instantly:

Bash


uv sync
(Note: If you haven't installed the custom extras on your machine yet, you can alternatively run uv run main.py directly, and uv will handle the environment lock sync automatically in the background).

Step 4: Add Input Specifications
Ensure your target parameters are configured prior to running the pipeline:

Place your raw academic info, projects, and tech stack into inputs/student_profile.txt

Place the full job specification text inside inputs/job_description.txt

Step 5: Execute the Engine
Run the multi-agent pipeline:

Bash


uv run main.py
Upon successful execution, the compiled files will be generated instantly in your outputs/ directory.

