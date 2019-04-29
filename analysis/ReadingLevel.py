import textstat

text = "this is easy, the quick brown fox jumped over the lazy dog"
textmany = ["Yeah, I think it's a good environment for learning English.",
"Cats are good pets, for they are clean and are not noisy.",
"This is the last random sentence I will be writing and I am going to stop mid-sent",
"She wrote him a long letter, but he didn't read it.",
"He told us a very exciting adventure story.",
"I checked to make sure that he was still alive."]

for i in textmany:
    level = textstat.flesch_reading_ease(i)
    print(level)
