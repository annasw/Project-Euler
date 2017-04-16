#include <stdio.h>

// Returns the sum of the proper divisors of n
int sumOfDivisors(int n);

// Checks to see if n is amicable
// i.e. if sumOfDivisors(sumOfDivisors(n)) == sumOfDivisors(n)
int isAmicable(int n);

int sumOfDivisors(int n) {
	int sum = 0;
	int i;
	for (i=1; i<n; i++) {
		if (n%i==0) {sum += i;}
	}
	return sum;
}

int isAmicable(int n) {
	int nDivisorsSum = sumOfDivisors(n);
	int partnersDivisorsSum = sumOfDivisors(nDivisorsSum);
	if (partnersDivisorsSum == n && nDivisorsSum!=n) {return 1;}
	else {return 0;}
}

int main() {
	printf("sum of divisors of 220: %d\n",sumOfDivisors(220));
	printf("isAmicable 284: %d\n",isAmicable(284));
	
	int sum = 0;
	int i;
	for (i=2; i<10000; i++) {
		if (isAmicable(i)==1) {sum+=i;}
	}
	printf("%d\n",sum);
	return 0;
}
