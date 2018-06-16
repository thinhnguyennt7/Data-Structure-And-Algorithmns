/*
Challenge 1 - Hash table word count (10 minutes)
Write a program which takes as its input a String of natural language text and outputs a HashMap<String,Integer>
whose keys are the unique words in the input and whose values are the number of times those words occur. The algorithm
should be case-insensitive (e.g. "Program" and "program" would count as the same word) and ignore punctuation and whitespace.

Example: Given the input ""To be or not to be, that is the question"", the outputted HashMap would contain 8 entries, with two
words having a count of 2 and six words having a count of 1:

"to"        → 2
"be"        → 2
"or"        → 1
"not"       → 1
"that"      → 1
"is"        → 1
"the"       → 1
"question"  → 1
*/

// Hash table word count
public class Solution {

  public HashMap<String, Integer> wordCount(String s) {
    s = s.replaceAll("^[a-zA-Z]", " ").toLowerCase();
    String[] split = s.split(" ");

    HashMap<String, Integer> map = new HashMap();

    for (int i=0; i < split.length; i++) {
      String word = split[i];
      if (!word.equals("")) {
        if (map.containsKey(word)) {
          map.put(word, map.get(word) + 1);
        } else {
          map.put(word, 1);
        }
      }
    }
    return map;
  }
}