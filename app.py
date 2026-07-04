import os
from dotenv import load_dotenv
from crew import ResumeBuilderCrew  # Standard python import or local crew reference

# Load environment variables from .env file
load_dotenv()


def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Required file missing at '{file_path}'. Please create it.")
        exit(1)


def main():
    # Verify API key is present
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY is not set in the environment or .env file.")
        return

    # Ensure output directory exists
    os.makedirs("outputs", exist_ok=True)

    print("Reading input files...")
    student_profile = read_file("inputs/student_profile.txt")
    job_description = read_file("inputs/job_description.txt")

    print("\nStarting CrewAI Resume Optimization Pipeline...")
    builder_crew = ResumeBuilderCrew(student_profile, job_description)

    # Run the crew
    result = builder_crew.kickoff()
    print(result)

    print("\nPipeline execution complete! Check your 'outputs/' folder for:")
    print("- outputs/resume.md")
    print("- outputs/ats_report.md")
    print("- outputs/improvement_plan.md")


if __name__ == "__main__":
    main()
