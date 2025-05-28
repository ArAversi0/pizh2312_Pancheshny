#include <fstream>
#include <bitset>
#include <iostream>
#include <vector>
#include "lib//decoder.h"

constexpr int HEADER_LENGTH = 10;

void displayError(const std::string& msg) {
    std::cerr << "[!] " << msg << '\n';
}

bool validateHeader(const std::string& buf) {
    return buf.size() == HEADER_LENGTH && buf.compare(0, 3, "ID3") == 0;
}

struct TagInfo {
    uint8_t version;
    uint8_t revision;
    uint8_t options;
    uint32_t length;
};

TagInfo extractTagData(const std::string& header) {
    TagInfo info;
    info.version = static_cast<uint8_t>(header[3]);
    info.revision = static_cast<uint8_t>(header[4]);
    info.options = static_cast<uint8_t>(header[5]);
    std::array<uint8_t, 4> sizeBytes = {
        static_cast<uint8_t>(header[6]),
        static_cast<uint8_t>(header[7]),
        static_cast<uint8_t>(header[8]),
        static_cast<uint8_t>(header[9])
    };
    info.length = calculateFrameSize(sizeBytes);
    return info;
}

int processAudioFile(const char* path) {
    std::ifstream audioFile(path, std::ios::binary);
    if (!audioFile.is_open()) {
        displayError("File access denied");
        return 2;
    }

    std::string headerData(HEADER_LENGTH, '\0');
    audioFile.read(headerData.data(), HEADER_LENGTH);

    if (!validateHeader(headerData)) {
        displayError("Invalid audio metadata");
        return 3;
    }

    TagInfo tag = extractTagData(headerData);
    std::cout << "[*] Metadata v" << static_cast<int>(tag.version)
        << "." << static_cast<int>(tag.revision)
        << ", size: " << tag.length << " bytes\n";

    parseMetadataBlocks(audioFile, tag.length);
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        displayError("Specify audio file path");
        return 1;
    }

    return processAudioFile(argv[1]);
}