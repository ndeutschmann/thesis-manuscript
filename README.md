# A variation on HarvardThesis

This is the template I used to write my thesis. I made a few modifications to suit my use.

## Compilation:
Compile using ```make``` or ```make compile```. The makefile calls ```latexmk``` to handle the compilation

## Frontmatter
By default, most of the front matter is suppressed to make editing of the body of the text easier. It can be restored by replacing ```\fullfalse``` by ```\fulltrue``` in ```harvard-thesis.cls```. Look for ```% IF FULL``` in that file to locate the command.
## Word count logging
Use ```make count``` to run ```texcount``` and update ```scripts/phdwordcount.pdf```, a pyplot graph of the number of words as a function of time
## Clean up
The command ```make clean``` removes all outputs from ```xelatex``` and ```bibtex```
## Viewing
Use ```make view``` to open the PDF output. It uses the ```open``` command which might not work outside of OSX, replace it in the Makefile by ```evince``` or some other PDF viewer.
## Original information
*This is the original README from the HarvardThesis I am modifying*

HarvardThesis 0.2
Jordan Suchow, April 2011.
http://jwsu.ch/ow/

For contributions, comments, and bug reports,
please contact me at suchow {at} fas.harvard.edu.

Modified by Andrew Leifer, August 2011
http://andrewleifer.com
andrew.leifer@post.harvard.edu

## License

This software is free and is covered under the MIT License, given here:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
