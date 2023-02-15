import os

def video_renamer(files_directory):
    i = 1
    for filename in os.listdir(files_directory):
        ext = filename.split(".")  # "vide.1123.d.as.mp4".split(".") -> ["vide", "1123"...., "mp4"]
        ext = ext[len(ext)-1]
         # ||
        # ext = ext[-1]

        if ext in ["mp4", "avi", "mkv"]:
            print(f"{filename} is not a video, skipping it...")
            continue

        final_name = f"video{str(i)}.{ext}"
        source_path = files_directory + filename
        final_name = files_directory + final_name
        os.rename(source_path, final_name)
        i += 1


def main():
    video_renamer("D:/Nicky/Videos/")


if __name__ == "__main__":
    main()