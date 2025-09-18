/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if (!root) return {};

        
        vector<tuple<int,int,int>> nodes;  // {col, row, value}
        queue<pair<TreeNode*, pair<int,int>>> q; // node -> {row, col}

        q.push({root, {0, 0}});

        while (!q.empty()) {
            auto [node, pos] = q.front();
            q.pop();

            int r = pos.first;
            int c = pos.second;

            nodes.push_back({c, r, node->val});

            if (node->left)
                q.push({node->left, {r+1, c-1}});
            if (node->right)
                q.push({node->right, {r+1, c+1}});
        }

        
        sort(nodes.begin(), nodes.end());

       
        vector<vector<int>> result;
        int curr_col = get<0>(nodes[0]);
        vector<int> curr_group;

        for (auto &[c, r, val] : nodes) {
            if (c != curr_col) {
                result.push_back(curr_group);
                curr_group.clear();
                curr_col = c;
            }
            curr_group.push_back(val);
        }
        result.push_back(curr_group); 

        return result;
    }
};
