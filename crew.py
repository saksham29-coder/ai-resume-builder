from crewai import Crew, Process
from agents import ResumeAgents
from tasks import ResumeTasks


class ResumeBuilderCrew:
    def __init__(self, student_profile: str, job_description: str):
        self.student_profile = student_profile
        self.job_description = job_description
        self.agents = ResumeAgents()
        self.tasks = ResumeTasks()

    def kickoff(self):
        # Initialize Agents
        profiler = self.agents.resume_profiler_agent()
        ats_expert = self.agents.ats_specialist_agent()
        coach = self.agents.career_coach_agent()

        # Initialize Tasks
        task_resume = self.tasks.profile_and_align_task(
            profiler, self.student_profile, self.job_description
        )
        task_ats = self.tasks.ats_evaluation_task(
            ats_expert, self.student_profile, self.job_description
        )
        task_coach = self.tasks.gap_improvement_task(
            coach, self.student_profile, self.job_description
        )

        # Assemble Crew
        crew = Crew(
            agents=[profiler, ats_expert, coach],
            tasks=[task_resume, task_ats, task_coach],
            process=Process.sequential,
        )

        return crew.kickoff()
