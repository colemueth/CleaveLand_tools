# CleaveLand_tools:
Add-ons for CleaveLand4

Background: I do Parallel Analysis of RNA Ends (PARE) experiments to study the interaction between plant pathogens and their hosts at the RNA level. My analysis pipeline uses CleaveLand4 software from the Axtell Lab at Penn State University. (https://github.com/MikeAxtell/CleaveLand4/releases). I'm not a member of this lab; I just use the software.
In analyzing my data, I needed some functionalities that CleaveLand4 doesn't currently offer. I've written two add-on tools in Python 3 that others may find useful.

Target audience: Scientists who use CleaveLand4 to analyze degradome data.

Dependencies: Python 3

Program 1: degThresh.py

One issue with CleaveLand4 is that it can output thousands of marginal T-plots even on stringent settings. Most of these result from an sRNA mapping to a site with a few random-looking reads here and there. Viewing them all to find a few good ones is inefficient. degThresh.py inputs a degradome density file, checks the reads distribution of each entry, and creates a new degradome density file with entries above a certain threshold of reads. Then the user can run CleaveLand4 in Mode 4 using the new degradome density file and a GSTAr alignment file. CleaveLand4 will now output only the results that are more likely to be interesting to the user.

To run from a terminal:
$ python degThresh.py I_TotalTnF.fa_dd.txt 10

This will output a new degradome density file called I_TotalTnF_thresh10_dd.txt. Instead of 13,266 degradome entries, the new file contains 810 entries, for which there are 10 reads or more at any position along each transcript. 

Program 2: degNostc.py

I have PARE libraries from both infected plants and uninfected controls. In analyzing the data, I noticed that many transcripts from the pathogen have high “Category 0” peaks that appear to be an sRNA-directed cut site, yet no sRNA from my sRNA-seq library is predicted to bind there. These are unique to infected libraries and present in multiple independent biological reps. degNostic.py pulls out these differences. It searches through two CleaveLand-generated degradome density files for Category 0 peaks with a user-defined reads cutoff. It compares the peak in one file with the data for the same transcript in a second file. For all transcripts with peaks that are unique to one file, it outputs the transcript name and the position of the cut site.

To run from a terminal:

$ python degNostic.py InfSample_dd.txt 15 UninfSample_dd.txt 2

This will output a .txt file with all Category 0 sites with > 15 reads that are exclusive to the Infected degradome. There should be 4 of them.

Disclaimer: This script will not identify new "genuine" sRNA/target pairs. It will identify one potentially interesting class of anomaly in PARE data: a clear transcript slicing site that is unique to one treatment with no corresponding sRNA binding site.
