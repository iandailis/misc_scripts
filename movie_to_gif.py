import sys

import subprocess

# http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html
def main():
    if (len(sys.argv) != 2):
        print(f"usage: python3 {sys.argv[0]} <mov path>")
        return

    input_filename = sys.argv[1]
    output_filename = "".join(sys.argv[1].split(".")[:-1]) + "_converted.gif"
    palette_filename = "palette.png"

    print(f"-------")
    print(f"output: {output_filename}")
    print(f"-------")

    common_filters="fps=14,scale=180:-1:flags=lanczos"

    subprocess.run(["rm", palette_filename])
    subprocess.run(["rm", output_filename])

    # timestamps: -ss 00:00:01 -to 00:00:02.3
    subprocess.run(
        [f"""ffmpeg -ss 00:00:01 -to 00:00:02.3 -v warning -i {input_filename} -vf "{common_filters},palettegen=max_colors=64:reserve_transparent=0" -y {palette_filename} """], shell=True
    )
    subprocess.run(
        [f"""ffmpeg -ss 00:00:01 -to 00:00:02.3 -v warning -i {input_filename} -i {palette_filename} -lavfi "{common_filters} [x]; [x][1:v] paletteuse=dither=sierra3" -loop 0 -y {output_filename}"""], shell=True
    )

if (__name__ == "__main__"):
    main()
