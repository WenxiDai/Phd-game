from crewai import Crew
from crew_assets.image_tasks import phd_image_tasks

def main():
    crew = Crew(tasks=phd_image_tasks)
    crew.kickoff()  # 启动任务队列

if __name__ == "__main__":
    main()