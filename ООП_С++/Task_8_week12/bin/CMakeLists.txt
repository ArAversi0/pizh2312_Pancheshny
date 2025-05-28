add_executable(lab13 main.cpp)

target_link_libraries(lab13 BST)
target_include_directories(lab13 PRIVATE ${PROJECT_SOURCE_DIR})
