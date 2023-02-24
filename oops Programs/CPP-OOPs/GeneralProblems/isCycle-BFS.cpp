#include <iostream>
#include<bits/stdc++.h>
using namespace std;


bool bfs(int s,int V,vector<int> adj[], vector<int>& visited){
    vector<int>bfs;
          queue<pair<int,int>> q;
          visited[s] = true;
          q.push({s,-1});
          while(!q.empty()){
             int node = q.front().first;
             int par = q.front().second;
             q.pop();
             for(auto it : adj[node]) {
                if(!visited[it]){
                    q.push({it,node});
                    visited[it] =1;
                }
                else if (par!= it){
                    return true;
                }
	        }
          }
    return false;
}

bool isCycle(int V,vector<int> adj[]){
    vector<int> vis(V+1,0);
    for(int i=1;i<=V;i++){
        if(!vis[i]){
            if(bfs(i,V,adj,vis)) return true;
        }
    }
}


int main()
{
    int n,m;//node = n, edges = m
    cin>>n>>m;
    vector<int> adj[n+1];
    
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    cout<<isCycle(n,adj);
    return 0;
}