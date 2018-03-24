#ifndef __BST_HPP__
#define __BST_HPP__
#include<iostream>
#include<iterator>

namespace BST  {

template<class K, class V>
struct node {
  node<K,V>* parent;
  node<K,V>* left;
  node<K,V>* right;
  const K key;
  const V value;

  explicit node(K, V,
      node<K,V>* = nullptr,
      node<K,V>* = nullptr,
      node<K,V>* = nullptr);
};

template<class K, class V>
class bst {
 private:
   node<K,V>* root;
   node<K,V>* _min();
   node<K,V>* _max();
   node<K,V>* _find(const K&);
   void transplant(node<K,V>*, node<K,V>*);
  public:
   V max();
   V min();
   V find(const K&);
   void remove(const K&);
   void insert(const K&, const V&);
};

template<class K, class V>
inline node<K,V>::node(K key, V value, node<K,V>* parent, node<K,V>* left, node<K,V>* right)
    : key {std::move(key)}
    , value {std::move(value)}
    , parent(parent)
    , left(left)
    , right(right)
{}

template<class K, class V>
node<K,V>* bst<K,V>::_min() {
  auto it = root;
  if (root != nullptr) {
    while (it->left != nullptr)
      it = it->left;
  }
  return it;
}

template<class K, class V>
node<K,V>* bst<K,V>::_max() {
  auto it = root;
  if (root != nullptr) {
    while (it->right != nullptr)
      it = it->right;
  }
  return it;
}

template<class K, class V>
node<K,V>* bst<K,V>::_find(const K &key) {
  auto it = root;
  while (it != nullptr) {
    if (it->key == key)
      return it;
    it = it->key >= key ? it->left : it->right;
  }
  return it;
}

template<class K, class V>
V bst<K,V>::find(const K& key) {
  auto it = _find(key);
  return it != nullptr ? it->value : V {};
}

template<class K, class V>
V bst<K,V>::max() {
  auto it = _max();
  return it != nullptr ? it->value : V {};
}

template<class K, class V>
V bst<K,V>::min() {
  auto it = _min();
  return it != nullptr ? it->value : V {};
}

template<class K, class V>
void bst<K,V>::insert(const K &key, const V &value) {
  if (root == nullptr) {
    root = new node<K,V>(key, value);
    return root;
  }
  auto parent = root;
  auto it = root;
  while (it != nullptr) {
    parent = it;
    it = it->key < key ? it->right : it->left;
  }
  auto target = new node<K,V>(it->key, it->value, parent);
  if (parent->key < key)
    parent->right =target;
  else
    parent->left = target;
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
void bst<K,V>::remove(const K &key) {
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
}4

}
#endif
