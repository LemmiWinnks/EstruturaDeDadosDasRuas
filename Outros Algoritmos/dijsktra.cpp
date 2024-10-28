#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main()
{

    int vertices, arestas;
    cin >> vertices >> arestas;

    vector<vector<pair<int, int>>> grafo(vertices);

    for (int i = 0; i < arestas; i++)
    {
        int verticeA, verticeB, aresta;
        cin >> verticeA >> verticeB >> aresta;
        verticeA --;
        verticeB --;
        
        grafo[verticeA].push_back({verticeB, aresta});
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> fila;
    vector<int> peso(vertices, INT_MAX);

    peso[0] = 0;
    fila.push({0, 0});

    while (!fila.empty())
    {

        int verticeX = fila.top().second;
        int pesoX = fila.top().first;
        fila.pop();

        if (pesoX > peso[verticeX])
            continue;

        for (auto &conjunto : grafo[verticeX])
        {
            int verticeY = conjunto.first;
            int arestaX_Y = conjunto.second;

            if (peso[verticeY] > peso[verticeX] + arestaX_Y)
            {
                peso[verticeY] = peso[verticeX] + arestaX_Y;

                fila.push({peso[verticeY], verticeY});
            }
        }
    }

    for (int d : peso)
    {
        cout << d << " ";
    }

    cout << "\n";

    return 0;
}