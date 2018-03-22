#ifndef __LRU_HPP__
#define __LRU_HPP__
#include <map>
template<class K, class V>
struct node {
  K key;
  V value;
  node(K key, V value);
};

template<class K, class V>
class lru {
  node<K,V>* head;
  map<K,Node<K,V>> map;
public:
   lru();
  ~lru();

  void put(K key, V value);
  V get(K key);
};

#endif
