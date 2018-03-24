#ifndef RED_BLACK_BINARY_SEARCH_TREE_HPP
#define RED_BLACK_BINARY_SEARCH_TREE_HPP
#include<iostream>
#include<assert.h>

namespace RBBST {

template<class K, class V>
struct node {
  node<K,V>* parent;
  node<K,V>* right;
  node<K,V>* left;
  K key;
  V value;
  bool red = true;
  explicit node(K key, V value,
        node<K,V>* = nullptr,
        node<K,V>* = nullptr,
        node<K,V>* = nullptr);
};

template<class K, class V>
class rbbstree {
 private:
    node<K,V>* root;
    node<K,V>* _max();
    node<K,V>* _min();
    node<K,V>* _find(const K&);
    void lrotation(node<K,V>*);
    void rrotation(node<K,V>*);
    void ibalance(node<K,V>*);
  public:
    void insert(const K&, const V&);
    void remove(const K&);
    V max();
    V min();
    V find(const K&);
};

template<class K, class V>
inline node<K,V>::node(K key, V value, node<K,V>* parent,
    node<K,V>* left, node<K,V>* right)
    : key {std::move(key)}
    , value {std::move(value)}
    , parent(parent)
    , left(left)
    , right(right)
{}

template<class K, class V>
node<K,V>* rbbstree<K,V>::_min() {
  auto it = root;
  if (it != nullptr) {
    while (it->left != nullptr)
      it = it->left;
  }
  return it;
}

template<class K, class V>
node<K,V>* rbbstree<K,V>::_max() {
  auto it = root;
  if (it != nullptr) {
    while (it->right != nullptr)
      it = it->right;
  }
  return it;
}

template<class K, class V>
node<K,V>* rbbstree<K,V>::_find(const K &key) {
  for(auto it = root; it!= nullptr;) {
    if (it->key == key)
      return it;
    it = it->key < key ? it->right : it->left;
  }
  return nullptr;
}

template<class K, class V>
void rbbstree<K,V>::lrotation(node<K,V>* node) {
  if (node->parent != nullptr) {
    auto parent = node->parent;
    auto grandparent = parent->parent;
    auto left = node->left;
    parent->right = left;
    parent->parent = node;
    node->left = parent;
    if (grandparent != nullptr) {
      if (grandparent->left != parent)
        grandparent->right = node;
      else
        grandparent->left = node;
    }
  }
}

template<class K, class V>
void rbbstree<K,V>::rrotation(node<K,V>* node) {
  if (node->parent != nullptr) {
    auto parent = node->parent;
    auto grandparent = parent->parent;
    auto right = node->right;
    parent->parent = node;
    parent->left = right;
    node->right = parent;
    if (grandparent != nullptr) {
      if (grandparent->left != node)
        grandparent->right = node;
      else
        grandparent->left = node;
    }
  }
}

template<class K, class V>
void rbbstree<K,V>::insert(const K &key, const V &value) {
  if (root == nullptr) {
    root = new node<K,V>(key, value);
    root->red = false;
    return;
  }

  auto it = root;
  auto parent = root;
  while (it != nullptr) {
    parent = it;
    it = it->key < key ? it->right : it->left;
  }
  auto target = new node<K,V>(key, value, parent);
  if (parent->key < key)
    parent->right = target;
  else
    parent->left = target;
  ibalance(target);
}

template<class K, class V>
void rbbstree<K,V>::ibalance(node<K,V>* node) {
  while (node->parent != nullptr && node->parent->red) {
    auto parent = node->parent;
    auto grandparent = parent->parent;
    if (grandparent == nullptr)
        return;
    auto uncle = grandparent->left != parent ?
      grandparent->left : grandparent->right;
    if (uncle == nullptr || !uncle->red) {
      grandparent->red = false;
      if (grandparent->right != parent) {
        if (parent->left != node) {
          lrotation(node);
          parent = node;
        }
        rrotation(parent);
      } else {
        if (parent->right != node) {
          rrotation(node);
          parent = node;
        }
        lrotation(parent);
      }
      parent->red = false;
      node = parent;
      root = node->parent != nullptr ? root : node;
    } else {
      grandparent->red = root != grandparent;
      parent->red = false;
      uncle->red = false;
      node = grandparent;
    }
  }
}

}
#endif
