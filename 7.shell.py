import os
import subprocess

def shell():
    print("Simple Shell. Type 'exit' to quit.")

    while True:
        try:
            # Prompt for user input
            command = input("$ ").strip()
            if command.lower() == "exit":
                break

            # Handle piping (|) and IO redirection (> and <)
            if '|' in command:
                commands = command.split('|')
                prev_output = None

                for cmd in commands:
                    cmd = cmd.strip().split()
                    if prev_output:
                        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        prev_output, _ = process.communicate(input=prev_output)
                    else:
                        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        prev_output, _ = process.communicate()

                print(prev_output, end="")

            elif '>' in command:
                parts = command.split('>')
                cmd = parts[0].strip().split()
                output_file = parts[1].strip()

                with open(output_file, 'w') as file:
                    subprocess.run(cmd, stdout=file)

            elif '<' in command:
                parts = command.split('<')
                cmd = parts[0].strip().split()
                input_file = parts[1].strip()

                with open(input_file, 'r') as file:
                    subprocess.run(cmd, stdin=file)

            else:
                # Simple command execution
                process = subprocess.run(command.split(), capture_output=True, text=True)
                print(process.stdout, end="")
                if process.stderr:
                    print(process.stderr, end="")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    shell()
