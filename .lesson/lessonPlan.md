# Exercise 06: Manipulating Data

## Learning Objectives
1. Students will be able to use iteration and list assignment operators on the global `list` to make changes and remove elements with search terms
2. Students will understand how to address individual fields through the indexing of individual rows accessed through pythonic iteration (*sounds clever, eh?*) 
3. Students will have experience searching and manipulating data based on standard NEA questioning techniques
4. Students will develop their knowledge of nesting with `if` statements to engage with multiple search criteria in a manageable way
 
## Overview
This unit should take two hours to complete. This combines together many of the post-process and storage requirements of the NEA into a manageable amount of content based around manipulation of a 2D `list`  which is infinitely more straightforward than them dumping the data into a file and trying to read it back in before manipulating it. In most cases this method reduces the amount of work needed for these kind of changes by an enormous amount, even to the point that this final bullet-point feels more like that than another insurmountable effort.

Students will gain experience in adding to the menu structure on the fly, this should be a small leap from previously where they have set up menus from scratch. It is a worthwhile skill to encourage the students to develop as they should not be afraid to hack into their code to improve.

Students will struggle with the search because of the exact matching nature, whilst this would be fixed with *fuzzy searching* in production code it is not necessary in the limited time and scope given in the NEA. Push the `lower()` or other text transformation method to ensure that both *needle* and *haystack* are at least in consistent formats.

You will need to reiterate the indexing of the rows based on their implementation of the data entry part of the algorithms, students should be encouraged to develop 2D lists structures on paper first so that they can note the indexes and use them for reference throughout the build. 

## Delivering the content in class

1. ***Back to the Game Rentals*** (5 minutes) Copy the code for the basic program and run through it with the students to show how the program is currently working and how it needs to be extended.

2. ***Changing the Menu*** (15 minutes) Model the build of the change of the menu, new subroutines and placeholders - and the testing of that. Students should be given time to alter the menu from the initial code themselves.

3. ***Building the Search*** (30 minutes)  Model the build step by step, identifying the search criteria needed, how to locate the criteria in the row, how to transform the needle and haystack text to be in the same format, and then how to use nesting to move onto the next level of the search criteria and repeat the process again. Do this more slowly that you'd expect to, as holding multiple levels of search in their heads on top of the new skills here can be overwhelming for some. Ask the students to implement each stage before going back to your modelling - do not ask the students to build it all in one go as they will make mistakes and will often just chalk it up as difficult.

4. ***Task*** (50 minutes ) This task requires thinking and planning, students will need support with the structure of their search criteria and taking user `input` to alter the values of a stored variable.
