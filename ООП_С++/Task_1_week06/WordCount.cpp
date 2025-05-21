#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

/**
 * class FileStats
 * Класс, хранящий статистику по одному файлу
 */
class FileStats {
public:
    int lines = 0;
    int words = 0;
    int bytes = 0;
    int chars = 0;

    /**
     * Подсчитывает строки, слова, байты и символы в переданном файле
     */
    void computeStats(const std::string& filename) {
        std::ifstream file(filename, std::ios::binary);

        if (!file.is_open()) {
            std::cerr << "Ошибка при открытии файла: " << filename << std::endl;
            return;
        }

        std::string line;
        while (std::getline(file, line)) {
            ++lines;
            std::istringstream iss(line);
            std::string word;
            while (iss >> word) ++words;
            chars += line.size(); // не учитывает \n
        }

        file.clear();
        file.seekg(0, std::ios::end);
        bytes = static_cast<int>(file.tellg());

        file.close();
    }
};

/**
 * class WordCountApp
 * Основной класс приложения для обработки аргументов и запуска анализа
 */
class WordCountApp {
private:
    std::vector<std::string> filenames;
    std::map<std::string, bool> options;

public:
    /**
     * Конструктор, разбирающий аргументы командной строки
     * (argc - Количество аргументов,
     * argv - Список аргументов)
     */
    WordCountApp(int argc, char* argv[]) {
        parseArguments(argc, argv);
    }

    /**
     * Разбирает аргументы командной строки, выделяя опции и имена файлов
     */
    void parseArguments(int argc, char* argv[]) {
        for (int i = 1; i < argc; ++i) {
            std::string arg = argv[i];
            if (arg[0] == '-') {
                if (arg == "-l" || arg == "--lines") options["lines"] = true;
                else if (arg == "-w" || arg == "--words") options["words"] = true;
                else if (arg == "-c" || arg == "--bytes") options["bytes"] = true;
                else if (arg == "-m" || arg == "--chars") options["chars"] = true;
                else {
                    // разбор как сокращенной группы -lwc
                    for (size_t j = 1; j < arg.size(); ++j) {
                        if (arg[j] == 'l') options["lines"] = true;
                        if (arg[j] == 'w') options["words"] = true;
                        if (arg[j] == 'c') options["bytes"] = true;
                        if (arg[j] == 'm') options["chars"] = true;
                    }
                }
            }
            else {
                filenames.push_back(arg);
            }
        }
    }

    /**
     * Запускает обработку файлов и выводит результаты
     */
    void run() {
        if (filenames.empty()) {
            std::cerr << "Нет указанных файлов." << std::endl;
            return;
        }

        for (const auto& filename : filenames) {
            FileStats stats;
            stats.computeStats(filename);
            printStats(stats, filename);
        }
    }

    /**
     * Проверяет, есть ли активные флаги опций
     */
    bool hasAnyOption() const {
        return options.count("lines") || options.count("words") || options.count("bytes") || options.count("chars");
    }

    /**
     * Выводит результаты анализа файла в зависимости от указанных опций
     * (stats - Статистика по файлу)
     */
    void printStats(const FileStats& stats, const std::string& filename) {
        if (!hasAnyOption()) {
            // По умолчанию: lines words bytes
            std::cout << stats.lines << " " << stats.words << " " << stats.bytes << " " << filename << std::endl;
            return;
        }

        if (options["lines"]) std::cout << stats.lines << " ";
        if (options["words"]) std::cout << stats.words << " ";
        if (options["bytes"]) std::cout << stats.bytes << " ";
        if (options["chars"]) std::cout << stats.chars << " ";

        std::cout << filename << std::endl;
    }
};

/**
 * Точка входа в программу
 */
int main(int argc, char* argv[]) {
    setlocale(LC_ALL, "ru");
    
    WordCountApp app(argc, argv);
    app.run();
    
    return 0;
}
