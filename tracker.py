class RemoteJobTracker:
    def __init__(self, target_salary):
        self.target_salary = target_salary
        self.completed_projects = []
        self.git_connected = True

    def add_project(self, project_name):
        self.completed_projects.append(project_name)
        print(f"🚀 Project '{project_name}' successfully added to portfolio!")

    def check_readiness(self):
        project_count = len(self.completed_projects)
        print(f"\n--- Graduation Readiness Report ---")
        print(f"Target Remote Salary: ${self.target_salary:,}")
        print(f"Portfolio Projects Completed: {project_count}/3")
        
        if project_count >= 3 and self.git_connected:
            print("✅ STATUS: Ready to apply for $100k remote positions.")
        else:
            print(f"⚠️ STATUS: Pending. Need {3 - project_count} more production-grade apps.")

# Initialize the tracking system for Jordon
jordon_track = RemoteJobTracker(target_salary=100000)
jordon_track.add_project("Terminal Portfolio Pipeline")
jordon_track.check_readiness()

