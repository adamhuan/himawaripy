from os.path import expanduser

# Increases the quality and the size. Possible values: 4, 8, 16, 20
level = 4

#Define a ourly offset or let the script calculate it depending on your timezone
auto_offset = False
hour_offset = 2

# Path to the output file
output_file = expanduser("~/.himawari/himawari-latest.png")

# Xfce4 displays to change the background of
xfce_displays = ["/backdrop/screen0/monitor0/image-path",
                 "/backdrop/screen0/monitor0/workspace0/last-image"]
