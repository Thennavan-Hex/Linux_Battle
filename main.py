import datetime

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirectories = []

    def add_subdirectory(self, name):
        subdirectory = Directory(name, parent=self)
        self.subdirectories.append(subdirectory)
        return subdirectory

    def get_subdirectory(self, name):
        for subdirectory in self.subdirectories:
            if subdirectory.name == name:
                return subdirectory
        return None

    def list_subdirectories(self):
        return [sub.name for sub in self.subdirectories]

class Terminal:
    def __init__(self):
        self.root = Directory("/")
        self.root.add_subdirectory("bin")
        self.root.add_subdirectory("tmp")
        self.current_directory = Directory("~")

    def execute_command(self, command):
        if command == "pwd":
            return self.get_current_path()
        elif command in ["ls", "l"]:
            return " ".join(self.current_directory.list_subdirectories())
        elif command.startswith("cd"):
            path = command.split(" ")[1] if len(command.split(" ")) > 1 else ""
            return self.change_directory(path)
        elif command.startswith("mkdir"):
            directory_name = command.split(" ")[1]
            return self.create_directory(directory_name)
        else:
            return "Invalid command."

    def get_current_path(self):
        path = []
        current = self.current_directory
        while current:
            path.insert(0, current.name)
            current = current.parent
        return f"~{'/'.join(path[1:])}" if path else "~"

    def change_directory(self, path):
        if path == "..":
            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent
                return ""
            else:
                return "Already at root."

        parts = path.split("/")
        for part in parts:
            if part:
                next_directory = self.current_directory.get_subdirectory(part)
                if next_directory:
                    self.current_directory = next_directory
                else:
                    return "Directory not found."
        return ""

    def create_directory(self, directory_name):
        self.current_directory.add_subdirectory(directory_name)
        return ""

class Logger:
    def __init__(self):
        self.log_file_path = self.generate_log_file_path()
        self.initialize_log_file()

    def generate_log_file_path(self):
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"logs/session_{current_time}.log"

    def initialize_log_file(self):
        with open(self.log_file_path, "w") as file:
            file.write("Session Started:\n")

    def log_activity(self, activity):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file_path, "a") as file:
            file.write(f"{current_time} - {activity}\n")

def main():
    terminal = Terminal()
    logger = Logger()

    while True:
        try:
            prompt_symbol = f"{terminal.get_current_path()} $ "
            input_command = input(f"{prompt_symbol}")

            if input_command.lower() == "exit":
                logger.log_activity("Session Ended.")
                break

            result = terminal.execute_command(input_command)
            if result:
                print(result)

            logger.log_activity(input_command)

        except KeyboardInterrupt:
            logger.log_activity("Session Interrupted.")
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
