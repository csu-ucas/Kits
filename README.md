# Kubenetes in the Sky (Kits)
## Developing and Debugging Process
0. Put your header files in `$BASE_DIR/include` and source files (.cpp) at `$BASE_DIR/src`
1. Modify `CMakeLists.txt` on source file you would like to include
2. `cmake .`
3. `make`
4. run `./debug`
4. Remove all your binaries and cmake caches before you commit