**NAME**: ccwc – word, line, character, and byte count

**SYNOPSIS**: ccwc [OPTION]... [FILE]...

**DESCRIPTION**:
The wc utility displays the number of lines, words, and bytes contained in each input file ~~, or standard input (if no file is specified) to the standard
output.~~  A line is defined as a string of characters delimited by a ⟨newline⟩ character.  Characters beyond the final ⟨newline⟩ character will not be
included in the line count.
 
**OPTIONS**:
     
     -c      The number of bytes in each input file is written to the standard output.  This will cancel out any prior usage of the -m option.

     -l      The number of lines in each input file is written to the standard output.

     -m      The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters,
             this is equivalent to the -c option.  This will cancel out any prior usage of the -c option.

     -w      The number of words in each input file is written to the standard output.