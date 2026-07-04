```text
📥 INPUTS
 └── 📄 inputs/student_profile.txt (Raw Student Data)
 └── 📄 inputs/job_description.txt (Target Job Role)
        │
        ▼
🤖 ORCHESTRATION PIPELINE
 └── 🧩 crew.py (ResumeBuilderCrew)
        │
        ├── 🔹 [Agent 1] Expert Resume Strategist
        │      └── 📋 Task: Profile & Align
        │             └─► 💾 Result: outputs/resume.md
        │
        ├── 🔹 [Agent 2] ATS Optimization Expert
        │      └── 📋 Task: ATS Evaluation
        │             └─► 💾 Result: outputs/ats_report.md
        │
        └── 🔹 [Agent 3] Professional Career Coach
               └── 📋 Task: Gap Improvement
                      └─► 💾 Result: outputs/improvement_plan.md



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

### Step 1: Clone the Repository
git clone <your-github-repo-url>

Step 2: Navigate to root folder
cd ai-resume-builder

Step 3: Configure Environment Variables
Create a .env file in the root of your directory to secure your Gemini API Key:
GEMINI_API_KEY=your_actual_gemini_api_key_here

Step 3: Install and Sync Dependencies
uv sync

Step 4: Add Input Specifications

Place your raw academic info, projects, and tech stack into inputs/student_profile.txt

Place the full job specification text inside inputs/job_description.txt

Step 5: Execute the Engine
uv run app.py

Upon successful execution, the compiled files will be generated instantly in your outputs/ directory.

