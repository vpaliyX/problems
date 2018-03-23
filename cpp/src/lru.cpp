#include "lru.hpp"

int main(int argc, char** argv) {
  LRU::lru<int,int> cache(10);
  cache.put(1, 2);
  cache.put(2, 10);
  cache.put(10, 10);
  cache.put(20, 20);
  cache.put(30, 30);
  cache.put(3,1);
  cache.put(40, 10);
  std::cout<<cache.get(1)<<std::endl;
  std::cout<<cache.get(2)<<std::endl;
  std::cout<<cache.get(3)<<std::endl;
  return 1;
}
