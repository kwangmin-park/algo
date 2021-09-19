#include<iostream>
#include<string>
#include<queue>
using namespace std;

int N;
#define MAX 51
bool graph[MAX][MAX];


int main(void) {
	int max = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string str;
		cin >> str;
		for (int j = 0; j < str.size(); j++) {
			if (str[j] == 'Y')
				graph[i][j] = true;
		}
	}

	for (int i = 0; i < N; i++) {
		int tmpCnt = 0;
		queue<int> q;
		bool visit[MAX] = { false, };
		for (int j = 0; j < N; j++) {
			if (graph[i][j]) {
				visit[j] = true;
				tmpCnt++;
				q.push(j);
			}
		}
		while (!empty(q)) {
			int nNode = q.front();
			q.pop();

			for (int j = 0; j < N; j++) {
				if (i != j && !visit[j] && graph[nNode][j]) {
					tmpCnt++;
					visit[j] = true;
				}
			}
		}
		if (tmpCnt > max)
			max = tmpCnt;
	}
	cout << max;

	int a = 3;
}