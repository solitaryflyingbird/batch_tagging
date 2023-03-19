import os

def create_txt_file(directory, file_name, content):
    with open(os.path.join(directory, file_name), 'w') as txt_file:
        txt_file.write(content)

def rename_png_files_and_create_txt(directory, content):
    png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
    num_files = len(png_files)

    for i, png_file in enumerate(png_files):
        new_name = f"{i+1:0{len(str(num_files))}d}.png"
        new_txt_name = f"{i+1:0{len(str(num_files))}d}.txt"
        os.rename(os.path.join(directory, png_file), os.path.join(directory, new_name))
        create_txt_file(directory, new_txt_name, content)

if __name__ == "__main__":
    current_directory = os.getcwd()
    txt_file_content = "face_framing_layers, fighter, athletic_body, long_black_hair, (red_eyes: 0.01), ufc, abs, big_breast, simple_background"
    rename_png_files_and_create_txt(current_directory, txt_file_content)
