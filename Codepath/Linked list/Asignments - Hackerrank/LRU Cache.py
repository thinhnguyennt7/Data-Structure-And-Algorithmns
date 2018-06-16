'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?



LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node:
	def __init__(self, k, v):
		self.key = k
		self.val = v
		self.prev = None
		self.next = None

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.dic = dict()
		self.head = Node(0, 0)
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key):
		if key in self.dic:
			n = self.dic[key]
			self._remove(n)
			self._add(n)
			return n.val
		return -1

	def put(self, key, value):
		if key in self.dic:
			self._remove(self.dic[key])
		n = Node(key, value)
		self._add(n)
		self.dic[key] = n
		if len(self.dic) > self.capacity:
			n = self.head.next
			self._remove(n)
			del self.dic[n.key]

	def _remove(self, node):
		p = node.prev
		n = node.next
		p.next = n
		n.prev = p

	def _add(self, node):
		p = self.tail.prev
		p.next = node
		self.tail.prev = node
		node.prev = p
		node.next = self.tail


########
#


class LRUCache {
    Map<Integer, Integer> map;
    int capacity=0;
    public LRUCache(int capacity) {
        map = new LinkedHashMap<>(capacity);   
        this.capacity=capacity;
    }
    
    public int get(int key) {
        Integer value=-1;
        if(map.containsKey(key)){
            value=map.remove(key);
             map.put(key,value);
        }
        return value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            map.remove(key);
        }
        if(map.size()==capacity){
            Map.Entry<Integer,Integer> first =map.entrySet().iterator().next();
            map.remove(first.getKey());
        }
        map.put(key,value);
    }
}






# Another way to do put method
if(record.containsKey(key))
            record.remove(key);
        if(record.size() == capacity) {
            Iterator itr = record.keySet().iterator();
            if(itr.hasNext()) {             
                // Removing the top element of the map (As technically, it appeared before rest of the members of the map.)
                Integer key_toRm = (Integer) itr.next();
                record.remove(key_toRm);
            }
        }
        record.put(key,value); // Added at the record's tail.
    }