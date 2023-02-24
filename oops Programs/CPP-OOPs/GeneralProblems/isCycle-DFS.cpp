#include<bits/stdc++.h>
using namespace std;

    bool check(int node,int parent,vector<int> &vis, vector<int> adj[]){
        vis[node]=1;
        for(auto it:adj[node]){
            if(!vis[it]){
                if(check(it,node,vis,adj)){
                    return true;
                }
            }
            else if(it != parent){
                return true;
            }
        }
        return false; 
    }
    
    bool isCycle(int V, vector<int> adj[]){
        vector<int> vis(V+1,0);
        for(int i=1;i<=V;i++){
            if(!vis[i]){
                if(check(i,-1,vis,adj)){
                    return true;
                }            
            }
        }
        return false;
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
    cout<<isCycle(n,adj);
    return 0;
}