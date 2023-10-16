WhichBatman Database Creator Planning Doc
Christian Silva                                                                                                                                8/27/23


This primary function of this tool is to create an easy to use command line program which takes as input a file containing a list of labeled urls to youtube videos, and produces as output a folder of video files which are properly named in an organized fashion.


Input File 
The input file shall be a .txt file created as such:
* There will be 3 types of lines, titles, actors, and urls
* Actor lines shall all be preceded with the following characters: “ACTOR: “
* Title lines shall all be preceded with the following characters: “TITLE: “
* Url lines shall all be preceded with the following characters: “URL: “
* Each title shall correspond to an individual movie
* For user readability, there shall be an empty line between the last url of a title block, and the new title line


For example:
ACTOR: Adam West


TITLE: Dark Knight Rises
URL: https://www.youtube.com/
URL: https://www.youtube.com/


TITLE: Batman Begins
URL: https://www.youtube.com/


Output Format
The program shall be passed a relative folder path within the github repository, at which point it will look to see if this folder exists. In its absence, the folder shall be created. Video files will then be downloaded via their given urls from the input file, and named as such:


<actor_name>-<movie_title>-<numeric identifier>


The numeric identifier in question shall be calculated by simply iterating over the files currently in existence in the output folder, and adding 1 to the largest existing numeric identifier corresponding to the same movie title. This process will assume 1 based indexing for numeric identifiers. NOTE, the movie_title portion of the naming scheme shall separate individual words via a _ character and shall not include a - character.


Program Function
The program will take as input the relative paths to the input file, and the desired output folder, in that order. The program will then do the following in order:


1. Look for the existence of the input file, throwing an error if it cannot find it.
2. Look for the existence of the output folder, prompting the user for input to request permission to create the folder if it cannot find it, and stopping if it does not get this permission.
3. Create a map which uses as a key titles and as a value the largest in use numeric identifier for that title, initializing at 0.
4. Iterate through the files in the output folder, finding all unique titles and updating the title-index map with the findings. This process assumes the naming scheme laid out in the input file section of this document.
5. Iterate through the input file, at each line do the following:
   1. If it is a title line:
      1. Create a name string from the title as laid out in the input file section
      2. Lookup the name string in the title-index map
      3. If lookup fails, create new entry and initialize value to 0
      4. Move to next line
   2. If it is a url line:
      1. Download the video from the url
      2. If download fails, log it and move to next line
      3. Create video-title string by looking up the name string in title-index map, and concatenate the name string with the incremented value, as described in the input file section of this document
      4. Increment the value of the name string lookup in the title-index map
      5. Move to next line
   3. If it is a blank line
      1. Move to next line
   4. If EOD is found
      1. Stop