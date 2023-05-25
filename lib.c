#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* convert_str(char* str) {
    size_t length = strlen(str);
    
    for (size_t i = 0; i < length; i++) {
        if (ispunct(str[i])) {
            str[i] = ' ';
        }
    }
    
    // Convert the string to lowercase
    for (size_t i = 0; i < length; i++) {
        str[i] = tolower(str[i]);
    }
    
    int i, j;
    
    // Iterate over the characters in the string
    for (i = 0, j = 0; str[i] != '\0'; i++) {
        // If the current character is a space
        if (str[i] == ' ') {
            // Check if the next character is also a space
            if (str[i + 1] == ' ') {
                // Skip the consecutive spaces
                continue;
            }
        }
        str[j++] = str[i];  // Copy the character to the new position
    }
    str[j] = '\0';  // Null-terminate the modified string
    
    return str;
}

int main() {
    
    return 0;
}
