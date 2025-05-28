add_executable(lab7 main.cpp)

target_link_libraries(lab7 Decoder)
target_include_directories(lab7 PRIVATE ${PROJECT_SOURCE_DIR})