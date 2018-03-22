#ifndef __LRU_HPP__
#define __LRU_HPP__
#include <map>
#include<iostream>
#include<assert.h>

template<class T>
struct Default {
  T value;
  Default():value(){}
};

template<class K, class V>
struct node {
  K key;
  V value;
  node<K,V>* next;
  node<K,V>* prev;
  explicit node(K key, V value);
};

template<class K, class V>
class lru {
private:
  node<K,V>* head;
  node<K,V>* tail;
  std::map<K,node<K,V>*> map;
  std::size_t capacity;
  void replace(node<K,V>*);
public:
  explicit lru(std::size_t);
  void put(K key, V value);
  V get(K key);
};

template<class K, class V>
inline node<K,V>::node(K key, V value) {
  this->key = key;
  this->value = value;
}

template<class K, class V>
inline lru<K,V>::lru(std::size_t capacity) {
  assert(capacity > 1);
  this->capacity = capacity;
  this->head = tail = nullptr;
}

template<class K, class V>
void lru<K,V>::put(K key, V value) {
  auto it = map.find(key);
  if (it != map.end()) {
    node<K,V>* temp = it->second;
    temp->value = value;
    replace(temp);
    return;
  }
  if(capacity == map.size()) {
    tail->prev->next = tail->next;
    node<K,V>* target = tail;
    map.erase(target->key);
    tail = tail->prev;
    delete tail;
  }
  node<K,V>* temp = new node<K,V>(key, value);
  temp->prev = nullptr;
  temp->next = head;
  if(head != nullptr)
    head->prev = temp;
  else
    tail = temp;
  head = temp;
  map.insert(std::pair<K,node<K,V>*> {key, temp});
}

template<class K, class V>
V lru<K,V>::get(K key) {
  auto it = map.find(key);
  if(it != map.end()) {
    replace(it->second);
    return it->second->value;
  }
  return Default<V>().value;
}

template<class K, class V>
void lru<K,V>::replace(node<K,V>* temp) {
  if (temp->prev != nullptr)
    temp->prev->next = temp->next;
  if (temp->next != nullptr)
    temp->next->prev = temp->prev;
  if (tail == temp)
    tail = temp->prev != nullptr ? temp->prev : temp;
  if (head != temp) {
    head->prev = temp;
    temp->next = head;
    head = temp;
  }
}
#endif
