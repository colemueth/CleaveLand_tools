# CleaveLand_tools:
Add-on tools for CleaveLand4

Background: I do Parallel Analysis of RNA Ends (PARE) experiments to study the interaction between plant pathogens and their hosts at the RNA level. My data analysis involves CleaveLand4 software from the Axtell Lab at Penn State University. (https://github.com/MikeAxtell/CleaveLand4/releases). I'm not a member of this lab; I just use the software.
I have PARE libraries from both infected plants and uninfected controls. In analyzing the data, I noticed that many fungal transcripts have high “Category 0” peaks that appears to be an sRNA-directed cut site, yet no sRNA from my sRNA-seq library is predicted to bind there. These are unique to infected libraries and present in multiple independent biological reps.
I wrote a script called degNostic.py that pulls out these differences. It searches through two CleaveLand-generated degradome density files for Category 0 peaks with a user-defined reads cutoff. It compares the peak in one file with the data for the same transcript in a second file. For all transcripts with peaks that are unique to one file, it outputs the transcript name and the position of the cut site.

Target audience: Scientists who use CleaveLand4 to analyze degradomes from multiple treatments.

Software Dependencies: Python 3

To run: Enter this sample command in a terminal:
$ python degNostic.py InfSample_dd.txt 15 UninfSample_dd.txt 2
This will output a .txt file with all Category 0 sites with > 15 reads that are exclusive to the Infected degradome. There should be 4 of them.

Disclaimer: This script will not identify new "genuine" sRNA/target pairs. It will identify one potentially interesting class of anomaly in PARE data: a clear transcript slicing site with no corresponding sRNA. 
