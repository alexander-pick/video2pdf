# video2pdf

I wanted to take a video class for certification, but the chosen video training lacked the slides. As I prefer printed slides to take my notes, I decided that these need to be extracted.

After some time of googling I came up with various ideas and a script by Dr. Andreas Boehler, which was close to what I needed but not 100% matching. So I took his script and modified it to fit my needs. As matching histograms is something what doesn’t works well with text only slides, I replaced that part with a phash based check. Furthermore, I do not match against the last valid slide, not against the last one in the list to improve the hit rate. Another big change was the dynamically generated output folder which is needed as I used this script with a bash script to process the subfolder structure the course came with. In the end the script generated very useful results with nearly no glitches.

If someone is interested in using the script, please make sure you adjust the ffmpeg params. To avoid many transition effects slides in my output I use a fixed stepping, 1 shot every 5 seconds. There is also a parameter to skip the intro, that is the -ss part, make sure you adjust it to your needs.
Have fun!

Link to the original script:
https://www.aboehler.at/doku/doku.php/blog:2012:0801_extracting_lecture_slides_from_video
