#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdint>
#include <cstring>
#include <direct.h> // mkdir
#include <map>

using namespace std;

/*
 * Структура конфигурации программы.
 * Сюда парсятся аргументы командной строки: размеры сетки, файл ввода, директория вывода, макс. итерации и частота сохранения.
 */
struct Config {
    uint16_t width = 0;
    uint16_t height = 0;
    string input_file;
    string output_dir;
    uint64_t max_iter = 0;
    uint64_t freq = 0;
};

/*
 * Структура BMP-заголовка для 24-битных изображений.
 * Используется при сохранении состояния сетки в BMP-файл.
 * #pragma pack гарантирует отсутствие выравнивания между полями.
 */
#pragma pack(push, 1)
struct BMPHeader {
    uint16_t file_type = 0x4D42; // "BM" — сигнатура BMP-файла
    uint32_t file_size;
    uint32_t reserved = 0;
    uint32_t offset_data = 54;   // смещение начала пиксельных данных
    uint32_t size = 40;          // размер DIB-заголовка
    int32_t width;
    int32_t height;
    uint16_t planes = 1;
    uint16_t bit_count = 24;     // 24 бита на пиксель (RGB)
    uint32_t compression = 0;
    uint32_t size_image = 0;
    int32_t x_pixels_per_meter = 1000;
    int32_t y_pixels_per_meter = 1000;
    uint32_t colors_used = 0;
    uint32_t colors_important = 0;
};
#pragma pack(pop)

/*
 * Цветовая карта. Каждое число в сетке будет отображаться как цвет пикселя.
 * Значения от 0 до 3 — свои цвета, всё что больше — чёрное.
 */
uint8_t color_map[5][3] = {
    {255, 255, 255}, // 0 - белый
    {0, 255, 0},     // 1 - зелёный
    {128, 0, 128},   // 2 - фиолетовый
    {255, 255, 0},   // 3 - жёлтый
    {0, 0, 0}        // >3 - чёрный
};

/*
 * Сохраняет двумерный массив значений в BMP-файл.
 * Каждое значение преобразуется в цвет с помощью color_map.
 */
void save_bmp(const string& filename, const vector<vector<uint64_t> >& grid) {
    int height = grid.size();
    int width = grid[0].size();
    int row_stride = (width * 3 + 3) & ~3; // размер строки в байтах, кратный 4
    int filesize = 54 + row_stride * height;

    BMPHeader header;
    header.file_size = filesize;
    header.width = width;
    header.height = height;
    header.size_image = row_stride * height;

    ofstream file(filename.c_str(), ios::binary);
    file.write(reinterpret_cast<char*>(&header), sizeof(header));

    vector<uint8_t> row(row_stride);

    // Сохраняем строки снизу вверх (BMP-порядок)
    for (int y = height - 1; y >= 0; --y) {
        memset(&row[0], 0, row_stride);
        for (int x = 0; x < width; ++x) {
            uint64_t val = grid[y][x];
            int idx = val > 3 ? 4 : static_cast<int>(val);
            row[x * 3 + 0] = color_map[idx][2]; // B
            row[x * 3 + 1] = color_map[idx][1]; // G
            row[x * 3 + 2] = color_map[idx][0]; // R
        }
        file.write(reinterpret_cast<char*>(&row[0]), row_stride);
    }
}

/*
 * Загружает начальные значения из TSV-файла.
 * Каждая строка содержит координаты и количество песка: X<TAB>Y<TAB>COUNT.
 */
void load_input(const string& filename, vector<vector<uint64_t> >& grid) {
    ifstream file(filename.c_str());
    string line;
    while (getline(file, line)) {
        istringstream iss(line);
        int x, y;
        uint64_t count;
        iss >> x;
        iss.ignore();
        iss >> y;
        iss.ignore();
        iss >> count;
        if (y < (int)grid.size() && x < (int)grid[0].size())
            grid[y][x] += count;
    }
}

/*
 * Выполняет одну итерацию "сыпучего автомата".
 * Ячейки с количеством >= 4 теряют 4 и раздают по 1 соседям.
 * Возвращает true, если были изменения, иначе false.
 */
bool iterate(vector<vector<uint64_t> >& grid) {
    int h = grid.size();
    int w = grid[0].size();
    vector<vector<uint64_t> > next = grid;
    bool changed = false;

    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            if (grid[y][x] >= 4) {
                uint64_t fall = grid[y][x] / 4;
                next[y][x] -= fall * 4;

                if (y > 0) next[y - 1][x] += fall;
                if (y < h - 1) next[y + 1][x] += fall;
                if (x > 0) next[y][x - 1] += fall;
                if (x < w - 1) next[y][x + 1] += fall;

                changed = true;
            }
        }
    }

    grid = next;
    return changed;
}

/*
 * Замена std::to_string для старых компиляторов.
 */
string to_string_alt(uint64_t value) {
    ostringstream oss;
    oss << value;
    return oss.str();
}

/*
 * Парсинг аргументов командной строки.
 * Аргументы передаются парами: -ключ значение.
 */
Config parse_args(int argc, char* argv[]) {
    Config cfg;
    map<string, string> args;

    for (int i = 1; i < argc - 1; i += 2) {
        args[argv[i]] = argv[i + 1];
    }

    if (args.count("-l")) cfg.height = (uint16_t)atoi(args["-l"].c_str());
    if (args.count("--length")) cfg.height = (uint16_t)atoi(args["--length"].c_str());

    if (args.count("-w")) cfg.width = (uint16_t)atoi(args["-w"].c_str());
    if (args.count("--width")) cfg.width = (uint16_t)atoi(args["--width"].c_str());

    if (args.count("-i")) cfg.input_file = args["-i"];
    if (args.count("--input")) cfg.input_file = args["--input"];

    if (args.count("-o")) cfg.output_dir = args["-o"];
    if (args.count("--output")) cfg.output_dir = args["--output"];

    if (args.count("-m")) cfg.max_iter = strtoull(args["-m"].c_str(), NULL, 10);
    if (args.count("--max-iter")) cfg.max_iter = strtoull(args["--max-iter"].c_str(), NULL, 10);

    if (args.count("-f")) cfg.freq = strtoull(args["-f"].c_str(), NULL, 10);
    if (args.count("--freq")) cfg.freq = strtoull(args["--freq"].c_str(), NULL, 10);

    return cfg;
}

/*
 * Создаёт папку вывода. Работает только в Windows (_mkdir).
 */
void create_output_dir(const string& path) {
    _mkdir(path.c_str());
}

/*
 * Главная функция:
 * - Читает конфигурацию
 * - Загружает стартовое состояние
 * - Проводит симуляцию до стабилизации или достижения max_iter
 * - Периодически сохраняет изображение состояния
 */
int main(int argc, char* argv[]) {
    if (argc < 9) {
        cout << "Используйте: ./Sandpile.exe -l <height> -w <width> -i <input.tsv> -o <output_dir> -m <max_iter> -f <freq>\n";
        return 1;
    }

    Config cfg = parse_args(argc, argv);
    create_output_dir(cfg.output_dir);

    vector<vector<uint64_t> > grid(cfg.height, vector<uint64_t>(cfg.width, 0));
    load_input(cfg.input_file, grid);

    for (uint64_t iter = 0; iter <= cfg.max_iter; ++iter) {
        if (cfg.freq != 0 && iter % cfg.freq == 0) {
            string filename = cfg.output_dir + "/state_" + to_string_alt(iter) + ".bmp";
            save_bmp(filename, grid);
        }

        if (!iterate(grid)) {
            cout << "Текущая итерация: " << iter << endl;
            break;
        }
    }

    if (cfg.freq == 0) {
        string filename = cfg.output_dir + "/final.bmp";
        save_bmp(filename, grid);
    }

    return 0;
}
