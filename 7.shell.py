import os
import subprocess

def ex_command(command):
    try:
        # Split command -> parts
        parts = command.split('|')
        processes = []

        for i, part in enumerate(parts):
            part = part.strip()

            # Handle input redirection
            if '<' in part:
                cmd, input_file = map(str.strip, part.split('<'))
                input_file = open(input_file, 'r')
            else:
                cmd = part
                input_file = None

            # Handle output redirection
            if '>' in cmd:
                cmd, output_file = map(str.strip, cmd.split('>'))
                output_file = open(output_file, 'w')
            else:
                output_file = None

            # Parse the command
            cmd_parts = cmd.split()

            if i == 0:
                # First command, potentially with input redirection
                proc = subprocess.Popen(cmd_parts, stdin=input_file, stdout=subprocess.PIPE)
            else:
                # Subsequent commands in the pipeline
                proc = subprocess.Popen(cmd_parts, stdin=processes[-1].stdout, stdout=subprocess.PIPE)

            if input_file:
                input_file.close()

            processes.append(proc)

        # Handle output of the final command
        final_output = processes[-1].stdout

        if output_file:
            # Write output -> file
            with open(output_file.name, 'w') as f:
                f.write(final_output.read().decode('utf-8'))
            output_file.close()
        else:
            # Print output -> console
            print(final_output.read().decode('utf-8'))

        # Wait for all processes to complete
        for proc in processes:
            proc.wait()

    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        try:
            command = input("shell> ").strip()
            if command.lower() in {"exit", "quit"}:
                break
            ex_command(command)
        except KeyboardInterrupt:
            print("\nExit shell.")
            break

if __name__ == "__main__":
    main()
