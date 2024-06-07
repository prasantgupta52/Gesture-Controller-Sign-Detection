import subprocess
import sys
import os

# Function to execute a script
def run_script(script_path):
    result = subprocess.run([sys.executable, script_path])
    if result.returncode == 0:
        print(f"{script_path} finished successfully.")
    else:
        print(f"Error: {script_path} exited with code {result.returncode}.")


# Main function to handle user input and run the appropriate script
def main():
    while True:
        user_input = input("Enter '1' to run Gesture Controller \nEnter '2' to run Sign Detection\n").strip()   
        if user_input == '1':
            script_path = os.path.join('Mouse-Controll-USing-Gesture','src', 'Main_Gesture_Controller.py')
            run_script(script_path)
            print("Started Gesture controller")
            break
        elif user_input == '2':
            script_path = os.path.join('sign-language-detector-python','inference_classifier.py')  # Adjust this if script2.py is also inside a directory
            run_script(script_path)
            print("Started sign detection")
            break
        else:
            print("Invalid input. Please enter '1' or '2'.")
        

if __name__ == "__main__":
    main()
