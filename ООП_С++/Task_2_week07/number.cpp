#include "number.h"
#include <cstring>
#include <string>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <utility>

int chuse() {
    std::setlocale(LC_ALL, "Russian");
    int chuse = 0;
    std::cout << "Выберите режим: обрезать число справа при переполнении (1), использовать числа любой длины (2): ";
    std::cin >> chuse;
    return chuse;
}

uint2022_t from_uint(uint32_t i) {
    uint2022_t result = {};
    result.data[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);
    std::string str(buff);

    for (char c : str) {
        if (c < '0' || c > '9') {
            throw std::invalid_argument("Недопустимый символ в строке");
        }
        result = result * from_uint(10);
        result = result + from_uint(c - '0');
    }

    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result = {};
    uint64_t carry = 0;
    bool overflow_happened = false;

    const uint2022_t MAX_70_DIGIT = []() {
        uint2022_t num = from_uint(1);
        for (int i = 0; i < 70; i++) {
            num = num * from_uint(10);
        }
        return num;
    }();

    if (lhs > MAX_70_DIGIT || rhs > MAX_70_DIGIT || MAX_70_DIGIT - lhs < rhs) {
        throw std::overflow_error("Переполнение при сложении");
    }

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t sum = static_cast<uint64_t>(lhs.data[i]) + rhs.data[i] + carry;
        result.data[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;

        if (i == LIMBS - 1 && carry != 0) {
            overflow_happened = true;
        }
    }

    if (overflow_happened || result > MAX_70_DIGIT) {
        throw std::overflow_error("Переполнение при сложении");
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (lhs < rhs) {
        throw std::overflow_error("Переполнение при вычитании (отрицательный результат)");
    }

    uint2022_t result = {};
    int64_t borrow = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        int64_t diff = static_cast<int64_t>(lhs.data[i]) - rhs.data[i] - borrow;
        if (diff < 0) {
            diff += (1LL << 32);
            borrow = 1;
        } else {
            borrow = 0;
        }
        result.data[i] = static_cast<uint32_t>(diff);
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint64_t temp[2 * LIMBS] = {};
    bool nonZeroLhs = false, nonZeroRhs = false;

    for (size_t i = 0; i < LIMBS; ++i) {
        if (lhs.data[i] != 0) nonZeroLhs = true;
        if (rhs.data[i] != 0) nonZeroRhs = true;
    }

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < LIMBS; ++j) {
            size_t k = i + j;
            if (k >= 2 * LIMBS) continue;
            uint64_t mul = static_cast<uint64_t>(lhs.data[i]) * rhs.data[j];
            uint64_t sum = temp[k] + mul + carry;
            carry = sum >> 32;
            temp[k] = static_cast<uint32_t>(sum);
        }

        size_t carry_index = i + LIMBS;
        if (carry_index < 2 * LIMBS) {
            temp[carry_index] += carry;
        } else if (carry != 0) {
            throw std::overflow_error("Переполнение при умножении (лишний перенос)");
        }
    }

    for (size_t i = LIMBS; i < 2 * LIMBS; ++i) {
        if (temp[i] != 0) {
            throw std::overflow_error("Переполнение при умножении (старшие разряды)");
        }
    }

    uint2022_t result = {};
    for (size_t i = 0; i < LIMBS; ++i) {
        result.data[i] = static_cast<uint32_t>(temp[i]);
    }

    if (result == from_uint(0) && (nonZeroLhs && nonZeroRhs)) {
        throw std::overflow_error("Переполнение при умножении (неожиданный ноль)");
    }

    return result;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) {
        throw std::domain_error("Деление на ноль");
    }

    uint2022_t result = from_uint(0);
    uint2022_t remainder = from_uint(0);

    for (int i = LIMBS * 32 - 1; i >= 0; --i) {
        for (int j = LIMBS - 1; j > 0; --j) {
            remainder.data[j] = (remainder.data[j] << 1) | (remainder.data[j - 1] >> 31);
        }
        remainder.data[0] = (remainder.data[0] << 1) | ((lhs.data[i / 32] >> (i % 32)) & 1);

        if (!(remainder < rhs)) {
            remainder = remainder - rhs;
            result.data[i / 32] |= (1u << (i % 32));
        }
    }

    return result;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (size_t i = 0; i < LIMBS; ++i) {
        if (lhs.data[i] != rhs.data[i]) return false;
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = static_cast<int>(LIMBS) - 1; i >= 0; --i) {
        if (lhs.data[i] < rhs.data[i]) return true;
        if (lhs.data[i] > rhs.data[i]) return false;
    }
    return false;
}

bool operator>(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = static_cast<int>(LIMBS) - 1; i >= 0; --i) {
        if (lhs.data[i] < rhs.data[i]) return false;
        if (lhs.data[i] > rhs.data[i]) return true;
    }
    return false;
}

std::pair<uint2022_t, uint8_t> divmod10(const uint2022_t& value) {
    uint2022_t quotient = from_uint(0);
    uint64_t remainder = 0;

    for (int i = static_cast<int>(LIMBS) - 1; i >= 0; --i) {
        uint64_t part = (remainder << 32) | value.data[i];
        quotient.data[i] = static_cast<uint32_t>(part / 10);
        remainder = part % 10;
    }

    return std::make_pair(quotient, static_cast<uint8_t>(remainder));
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    uint2022_t temp = value;
    std::string result;

    while (!(temp == from_uint(0))) {
        std::pair<uint2022_t, uint8_t> qr = divmod10(temp);
        result += static_cast<char>('0' + qr.second);
        temp = qr.first;
    }

    if (result.empty()) {
        result = "0";
    }

    std::reverse(result.begin(), result.end());
    stream << result;
    return stream;
}