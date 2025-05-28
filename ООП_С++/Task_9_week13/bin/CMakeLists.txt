set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(lab14 main.cpp)

target_link_libraries(lab14 LazyAdapters)
target_include_directories(lab14 PRIVATE ${PROJECT_SOURCE_DIR})
