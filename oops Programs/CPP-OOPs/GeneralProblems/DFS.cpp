#include<bits/stdc++.h>
using namespace std;

    void dfs(int node,vector<int> &vis, vector<int> adj[], vector<int>&storeDfs){
        storeDfs.push_back(node);
        vis[node]=1;
        for(auto it:adj[node]){
            if(!vis[it]){
                dfs(it,vis,adj,storeDfs);
            }
        }
    }
    
    vector<int> dfsGraph(int V, vector<int> adj[]){
        vector<int> storeDfs;
        vector<int> vis(V+1,0);
        for(int i=1;i<=V;i++){
            if(!vis[i]){
                dfs(i,vis,adj,storeDfs);
            }
        }
        return storeDfs;
    }


int main()
{
    int n,m;//node = n, edges = m
    cin>>n>>m;
    vector<int> v;
    vector<int> adj[n+1];
    
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    v = dfsGraph(n,adj);
    for(int i:v){
        cout<<i<<" ";
    }
    return 0;
}