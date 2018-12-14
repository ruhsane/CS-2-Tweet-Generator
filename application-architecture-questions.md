###What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
     Tweet Generator's main purpose is to generate a random sentence that a person most likely would say. To achieve this, we need to take in large amount of quotes that a person have said, organize them into a form of data structure, analyze the most frequent used words, and sample those words into a new sentence. We used different files and modules for each of these features.

###Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
    Yes. We generated histogram in different data structures. Thus the files were named such as "histogram_dictionary", "histogram_list_of_lists", "histogram_list_of_tuples". Function names were straightforward such as "frequency", "unique_words".

###What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
    Scope of variables are mostly function based.


###Are the functions small and clearly specified, with as few side effects as possible?
    yes.

###Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
    yes.

###Can files be used as both modules and as scripts?
    yes.

###Do modules all depend on each other or can they be used independently?
    They can be used independently.
