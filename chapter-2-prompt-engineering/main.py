from generators.weekly_report import weekly_status_report
from config import OPENAI_API_KEY

def main():
    weekly_data = {
        "project_name": "Project Omega",
        "achievements": "Completed phase 1, finished code review.",
        "next_steps": "Start testing, plan next sprint."
    }


    weekly = weekly_status_report(api_key=OPENAI_API_KEY)
    print("Generating report...")
    report = weekly.generate_report(weekly_data)
    print("Report generated:\n", report)

if __name__ == "__main__":
    main()
