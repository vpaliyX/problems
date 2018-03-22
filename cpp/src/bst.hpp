#ifndef __BST_HPP__
#define __BST_HPP__
#include<iostream>

template<class T>
struct Default {
  T value;
  Default():value(){}
};

template<class K, class V>
struct node {
  node<K,V>* parent;
  node<K,V>* left;
  node<K,V>* right;
  K key;
  V value;
  explicit node(K key, V value);
};

template<class K, class V>
class bst {
 private:
   node<K,V>* root;
   std::size_t count;
   void transplant(node<K,V>*, node<K,V>*);
   node<K,V>* _search(K);
   node<K,V>* _min();
   node<K,V>* _max();
 public:
   explicit bst();
   void put(K, V);
   void remove(K);
   V search(K);
   V min();
   V max();
};

template<class K, class V>
inline node<K,V>::node(K key, V value) {
  this->key = key;
  this->value = value;
}

template<class K, class V>
inline bst<K,V>::bst(){}

template<class K, class V>
void bst<K,V>::put(K key, V value) {
  auto temp = root;
  auto parent = root;
  auto target = new node<K,V>(key, value);
  while (temp != nullptr) {
    parent = temp;
    temp = temp->key >= key ? temp->left : temp->right;
  }
  if (parent->key >= key)
    parent->left = target;
  else
    parent->right = target;
  target->parent = parent;
}

template<class K, class V>
node<K,V>* bst<K,V>::_search(K key) {
  auto temp = root;
  while (temp != nullptr) {
    if (temp->key == key)
      return temp;
    temp = temp->key >= key ? temp->left : temp->right;
  }
  return temp;
}

template<class K, class V>
void bst<K,V>::transplant(node<K,V>* first, node<K,V>* second) {
  if (first == nullptr || second == nullptr)
        return;
  auto parent = first->parent;
  if (parent == nullptr)
    root = second;
  else if (parent->right != first)
    parent->left = second;
  else
    parent->right = second;
  second->parent = parent;
}

template<class K, class V>
node<K,V>* bst<K,V>::_max() {
  if (root != nullptr) {
    auto max = root;
    while (max->right != nullptr)
      max = max->right;
    return max;
  }
  return nullptr;
}

template<class K, class V>
node<K,V>* bst<K,V>::_min() {
  if (root != nullptr) {
    auto max = root;
    while (max->left != nullptr)
      max = max->left;
    return max;
  }
  return nullptr;
}

template<class K, class V>
inline V bst<K,V>::min() {
  auto min = _min();
  return min != nullptr ? min->value : Default<V>().value;
}

template<class K, class V>
inline V bst<K,V>::max() {
  auto max = _max();
  return max != nullptr ? max->value : Default<V>().value;
}

template<class K, class V>
inline V bst<K,V>::search(K key) {
  auto target = _search(key);
  return target != nullptr ? target->value : Default<V>().value;
}

template<class K, class V>
void bst<K,V>::remove(K key) {
  auto target = _search(key);
  if (target != nullptr) {
    auto successor = target->left;
    if (target->left == nullptr) {
      successor = target->right;
      transplant(target, successor);
    } else if (target->right == nullptr) {
      transplant(target, successor);
    } else {
      auto right = target->right;
      successor = _min(right);
      if (successor->parent != target) {
        successor->parent->left = successor->right;
        if (successor->right != nullptr)
          successor->right->parent = successor->parent;
        successor->right = right;
        right->parent = successor;
      }
      transplant(target, successor);
      successor->left = target->left;
      target->left->parent = successor;
    }
    delete target;
  }
}
#endif
