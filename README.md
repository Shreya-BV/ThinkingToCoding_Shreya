# Count Vowels in a Word
## Task- Ask the user to enter a word or a sentence,then count and display the njumber of vowels in the input.  Example-   Input: "Hello World"    Output: 3 vowels

#Logic Summary
1.Accept input (word/sentence) from the user.

2.Define a string containing all vowels (aeiouAEIOU).

3.Initialize a counter variable to 0.

4.Loop through each character in the input.

5.If the character is a vowel, increment the counter.

6.Display the total number of vowels.

7.Connect to MongoDB using MongoClient.

8.Create/connect to database (internship_db) and collection (vowel_data).

9.Store the input and vowel count as a document using insert_one()
