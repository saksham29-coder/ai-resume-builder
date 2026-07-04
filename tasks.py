from crewai import Task


class ResumeTasks:
    def profile_and_align_task(self, agent, student_profile, job_description) -> Task:
        return Task(
            description=(
                f"Analyze the following student profile:\n{student_profile}\n\n"
                f"Cross-reference it with this target job description:\n{job_description}\n\n"
                "Extract the most relevant experiences, projects, and skills. Tailor the phrasing "
                "to emphasize alignment with the role's requirements while maintaining absolute honesty."
            ),
            expected_output="A perfectly formatted, professional markdown resume tailored specifically to the job description.",
            agent=agent,
            output_file="outputs/resume.md",
        )

    def ats_evaluation_task(self, agent, student_profile, job_description) -> Task:
        return Task(
            description=(
                f"Review the student profile:\n{student_profile}\n against the job requirements:\n{job_description}.\n\n"
                "Run a mock ATS scan. Identify missing keywords, calculate a simulated match score (0-100%), "
                "and list formatting issues or structural issues that might cause an ATS to reject the application."
            ),
            expected_output="A comprehensive ATS Audit Report in markdown format containing a score, keyword analysis, and clear green/yellow/red flags.",
            agent=agent,
            output_file="outputs/ats_report.md",
        )

    def gap_improvement_task(self, agent, student_profile, job_description) -> Task:
        return Task(
            description=(
                f"Based on the student's current profile:\n{student_profile}\n and the expectations of the job:\n{job_description},\n"
                "identify the explicit gaps in skills, certifications, or project depth. "
                "Create a realistic improvement plan outlining specific topics to learn or project enhancements to make."
            ),
            expected_output="A detailed, structured improvement plan in markdown format featuring a 4-week actionable roadmap.",
            agent=agent,
            output_file="outputs/improvement_plan.md",
        )
