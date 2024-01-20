import subprocess


def call_whisper(filename: str) ->None:
    exe_path = '/Users/pradyu/whisper.cpp/main'
    working_directory = '/Users/pradyu/whisper.cpp'
    result = subprocess.run([exe_path,'-f', filename], capture_output = True, text = True, cwd = working_directory)
    if (result.stdout == ''):
        print("The Error is", result.stderr)
    else:
        print("The output is", result.stdout)

def mp3_to_wav(input_path: str, output_name: str) -> None:
    try:
        subprocess.call(['ffmpeg', '-i', input_path,'-ar' , '16000', output_name + '.wav'])
    except Exception as e:
        return 

def main(input_path: str) -> None:
    if (input_path.endswith('.mp3')):
        mp3_to_wav(input_path, 'output_new')
        input_path = 'output_new.wav'
    print("main")