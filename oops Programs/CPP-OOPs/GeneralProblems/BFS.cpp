#include <iostream>
#include<bits/stdc++.h>
using namespace std;


vector<int> bfsGraph(int n,vector<int> adj[]){
    vector<int>bfs;
    vector<int> vis(n+1,0);
    
    for(int i=0;i<=n;i++){
       if(!vis[i]){
          queue<int> q;
          q.push(i);
          vis[i] =1;
          while(!q.empty()){
             int node = q.front();
             q.pop();
             bfs.push_back(node);
             for(auto it : adj[node]) {
	     if(!vis[it]){
	        q.push(it);
	        vis[it] =1;
	     }
	  }
          }
       }
    }
    return bfs;
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
    bfsGraph(n,adj);
    return 0;
}s