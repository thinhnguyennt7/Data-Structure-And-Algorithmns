/*

One common pattern when using hash tables requires building a Map whose values are Collection instances. In this challenge,
we'll take the output of the previous challenge and invert it.

Write a program that takes as its input a HashMap<String,Integer> and returns a HashMap<Integer,HashSet<String>> containing

the same data as the input map, only inverted, such that the input map's values are the output map's keys and the input
map's keys are the output map's values.

Example: Consider the example output for Challenge #1. Using that map as the input, the output for this challenge would be:

2 → ["to", "be"]
1 → ["or", "not", "that", "is", "the", "question"]

 */

// Multimaps
public class Solution {

	public Map<Integer, Set<String>> multiMap(Map<String, Integer> wordCounts) {
		Map<Integer, Set<String>> multiMap = new HashMap<Integer, Set<String>>();
		for (Entry<String, Integer> wordCount : wordCounts.entrySet()) {
			String word = wordCount.getKey();
			Integer count = wordCount.getValue();

			Set<String> words = null;

			if (!multiMap.containsKey(count)) {
				words = new HashSet<String>();
				multiMap.put(count, words);
			} else {
				words = multiMap.get(count);
			}

			words.add(word);
		}
		return multiMap;
	}
}