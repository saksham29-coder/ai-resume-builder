from crewai import Agent, LLM

# Initialize the Gemini model
# CrewAI uses litellm under the hood, so prefix with 'gemini/'
gemini_llm = LLM(model="gemini/gemini-2.5-flash", temperature=0.5)


class ResumeAgents:
    def resume_profiler_agent(self) -> Agent:
        return Agent(
            role="Expert Resume Strategist",
            goal="Analyze a student's profile and match it optimally against a target job description.",
            backstory=(
                "With decades of experience in tech recruitment, you know exactly how to extract "
                "hidden value from a student's academic projects, skills, and coursework to make "
                "them look like a perfect fit for a role."
            ),
            llm=gemini_llm,
            verbose=True,
        )

    def ats_specialist_agent(self) -> Agent:
        return Agent(
            role="ATS (Applicant Tracking System) Optimization Expert",
            goal="Evaluate resumes against strict ATS screening criteria and identify keyword gaps.",
            backstory=(
                "You understand the algorithms behind major ATS platforms. You ensure resumes "
                "are parsed correctly and rank highly by identifying missing critical technical "
                "and soft skills keywords."
            ),
            llm=gemini_llm,
            verbose=True,
        )

    def career_coach_agent(self) -> Agent:
        return Agent(
            role="Professional Career Coach",
            goal="Provide highly actionable roadmaps to help students bridge their professional and technical gaps.",
            backstory=(
                "You are passionate about helping young engineers grow. You don't just point out "
                "what's missing; you provide step-by-step guidance on what to learn, build, or revise next."
            ),
            llm=gemini_llm,
            verbose=True,
        )
