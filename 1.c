#include <ctype.h>
#include <string.h>
#include <stdio.h>

const char *nums[] = {"zero", "one", "two", "three", "four", "five",
	"six", "seven", "eight", "nine"};

int find_spelled_num_in_prefix(const char *line, int i) {
	for (int j = 0; j < 10; j++) {
		size_t numlen = strlen(nums[j]);
		const char *cmp = line + i - numlen + 1;
		if (cmp < line) // memory saftey
			continue;
		if (!strncmp(cmp, nums[j], numlen))
			return j;
	}
	return -1;
}

int main(void) {
	FILE *in = fopen("1.txt", "r");
	char *line = NULL;
	size_t linecap = 0;
	int sum = 0;

	// part 1
	while (getline(&line, &linecap, in) > 0) {
		int last_dig = -1;
		char *ptr = line;
		while (*ptr) {
			if (!isdigit(*ptr)) {
				ptr++;
				continue;
			}

			if (last_dig == -1)
				sum += (*ptr - 48) * 10;
			last_dig = *ptr - 48;
			ptr++;
		}
		sum += last_dig;
	}
	printf("%d\n", sum);

	sum = 0;
	fseek(in, 0, SEEK_SET);

	// part 2
	ssize_t linelen;
	while ((linelen = getline(&line, &linecap, in)) > 0) {
		int last_dig = -1;
		for (int i = 0; i < linelen - 1; i++) {
			int digit = -1;
			if (isdigit(line[i])) {
				digit = line[i] - 48;
			} else {
				digit = find_spelled_num_in_prefix(line, i);
			}

			if (digit == -1)
				continue;
			if (last_dig == -1)
				sum += 10 * digit;
			last_dig = digit;
		}
		sum += last_dig;
	}
	printf("%d\n", sum);
}
