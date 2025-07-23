int maximumGain(char* s, int x, int y) {
    int size = strlen(s);
    char* stack = (char*)malloc(sizeof(char) * size);
    int top = 0;
    int count = 0;
    if (x > y) {
        for (int i = 0; i < size; i++) {
            if (top > 0 && stack[top - 1] == 'a' && s[i] == 'b') {
                s[i] = '#';
                count += x;
                top--;
            } else {
                stack[top++] = s[i];
            }
        }
        int size2 = 0;
        for (int i = 0; i < top; i++) {
            s[size2++] = stack[i];
        }
        top = 0;
        for (int i = 0; i < size2; i++) {
            if (top > 0 && stack[top - 1] == 'b' && s[i] == 'a') {
                count += y;
                top--;
            } else {
                stack[top++] = s[i];
            }
        }
    }
    else{
         for (int i = 0; i < size; i++) {
            if (top > 0 && stack[top - 1] == 'b' && s[i] == 'a') {
                s[i] = '#';
                count += y;
                top--;
            } else {
                stack[top++] = s[i];
            }
        }
        int size2 = 0;
        for (int i = 0; i < top; i++) {
            s[size2++] = stack[i];
        }
        top = 0;
        for (int i = 0; i < size2; i++) {
            if (top > 0 && stack[top - 1] == 'a' && s[i] == 'b') {
                count += x;
                top--;
            } else {
                stack[top++] = s[i];
            }
        }
    }
    return count;
}
